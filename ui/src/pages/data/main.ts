import {createApp} from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from "vue-router";


function lazyLoad(viewName: string) {
    return () => import(`./${viewName}.vue`)
}


const routes = [
    {
        path: "/",
        component: lazyLoad('_DataSet')
    },
    {
        path: "/dataset",
        component: lazyLoad('_DataSet')
    },
    {
        path: "/datasource",
        component: lazyLoad('_DataSource')
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});


createApp(App).use(router).mount('#app')
