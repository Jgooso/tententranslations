<template>
  <div id="app">
   <div id = 'sidemenu'>
    <div id = 'sidebar'>
      <h3 @click='swap()' id = 'close-sidebar-button'>&#9587;</h3>
      <router-link :to = "{name: 'Browse'}" class='sidebar-nav'  @click.native='changesidebar()' style="text-decoration:none;">Browse</router-link>
      <router-link :to = "{name: 'aboutPage'}" class='sidebar-nav' @click.native='changesidebar()' style="text-decoration:none;">About</router-link>
      <router-link :to = "{name: 'contactPage'}" class='sidebar-nav' @click.native='changesidebar()' style="text-decoration:none;">Contact</router-link>
      <KoFiButton class = 'nav' id = 'KoFi-sidebar'/>
    </div>
    <div id ='shade' @click='changesidebar()'/><!--SHADE THE COVERS BACKGROUND AND REMOVES SIDEBAR WHEN CLICKED-->
  </div>
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
 
  <div class = 'view-border-one bord'/><!--LEFT BORDER  PADDING-->
  <!--CENTER CONTENT-->
    <router-view
      :tier = 'user.tier'
      class = 'view-content'
      v-on:switchmode='switchdarkmode()'
    />
   <!--CENTER CONTENT END-->
  <div class = 'view-border-two bord'/><!--RIGHT BORDER  PADDING-->

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
export default {
  name: 'App',
  data(){
    return{
      darkmode:($cookies.get('darkmode')=='true'),//WHETHER OR NOT IN DARK MODE
      user: [],//USER INFO
      url:'http://ipinfo.io/json',//FOR LOCATION TRACKING WHEN IMPLEMENTED TODO
      status:1//TIER AS A USER; SET TO ONE FOR NOW TODO
    }
  },
  methods:{
        /* OPENS AND CLOSES THE SIDEBAR*/
        changesidebar(){
          const menuBtn = document.getElementById("menubutton");
          const sidebar = document.getElementById("sidebar");
          const shade = document.getElementByID("shade");
          if(sidebar.style.left=='0px'){
            sidebar.style.left='-300px';
            shade.style.opacity='0';
            menuBtn.classList.remove('open');
          }else{
            sidebar.style.left='0px';
            shade.style.opacity='0.5';
            menuBtn.classList.add('open');
          }
          
        },
        /*SETS DARKMODE WHEN FIRST CREATED*/
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
        /* SWITCHES BEWTWEEN LIGHT AND DARKMODE*/
        switchdarkmode(){
          this.darkmode=!this.darkmode
          this.setdarkmode()
          $cookies.set('darkmode',this.darkmode)
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
  button{
  border:none;
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
    outline:none;
    min-height:1000px;
  }
  .fade-enter-active {
    transition: opacity 1s ease-out;
    transition-delay: 1s;
  }
  .fade-enter {
    opacity: 0;
  }
  .fade-enter-to {
    opacity: 1;
  }
  .fade-move {
    transition: transform 1s;
  }
  /********HEADER CSS*********/
  #header{
    align-items: center;
    justify-content:center;
    display:flex;
    flex-direction:row;
    margin-bottom:20px;
    border-bottom:1px solid var(--borderColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
  }
  #header-navigation-bar{
    height:100%;
    display:flex;
    align-items:center;
    margin-left: 35px;
    width:800px;
    height:100%;
    align-items:center;
  }
  #home-button{
    background:none;
    width:fit-content;
    height:fit-content;
    margin-top:auto;
    margin-bottom:auto;
    font-family:cursive;
    color:var(--styleColor);
    font-size:25px;
    float:left;
    margin-left:20px;
  }
  .header-nav{
    color: var(--textColor);
    font-weight:bold;
    margin-left: 35px;
    font-size: 15px;
    position: relative;
    transition: all .3s ease-in-out;
    overflow:hidden;
    text-align: center;
    padding:10px;
    height:100%;
    border-radius:5px;
  }
  .header-nav:hover{
    background-color:rgba(50,50,50,0.2)
  }
  #KoFi{
    width:200px;
    margin-left:35px;
  }
  .menu-btn {
    display:none;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 40px;
    cursor: pointer;
    transition: all .3s ease-in-out;
  }
  .menu-btn__burger {
    width: 30px;
    height: 3px;
    background: var(--textColor);
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(255,101,47,.2);
    transition: all .3s ease-in-out;
  }
  .menu-btn__burger::before,
  .menu-btn__burger::after {
    content: '';
    position: absolute;
    width: 30px;
    height: 3px;
    background: var(--textColor);
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(255,101,47,.2);
    transition: all .3s ease-in-out;
    
  }
  .menu-btn__burger::before {
    transform: translateY(-16px);
  }
  .menu-btn__burger::after {
    transform: translateY(16px);
  }
  /* ANIMATION */
  .menu-btn.open .menu-btn__burger {
    transform: translateX(-50px);
    background: transparent;
    box-shadow: none;
    
  }
  .menu-btn.open .menu-btn__burger::before {
    transform: rotate(45deg) translate(35px, -35px);
  }
  .menu-btn.open .menu-btn__burger::after {
    transform: rotate(-45deg) translate(35px, 35px);
  }
  .user-dropdown-box{
    display:none;
  }
  /*HEADER CSS END*/
  /*FOOTER CSS*/
  #footer{
    height: 150px;
    align-items: center;
    justify-content:center;
    display:flex;
    flex-direction:row;
    margin-bottom:50px;
    margin-top:50px;
    grid-row: 3;
    grid-column: 1 / span 3;
    border-top:5px rgba(200,200,200,0.6) solid
    }
  #footer-navigation{
    height:15px;;
    display:flex;
    align-items:middle;
    margin:auto;
    width:fit-content;
  }
  .footer-nav{
    color: var(--textColor);
    margin-left: 15px;
    margin-right:15px;
    font-size: 15px;
    height:15px;
    position: relative;
  }
  #footer-divider{
    height:15px;
    vertical-align:center;
    line-height:15px;
  }
  .footer-nav:hover{
    color:var(--styleColor);
    text-decoration: none;
    transition: all .3s ease;
  }
  /*FOOTER CSS END*/
