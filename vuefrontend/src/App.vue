<template>
  <div id="app">
     <sidebar ref='sidemenu'
     v-on:changesidebar='changesidebar()'
     />
  <Header ref='header'
   v-on:changesidebar='changesidebar()'
   :tier='tier'
  />

    <router-view
      :tier = 'tier'
    />
 
  <Footer/>
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'
import sidebar from './components/Sidebar'
import { getAPI } from './axios-api'
export default {
  
  name: 'App',
  components:{
    Header,
    Footer,
    sidebar
  },
  data(){
    return{
    tier: 5,
    darkmore:false,
    testing:[],
    }
  },
  methods:{
        changesidebar(){
          const menuBtn = this.$refs.header.$refs.menubutton;
          if(this.$refs.sidemenu.$refs.sidebar.style.left=='0px'){
            this.$refs.sidemenu.$refs.sidebar.style.left='-300px';
            this.$refs.sidemenu.$refs.shade.style.opacity='0';
            menuBtn.classList.remove('open');
          }else{
            this.$refs.sidemenu.$refs.sidebar.style.left='0px';
            this.$refs.sidemenu.$refs.shade.style.opacity='0.5';
            menuBtn.classList.add('open');
          }
          
        },
        darkmode(){
          if(darkmode){
            document.style.color='white'
            document.body.style.backgroundColor='black'
          }
        }
            
        },
    errorCaptured: function(err) {
      //this.$router.push({name:'errorPage'})
      
    },
    created(){
    }
  
}
</script>

<style>
*{
  font:Arial, Helvetica;
  color:black;
}
  body {
    margin: 0;
    padding: 0;
    background-color:white!important;
    
  }
  .content{
      width: 1110px;
      margin:auto;
      position:relative;
      height: 100%;
      background-color:rgba(0,0,0,0)
  }
  

  @media (max-width: 1200px){
     .content{
         width: 92.5%;
         transition: all .3s ease;
     }
  }

@media (max-width: 775px) {
    .content{
        display: flex;
        flex-direction: column;
        margin-top: 30px;
        margin: auto;
        transition: all .3s ease;
    }
}
</style>
