<template>
    <footer class = "footer">
        <div class = "content">
            <div id = "navigation">
                <router-link :to = "{name: 'aboutPage'}" class='nav'>About</router-link>
                <p style="font-size:15px;">|</p>
                <router-link :to = "{name: 'contactPage'}" class='nav'>Contact</router-link>
            </div>
            <br>
        </div>  
    </footer>
</template>

<script>
export default{
    name: 'Footer',
}
</script>
<style scoped>
  .footer{
      height: 75px;
      align-items: center;
      justify-content:center;
      display:flex;
      flex-direction:row;
      margin-top:50px;
      margin-bottom:50px;
      grid-row: 3;
      grid-column: 1 / span 3;
 
  }
    #navigation{
        height:15px;;
        display:flex;
        align-items:middle;
        margin:auto;
        width:fit-content;
        
    
    }
  .nav{
      color: var(--textColor);
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
      color:var(--styleColor);
      text-decoration: none;
      transition: all .3s ease;
  }
  .content{
      display: flex;
      flex-direction:column;
      
      
  }


</style>