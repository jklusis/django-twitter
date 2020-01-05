<template>
    <div>
        {{ 'feed' }}
    </div>
</template>

<script>
    export default {
        props: {
            /** Pass user id in order to get the posts from the specific user */
            userId: {
                required: false,
                default: null,
            }
        }
    }
</script>
