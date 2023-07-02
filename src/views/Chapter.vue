<template>
<div id = 'chapter'>
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" id="novel-title" v-html='novelData.title'/>
    <div id = 'control-bar'>
        <div id='control-buttons-container'>
            <button class = 'control-buttons' @click='changeFontSize(1)'>&#65291;</button>
            <button class = 'control-buttons' @click='changeFontSize(-1)'>&#65293;</button>
            <button class = 'control-buttons' @click='switchdarkmode()'>&#9680;</button> 
        </div>
        <br><br>
        <div class = "NavButtons" id = "TopButtons">
            <button v-if='this.chapter.chapter != 1' @click ="go(this.chapter.chapter-1)" class = 'move-button'>&#8592; Prev</button>
            <button v-if='this.chapter.chapter < chapterList.length' @click ="go(parseInt(this.chapter.chapter)+1)" class = 'move-button'>Next &#8594;</button>
        </div>
    </div>
    <!--CHAPTER DEPENDENT-->
    <h1 style='font-size:20px;'>{{chapterTitle}}</h1>
    <pre v-html = 'chapterContent' id = 'chapter-content'/>
    <!--CHAPTER DEPENDENT-->
    <div class = "NavButtons" id = "BottomButtons">
        <button v-if='this.chapter.chapter != 1' @click ="go(this.chapter.chapter-1)" class = 'move-button'>&#8592; Prev</button>
        <button v-if='this.chapter.chapter < chapterList.length' @click ="go(parseInt(this.chapter.chapter)+1)" class = 'move-button'>Next &#8594;</button>
    </div>
        
</div>
</template>
<script>
import axios from 'axios'
export default{
    name: 'Chapter',
    props:[
        'novelData',
        'chapterList',
    ],
    data(){
        return{
            chapter:[],
            chapterContent:null,
             error:null,
            chapterTitle:null,
        }
    },
    methods:{
        changeFontSize(change){
            const v = document.getElementById('chapter-content')
            const newFontSize = parseInt(getComputedStyle(v).getPropertyValue('font-size').slice(0,2))+change
            if(newFontSize > 6){
                v.style.fontSize=newFontSize+'px'
                $cookies.set('font-size',newFontSize+'px')
            }
        },
        switchdarkmode(){
            this.$emit("switchmode")
        },
        go(chapter){
              this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:chapter}})
        }
    },
    created(){
        this.chapter = this.$route.params
        const url = `http://127.0.0.1:5000/chapter?novel=${this.chapter.title}&chapter=${this.chapter.chapter}`
        axios.get(url).then(response => {
            this.chapterContent = response.data['content']
            this.chapterTitle = response.data['chapter_title']
        }).catch(err => {
            console.log(err)
        })          
    },
    mounted(){
        const v = document.getElementById('chapter-content')
        if($cookies.get('font-size') == null){
            $cookies.set('font-size','19px')
            v.style.fontSize='19px'
        }else{
            v.style.fontSize = $cookies.get('font-size')
        } 
  }
  
}
</script>
<style scoped>
#chapter{
    width:100%;
    display: flex;
    flex-direction:column;
}
#novel-title{
    color:var(--textColor);
    font-style: italic;
    font-weight:bold;
    font-size:16px;
}
#novel-title:hover{
    color:var(--styleColor)
}
#control-bar{
    position:relative;
    width:100%;
    right:0px;
}
#control-buttons-container{
    position:absolute;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    padding:5px;
    border-radius:5px;
    width:180px;
    right:0px;
    border: 1px solid var(--borderColor);
}
.control-buttons{
    border-radius:15px;
    height:30px;
    width:30px;
    font-size:20px;
    text-align:center;
    vertical-align:middle;
    font-weight:bold;
    margin-left:22.5px;
    background-color:var(--backgroundColor);
    line-height:20px;
    color:var(--styleColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
#TopButtons{
    width:180px;
    height:50px;
    padding:5px;
}
#chapter-content{
    font-family: sans-serif;
    white-space: pre-wrap;
    font-weight: 100;
    margin:auto;
    margin-top:25px;
    margin-bottom:40px;
    font-size:19px;
    min-height:1000px;
}
 .move-button:hover {
    transform: scale(0.98);
  }
  .move-button {
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
  .NavButtons{
    position:absolute;
    right:0px;
    display:flex;
    flex-direction:row;
  }
  #BottomButtons{
    margin:auto;
    float:center;
    position:relative;
    left:0px
  }


</style>