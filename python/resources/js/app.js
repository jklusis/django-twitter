import './bootstrap';
import Vue from 'vue';

import DashboardComponent from '@/modules/Dashboard/DashboardIndex.vue';
Vue.component('dashboard-component', DashboardComponent);

import UserProfileComponent from '@/modules/UserProfile/UserProfileIndex.vue';
Vue.component('user-profile-component', UserProfileComponent);

const app = new Vue({
    el: '#app',
});

export default app;
