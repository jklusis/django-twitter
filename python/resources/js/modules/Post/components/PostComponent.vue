<template>
    <div>
        <div class="row">
            <div class="col-md-8">
                <h5 class="mt-0 mb-1">
                    <a :href="getUrl()">@{{ post.username }}</a>
                    
                    <template v-if="isPostOwner">
                        <button class="btn btn-sm btn-danger py-0 px-2" @click="deletePost">Delete post</button>
                    </template>
                </h5>
            </div>
            
            <div class="col-md-4 text-md-right">
                {{ post.created_at | formatUnix }}
            </div>
        </div>
        {{ post.post }}
        <hr/>
    </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
import {PostDataStructure} from '@/modules/Post/post.structures';

    export default {
        filters: {
            formatUnix(string) {
                return moment.unix(string).format("YYYY/MM/DD HH:mm:ss");
            }
        },
        
        props: {
            activeUserId: {
                type: Number,
                required: true,
            },

            post: {
                type: PostDataStructure,
                required: true,
            }
        },

        computed: {
            isPostOwner() {
                return this.activeUserId === this.post.user_id;
            }
        },

        methods: {
            getUrl() {
                return '/user/' + this.post.username;
            },

            deletePost() {
                if (!this.isPostOwner) {
                    return;
                }

                axios.post('/post-rpc/delete', {
                    'post_id': this.post.id
                }).then((response) => {
                    this.$emit('post-deleted');
                });
            }
        }
    }
</script>
