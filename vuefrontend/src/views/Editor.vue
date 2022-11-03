<template>
<div id = 'editPage'>
    <div id = 'confirmationBox'>
        <h1 style = 'margin:auto;'>{{novelData.novelactive==0 ? 'Confirm Activate Novel' : "Confirm Deactivate Novel"}}</h1>
        <div style='display:flex;flex-direction:row;margin:auto; width:220px'>
        <button @click='confirm(2)' class = 'confirmation-button'>Confirm</button>
        <button @click='confirm(1)' class = 'confirmation-button'>Cancel</button>
        
        </div>
    </div>
    <select id = 'novel-selector' @change="selectNovel()">
        <option v-for='novel in novelList' :value='novel.novelid'>{{novel.title}}</option>
    </select>
    <!-- Novel Edit-->
    <!-- Novel Edit End-->
    <div id="cover" ref = 'cover'>
    <div v-if='novelData.title'>
        <p id = "noveltitle" v-text='novelData.title' contenteditable="true"/>
    <div id = "inner">
        <div id = "novel-information">
             <div id = "data">
                <table>
                    <tr>
                        <td>Author</td>
                        <td class="info">{{novelData.author}}</td>
                    </tr>
                    <tr>
                        <td>Genres</td>
                         <td  class = 'category'><button class = 'show' @click='showGenres()'>Show</button></td>
                    </tr>
                    <tr>
                        <td>Tags</td>
                        <td  class = 'category'><button class = 'show' @click='showTags()'>Show</button></td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <td>Raw Status</td>
                        <td class="info">
                                <select id = 'completedEdit' :selected='value=novelData.novelstatus'>
                                    <option value = 'Ongoing'>Ongoing</option>
                                    <option value = 'Completed'>Completed</option>
                                    <option value = 'On Hold'>On Hold</option>
                                    <option value = 'Dropped'>Dropped</option>
                                </select>
                        </td>
                    </tr>
                    <tr>
                        <td>Novel Active</td>
                        <td><button @click='confirm(0)'>{{novelData.novelactive==0 ? 'Activate Novel' : "Deactivate Novel"}}</button></td>
                    </tr>
                    <!--
                    <tr>
                        <td>Pages<span id = 'pageSuper'>(Approx.)</span><p id = 'disclaimer'>~1800 characters/360 words per Page</p></td>
                        <td class="info"><p>{{novelData.pages}}</p></td>
                    </tr>
                    -->
                </table>
             </div>
             <div id = 'genre-selector'>
             <GenreSelector
                :genres='genres'
                :selectedgenres='novelData.genres'
                
                />
            </div>
            <TagSelector
                :tags='tags'
                :selectedtags='novelData.tags'
                id = 'tag-selector'
                />
        </div>   
    </div>    
    <div id = "summary">
        <div v-if='novelData.title'>
           <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;"><UtfBox shape = '&#9733;'/><h3 id = "divider">SUMMARY</h3></div><br>
            <p id="noveldescription" v-html = 'novelData.description' contenteditable="true"/>
        </div>
    </div>
    <!-- Chapter Edit-->
    <div id = "TableOfContents">
        <ul  id = 'table' ref='tableofcontentlist'>
            <li v-for='section in sectionList'>
                <li class='section' v-html='section.title' :id ='"section"+section.section' contenteditable='True'/>
                <ul>
                    <li v-for="chapter in chapterList.filter(chapter=>chapter.section==section.section)" :key="chapter.chapternumber" class='table-list' :id='"chapter"+chapter.chapternumber'>
                        <label>
                        {{chapter.title}}
                        <input type='button'  class = 'chapter-list' value = chapter.chapternumber @click='displayChapter(chapter.chapternumber)'>
                        </label>
                       
                        <br>
                    </li>
                </ul>
            </li>
        </ul>
        <div id = 'chapterEditor'>
            <label>&#8592;
            <input type='button' id ='back-button' @click='hideChapter()'>
            </label>
            <h3>Title</h3>
                 <pre v-html='chapterContent' id = 'chapter-content' contenteditable='True'/>
        </div>
    </div>
    </div>
    </div>
    <!-- Chapter Edit End-->
<button @click='submit()'>Submit</button>
</div>
</template>


