<template>
<div id = 'chapter' v-if='chapter' onscroll='handleScroll()'>
    <div>
     <br>
        <h3 style = "font-size: 15px;" class='novel-title' v-html='novelData.title'/><!-- chapter number-->
        <div id = 'control-bar'>
            <div class='control-buttons-container' selectable='false'>
             
                <button class = 'controlbuttons' @click='changeFontSize(1)'>&#65291;</button>
                <button class = 'controlbuttons' @click='changeFontSize(-1)'>&#65293;</button>
                  <!--
                <button class = 'controlbuttons'><font-awesome-icon icon="fa-solid fa-bookmark" /></button>-->
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
            <h1 style='font-size:20px;'>{{chapter.title}}</h1>
          <pre v-html = 'chapterContent' id = 'chapter-content'/>
          <NavButton 
            :previous='this.$route.params.chapter != 1'
            :next='this.$route.params.chapter<chapterList.length'
            v-on:move="moveChapters($event)"
            id ='NavButtons'
            />
    </div>
</div>
</template>
<script>
import ChapterSelector from '../components/ChapterSelector'
import Navigator from '../components/Navigator'
import { getAPI } from '../axios-api'
import KoFiButton from '../components/KoFiButton'
import NavButton from '../components/Navbutton'
    export default{
        name: 'Chapter',
        components:{
            ChapterSelector,
            Navigator,
            KoFiButton,
            NavButton
        },props:[
        'novelData',
        'chapterList',
        'tier'
        ],data(){
            this.chapterList.sort((a,b) =>(a.chapternumber > b.chapternumber ? 1:-1))
            return{
                chapter:this.chapterList[this.$route.params.chapter-1],
                chapterContent:'',
                selectorList:[]
            }
        },methods:{
            triggerEdit(){
                if(document.getElementById('chapter-content').contentEditable=='true'){
                    const url = '/chapter?chapter='+this.chapter.id
                    document.getElementById('content').contentEditable='false'
                    document.getElementById('editButton').innerHTML='Edit'
                    const content = document.getElementById('content').innerHTML
                    getAPI.put(url,{content:content})
                        .then(function (response) {
                            console.log(response);
                        })
                        .catch(function (error) {
                            console.log(error);
                        })
                }else{
                document.getElementById('chapter-content').contentEditable='true'
                document.getElementById('editButton').innerHTML='Save'
                }
            }, 
        },
        created(){
            const url = '/chapter?chapter='+this.chapter.id
            getAPI.get(url)
          .then(response => {
            console.log('Chapter API has recieved data')
            this.chapterContent = response.data
          })
          .catch(err => {
            console.log(err)
          })
            for(var i=0;i < this.chapterList.length; i++){
                this.selectorList.push((({ title, chapternumber }) => ({ title, chapternumber }))(this.chapterList[i]))
            }
            this.selectorList.sort((a,b) =>(a.chapternumber > b.chapternumber ? -1:1))
        },
    }
</script>
<style scoped>
#chapter-content{
font-family: sans-serif;
white-space: pre-wrap;
font-weight: 100;
margin:auto;
margin-top:25px;
margin-bottom:40px;
font-size:19px;

}
.novel-title{
    text-decoration:underline;
}
.novel-title:hover{
    color:var(--styleColor)
}
#chapter-navigator{
    margin-bottom:20px;
    left:50;
    z-index:10;
    top:20px;
    height:fit-content;
    transition: all .3s ease-in-out;
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
#myselect{
    padding-left:10px;
    padding-right:10px;
    font-size:15px;
    height:35px;
    background-color: var(--backgroundColor);
    border:none;
    border-radius:5px;
    font-weight:300;
    width:50%;
    color:var(--borderColor);
}
#NavButtons{
    position:relative;
    width:180px;
    height:50px;
    padding:5px;
    margin-left:35%;
}
#control-bar{
    top: 0;
    background-color: var(--backgroundColor);
    padding-top:10px;
    padding-bottom:20px;
    
}

.control-buttons-container{
    float:right;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    padding:5px;
    border-radius:5px;
    position:sticky;
    top:10px;
}
button.controlbuttons{
    border-radius:15px;
    height:30px;
    width:30px;
    font-size:20px;
    text-align:center;
    vertical-align:middle;
    font-weight:bold;
    background-color:var(--backgroundColor);
    line-height:20px;
    margin-left:17px;
    margin-right:10px;
    color:var(--styleColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
#myselect.items{
    background-color:red;
}

@media (max-width:1000px) {
   #myselect{
       min-width:200px;
   }
  }
html:not([data-scroll='0']) {
    #chapter-content{
        background-color:blue;
    }

}
@media (max-width: 775px) {

}
</style>