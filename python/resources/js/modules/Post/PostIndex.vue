<template>
    <div>
        <post-component/>
        <post-component/>
        <post-component/>
    </div>
</template>

<script>
    import PostComponent from './components/PostComponent';

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
        }
    }
</script>
