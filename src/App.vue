<template>
  <div id="app" v-cloak>
    <sidebar ref='sidemenu'
    v-on:changesidebar='changesidebar()'
    v-on:closesignin='close_signin()'
  />
  <SignIn ref = 'signin'/>
  <header id = "header" class = 'view-header'>
    <router-link :to = "{name: 'homePage'}" id = 'home-button'>TenTenTranslations</router-link>
    <div id = "header-navigation-bar">
      <router-link :to = "{name: 'Browse'}" class='header-nav' style="text-decoration:none;">Browse</router-link>
      <router-link :to = "{name: 'aboutPage'}" class='header-nav' style="text-decoration:none;">About</router-link>
      <router-link :to = "{name: 'contactPage'}" class='header-nav' style="text-decoration:none;">Contact</router-link>
      <router-link :to = "{name: 'uploadPage'}" class='header-nav' v-if='user.tier == 0'>Manage</router-link>
      <KoFiButton id = 'KoFi' v-else/>
      <div class="menu-btn"  @click='changesidebar()' id = 'menubutton'><div class="menu-btn__burger" ></div></div>
    </div>
  </header>
  <div class = 'view-border-one bord'></div>
    <router-view
      :tier = 'user.tier'
      class = 'view-content'
      v-on:switchmode='switchdarkmode()'
    />
  <div class = 'view-border-two bord'></div>
  <footer id = "footer" class = 'view-footer'>
    <div id = "footer-navigation">
      <router-link :to = "{name: 'aboutPage'}" class='footer-nav'>About</router-link>
      <p id = 'footer-divider' style="font-size:15px;">|</p>
      <router-link :to = "{name: 'contactPage'}" class='footer-nav'>Contact</router-link>
    </div>
    <br>
  </footer>
  </div>
</template>

<script>
import sidebar from './components/Sidebar'
//import SignIn from './components/SignIn'
export default {
  name: 'App',
  components:{
    sidebar
  },
  data(){
    return{
    darkmode:($cookies.get('darkmode')=='true'),
    testing:[],
    user: [],
    url:'http://ipinfo.io/json',
    status:1
    }
  },
  methods:{
        changesidebar(){
          const menuBtn = getElementById("menubutton");
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
      this.user = {'id':838383,'status':'a','fontsize':19,'tier':this.status}
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
<style src = '../assets/css/app.css'</style>

