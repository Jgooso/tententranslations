<template>
<div>
    <div id = "MoveButton">
        <button v-if='previous' @click ="go(this.$route.params.chapter-1)">&#8592; Prev</button>
        <button v-if='next' @click ="go(parseInt(this.$route.params.chapter)+1)">Next &#8594;</button>
    </div>
</div>
</template>
<script>
    export default{
        name: 'NavButton',
        props:[
            'first',
            'last',
            'previous',
            'next'
        ],
        methods:{
            go(chapter){
              this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:chapter}})
            }

        }
    }
</script>
<style scoped>  
  button:hover {
    transform: scale(0.98);
  }
  #MoveButton button {
    cursor: pointer;
    background: var(--styleColor);
    color: white;
    font-size: 17px;
    font-weight: 300;
    border: 0;
    padding-left:0px;
    padding-right:0;
    align-self:center;
    border-radius: 5px;
    margin-right: 2px;
    width:86px;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    border: 1px solid var(--borderColor);
  }
  #MoveButton{
    position:absolute;
    right:0px;
  }
  button:hover {
    transform: scale(0.98);
  }
  </style>