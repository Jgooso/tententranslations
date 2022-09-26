<template>
  <div id="app">
  
    <SignIn/>
     <sidebar ref='sidemenu'
     v-on:changesidebar='changesidebar()'
     v-on:closesignin='close_signin()'
     />
    <SignIn ref = 'signin'/>

  <Header ref='header'
   v-on:changesidebar='changesidebar()'
   v-on:signin='open_signin()'
   v-on:signup='signup()'
   :tier='tier'
   class = 'view-header'
  />
  <div class = 'view-border-one border'></div>
    <router-view
      :tier = 'tier'
      class = 'view-content'
    />
  <div class = 'view-border-two border'></div>
  <Footer class = 'view-footer'/>
  </div>
</template>

<script>
import Header from './components/Header'
import Footer from './components/Footer'
import sidebar from './components/Sidebar'
import SignIn from './components/SignIn'
import { getAPI } from './axios-api'
export default {
  
  name: 'App',
  components:{
    Header,
    Footer,
    sidebar,
    SignIn
  },
  data(){
    return{
    tier: 5,
    darkmode:false,
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
        open_signin(){
          //this.$refs.signin.$refs.signin.style.display='block'
          this.switchdarkmode()
          console.log('open')
        },
        close_signin(){
          this.$refs.signin.$refs.signin.style.display='none'
        },
        signup(){
           this.$refs.signin.$refs.signin.style.display='block'
        },
        switchdarkmode(){
          var r = document.querySelector(':root');
         
          if(this.darkmode){
           r.style.setProperty('--backgroundColor', 'white')
           r.style.setProperty('--textColor', 'black')
          }else{
            r.style.setProperty('--backgroundColor', '#262626')
            r.style.setProperty('--textColor', '#848484')
          }
          this.darkmode = !this.darkmode;

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
:root{
  --styleColor: #75147C;
  --backgroundColor: #FFFFFF;
  --textColor: #000000;
}
*{
  font:Arial, Helvetica;
  color:var(--textColor);
}
#app{
  display:grid;
  padding:0px;
  gap:0;
}
  body {
    margin: 0;
    padding: 0;
    background-color:var(--backgroundColor)!important;
    
  }
  /*
  .content{
      position:relative;
      height: 100%;
      width:100%;
      
  }
  */
  .view-header{
    grid-row:1;
    grid-column: 1 / span 3;
    height:fit-content;
    width:100%;
  }
  .view-border-one{
   grid-row:2;
   grid-column:1;
  }
  .view-content{
      grid-row:2;
      grid-column:2;
      margin:auto;
      max-width:1300px;
      padding:0px;
  }
  .view-border-two{
    grid-row:2;
    grid-column:3;
  }
  .view-footer:{
    grid-row: 3;
    grid-column: 1 / span 3;
  }
  .border{
    height:100%;
    margin:0px;
    width:100%;

  }

  @media (max-width: 1200px){
     .view-content{
        width:92.5%;
         transition: all .3s ease;
     }
  }

@media (max-width: 775px) {
    .view-content{
        display: flex;
        flex-direction: column;
        margin-top: 30px;
        /*margin: auto;*/
        transition: all .3s ease;
        width:92.5%;
        grid-column: 1 / span 3;
    }
}
</style>
