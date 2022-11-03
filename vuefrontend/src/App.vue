<template>
  <div id="app" v-if='user.status'>
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
  <button @click='switchdarkmode()'>Switch</button>
  <div class = 'view-border-one bord'></div>
    <router-view
      tier = 1
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
    user: []
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
        setdarkmode(){
          var r = document.querySelector(':root');
          if(this.darkmode){
            r.style.setProperty('--backgroundColor', '#262626')
            r.style.setProperty('--textColor', '#959595')
            r.style.setProperty('--shadowColor', 'rgba(255,255,255,0.19)')
            r.style.setProperty('--borderColor', 'white')
            r.style.setProperty('--styleColor', '#A837AF')
            console.log('darkmode')
          }else{
            r.style.setProperty('--backgroundColor', 'white')
            r.style.setProperty('--textColor', 'black')
            r.style.setProperty('--shadowColor', 'rgba(0,0,0,0.19)')
            r.style.setProperty('--borderColor', 'black')
            r.style.setProperty('--styleColor', '#75147C')
          }

        },
        switchdarkmode(){
          this.darkmode=!this.darkmode
          this.setdarkmode()
          $cookies.set('darkmode',this.darkmode)
        }
            
        },
    errorCaptured: function(err) {
      //this.$router.push({name:'errorPage'})
      
    },
    created(){
      this.setdarkmode()
      /*
      const userID = $cookies.get('user')
      console.log(userID)
      if(userID==null){
        const id = parseInt(Math.random()*1000000)
        $cookies.set('user',id)
        getAPI.post('/user',{userID:id})
            .then(response => {
            console.log(response)
          })
          .catch(err => {
            console.log(err)
          })
      }else{
            getAPI.get('/user?userID='+userID)
            .then(response => {
            
            console.log(response['data'])
            this.user = response['data']
            console.log(this.user)
            var r = document.querySelector(':root');
            r.style.setProperty('--fontsize', this.user.fontsize+'px')
          })
          .catch(err => {
            console.log(err)
          })
     */
     this.user = {'id':838383,'status':'Moderator','fontsize':19,'tier':1}
    }
  
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
    grid-column: 1 / span 3;
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
      height:100%;
      border:none;
      /*box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) inset, 0 6px 20px 0 rgba(0, 0, 0, 0.19) inset;*/
  }
  .view-border-two{
    grid-row:2;
    grid-column:3;
    border:none;
  }
  .view-footer:{
    grid-row: 3;
    grid-column: 1 / span 3;
  }
  .bord{
    height:100%;
    margin:0px;
    width:100%;
    border:none;

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
        width:92.5%;
        grid-column: 1 / span 3;
        
        padding:20px;
    }
}
</style>
