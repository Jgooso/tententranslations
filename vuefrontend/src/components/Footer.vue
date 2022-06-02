<template>
    <header>
    <div id="footer">
        <div class = "content">
            <div id = "navigation">
                <router-link :to = "{name: 'aboutPage'}" class='nav'>About</router-link>
                <p style="font-size:15px;">|</p>
                <router-link :to = "{name: 'contactPage'}" class='nav'>Contact</router-link>
            </div>
            <br>
        </div>  
    </div>
    </header>
</template>

<script>
export default{
    name: 'Footer',
}
</script>
<style scoped>
  #footer{
      height: fit-content;
      width: 100%;
      align-items: center;
      justify-content:center;
      display:flex;
      flex-direction:row;
      margin-top:50px;
      margin-bottom:50px;
  }
    #navigation{
        height:15px;;
        display:flex;
        align-items:middle;
        margin:auto;
        width:fit-content;
        
    
    }
  .nav{
      color: black;
      margin-left: 15px;
      margin-right:15px;
      font-size: 15px;
      height:15px;
      position: relative;
  }
  p{
      height:15px;
      vertical-align:center;
      line-height:15px;
  }
  .nav:hover{
      color:purple;
      text-decoration: none;
      transition: all .3s ease;
  }
  .content{
      display: flex;
      flex-direction:column;
      
      
  }


</style>