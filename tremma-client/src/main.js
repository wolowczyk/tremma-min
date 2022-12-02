import { createApp } from 'vue';
import App from './App.vue';
import { createWebHistory, createRouter } from "vue-router";
import Navigation from './components/Navigation';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/navigation', component: Navigation }
    ]
});

const app = createApp(App)
app.use(router)
app.mount('#app')