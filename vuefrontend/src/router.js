import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {path: '/novel/:title', 
        children:[
            {path: '',name: 'coverPage',component: ()=> import('@/views/CoverPage.vue')},
            {path:':chapter/:password?',name: 'chapterPage',component: ()=> import('@/views/Chapter.vue')},     
        ],
        component: ()=> import('@/views/Novel.vue')},
        {path:'',name: 'Browse',component: ()=> import('@/views/Browse.vue')},
        {path:'/:browsetype/:identifier/',name: 'explorePage',component: ()=> import('@/views/Browse.vue')},
        {path:'/about',name: 'aboutPage',component: ()=> import('@/views/About.vue')},
        {path:'/contact',name: 'contactPage',component: ()=> import('@/views/Contact.vue')},
        {path:'/support',name: 'supportPage',component: ()=> import('@/views/Support.vue')},
        {path:'/upload',name: 'uploadPage',component: ()=> import('@/views/Upload.vue')},
        {path:'/404',name:'errorPage',component: ()=>import('@/views/Error.vue')}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router

