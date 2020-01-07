<template>
    <div>
        <post-input-component/>
        
        <h2>Recent posts</h2>
        <post-component :active-user-id="activeUserId"/>
    </div>
</template>

<script>
    import PostInputComponent from '@/modules/Post/components/PostInputComponent';
    import PostComponent from '@/modules/Post/PostIndex';
    import {UserDataStructure} from '@/structures/user.structures';

    export default {
        components: {
            PostInputComponent,
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

