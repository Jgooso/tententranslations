<template>
<div id = 'sidemenu'>
    <div id = 'sidebar' ref='sidebar'>
        <h3 @click='swap()'>&#9587;</h3>
        <router-link :to = "{name: 'Browse'}" class='nav'  @click.native='swap()' style="text-decoration:none;">Browse</router-link>
        <router-link :to = "{name: 'aboutPage'}" class='nav' @click.native='swap()' style="text-decoration:none;">About</router-link>
        <router-link :to = "{name: 'contactPage'}" class='nav' @click.native='swap()' style="text-decoration:none;">Contact</router-link>
        <KoFiButton class = 'nav' id = 'KoFi'/>
    </div>
    <div id ='shade' @click='swap()' ref='shade'/>
    </div>
</template>

<script>
import KoFiButton from '../components/KoFiButton'
export default{
    name:'sidebar',
    components:{
        KoFiButton
    },
    methods:{
        swap(){
            this.$emit("changesidebar")
        }
    }
}

</script>

<style scoped>
*{
     user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none;
}
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
}
h3{
    color:var(--textColor);
    font-weight:100;
    margin-top:100px;
    transition: all .3s ease-in-out;
    height:fit-content;
    margin:auto;
    width:fit-content;
    
}
h3:hover{
   transform: rotate(90deg)

}
#shade{
    width:100%;
    height:100%;
    background-color:rgba(20,20,20);
    transition: all .3s ease-in-out;
    opacity:0;
}
.nav{
       color:var(--textColor);
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
  #KoFi{
      margin-top:20px;
  }
</style>