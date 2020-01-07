<template>
    <div>
        <div class="row">
            <div class="col-md-8">
                <h5 class="mt-0 mb-1">
                    <a :href="getUrl()" target="_blank">@{{ post.username }}</a>
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
import moment from 'moment';
import {PostDataStructure} from '@/modules/Post/post.structures';

    export default {
        filters: {
            formatUnix(string) {
                return moment.unix(string).format("YYYY/MM/DD HH:mm:ss");
            }
        },
        
        props: {
            post: {
                type: PostDataStructure,
                required: true,
            }
        },

        methods: {
            getUrl() {
                return '/user/' + this.post.username;
            }
        }
    }
</script>
