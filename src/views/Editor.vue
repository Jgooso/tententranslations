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
        <option v-for='novel in novelList' :value='novel.novelid' >{{novel.title}} {{novel.completed_percentage*100}}%</option>
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
                        <td>URL</td>
                        <td class="info"><a :href="novelData.url" class = 'selectable'>{{novelData.url}}</a></td>
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
                        <td>Release Date</td>
                        <td class = "info" contenteditable='true' id = 'releaseDate'>{{novelData.novelrelease}}</td>
                    </tr>
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
    <button @click='uploadchapter()' id = 'upload-button'>Upload chapter</button>
    <button @click='resetschedule()' id = 'reset-button'>Reset Schedule</button>
    <button @click='deletenovel()' id = 'delete-button'>DELETE</button>  
    <div id = "summary">
        <div v-if='novelData.title'>
           <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;"><UtfBox shape = '&#9733;'/><h3 id = "divider">SUMMARY</h3></div><br>
            <p id="noveldescription" v-html = 'novelData.description' contenteditable="true"/>
        </div>
    </div>
    <!-- Chapter Edit-->
     <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;"><UtfBox shape = '&#9733;'/><h3 id = "divider">CHAPTERS</h3></div><br>
    <div id = "TableOfContents">
        <table  id = 'table' ref='tableofcontentlist'>
            <tr class='table-list'>
            <td class = 'chapter-title'>Chapter Title</td>
            <td class = 'chapter-check-box' style='font-size:15px'>Edited</td>
            <td class = 'chapter-check-box' style='font-size:15px'>Uploaded</td>
            <td style='font-size:15px'>Upload Date</td>
            </tr>
            <tr v-for='section in sectionList' style='display:flex;flex-direction:column'>
                <p v-if='section.chapter_title' class='section' v-html='section.chapter_title' :id ='"section"+section.section' contenteditable='True'/>
                <tr style='width:100%'>
                    <tr v-for="chapter in chapterList.filter(chapter=>chapter.section==section.section)" :key="chapter.chapter_number" class='table-list' :id='"chapter"+chapter.chapter_number'>
                        <td class='chapter-title'>
                        <label>
                        {{chapter.chapter_title}}
                        <input type='button'  class = 'chapter-list' :value = 'chapter.chapter_number' @click='displayChapter(chapter)'>
                        </label>
                        </td>
                        <td v-if='chapter.chapter_edited == 1' style='color:lightgreen;' class = 'chapter-check-box edited-check' @click='chapteredit(chapter)'>&#10003;</td>
                        <td v-else style='color:red;' class = 'chapter-check-box edited-check' @click='chapteredit(chapter)'>X</td>
                        <td v-if='chapter.chapter_actived == 1' style='color:lightgreen;x' class = 'chapter-check-box'>&#10003;</td>
                        <td v-else style='color:red;' class = 'chapter-check-box'>X</td>
                        <td>
                            <input type = 'datetime-local' 
                                    :id ='"date"+chapter.chapter_order'
                                    :value='chapter.upload_date' 
                                    @change='changeupload(chapter)' 
                                    min="2023-01-01T00:00"
                                    style='width:fit-content;margin-right:20px;' >
                        </td>
                    </tr>
                </tr>
            </tr>
        </table>
        <div id = 'chapterEditor'>
            <label v-if='saved'>&#8592;
                <input type='button' id ='back-button' @click='hideChapter()' >
            </label>
            <p v-else> Unsaved Changes</p>
            <h3 contenteditable ='True' id = 'chapter-title'>{{chapterTitle}}</h3>
                 <textarea v-text='chapterContent' id = 'chapter-content'/>
        </div>
    </div>
    </div>
    </div>
    <!-- Chapter Edit End-->
<button @click='submit()'>Submit</button>
</div>
</template>


