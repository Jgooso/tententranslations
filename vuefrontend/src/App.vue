<template>
  <div id="app" v-cloak>
     <sidebar ref='sidemenu'
     v-on:changesidebar='changesidebar()'
     v-on:closesignin='close_signin()'
     />
    <SignIn ref = 'signin'/>
  <Header ref='header'
   v-on:changesidebar='changesidebar()'
   v-on:signin='open_signin()'
   v-on:signup='signup()'
   :status='user.status'
   class = 'view-header'
  />
  <div class = 'view-border-one bord'></div>
    <router-view
      :tier = 'user.tier'
      class = 'view-content'
      v-on:switchmode='switchdarkmode()'
    />
  <div class = 'view-border-two bord'></div>
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
    darkmode:($cookies.get('darkmode')==='true'),
    testing:[],
    user: [],
    url:'http://ipinfo.io/json'
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
        },
        close_signin(){
          this.$refs.signin.$refs.signin.style.display='none'
        },
        signup(){
           this.$refs.signin.$refs.signin.style.display='block'
        },
        setdarkmode(){
          var r = document.querySelector(':root');
          if(this.darkmode){
            r.style.setProperty('--backgroundColor', '#262626')
            r.style.setProperty('--textColor', '#959595')
            r.style.setProperty('--shadowColor', 'rgba(255,255,255,0.19)')
            r.style.setProperty('--borderColor', 'white')
            r.style.setProperty('--styleColor', '#A837AF')
          }else{
            r.style.setProperty('--backgroundColor', 'white')
            r.style.setProperty('--textColor', 'black')
            r.style.setProperty('--shadowColor', 'rgba(0,0,0,0.19)')
            r.style.setProperty('--borderColor', 'black')
            r.style.setProperty('--styleColor', '#A837AF')
          }

        },
        switchdarkmode(){
          this.darkmode=!this.darkmode
          this.setdarkmode()
          $cookies.set('darkmode',this.darkmode)
        },
    errorCaptured: function(err) {
      //this.$router.push({name:'errorPage'})
      
    },
    },
    created(){
      this.setdarkmode()
      if($cookies.get('verified') == null){
        $cookies.set('verified',1)
      }
      this.user = {'id':838383,'status':'a','fontsize':19,'tier':$cookies.get('verified')}
    },
    mounted(){
      //console.log(await ipify());
      /*
      let apiKey = '8ec778b9a4c4ba813db900bd2c328e6d9afbc4579c1c0d0ac13cc69c';
      getAPI.get(`https://api.ipdata.co?api-key=${apiKey}`)
          .then(response => {
            const data = response.data
            console.log(data.ip)
            console.log(data.longitude)
            console.log(data.latitude)
          })
          .catch(err => {
            console.log(err)
          })
          */
        },
  }
</script>

<style>
:root{
  --styleColor: #75147C;
  --backgroundColor: #FFFFFF;
  --textColor: #000000;
  --shadowColor: rgba(0,0,0,0.19);
  --borderColor:black;
}
*{
  font:Arial, Helvetica;
  color:var(--textColor);
}
[v-cloak] { display: none }
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
  .view-header{
    grid-row:1;
    grid-column: 1/span 3;
    height:fit-content;
    width:100%;
  }
  .view-border-one{
   grid-row:2;
   grid-column:1;
   border:none;
  }
  .view-content{
      grid-row:2;
      grid-column:2;
      margin:auto;
      max-width:1200px;
      min-width:1000px;
      padding:20px;
      height:fit-content;
      border:none;
      min-height:1000px;
      width:100%;
      /*box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) inset, 0 6px 20px 0 rgba(0, 0, 0, 0.19) inset;*/
  }
  .view-border-two{
    grid-row:2;
    grid-column:3;
    border:none;
  }
  .view-footer{
    grid-row: 3;
    grid-column: 1 / span 3;
  }
  .bord{
    height:100%;
    margin:0px;
    width:100%;
    border:none;
    min-height:1000px;

  }

  @media (max-width: 1200px){
     .view-content{
        width:92.5%;
         transition: all .3s ease;
         min-width:0px;
     }
     .border{
       display:none;
     }
  }

@media (max-width: 775px) {
    .view-content{
        display: flex;
        flex-direction: column;
        margin-top: 30px;
        /*margin: auto;*/
        transition: all .3s ease;
        width:100%;
        grid-column: 1 / span 3;
        padding:10px;
    }

}
</style>
