<template>
    <div>
        <h2>Recent posts</h2>
        <feed-component/>
    </div>
</template>

<script>
    import FeedComponent from '@/modules/Feed/FeedIndex';
    import {UserDataStructure} from '@/structures/user.structures';

    export default {
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
        created() {
            this.user = UserDataStructure.fromArray(this.pUser);
        }
    }
</script>

