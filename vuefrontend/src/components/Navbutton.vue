<template>
<div>
    <div id = "NavButton" v-if='first'>
        <button @click ="go(first)">Read First</button>
        <button @click ="go(last)">Read Last</button>
    </div>
    <div id = "MoveButton" v-else>
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
#NavButton button {
    cursor: pointer;
    background: purple;
    color: white;
    font-size: 12px;
    border: 0;
    padding: 0.75rem 1rem;
    border-radius: 5px;
    font-weight: bold;
    float:center;
    margin-right: 10px;
  }
  
  button:hover {
    transform: scale(0.98);
  }
  #MoveButton button {
    cursor: pointer;
    background: purple;
    color: white;
    font-size: 17px;
    font-weight: 300;
    border: 0;
    padding: 0.75rem 1rem;
    padding-left:0px;
    padding-right:0;
    align-self:center;
    border-radius: 5px;
    margin-right: 2px;
    width:84px;
    
  }
  #MoveButton{
    position:absolute;
    right:0px;
  }
  button:hover {
    transform: scale(0.98);
  }
  </style>