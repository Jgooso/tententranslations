<template>
<div id = 'chapter' v-if='chapterList.length>0'>
    <div class = "content">
     <br>
        <h3 style = "font-size: 25px" v-html='novelData.title+" - "+chapterList[chapterNum].chapterNumber'/>
        <Navigator
         :novel-id='novelData.novel'
         :novel='novelData.title'
         :chapter='chapterList[chapterNum]'
        />
        <br><br><br>
        <ChapterSelector
            :chapterList= 'chapterList'
            v-on:changeChapter="updateContent($event)"
        />
        <br><br>
          <pre v-html = 'chapterList[chapterNum].content' v-if='this.$route.params.password=="abcd"' contenteditable="true" id = 'editable'/>
          <pre v-html = 'chapterList[chapterNum].content' v-else/>
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
    export default{
        name: 'Chapter',
        components:{
            ChapterSelector,
            Navigator,
        },props:[
        'novelData',
        'chapterList',
    ],
        data () {
            return {
                chapterNum: this.$route.params.chapter-1,
            }
        },methods:{
        updateContent(chp){
            this.chapterNum = chp-1
            window.scrollTo({top:0,left:0,behavoir:'smooth'});
            
        }
    },
    
    }
</script>
<style scoped>
pre{
scroll-behavior: smooth;
font-family: Arial, Helvetica, sans-serif;
font-size:20px;
white-space: pre-wrap;
}
</style>