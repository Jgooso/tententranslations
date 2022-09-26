<template>
<div id = 'chapter' v-if='chapter'>
    <div class = "content">
     <br>
        <h3 style = "font-size: 25px" v-html='novelData.title+" - "+chapter.chapternumber'/><!-- chapter number-->
        <Navigator
         :novel-id='novelData.novel'
         :novel='novelData.title'
         :chapter='chapter'
         id = 'chapter-navigator'
        />
        <div id = 'control-bar'>
            <div class='control-buttons-container' selectable='false'>
                <button class = 'controlbuttons' @click='changeFontSize(1)'>+</button>
                <button class = 'controlbuttons' @click='changeFontSize(-1)'>-</button>
                <button class = 'controlbuttons'><font-awesome-icon icon="fa-solid fa-bookmark" /></button>
                <button class = 'controlbuttons'>&#xF288;</button>
            </div>
        <br><br>
        <ChapterSelector
            :chapterList= 'selectorList'
            v-on:changeChapter="updateContent($event)"
        />
       </div>
        <!--<br> <button id = 'editButton' @click='triggerEdit' v-if='tier==5'>Edit</button><br><br>-->
          <pre v-html = 'chapterContent' id = 'chapter-content'/>
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
            this.chapterList.sort((a,b) =>(a.chapternumber > b.chapternumber ? 1:-1))
            return{
                chapter:this.chapterList[this.$route.params.chapter-1],
                chapterContent:'',
                selectorList:[]
            }
        },methods:{
            changeFontSize(change){
                const txt = document.getElementById('chapter-content');
                const style = window.getComputedStyle(txt, null).getPropertyValue('font-size');
                const currentSize = parseFloat(style);
                txt.style.fontSize = (currentSize + change) + 'px';
            },
            triggerEdit(){
                if(document.getElementById('chapter-content').contentEditable=='true'){
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
                document.getElementById('chapter-content').contentEditable='true'
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
            for(var i=0;i < this.chapterList.length; i++){
                this.selectorList.push((({ title, chapternumber }) => ({ title, chapternumber }))(this.chapterList[i]))
            }
            this.selectorList.sort((a,b) =>(a.chapternumber > b.chapternumber ? -1:1))
            
        
        },
    }
</script>
<style scoped>
#chapter-content{
font-family: Times;
font-size:19px;
white-space: pre-wrap;
font-weight:lighter;
overflow:hidden;
margin:auto;
margin-top:25px;
margin-bottom:40px;
}
#control-bar{
    position: -webkit-sticky;
    position:sticky;
    top: 0;
    background-color: var(--backgroundColor);
    padding-top:10px;
    padding-bottom:10px;
}
#editButton{
    width:170px;
    background-color:var(--styleColor);
    color:white;
    float:right;
    border-radius:5px;
}
.control-buttons-container{
    float:right;
    
}
#chapter-navigator{
    margin-bottom:20px;
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