<script>
import { getAPI } from '../axios-api'
import GenreSelector from '../components/GenreSelector'
import TagSelector from '../components/TagSelector'
import ChapterSelector from '../components/ChapterSelector'
import UtfBox from '../components/UtfBox'
export default{
    data (){
        return{
            selectednovel:'',
            novelList:[],
            novelData:[],
            tags:[],
            genres:[],
            chapterList:[],
            sectionList:[],
            chapterContent:'',
            currentChapter:[],
            saved:'',

        }
    },
    components:{
        GenreSelector,
        TagSelector,
        ChapterSelector,
        UtfBox
    },
    methods:{
        confirm(open){
            var confirmationBox = document.getElementById('confirmationBox')
            if(open == 0){
                confirmationBox.style.display = 'flex'
            }else if(open == 1){
                confirmationBox.style.display = 'none'
            }else if(open == 2){
                if(this.novelData.novelactive == 1){this.novelData.novelactive=0}
                else{this.novelData.novelactive=1}
                confirmationBox.style.display = 'none'
            }
        },
        selectNovel(a){
            if(a){
                this.selectednovel=a
            }else{
                this.selectednovel = document.getElementById("novel-selector").value
            }
            const url = '/novel/single?novel='+this.selectednovel+'&tier=5&edit=True'
            getAPI.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelData=response.data['Novel']
            const sections = response.data['Chapters'].filter(chapter => chapter.chapternumber == 0)
            if(sections.length > 0){
                this.sectionList = sections
            }else{
                this.sectionList = [{'section':0}]
            }
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapternumber != 0)
            this.genres = response.data['Genres']
            this.tags = response.data['Tags']
            this.isMounted=true
            this.currentChapter = null
            this.chapterContent = ''
          })
          .catch(err => {
            console.log(err)
          })
       
        },
        submit(){
            //const loadingscreen = document.getElementById('loadingscreen')
            //loadingscreen.style.display = 'block'
            const genres = document.getElementsByClassName('genrecheckbox')
            var selectedGenres = []
            for(var i=0; i < genres.length; i++){
                if(genres[i].checked==true){
                    selectedGenres.push(genres[i].value)
                }
            }
               this.novelData.novelstatus=document.getElementById('completedEdit').value
               this.novelData.description=document.getElementById('noveldescription').innerHTML
               this.novelData.title=document.getElementById('noveltitle').innerHTML
               const url = '/novel/single?novel='+this.selectednovel
            getAPI.put(url,{
                   description:this.novelData.description,
                   tags:this.novelData.tags,
                   genres:selectedGenres,
                   completed:this.novelData.novelstatus,
                   title:this.novelData.title,
                   novelactive:this.novelData.novelactive
               }).then(function (response) {
                    console.log(response);
            })
                .catch(function (error) {
                    console.log(error);
            })
        },
        showGenres(){
            var genre_selector = document.getElementById('genre-selector')
            if(genre_selector.style.display=='flex'){
                genre_selector.style.display = 'none'
            }else{
                genre_selector.style.display = 'flex'
            }
        },
        showTags(){
            var tag_selector = document.getElementById('tag-selector')
            if(tag_selector.style.display=='flex'){
                tag_selector.style.display = 'none'
            }else{
                tag_selector.style.display = 'flex'
            }
        },
        save(e){
            if(e.key != 's'){
                this.saved = false
            }
            if (e.ctrlKey && e.key === 's') {
                 this.chapterContent = document.getElementById('chapter-content').innerHTML
                 this.saved=true;
            }
             
        },
        displayChapter(chapterItem){
            const chapter_contents = document.getElementsByClassName('selected')
            document.getElementById('chapterEditor').style.left='0px';
            document.getElementById('table').style.width='0px';
            document.getElementById('chapter-content').addEventListener('keydown', this.save, false);
            const url = '/chapter?novel='+this.novelData.id+'&chapter='+chapterItem
            getAPI.get(url)
            .then(response => {
                console.log('Chapter API has recieved data')
                this.chapterContent = response.data
            })
            .catch(err => {
                console.log(err)
            })
        },
        hideChapter(){
            console.log(this.saved)
            if(this.saved==true){
                console.log('orking')
                document.getElementById('chapterEditor').style.left='100%'
                document.getElementById('table').style.width='100%';
                document.getElementById('chapter-content').removeEventListener('keyup', this.save);
            }else{
                
            }
        }
    },
    created(){
        getAPI.get('/noveltitles')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.novelList = response.data
            this.selectNovel(this.novelList[0].novelid)
            
          })
          .catch(err => {
            console.log(err)
          })
    },
    mounted(){
       
    }
}
</script>
<style scoped>
#editPage{
    width:100%;
    height:fit-content;
    max-width:800px;

}
#novel-selector{
    width:80%;
}
.category{
    width:100px;
    height:50px;
}
#confirmationBox{
    display:none;
    background-color:lightgray;
    width:350px;
    height:350px;
    flex-direction:column;
    padding:20px;
    position:fixed;
    top:50%;
    justify-content:center;
    z-index:10;

}
.confirmation-button{
    width:100px;
    height:50px;
    font-size:20px;
    margin:auto;
}
tr{
    margin-bottom:30px;
}

