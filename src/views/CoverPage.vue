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
        'tier',
        'timezoneOffset'
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
/************************MAIN INFO COVER***************************/
#novel-cover{
    display:grid;
    grid-template-columns: 7.5% 60% 10% 10%;
    align-self:center;
    column-gap:20px;
    row-gap:10px;
    width:100%;
    transition: all .2s ease;
    margin-top:20px;
    padding:20px;   
}
#cover{
    background-color:var(--backgroundColor);
    padding:0px;
    width: 100%;
    height: fit-content;
    display: flex;
    flex-direction: column;
    margin-top:0;
    min-height:500px;
}
#inner{
    display:flex;
    flex-direction:column;
    width:100%;
    transition: all .2s ease;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    margin-top:20px;
    border-radius:25px;
    border: 1px solid var(--borderColor);
}
#noveltitle{
    color: var(--styleColor);
    font-size: 20px;
    margin-bottom: 25px;
    line-height:20px;
    height:fit-content;
    margin-top:30px;
    font-weight:bold;
    font-family: 'Times New Roman', serif;
    
}
#novel-information{
    background-color: rgba(250, 250, 250, 0.8);
    padding:20px;
    width: 100%;
    height:fit-content;
    display: flex;
    flex-direction: column;
}
.label{
    font-weight: bold;
    vertical-align: top;
    color:var(--textColor);
    line-height: 20px;
    vertical-align: bottom;
    
}
.info{
    font-weight:normal;
    line-height: 20px;
    vertical-align: bottom;
    color:rgb(136,136,136);
    font-size:14px;

}
a{
    color:rgb(139, 139, 139);
    font-size: 12px;
    text-decoration:none;
}
a:hover{
    color:var(--styleColor)
}

.selectable{
    font-size:14px;
    color:var(--textColor);
}
a:hover { 
  color: var(--styleColor);
  transition: all .2s ease;
}
.comma-list {
    display: inline;
}
.comma-list li {
    display: inline;
}
.selectable:hover {
    color:var(--styleColor);
    text-decoration:none;
}
.comma-list li::after {
    content: ", ";
}
.comma-list li:last-child::after {
      content: "";
}
 .column1{
     grid-column:1 / span 1;
 }
 .column2{
     grid-column:2 / span 1
 }
 .column3{
     grid-column:3/ span 1;
 }
 .column4{
     grid-column:4/ span 1
 }
@media (max-width: 775px) {
    #inner{
        flex-direction:column;
    }
    #novel-cover{
        display:flex;
        flex-direction:column;
    }
    #noveltitle{
        margin-bottom: 0px;
    }
 }
/************************MAIN INFO COVER END***************************/

/***************************DESCRIPTION********************************/
#summary{
    width: 100%;
    text-align: left;
    display: flex;
    flex-direction: column;
    align-self: center;
    height:fit-content;
    padding:20px;
}
#description{
    width:100%;
    font-size: 14px;
    color:rgb(136,136,136);
    height:fit-content;
}
/************************DESCRIPTION END******************************/

/***********************TABLE OF CONTENTS*****************************/
#TableOfContents{
    width: 100%;
    margin:auto;
    vertical-align:center;
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
    border:none;
}

#tableofcontentList{
    height:fit-content;
    /*max-height:1000px;*/
    overflow-y:hidden;
}

.section{
    width:100%;
    display:flex;
    flex-direction:row;
    border:none;
    background:none;
    height:fit-content;
    /*min-height:45px;*/
    position: relative;
    font-weight:bold;
    height:30px;
    font-size:20px;

}
#switcher{
    width:30px;
    height:30px;
    font-size:18px;
    padding:0;
    margin-left:50px;
    font-weight:bold;
    background:none;
    justify-content:center;
}
.expand{
    position:absolute;
    right:0;
    background-color:lightgray;
    height:25px;
    width:25px;
    vertical-align:center;
    line-height:25px;
    font-size:20px;
    font-weight:lighter;
    
}
.full-section{
     box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
button:hover{
    color:var(--styleColor);
}
ul{
    list-style: none;
    padding: 0px;
}
.date{
    font-size:12px;
    position:absolute;
    right:0;
    font-style:italic;
    line-height:15px;
    color:gray;
    margin-right:10px;
    padding:8px;
    border-radius:5px;
}
.title{
    padding:8px;
    position:absolute;
    line-height:17px;
    left:5;
    font-size:17px;
    border-radius:5px;
}

.group{
    width:100%;
    display:flex;
    flex-direction:row;
    background:none;
    min-height:35px;
    height:fit-content;
    position: relative;
    font-weight:300;
    vertical-align:center;
    margin-top:8px;
    border-radius:5px;
    border: 1px solid var(--borderColor);
    transition: all .1s ease;
    
}
.group:hover{
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
#group:hover #title{
color:var(--styleColor);
font-weight:bold;

}
select{
    background:none;
    border:none;
    -webkit-appearance: none;
}
@media (max-width: 1200px){
    #TableOfContents{
        width:100%; 
     }
 }
@media (max-width: 775px) {
    .group{
        flex-direction:column;
    }
    .date{
       position:relative;
       padding-left:10px;
    }
    .title{
        position:relative;
        margin-bottom:10px;
    }
}
/*********************TABLE OF CONTENTS END***************************/

</style>

