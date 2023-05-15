<template>
<div id = 'chapter'>
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" class="novel-title" v-html='novelData.title'/>
    <div id = 'control-bar'>
        <div class='control-buttons-container' selectable='false'>
            <button class = 'controlbuttons' @click='changeFontSize(1)'>&#65291;</button>
            <button class = 'controlbuttons' @click='changeFontSize(-1)'>&#65293;</button>
            <button class = 'controlbuttons' @click='switchdarkmode()'>&#9680;</button> 
        </div>
        <br><br>
        <div  id = "navigation">
            <NavButton 
                :previous='this.$route.params.chapter != 1'
                :next='this.$route.params.chapter<chapterList.length'
                v-on:move="moveChapters($event)"
                id ='NavButtons'
            />
        </div>
    </div>
    <!--CHAPTER DEPENDENT-->
    <h1 style='font-size:20px;'>{{chapterTitle}}</h1>
    <pre v-html = 'chapterContent' id = 'chapter-content'/>
    <!--CHAPTER DEPENDENT-->
    <NavButton 
        :previous='this.$route.params.chapter != 1'
        :next='this.$route.params.chapter<chapterList.length'
        v-on:move="moveChapters($event)"
        style='margin:auto;float:center;position:relative;left:0px'
    />
</div>
</template>
<script>
import KoFiButton from '../components/KoFiButton'
import NavButton from '../components/Navbutton'
import axios from 'axios'
    export default{
        name: 'Chapter',
        components:{
            KoFiButton,
            NavButton
        },props:[
        'novelData',
        'chapterList'
        ],data(){
            return{
                chapter:[],
                chapterContent:null,
                error:null,
                chapterTitle:null,
            }
        },methods:{
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
        setData(content,title) {
                this.chapterContent = content
                this.chapterTitle = title
        }
        },
        created(){
            const chapter = this.$route.params
            const url = `http://tententranslation.com/chapter?novel=${chapter.title}&chapter=${chapter.chapter}`
            axios.get(url)
                    .then(response => {
                    this.chapterContent = response.data['content']
                    this.chapterTitle = response.data['title']
                    })
                    .catch(err => {
                    console.log(err)
                    }) 
            
            
  },
  mounted(){
      /*
      const v = document.getElementById('chapter-content')
            if($cookies.get('font-size') == null){
                $cookies.set('font-size','19px')
                v.style.fontSize='19px'
            }else{
                v.style.fontSize = $cookies.get('font-size')
            }
            */
  }
  
    }
</script>
<style scoped>
#chapter{
    width:100%;
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
.novel-title{
    color:var(--textColor);
    font-style: italic;
    font-weight:bold;
    font-size:16px;
}
.novel-title:hover{
    color:var(--styleColor)
}
#navigation{
    display:flex;
    flex-direction:row;
}
#custom-select{
    display:flex;
    flex-direction:column;
    position:absolute;
    background-color:white;
    max-height:500px;
    overflow:scroll;
    border:1px solid black;
    border-bottom:2px solid black;
    top:307px;
    width:50%;
    display:none;
}
#control-bar{
    position:relative;
    width:100%;
    right:0px;
}
.chapter-link{
    color:black;
    border-left:1px solid black;
    border-right:1px solid black;
    border-bottom:1px solid black;
    position:relative;
    padding:5px;
    width:100%;
    z-index: 1000;
}
.chapter-link:hover{
    color:var(--styleColor);
    font-weight:bold;
}
#selected-chapter{
    border:1px solid black;
    vertical-align:middle;
    padding-top:12.5px;
    margin-bottom:-5px;
    padding-left:5px;
    font-size:15px;
    height:50px;
    border-radius:5px;
    width:50%;
}
#NavButtons{
    width:180px;
    height:50px;
    padding:5px;
}

.control-buttons-container{
    position:absolute;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    padding:5px;
    border-radius:5px;
    width:180px;
    right:0px;
    border: 1px solid var(--borderColor);
}
button.controlbuttons{
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

</style>