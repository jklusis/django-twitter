<template>
    <div>
        <div class="jumbotron py-3">
            <h3>{{ user.first_name }}'s profile (@{{ user.username}})</h3>

            <h5>About:</h5>
            <p>
                Posts: {{ user.post_count }}<br/>
                Following: {{ user.following_count }}<br/>
                Followers: {{ user.follower_count }}<br/>
                Date joined: {{ user.date_joined | formatUnix }}
            </p>

            <template v-if="!isOwner">
                <hr class="my-4">
                <button class="btn" :class="{'btn-danger': isFollowing, 'btn-success': !isFollowing}" @click="toggleFollowing">
                    {{ isFollowing ? 'Unfollow' : 'Follow'}}
                </button>
            </template>
        </div>

        <post-input-component v-if="isOwner" @post-created="onPostCreated"/>
        
        <div class="px-3 pb-3">
            <h2>Posts</h2>
            <post-component 
                ref="postComponent" 
                :active-user-id="activeUserId" 
                :user-id="user.id"
                @post-deleted="onPostDeleted"
            />
        </div>
        
    </div>
</template>

<script>
    import axios from 'axios';
    import moment from 'moment';
    import PostInputComponent from '@/modules/Post/components/PostInputComponent';
    import PostComponent from '@/modules/Post/PostIndex';
    import {UserDataStructure} from '@/structures/user.structures';

    export default {
        filters: {
            formatUnix(string) {
                return moment.unix(string).format("DD/MM/YYYY");
            }
        },
        components: {
            PostInputComponent,
            PostComponent,
        },
        props: {
            activeUserId: {
                required: true,
                type: Number,
            },
            pIsFollowing: {
                required: true,
                type: Boolean,
            },
            pUser: {
                required: true,
                type: Object,
            },
        },
        data: () => ({
            isFollowing: null,
            user: null,
        }),
        computed: {
            isOwner() {
                return this.activeUserId === this.user.id;
            }
        },
        created() {
            this.isFollowing = this.pIsFollowing;
            this.user = UserDataStructure.fromArray(this.pUser);
        },
        methods: {
            toggleFollowing() {
                axios.post('/user-rpc/toggle-follow', {
                    'user_id': this.user.id,
                }).then((response) => {
                    this.isFollowing ? this.user.follower_count-- : this.user.follower_count++;
                    this.isFollowing = response.data.is_following;
                });
            },

            onPostCreated() {
                this.user.post_count++;
                this.$refs['postComponent'].loadPosts();
            },

            onPostDeleted() {
                this.user.post_count--;
            }
        }
    }
</script>
