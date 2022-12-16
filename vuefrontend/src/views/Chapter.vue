<template>
<div id = 'chapter' v-if='chapter' onscroll='handleScroll()'>
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
            v-on:switchmode='$emit("switchmode")'
        />
          <pre v-html = 'chapterContent' id = 'chapter-content'/>
    </div>
</div>
</template>
<script>
import ChapterSelector from '../components/ChapterSelector'
import Navigator from '../components/Navigator'
import { getAPI } from '../axios-api'
import KoFiButton from '../components/KoFiButton'
    export default{
        name: 'Chapter',
        components:{
            ChapterSelector,
            Navigator,
            KoFiButton
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
            handleScroll(){
            if(window.scrollY > 200){
                document.getElementById("chapter-navigator").classList.add('sticky-navigation')
            }else{
                 document.getElementById("chapter-navigator").classList.remove('sticky-navigation')
            }
        }   
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
        mounted(){
            window.addEventListener('scroll', this.handleScroll);
        }
    }
</script>
<style scoped>
#chapter-content{
font-family: Times;
white-space: pre-wrap;
font-weight:lighter;
margin:auto;
margin-top:25px;
margin-bottom:40px;
font-size:19px;

}
#chapter-navigator{
    margin-bottom:20px;
    position:fixed;
    left:50;
    z-index:10;
    top:20px;
    height:50px;
    position: -webkit-sticky;
    text-overflow:ellipsis;
    overflow:hidden;
    transition: all .3s ease-in-out;
}
.sticky-navigation{
    width:75%;
    white-space: nowrap;
   

}
@media (max-width: 775px) {
    .sticky-navigation{
        width:65%;
    }
}
</style>