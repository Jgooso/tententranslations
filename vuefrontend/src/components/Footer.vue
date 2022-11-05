<template>
    <footer id = "footer">
            <div id = "navigation">
                <router-link :to = "{name: 'aboutPage'}" class='footer-nav'>About</router-link>
                <p style="font-size:15px;">|</p>
                <router-link :to = "{name: 'contactPage'}" class='footer-nav'>Contact</router-link>
            </div>
            <br>
    </footer>
</template>

<script>
export default{
    name: 'Footer',
}
</script>
<style scoped>
  #footer{
      height: 150px;
      align-items: center;
      justify-content:center;
      display:flex;
      flex-direction:row;
      margin-bottom:50px;
      grid-row: 3;
      grid-column: 1 / span 3;
      border-top:5px rgba(200,200,200,0.6) solid
 
  }
    #navigation{
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