<template>
    <div>
        <h2>Recent posts</h2>
        <post-component :active-user-id="activeUserId"/>
    </div>
</template>

<script>
    import PostComponent from '@/modules/Post/PostIndex';
    import {UserDataStructure} from '@/structures/user.structures';

    export default {
        components: {
            PostComponent,
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

