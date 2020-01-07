<template>
    <div>
        <template v-for="post in posts">
            <post-component :post="post" :key="post.id"/>
        </template>
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
        },
    }
</script>
