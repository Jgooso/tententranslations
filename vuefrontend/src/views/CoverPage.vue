<template>
<div>

 <!--COVER-->
  <div id="cover" ref = 'cover'>
    <div v-if='novelData.title'>

        <Navigator
         :novelid='novelData.id'
         :novel='novelData.title'
        />
        <p id = "noveltitle" v-text='novelData.title'/>
        <div id = "inner">
            <img id = "image-border" :src="novelData.imageurl" v-if='novelData.imageurl'>
            <div id = "novel-information">
             <div id = "data">
                <table>
                    <tr>
                        <td>Views</td>
                        <td v-text='novelData.views' class='info'/>
                    </tr>
                    <tr>
                        <td>Alternative</td>
                        <td v-text='novelData.alternativetitle' class="info"/>
                    </tr>
                    <tr>
                        <td>Raw</td>
                        <td class="info"><a :href="novelData.url" class = 'selectable'>{{novelData.url}}</a></td>
                    </tr>
                    <tr>
                        <td>Author</td>
                        <td class="info"><router-link :to = "{name: 'explorePage', params:{browsetype:'novel-authors',identifier:novelData.authors}}" class='selectable' v-text='novelData.authors'/></td>
                    </tr>
                    <tr>
                        <td>Genres</td>
                        <td class="info">
                            <ul class='comma-list'>
                                <li v-for='genre in novelData.genres' :key='genre'>
                                    <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-genres',identifier:genre}}" class='selectable' v-text='genre'/>
                                </li>
                            </ul>
                        </td>
                    </tr>
                    <tr>
                        <td>Tags</td>
                        <td class="info">
                            <ul class='comma-list'>
                                <li v-for='tag in novelData.tags' :key='tag'>
                                    <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-tags',identifier:tag}}" class='selectable' v-html='tag'/>
                                </li>
                            </ul>
                        </td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <td>Release</td>
                        <td class="info" v-text='novelData.novelrelease'/>
                    </tr>
                    <tr>
                        <td>Status</td>
                        <td class="info">
                            <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-status',identifier:novelData.uploadstatus}}" class='selectable' v-text='novelData.uploadstatus'/>
                        </td>
                    </tr>
                    <tr>
                        <td>Novel</td>
                        <td class="info" v-if='!editable' v-text='novelData.novelstatus'/>
                    </tr>
                </table>
             </div>
             <br>
             
             <NavButton 
                :first="1"
                :last='chapterList.length'
             />
             <br>
            </div>   
        </div>     
    </div>
</div>
  <br>
  <!--SUMMARY-->
  <div id = "summary">
        <div v-if='novelData.title'>
           <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;"><UtfBox shape = '&#9733;'/><h3 id = "divider">SUMMARY</h3></div><br>
            <p id="description" v-html = 'novelData.description'/>
        </div>
    </div>
 <!--TABLE OF CONTENTS-->
  <div id = "TableOfContents">
        <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;">
            <UtfBox shape = '&#xe047;'/>
            <h3  id = "divider">Latest Chapters</h3>
            <button id = "switcher" @click ="sortToc">&#x21C5;</button>
        </div>
        <ul  id = 'table' ref='tableofcontentlist'>
        <li v-for="section in sectionList" :key="section.section">
            <button v-if='section.title' @click="trigger(section.section)" class = 'section'>
                <h3 v-text='section.title'/>
                <p class = "expand">-</p>
            </button>
            <br>
            <ul v-bind:id = "section.section">
                <li v-for="chapter in chapterList.filter(chapter=>chapter.section==section.section)" :key='chapter.chapterorder'>
                <router-link 
                    :to = "{name: 'chapterPage', params:{title:novelData.novelid,chapter:chapter.chapternumber}}" class="group">
                    <p class = 'title'>{{chapter.title}}</p>
                    <p class = 'date'>{{new Date(chapter.uploaddate).toLocaleString('default', { month: 'long', day:'numeric', year:'numeric' })}}</p>
                </router-link>
                </li>
            </ul>
        </li>
        </ul>
        <button @click='showMore()' id = 'showMore' v-if='chapterList.length+sectionList.length > 25'>Show More &#9662;</button>
    </div>
</div>
</template>

