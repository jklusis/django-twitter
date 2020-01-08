<template>
    <div>
        <div v-if="!posts.length && isLoading">
            Loading..
        </div>

        <div v-else-if="posts.length">
            <post-component 
                v-for="post in posts" 
                :active-user-id="activeUserId" 
                :post="post" 
                :key="post.id"
                @post-deleted="onPostDeleted"
            />
        </div>

        <div v-else>
            Nothing posted yet
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import PostComponent from './components/PostComponent';
    import {PostDataStructure} from '@/modules/Post/post.structures';

    export default {
        components: {
            PostComponent
        },

        props: {
            activeUserId: {
                required: true,
                type: Number,
            },
            /** Pass user id in order to get the posts from the specific user */
            userId: {
                required: false,
                default: null,
            }
        },

        data: () => ({
            posts: [],
            isLoading: false,
        }),
        
        computed: {
            postUrl() {
                return this.userId ? '/post-rpc/user-feed/' + this.userId : '/post-rpc/get';
            }
        },

        created() {
            this.loadPosts();
        },

        methods: {
            loadPosts() {
                if (this.isLoading) {
                    return;
                }
                
                this.isLoading = true;

                axios.post(this.postUrl)
                .then((response) => {
                    const posts = [];

                    for (let i = 0; i < response.data.postData.length; i++) {
                        posts.push(PostDataStructure.fromArray(response.data.postData[i]));
                    }

                    this.posts = posts;
                }).finally(() => {
                    this.isLoading = false;
                });
            },

            onPostDeleted() {
                this.loadPosts();
                this.$emit('post-deleted');
            }
        },
    }
</script>
