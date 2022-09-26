<template>
<div>

 <!--COVER-->
  <div id="cover" ref = 'cover'>
    <div class = "content"  v-if='novelData.title'>
        <Navigator
         :novelid='novelData.id'
         :novel='novelData.title'
        />
        <p id = "noveltitle" v-text='novelData.title'/>
        <div id = "inner">
            <img id = "image-border" :src="novelData.imageurl" v-if='novelData.imageurl'>
            <div id = "tables">
             <div id = "data">
                <table>
                    <tr><td>Views</td><td v-text='novelData.views' class='info'/></tr>
                    <tr><td>Alternative</td><td v-text='novelData.alternativetitle' class="info"/></tr>
                    <tr><td>Raw</td><td class="info"><a :href="novelData.url">{{novelData.url}}</a></td></tr>
                    <tr><td>Author</td><td class="info">
                        <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-authors',identifier:novelData.authors}}" class='selectable'>{{novelData.authors}}</router-link>
                    </td></tr>
                    <tr>
                        <td>Genres</td>
                        <td class="info">
                            <ul class='comma-list' v-if='!editable'>
                                <li v-for='genre in novelData.genres' :key='genre'>
                                    <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-genres',identifier:genre}}" class='selectable'>{{genre}}</router-link>
                                </li>
                            </ul>
                            <p v-else v-text='novelData.genres.join()' contenteditable="true" id = 'genreEdit' class='editor'/>
                        </td>
                    </tr>
                    <tr>
                        <td>Tags</td>
                        <td class="info">
                            <ul class='comma-list' v-if='!editable'>
                                <li v-for='tag in novelData.tags' :key='tag'>
                                    <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-tags',identifier:tag}}" class='selectable' v-html='tag'/>
                                </li>
                            </ul>
                            <p v-else v-html='novelData.tags.join()' contenteditable="true" id = 'tagEdit' class='editor'/>
                        </td>
                    </tr>
                </table>
                <table>
                    <tr><td>Release</td><td class="info" v-text='novelData.novelrelease'/></tr>
                    <tr><td>Status</td>
                      <td class="info">
                      <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-status',identifier:novelData.uploadstatus}}" class='selectable'>
                        {{novelData.uploadstatus}}
                      </router-link></td>
                    </tr>
                    <tr><td>Novel</td>
                        <td class="info" v-if='!editable'>{{ novelData.novelstatus}}</td>
                        <td class="info" v-else>
                            <select id = 'completedEdit' :selected='value==novelData.novelstatus'>
                                <option value = 'Ongoing'>Ongoing</option>
                                <option value = 'Completed'>Completed</option>
                                <option value = 'On Hold'>On Hold</option>
                                <option value = 'Dropped'>Dropped</option>
                                <option value = 'Unreleased'>Unreleased</option>
                            </select>
                        </td>
                    </tr>
                </table>
             </div>
             <br>
             
             <NavButton 
                :first="1"
                :last='chapterList.length'
             />
             <br>
             <button v-if='tier==5' id = 'editButton' @click='changeEditMode()'>Edit</button>
            </div>   
        </div>     
    </div>
</div>
  <br>
  <!--SUMMARY-->
  <div id = "summary">
        <div class = "content"  v-if='novelData.title'>
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
                <li v-for="chapter in chapterList.filter(chapter=>chapter.section==section.section)" :key='chapter.chapterNumber'>
                <router-link 
                    :to = "{name: 'chapterPage', params:{title:novelData.novelid,chapter:chapter.chapternumber}}" id="group">
                    <p id = "title">{{chapter.title}}</p>
                    <p id = "date">{{new Date(chapter.date).toLocaleString('default', { month: 'long', day:'numeric', year:'numeric' })}}</p>
                </router-link>
                </li>
            </ul>
        </li>
        </ul>
        <ul v-if='sectionList.length==0'>
                <li v-for="chapter in chapterList" :key='chapter.chapterNumber'>
                <router-link 
                    :to = "{name: 'chapterPage', params:{title:novelData.novelid,chapter:chapter.chapternumber}}" id="group">
                    <p id = "title">{{chapter.title}}</p>
                    <p id = "date">{{new Date(chapter.date).toLocaleString('default', { month: 'long', day:'numeric', year:'numeric' })}}</p>
                </router-link>
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
  import {getAPI} from '../axios-api'
  export default {
    name: 'CoverPage',
    components: {
      UtfBox,
      Navigator,
      NavButton
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
       changeEditMode(){
           if(this.editable){
               this.editable=false
               this.novelData.genres = document.getElementById('genreEdit').innerHTML.split(',')
               this.novelData.tags = document.getElementById('tagEdit').innerHTML.split(',')
               this.novelData.completed=document.getElementById('completedEdit').value
               this.novelData.description=document.getElementById('description').innerHTML
               this.novelData.title=document.getElementById('noveltitle').innerHTML
               const url = '/novel/single?novel='+this.$route.params.title
               document.getElementById('editButton').innerHTML='Edit'
               document.getElementById('description').contentEditable = "false"
               document.getElementById('noveltitle').contentEditable = "false"
               getAPI.put(url,{
                   description:this.novelData.description,
                   tags:this.novelData.tags,
                   genres:this.novelData.genres,
                   completed:this.novelData.completed,
                   title:this.novelData.title
               }).then(function (response) {
                    console.log(response);
            })
                .catch(function (error) {
                    console.log(error);
            })
               
    
            }else{
               this.editable=true
               document.getElementById('editButton').innerHTML='Save'
               document.getElementById('description').contentEditable = "true"
               document.getElementById('noveltitle').contentEditable = "true"
            }
          
       }
       
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
    width: 1110px;
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
  }
 
  #tables{
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
  td.info{
      font-weight:normal;
      width: 85%;
      line-height: 20px;
      vertical-align: bottom;
      color:rgb(136,136,136);
  }
  td.info a{
    color:black;
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
#editButton{
    background-color:var(--styleColor);
    color:white;
}
.editor{
    font-size:12px;
    height:12px;
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
  }
  @media (max-width:675px) {
    #image-border{
        padding: 15px;
        width: 220px;
        height: 305px;
        
        
    }
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
#date{
    font-size:11px;
    position:absolute;
    right:0;
    font-style:italic;
    line-height:15px;
    color:gray;
    margin-right:10px;
}
#title{
    padding-left:10px;
    position:absolute;
    line-height:15px;
    left:5;
    font-size:17px;
}
#group{
    width:100%;
    display:flex;
    flex-direction:row;
    border:none;
    background:none;
    height:45px;
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
</style>

