<template>
<div id = 'chapter' v-if='chapter'>
    <div>
     <br>
        <h3 style = "font-size: 25px" v-html='novelData.title+" - "+chapter.chapternumber'/><!-- chapter number-->
        <Navigator
         :novel-id='novelData.novel'
         :novel='novelData.title'
         :chapter='chapter'
         id = 'chapter-navigator'

        />
        <ChapterSelector
            :chapterList= 'selectorList'
            v-on:changeChapter="updateContent($event)"
        />
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
            var r = document.querySelector(':root');
            console.log(parseInt(r.style.getPropertyValue('--fontsize').slice(0,2))+1 + 'px')
        },
    }
</script>
<style scoped>
#chapter-content{
font-family: Times;
font-size:var(--fontsize);
white-space: pre-wrap;
font-weight:lighter;
overflow:hidden;
margin:auto;
margin-top:25px;
margin-bottom:40px;
}
#chapter-navigator{
    margin-bottom:20px;
    position:relative;
    left:50;
    z-index:2;
}
</style>