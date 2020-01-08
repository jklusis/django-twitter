<template>
    <div>
        <h4>Post something</h4>

        <div class="input-group">
            <input v-model="post" type="text" class="form-control" placeholder="What's on your mind?">
            <div class="input-group-append">
                <button class="btn btn-primary" type="button" :disabled="!isLengthValid || isLoading" @click="submitPost">Post</button>
            </div>
        </div>

        <small :class="{'text-danger': isLengthExceeded}">{{ post.length }} characters out of 150</small>

        <hr class="mb-3"/>
    </div>
</template>

<script>
    import axios from 'axios';

    const MAX_LENGTH = 150;

    export default {
        data: () => ({
            post: '',
            isLoading: false,
        }),
        computed: {
            isLengthExceeded() {
                return this.post.length > MAX_LENGTH;
            },
            isLengthValid() {
                return this.post.length && !this.isLengthExceeded;
            }
        },
        methods: {
            submitPost() {
                this.isLoading = true;

                axios.post('/post-rpc/create', {
                    'post': this.post
                }).then((response) => {
                    this.$emit('post-created');
                    this.post = '';
                }).finally(() => {
                    this.isLoading = false;
                })
            },
        },
    }
</script>