<script>
  import Navigator from '../components/Navigator'
  import UtfBox from '../components/UtfBox'
  import NavButton from '../components/Navbutton'
  import KoFiButton from '../components/KoFiButton'
  import {getAPI} from '../axios-api'
  export default {
    name: 'CoverPage',
    components: {
      UtfBox,
      Navigator,
      NavButton,
      KoFiButton
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
        },
       showMore(){
           //console.log('clicked')
           document.getElementById('table').style.maxHeight="none";
           document.getElementById('showMore').style.display='none'
       },
       
       
    },
    created(){
        this.chapterList.sort((a,b) =>(a.chapternumber > b.chapternumber ? -1:1))
        this.sectionList.sort((a,b) =>(a.section > b.section ? -1:1))
    },
  }
</script>
<style scoped>
 *{
    font-weight:300;
 } 
 
#summary{
    width: 100%;
    text-align: left;
    display: flex;
    flex-direction: column;
    align-self: center;
    height:fit-content;
}

#description{
    width:100%;
    font-size: 14px;
    color:rgb(136,136,136);
    height:fit-content;
}
#TableOfContents{
    width: 100%;
    margin:auto;
    vertical-align:center;
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
    border:none;
}
 a{
      color:rgb(139, 139, 139);
      font-size: 12px;
      text-decoration:none;
  }
  a:hover{
      color:var(--styleColor)
  }
  #navigator{
      margin-bottom:30px;
      margin-top: 30px;
  }
  #inner{
      align-self:center;
      display:flex;
      flex-direction:row;
      width:100%;
      transition: all .2s ease;
  }
  
  #image-border{
    max-height:313px;
    background-color: var(--backgroundColor));
    float:left;
    padding-left: 15px;
    padding-right:15px;
    margin-right:30px;
    transition: all .2s ease;
}
  #noveltitle{
      color: var(--styleColor);
      font-size: 20px;
      margin-bottom: 25px;
      line-height:20px;
      height:fit-content;
      margin-top:30px;
  }
 
  #novel-information{
      background-color: rgba(250, 250, 250, 0.8);
      padding:20px;
      width: 100%;
      height:fit-content;
      display: flex;
      flex-direction: column;
  }
  #data{
      display:flex;
      flex-direction:row;
  }
  table{
      display:inline;
      font-size: 15px;
      max-width: 100%;
      
  }
  td{
      font-weight: bold;
      padding-bottom: 10px;
      padding-right:20px;
      width:15%;
      min-width:125px;
      vertical-align: top;
      
  }
  .info{
      font-weight:normal;
      width: 85%;
      line-height: 20px;
      vertical-align: bottom;
      color:rgb(136,136,136);
      font-size:14px;
  }
  .selectable{
      font-size:14px;
      color:#3c3c3c
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
  
  
#table{
    height:fit-content;
    max-height:1000px;
    overflow-y:hidden;
}
#showMore{
    margin-left:auto;
    margin-right:auto;
    width:fit-content;
    font-weight:bold;
    background:none;
}

.section{
    width:100%;
    display:flex;
    flex-direction:row;
    border:none;
    background:none;
    height:45px;
    position: relative;
    padding-top:15px;
    font-weight:300;
   

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
}
.title{
    padding-left:10px;
    position:absolute;
    line-height:17px;
    left:5;
    font-size:17px;
}
.group:hover .title{
    color:var(--styleColor);
    font-weight:bold;
}
.group{
    width:100%;
    display:flex;
    flex-direction:row;
    border-bottom:1px solid lightgray;
    background:none;
    min-height:45px;
    height:fit-content;
    position: relative;
    padding-top:15px;
    font-weight:300;
    vertical-align:center;
    margin-top:2px;
}
#group:hover{
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
      #buttons{
        margin: auto;
     }
     #TableOfContents{
         width:92.5%; 
      }
  }
  @media (max-width:1000px) {
    #image-border{
        padding: 0px;
        height:fit-content;
    }
    #data{
      flex-direction:column;
    }
  }
  @media (max-width: 775px) {
    /* CSS that should be displayed if width is equal to or less than 800px goes here */
    #image-border{
        margin:auto;
        margin-bottom: 20px;
    }
    #inner{
        flex-direction:column;
    }
    #noveltitle{
        margin-bottom: 0px;
    }
    #tables{
        margin: auto;
        min-width: 500px;
        
    }
    td.info{
        max-width: 100%; 
    }
    #TableOfContents{
    width:545;
    transition: all .3s ease;

}
.group{
    flex-direction:column;
}
.date{
   position:relative;
}
.title{
    position:relative;
    margin-bottom:10px;
}
  }
  @media (max-width:675px) {
    #image-border{
        padding: 15px;
        width: 220px;
        height: 305px;
        
        
    }
  }
</style>

