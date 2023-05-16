<template>
<div>
 <!--COVER-->
  <div id="cover" ref = 'cover'>
    <div v-if='novelData.title'>
        <p id = "noveltitle" v-text='novelData.title'/>
        <div id = "inner">
            <img id = "image-border" :src="novelData.imageurl" v-if='novelData.imageurl'>
                <div id = "novel-cover">
                    <div class = 'column1 label'>Views</div>
                    <div class = 'column2 info ' v-text='novelData.views'/>
                    <div class = 'column1 label'>Alternative</div>
                    <div class = 'column2 info ' v-text='novelData.alternativetitle'/>
                    <div class = 'column1 label'>Raw</div>
                    <div class = 'column2 info' ><a :href="novelData.url" class = 'selectable'>{{novelData.url}}</a></div>
                    <div class = 'column1 label'>Author</div>
                    <div class = 'column2 info' ><router-link :to = "{name: 'explorePage', params:{browsetype:'novel-authors',identifier:novelData.authors}}" class='selectable' v-text='novelData.authors'/></div>
                    <div class = 'column1 label'>Genres</div>
                    <div class = 'column2 info' >
                        <ul class='comma-list'>
                            <li v-for='genre in novelData.genres' :key='genre'>
                                <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-genres',identifier:genre}}" class='selectable' v-text='genre'/>
                            </li>
                        </ul>
                    </div>
                    <div class = 'column1 label'>Tags</div>
                    <div class = 'column2 info' >
                        <ul class='comma-list'>
                            <li v-for='tag in novelData.tags' :key='tag'>
                                <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-tags',identifier:tag}}" class='selectable' v-html='tag'/>
                            </li>
                        </ul>
                    </div>
                    <div class = 'column3 label' style='grid-row:1/span 1'>Release</div>
                    <div class = 'column4 info' style='grid-row:1/span 1' v-text='novelData.novelrelease'/>
                    <div class = 'column3 label' style='grid-row:2/span 1'>Status</div>
                    <div class = 'column4 info' style='grid-row:2/span 1'>
                        <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-status',identifier:'u'+novelData.uploadstatus}}" class='selectable' v-text='novelData.uploadstatus'/>
                    </div>
                    <div class = 'column3 label' style='grid-row:3/span 1'>Novel</div>
                    <div class = 'column4 info' style='grid-row:3/span 1' v-if='!editable' v-text='novelData.novelstatus'/>
            </div>    
        <div id = "summary">
        <div v-if='novelData.title'>
          <p style='font-weight:bold'>SUMMARY</p>
            <p id="description" v-html = 'novelData.description'/>
        </div>
    </div>
        </div>     
    </div>
</div>

  <!--SUMMARY-->
  
    <br>
 <!--TABLE OF CONTENTS-->
  <div id = "TableOfContents">
        <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;">
            <UtfBox shape = '&#xe047;'/>
            <h3  id = "divider">Table Of Contents</h3>
            <button id = "switcher" @click ="sortToc">&#x21C5;</button>
        </div>
        <ul  id = 'tableofcontentList' ref='tableofcontentlist'>
        <li v-for="section in sectionList" :key="section.section">
            <button v-if='section.title' class = 'section'>
                <h3 v-text='section.title'/>
                <!--<p class = "expand">-</p>-->
            </button>
            <br>
            <ul v-bind:id = "section.section" >
                <li v-for="chapter in chapterList.filter(chapter=>chapter.section==section.section)" :key='chapter.chapterorder' >
                <router-link 
                    :to = "{name: 'chapterPage', params:{title:novelData.novelid,chapter:chapter.chapternumber,id:chapter.id}}" class="group">
                    <p class = 'title'>{{chapter.title}}</p>
                    <p class = 'date'>{{chapter.uploaddate}}</p>
                </router-link>
                </li>
            </ul>
        </li>
        </ul>
    </div>
</div>
</template>

<script>
  import UtfBox from '../components/UtfBox'
  export default {
    name: 'CoverPage',
    components: {
      UtfBox
    },
    props:[
        'novelData',
        'sectionList',
        'chapterList',
        'tier'
    ],data(){
        return{
        editable:false
        }
    }
    ,methods:{
        trigger(d1){
            var x = document.getElementById(d1);
            if (x.style.display == "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
        },
        sortToc(){
            this.chapterList.reverse()
            this.sectionList.reverse()
        }
    },
    created(){
        this.chapterList.sort((a,b) =>(a.chapternumber > b.chapternumber ? -1:1));
        this.sectionList.sort((a,b) =>(a.section > b.section ? -1:1));
    },
  }
</script>
<style scoped>
@import '../../assets/css/cover-page-cover.css';
@import '../../assets/css/cover-page-summary.css';
@import '../../assets/css/cover-page-table.css';
 *{
    font-weight:300;
 } 
#divider{
    font-size:18px;
    font-weight:bold;
    margin-left:15px;
    line-height:18px;
    padding-top:6px;
}
</style>

