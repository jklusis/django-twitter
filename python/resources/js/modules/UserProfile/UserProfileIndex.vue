<template>
    <div>
        <div class="jumbotron py-3">
            <h3>{{ user.first_name }}'s profile (@{{ user.username}})</h3>

            <p>
                <b>About:</b> <br/>
                Posts: {{ user.post_count }}<br/>
                Following: {{ user.following_count }}<br/>
                Followers: {{ user.follower_count }}<br/>
                Date joined: {{ user.date_joined | formatUnix }}
            </p>

            <template v-if="!isOwner">
                <hr class="my-4">
                <button class="btn btn-primary">Follow</button>
            </template>
        </div>
        
        <div class="px-3 pb-3">
            <h3>Posts</h3>
            <feed-component :user-id="user.id"/>
        </div>
        
    </div>
</template>

<script>
    import moment from 'moment';
    import FeedComponent from '@/modules/Feed/FeedIndex';
    import {UserDataStructure} from '@/structures/user.structures';

    export default {
        filters: {
            formatUnix(string) {
                return moment.unix(string).format("DD/MM/YYYY");
            }
        },
        components: {
            FeedComponent,
        },
        props: {
            activeUserId: {
                required: true,
                type: Number,
            },
            pUser: {
                required: true,
                type: Object,
            },
        },
        data: () => ({
            user: null,
        }),
        computed: {
            isOwner() {
                return this.activeUserId === this.user.id;
            }
        },
        created() {
            this.user = UserDataStructure.fromArray(this.pUser);
        }
    }
</script>
