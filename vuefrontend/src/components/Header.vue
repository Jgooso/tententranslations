<template>
    <header>
    <div id="header">

        <div class = "content">
            <img src = '../assets/TenTenTranslations.png' alt = 'Search' id='logo'>
            <div id = "navigation">
                <router-link :to = "{name: 'Browse'}" class='nav'>Browse</router-link>
                <router-link :to = "{name: 'aboutPage'}" class='nav'>About</router-link>
                <router-link :to = "{name: 'contactPage'}" class='nav'>Contact</router-link>
                <router-link :to = "{name: 'Browse'}" id = 'search'><img src = '../assets/search.png' alt = 'Search'></router-link>
                <div class="menu-btn"  @click='$emit("changesidebar")' ref = 'menubutton'><div class="menu-btn__burger" ></div></div>
            </div>
        </div>  
    </div>
<!--
    <div id = "login">
        <div class = "content">
         <button> Sign-in </button>
         <button> Sign-up </button>
         </div>
    </div>
-->
    </header>
</template>

<script>
export default{
    name: 'Header',
}
</script>
<style scoped>
*{
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
  #header{
      height: 130px;
      width: 100%;
      align-items: center;
      justify-content:center;
      background-color: purple;
      display:flex;
      flex-direction:row;
  }
  #login{
      width:100%;
      padding: 12px;
      background-color:white;
      z-index: 10;  
  }
  button{
          height: 35px;
          width: 85px;
          border-radius: 40px;
          border: 2px solid rgb(107,107,107);
          background-color: white;
          font-size: 15px;
          font-weight: bold;
          color: rgb(107,107,107);
          margin-left: 5px;
          
      }
    #navigation{
        height:100%;
        display:flex;
        align-items:center;
    }
    button:hover{
        background-color:black;
        color:white;
        transition: all .2s ease;
        -webkit-transition: all .22s ease;
    }
  .nav{
      color: white;
      font-weight:bold;
      width: 100px;
      margin-left: 35px;
      font-size: 15px;
      position: relative;
      transition: all .3s ease-in-out;
      overflow:hidden;
  }
  
  #navigation{
    margin-left: 35px;
    width:800px;
    height:100%;
    align-items:center;
    
  }
  
  #search{
      margin-left:25px;
      width:35px;
      height:35px;
      border-radius:20px;
      background-color:white;
      display: flex;
      align-items:center;
      float: right;
      align-self:right;
      position: absolute;
      right:70px;
  }
  #search img{
      width: 20px;
      height: 20px;
      background-color:white;
      
      margin:auto;
  }
  .content{
      display: flex;
      position:relative;
      
  }
  p{
      font-size: 50px;
      color:white;
      margin-left: 35px;
      display:none;
  }
#logo{
     min-width:200px;
     height:110px;
     margin-top:auto;
     margin-bottom:auto;
}

.menu-btn {
  position: absolute;
  right:-800px;
  display: flex;
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
  background: #fff;
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
  background: #fff;
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
@media (max-width: 950px) {
    .content{
        display: flex;
        flex-direction: row;
    }
    .nav{
        width:0px;  
         transition: all .3s ease-in-out;
    }
    #search{
       
    }
    .menu-btn{
        right:0px;
        transition: all .2s ease-in-out;
    }
}
</style>