#sidemenu{
     position:absolute;
     width:100%;
     height:100%;
     top:0;
     left:0;
     pointer-events: none;
     z-index:8;
}
#sidebar{
   width:50%;
   max-width:300px;
   background-color:var(--backgroundColor);
   top:0;
   left:-300px;
   position:absolute;
   height:100%;
   z-index:10;
   pointer-events: auto;
   transition: all .3s ease-in-out;
   justify-content:center;
   padding-top:50px;
   border-right:1px solid var(--borderColor);
   user-select: none;
   -webkit-user-select: none;
   -webkit-touch-callout: none;
}
#close-sidebar-button{
   color:var(--textColor);
   font-weight:100;
   margin-top:100px;
   transition: all .3s ease-in-out;
   height:fit-content;
   margin:auto;
   width:fit-content;
   
}
#close-sidebar-button:hover{
  transform: rotate(90deg)

}
#shade{
   width:100%;
   height:100%;
   background-color:rgba(20,20,20);
   transition: all .3s ease-in-out;
   opacity:0;
}
.sidebar-nav{
    .ccolor:var(--textColor);
     max-width: 200px;
     font-size: 15px;
     position: relative;
     height:75px;
     border-bottom: 1px solid rgba(127, 127, 127, .5);
     margin:auto;
     font-weight:300;
     vertical-align: middle;
     line-height:75px;
 }
 #KoFi-sidebar{
     margin-top:20px;
 }
   
 @media (max-width: 1200px){
    #app{
      display:flex;
      flex-direction:column;
    }
    .view-content{
      width:92.5%;
      transition: all .3s ease;
      min-width:0px;
      background-color:red;
    }
    .bord{
      display:none;
    }
  }
  
  @media (max-width: 950px) {
      .header-nav{
          width:0;  
           transition: all .3s ease-in-out;
           display:none;
      }
      .menu-btn{
          right:10px;
          position:absolute;
          transition: all .2s ease-in-out;
          display: flex;
      }
      #header-navigation{
        width:0px;
      }
      #home-button{
        position:absolute;
        left:50px;
        transition: all .2s ease-in-out;
        margin-left:0px;
      }
      #KoFi{
        width:0px;
        display:none;
        transition: all .2s ease-in-out;
      }
  }
    @media (max-width: 775px) {
        .view-content{
            margin-top: 30px;
            /*margin: auto;*/
            transition: all .3s ease;
            width:100%;
            grid-column: 1 / span 3;
            padding:10px;
            background-color:blue;
        }
    
    }
    </style>