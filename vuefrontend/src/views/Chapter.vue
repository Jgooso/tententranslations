<template>
<div id = 'chapter' v-if='chapter'>
    <div class = "content">
     <br>
        <h3 style = "font-size: 25px" v-html='novelData.title+" - "+chapter.chapternumber'/>
        <Navigator
         :novel-id='novelData.novel'
         :novel='novelData.title'
         :chapter='chapter'
        />
        <br>
        <div class='controlbuttonscontainer' selectable='false'>
            <button class = 'controlbuttons' @click='changeFontSize(1)'>+</button>
            <button class = 'controlbuttons' @click='changeFontSize(-1)'>-</button>
            <!--
            <button class = 'controlbuttons'>{</button>
            <button class = 'controlbuttons'>{</button>
            -->
        </div>
        <br>
        <br>
        <ChapterSelector
            :chapterList= 'chapterList'
            v-on:changeChapter="updateContent($event)"
        />
       
        <br> <button id = 'editButton' @click='triggerEdit' v-if='tier==5'>Edit</button><br>
          <pre v-html = 'chapterContent' id = 'content'/>
        <ChapterSelector
            :chapterList='chapterList'
            v-on:changeChapter="updateContent($event)"
        />
        <br><br>
    </div>
</div>
</template>
<script>
import ChapterSelector from '../components/ChapterSelector'
import Navigator from '../components/Navigator'
import { getAPI } from '../axios-api'
    export default{
        name: 'Chapter',
        components:{
            ChapterSelector,
            Navigator,
        },props:[
        'novelData',
        'chapterList',
        'tier'
        ],data(){
            return{
                chapter:this.chapterList[this.$route.params.chapter-1],
                chapterContent:''
            }
        },methods:{
            changeFontSize(change){
                const txt = document.getElementById('content');
                const style = window.getComputedStyle(txt, null).getPropertyValue('font-size');
                const currentSize = parseFloat(style);
                txt.style.fontSize = (currentSize + change) + 'px';
            },
            triggerEdit(){
                if(document.getElementById('content').contentEditable=='true'){
                    const url = '/chapter?novel='+this.chapter.novelid+'&chapter='+this.chapter.chapternumber
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
                document.getElementById('content').contentEditable='true'
                document.getElementById('editButton').innerHTML='Save'
                }
            }    
        },
        created(){
            const url = '/chapter?novel='+this.chapter.novelid+'&chapter='+this.chapter.chapternumber
            getAPI.get(url)
          .then(response => {
            console.log('Chapter API has recieved data')
            this.chapterContent = response.data
          })
          .catch(err => {
            console.log(err)
          })
            
        
        },
    }
</script>
<style scoped>
pre{
font-family: Helvetica,sans-serif;
font-size:19px;
white-space: pre-wrap;
font-weight:lighter;
overflow:hidden;
}
#editButton{
    width:170px;
    background-color:var(--styleColor);
    color:white;
    float:right;
    border-radius:5px;
}
.controlbuttonscontainer{
    float:right;
    
}
button.controlbuttons{
    border-radius:15px;
    background-color:lightgray;
    height:30px;
    width:30px;
    font-size:20px;
    text-align:center;
    vertical-align:middle;
    line-height:20px;
    margin-left:17px;
    color:var(--styleColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
button.controlbuttons:hover{
    color:white;
    background-color:var(--styleColor);
    transition: all .2s ease;
}
</style>