<script>
import axios from 'axios'
import GenreSelector from '../components/GenreSelector'
import TagSelector from '../components/TagSelector'
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
            currentChapter:'',
            saved:'',
            chapterTitle:''

        }
    },
    components:{
        GenreSelector,
        TagSelector,
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
                if(this.novelData.novelactive == 1){
                    this.novelData.novelactive=0
                }
                else{
                    this.novelData.novelactive=1
                }
                confirmationBox.style.display = 'none'
                axios.put(`http://127.0.0.1:5000/activatenovel?novel=${this.novelData.novelid}'&active=${this.novelData.novelactive}`).then(response => {
                console.log('sent')
                 })
                    .catch(err => {
                    console.log(err)
                })
                }
        },
        selectNovel(a){
            if(a){
                this.selectednovel=a
            }else{
                this.selectednovel = document.getElementById("novel-selector").value
            }
            const url = `http://127.0.0.1:5000/novel/single?novel=${this.selectednovel}&tier=0&edit=True`
            axios.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelData=response.data['Novel']
            const sections = response.data['Chapters'].filter(chapter => chapter.chapter_number == 0)
            if(sections.length > 0){
                this.sectionList = sections
            }else{
                this.sectionList = [{'section':0}]
            }
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapter_number != 0)
            this.genres = response.data['Genres']
            this.tags = response.data['Tags']
            this.currentChapter = null
            this.chapterContent = ''
            console.log(this.novelData)
          })
          .catch(err => {
            console.log(err)
          })
            this.saved = true
            this.hideChapter()
        },
        submit(){
            const loadingscreen = document.getElementById('loadingscreen')
            loadingscreen.style.display = 'block'
            const genres = document.getElementsByClassName('genrecheckbox')
            var selectedGenres = []
            console.log(this.novelData.id)
            for(var i=0; i < genres.length; i++){
                if(genres[i].checked==true){
                    selectedGenres.push(genres[i].value)
                }
            }
               this.novelData.novelstatus=document.getElementById('completedEdit').value
               this.novelData.description=document.getElementById('noveldescription').innerHTML
               this.novelData.title=document.getElementById('noveltitle').innerHTML
               this.novelData.novelrelease = document.getElementById('releaseDate').innerHTML
               const url = `http://127.0.0.1:5000/novel/single?novel=${this.novelData.novelid}`
            axios.put(url,{
                title:this.novelData.title,
                description:this.novelData.description,
                novelrelease:this.novelData.novelrelease,
                novelstatus:this.novelData.novelstatus,
                tag:this.novelData.tags,
                genre:selectedGenres,
                   
                   
               }).then(function (response) {
                    console.log(response);
                    loadingscreen.style.display='none'
            })
                .catch(function (error) {
                    console.log(error);
                    loadingscreen.style.display='none'
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
                 this.currentChapter.content = document.getElementById('chapter-content').value
                 this.currentChapter.title = document.getElementById('chapter-title').innerHTML
                 this.saved=true;
                 axios.put(`http://127.0.0.1:5000/chapter?novel=${this.currentChapter.novelid}&chapter=${this.currentChapter.chapternumber}`,{
                     title:this.currentChapter.title,
                     content:this.currentChapter.content
                     })
                    .then(response => {
                        console.log(this.currentChapter)
                    })
                    .catch(err => {
                        console.log(err)
                    })
            }
             
        },
        displayChapter(chapterItem){
            console.log(chapterItem)
            document.getElementById('chapterEditor').style.left='0px';
             document.getElementById('chapterEditor').style.width='100%';
            document.getElementById('table').style.width='0px';
            document.getElementById('chapter-content').addEventListener('keydown', this.save, false);
            const url = `http://127.0.0.1:5000/chapter?novel=${chapterItem.novelid}&chapter=${chapterItem.chapter_number}`
            axios.get(url)
            .then(response => {
                console.log('Chapter API has recieved data')
                this.chapterContent = response.data['content']
                this.currentChapter = chapterItem
                this.chapterTitle = response.data['title']
            })
            .catch(err => {
                console.log(err)
            })
        },
        hideChapter(){
            if(this.saved==true){
                var editor = document.getElementById('chapterEditor')
                editor.style.left='100%'
                editor.style.width='0px'
                this.chapterContent = ''
                document.getElementById('table').style.width='100%';
                document.getElementById('chapter-content').removeEventListener('keyup', this.save);
            }else{
                
            }
        },
        chapteredit(chapter){
            if (chapter.chapteredited == 0){
                chapter.chapteredited = 1
            }else{
                chapter.chapteredited = 0
            }
            console.log(chapter)
            const url = `http://127.0.0.1:5000/chaptereditchange?edit=${chapter.chapteredited}&novel=${chapter.novelid}&chapter=${chapter.chapterorder}`
            axios.put(url)
            .then(response => {
                console.log('sent')
            })
            .catch(err => {
                console.log(err)
            })
        },
        changeupload(chapter){
            const date = document.getElementById('date'+chapter.chapterorder).value
            const url = `http://127.0.0.1:5000/chapteruploadchange?offset=${timezoneOffset}&novel=${chapter.novelid}&chapter=${chapter.chapterorder}`
            axios.put(url,{date:date}).then(response =>{
                console.log('send')
            }).catch(err =>{
                console.log(err)
            })
        },
        uploadchapter(){
            axios.put(`http://127.0.0.1:5000/uploadchapter?novel=${this.novelData.novelid}`).then(response=>{
                console.log('send')
            }).catch(err=>{
                console.log(err)
            })
        },
        resetschedule(){
            axios.put(`http://127.0.0.1:5000/resetschedule?novel=${this.novelData.novelid}`).then(response=>{
                console.log('send')
            }).catch(err=>{
                console.log(err)
            })
        },
        deletenovel(){
            console.log('delete')
        }
    },
    created(){
        axios.get('http://127.0.0.1:5000/noveltitles')
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
#reset-button{
    background-color:var(--backgroundColor);
    color:var(--textColor);
    border:1px solid black;
    width:100%;
    border-radius:5px;
    height:30px;
    margin-top:15px;
}
#upload-button{
    background-color:var(--backgroundColor);
    color:var(--textColor);
    border:1px solid black;
    width:100%;
    border-radius:5px;
    height:30px;
    margin-top:15px;
}
#delete-button{
    background-color:red;
    color:black;
    border:1px solid black;
    width:100%;
    border-radius:5px;
    height:30px;
    margin-top:15px;
    font-weight:bold;
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
    border:1px solid black
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
    -webkit-appearance: none;
    width:80%;
    text-align:left;
    margin-left:0px;
    border:none

}
.table-list{
    height:fit-content;
    max-height:30px;
    overflow:hidden;
    width:100%;
    margin-left:0px;
    display:flex;
    flex-direction:row;
    margin:0px;
    border-bottom:1px solid black
}
.chapter-select{
    margin-left:40px;
}
.chapter-title{
    width:60%;
    text-overflow:ellipsis;
    margin:0px;
    padding-left:20px;
}
.table-list:hover{
   background-color:var(--styleColor);
   color:white;
}
.chapter-check-box{
text-align:center;
font-weight:bold;
font-size:20px;
width:10%
}
.edited-check:hover{
    background-color:white;
}
/*Chapter Table of Contents End*/

/*Chapter Editor Page*/
#chapterEditor{
    position:relative;
    left:100%;
    transition: 1s ease-in-out;
    top:0px;
    width:0px;
    display:flex;
    flex-direction:column;
}
#back-button{
    background:none;
    border:none;
    font-size:30px;
}
#chapter-content{
    height:fit-content;
    width:100%;
    font-family: sans-serif;
    white-space: pre-wrap;
    font-weight: 100;
    position:relative;
    font-size:19px;
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