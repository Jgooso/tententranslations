import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {path: '/novel/:title', 
        children:[
            {path: '',name: 'coverPage',component: ()=> import('@/views/CoverPage.vue')},
            {path:':chapter',name: 'chapterPage',component: ()=> import('@/views/Chapter.vue')},     
        ],
        component: ()=> import('@/views/Novel.vue')},
        {path:'',name:'HomePage',component: ()=> import ('@/views/HomePage.vue')},
        {path:'/search',name: 'Browse',component: ()=> import('@/views/Browse.vue')},
        {path:'/search/:browsetype/:identifier/',name: 'explorePage',component: ()=> import('@/views/Browse.vue')},
        {path:'/about',name: 'aboutPage',component: ()=> import('@/views/About.vue')},
        {path:'/contact',name: 'contactPage',component: ()=> import('@/views/Contact.vue')},
        {path:'/manage',
        children:[
          {path:'upload',name:'uploadPage',component: ()=> import('@/views/Upload')},
          {path:'schedule',name:'schedulePage',component: ()=> import('@/views/Schedular')},
          {path:'edit',name:'editPage',component: ()=> import('@/views/Editor')}
        ]
        ,name: 'managePage',component: ()=> import('@/views/Manage.vue')},
        {path:'/404',name:'errorPage',component: ()=>import('@/views/Error.vue')}
]

const router = createRouter({
  history: createWebHistory(),
  routes:routes,
  mode:'history'
})
export default router