#completedEdit{
     background:none;
    border:none;
    -webkit-appearance: none;
}
.show{
    background-color:white;
    color: inherit;
    border: 1px solid black;
    width:100%;
}


/*Chapter Editor*/

/*Chapter Table of Contents*/
#TableOfContents{
    height:fit-content;
    width:100%;
    overflow:hidden;
    display:flex;
    flex-direction:row;
}
#table{
text-decoration:none;
    list-style:none;
    width:100%;
    position:relative;
    transition: 1s ease-in-out;
    
}
.section{
    color:#000000;
    font-size:18px;
    width:100%;
    padding-left:10px;
    border-radius:10px;
}
.chapter-list{
    background:none;
    border:none;
    -webkit-appearance: none;
    width:100%;
    text-align:left;
    margin-left:0px;
}
.table-list{
    height:fit-content;
    max-height:30px;
    overflow:hidden;
    border-bottom:1px solid lightgray;
    width:100%;
    margin-left:0px;
    
}
/*Chapter Table of Contents End*/

/*Chapter Editor Page*/
#chapterEditor{
    position:relative;
    left:100%;
    transition: 1s ease-in-out;
    top:0px;
    width:100%;
}
#back-button{
    background:none;
    border:none;
    font-size:30px;
}
.chapter-content{
    height:fit-content;
    width:100%;
    white-space: pre-wrap;
    font-weight:lighter;
    overflow:hidden;
}
/*Chapter Editor Page End*/

/*Chapter Editor End*/



.comma-list {
  display: inline;
  margin-left:0px;
}
.comma-list li {
  display: inline;
}
.comma-list li::after {
  content: ", ";
}
.comma-list li:last-child::after {
    content: "";
}
@media (max-width: 775px) {
    #editTable{
        width:350px;
    }
    #novel-selector{
        width:350px;
    }
}

/*Novel Editor*/
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

  /*Novel Informatio Table*/
    #inner{
        align-self:center;
        display:flex;
        flex-direction:row;
        width:100%;
        transition: all .2s ease;
        box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
        margin-top:20px;
    }
    #novel-information{
        background-color: rgba(250, 250, 250, 0.8);
        padding:20px;
        width: 100%;
        height:fit-content;
        display: flex;
        flex-direction: column;
    }
    #editTable{
        width:70%;
        height:fit-content;
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
        color:black;
      
    }
    .info{
        font-weight:normal;
        width: 85%;
        line-height: 20px;
        vertical-align: middle;
        color:rgb(136,136,136);
        font-size:14px;
    }
    #data{
        display:flex;
        flex-direction:row;
    }
    #genre-selector{
        display:none;
    }
    #tag-selector{
        display:none
    }
    

   /*Novel Informatio Table End*/
  #summary{
    width: 100%;
    text-align: left;
    display: flex;
    flex-direction: column;
    align-self: center;
    height:fit-content;
    margin-top:20px;
}
#noveldescription{
    width:100%;
    font-size: 14px;
    color:rgb(136,136,136);
    height:fit-content;
}
#divider{
    font-size:18px;
    font-weight:bold;
    margin-left:15px;
    line-height:18px;
    height:30px;
    padding-top:6px;
}
 /*Novel Editor End*/
</style>