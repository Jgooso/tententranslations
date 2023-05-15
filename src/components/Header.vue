<template>
    <header id = "header">
            <router-link :to = "{name: 'homePage'}" id = 'home-button'>TenTenTranslations</router-link>
            <div id = "header-navigation-bar">
                <router-link :to = "{name: 'Browse'}" class='header-nav' style="text-decoration:none;">Browse</router-link>
                <router-link :to = "{name: 'aboutPage'}" class='header-nav' style="text-decoration:none;">About</router-link>
                <router-link :to = "{name: 'contactPage'}" class='header-nav' style="text-decoration:none;">Contact</router-link>
                <router-link :to = "{name: 'uploadPage'}" class='header-nav' v-if='status.includes("Moderator")'>Manage</router-link>
                <KoFiButton id = 'KoFi' v-else/>
                <div class="menu-btn"  @click='$emit("changesidebar")' ref = 'menubutton'><div class="menu-btn__burger" ></div></div>
            </div>
    </header>
</template>

<script>
import KoFiButton from '../components/KoFiButton'
export default{
    name: 'Header',
    props:{
      'status': String
    },
    components:{
      KoFiButton
    }
}
</script>
<style scoped>
*{
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
  #header{
      align-items: center;
      justify-content:center;
      display:flex;
      flex-direction:row;
      margin-bottom:20px;
      border-bottom:1px solid var(--borderColor);
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
  /* border: 3px solid #fff; */
  
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
</style>