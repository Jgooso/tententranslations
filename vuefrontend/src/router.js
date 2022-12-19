import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {path: '/novel/:title', 
        children:[
            {path: '',name: 'coverPage',component: ()=> import('@/views/CoverPage.vue')},
            {path:':chapter',name: 'chapterPage',component: ()=> import('@/views/Chapter.vue')},     
        ],
        component: ()=> import('@/views/Novel.vue')},
        {path:'',name:'homePage',component: ()=> import ('@/views/HomePage.vue')},
        {path:'/novel/',name: 'Browse',component: ()=> import('@/views/Browse.vue')},
        {path:'/:browsetype/:identifier/',name: 'explorePage',component: ()=> import('@/views/Browse.vue')},
        {path:'/about',name: 'aboutPage',component: ()=> import('@/views/About.vue')},
        {path:'/contact',name: 'contactPage',component: ()=> import('@/views/Contact.vue')},
        {path:'/manage',
        children:[
          {path:'upload',name:'uploadPage',component: ()=> import('@/views/Upload')},
          {path:'schedule',name:'schedulePage',component: ()=> import('@/views/Schedular')},
          {path:'edit',name:'editPage',component: ()=> import('@/views/Editor')},
          {path:'feedback',name:'feedbackPage',component: ()=> import('@/views/Feedback')},
          {path:'descriptorbution',name:'descriptorPage',component: ()=> import('@/views/Descriptor')}
        ]
        ,name: 'managePage',component: ()=> import('@/views/Manage.vue')},
        {path:'/:pathmatch(.*)*',name:'not-found',component: ()=>import('@/views/Error.vue')}
]

const router = createRouter({
  history: createWebHistory(),
  routes:routes,
  mode:'history'
})
router.resolve({
  name: 'not-found',
  params: { pathMatch: ['not', 'found'] },
}).href
export default router

