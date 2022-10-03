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
    <label class="toggle">
        <input type="checkbox" @click='switchEdit()'>
        <span class="slider round"></span>
        <span class="labels" data-on="Chapter" data-off="Novel"></span>
    </label>
    <!-- Novel Edit-->
    <table id = 'editTable' v-if='editType=="novel"'>
        <tr>
            <td class = 'category'>Title</td>
            <td v-text = 'novelData.title' contenteditable="true" id = 'novelTitle'/>
        </tr>
        <tr>
            <td  class = 'category'>Description</td>
            <td v-html = 'novelData.description' contenteditable="true" id = 'novelDescription'/>
        </tr>
        <tr>
            <td  class = 'category'>Novel Active</td>
            <td><button @click='confirm(0)'>{{novelData.novelactive==0 ? 'Activate Novel' : "Deactivate Novel"}}</button></td>
        </tr>
        <tr>
            <td  class = 'category'>Raw Status</td>
            <td>
                <select id = 'completedEdit' :selected='value=novelData.novelstatus'>
                    <option value = 'Ongoing'>Ongoing</option>
                    <option value = 'Completed'>Completed</option>
                    <option value = 'On Hold'>On Hold</option>
                    <option value = 'Dropped'>Dropped</option>
                </select>
            </td>
        </tr>
        <tr>
            <td  class = 'category'><button id = 'show-genres' @click='showGenres()'>Genres</button></td>
            <td id = 'genre-selector'>
                <GenreSelector
                :genres='genres'
                :selectedgenres='novelData.genres'
                />
            </td>
        </tr>
        <tr>
            <td  class = 'category'>Tags</td>
            <td id = 'tag-selector'>
                <TagSelector
                :tags='tags'
                :selectedtags='novelData.tags'
                />
            </td>
        </tr>
        <tr>
        <td><button @click='submit()'>Submit</button></td>
        </tr>
        <tr>
        </tr>
    </table>
    <!-- Novel Edit End-->

    <!-- Chapter Edit-->
    <div id = "TableOfContents" v-if='editType=="chapters"'>
        <ul  id = 'table' ref='tableofcontentlist'>
        <li v-for="chapter in chapterList" :key="chapter.chapternumber" class='table-list'>
            <button v-html='chapter.title' class = 'chapter-list' @click='displayChapter(chapter.chapternumber)'/>
            <pre v-html='chapterContent' class = 'chapter-content' :id='chapter.chapternumber' contenteditable='True'/>
            <br>
        </li>
        </ul>
        <button @click='showMore()' id = 'showMore' v-if='chapterList.length > 25'>Show More &#9662;</button>
    </div>
    <!-- Chapter Edit End-->
</div>
</template>


<script>
import { getAPI } from '../axios-api'
import GenreSelector from '../components/GenreSelector'
import TagSelector from '../components/TagSelector'
import ChapterSelector from '../components/ChapterSelector'
export default{
    data (){
        return{
            selectednovel:'',
            novelList:[],
            novelData:[],
            tags:[],
            genres:[],
            editType:'novel',
            chapterList:[],
            chapterContent:'',
            currentChapter:[]
        }
    },
    components:{
        GenreSelector,
        TagSelector,
        ChapterSelector
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
        selectNovel(){
            this.selectednovel = document.getElementById("novel-selector").value
            console.log(this.selectednovel)
            const url = '/novel/single?novel='+this.selectednovel+'&tier=5&edit=True'
            getAPI.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelData=response.data['Novel']
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapternumber != 0)
            this.genres = response.data['Genres']
            this.tags = response.data['Tags']
            this.isMounted=true
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
            console.log('posted')
               this.novelData.novelstatus=document.getElementById('completedEdit').value
               this.novelData.description=document.getElementById('novelDescription').innerHTML
               this.novelData.title=document.getElementById('novelTitle').innerHTML
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
            console.log(genre_selector)
            if(genre_selector.style.display=='flex'){
                genre_selector.style.display = 'none'
                console.log('flex')
            }else{
                genre_selector.style.display = 'flex'
                console.log('none')
            }
        },
        switchEdit(){
            if(this.editType=='novel'){
                this.editType='chapters'
            }else{
                this.editType='novel'
            }
            console.log(this.editType)
        },
        displayChapter(chapterItem){
            const chapter_contents = document.getElementsByClassName('chapter-content')
            try{
            var editedContent = document.getElementById(this.currentChapter).innerHTML
            }catch{}
                const url = '/chapter?novel='+this.selectednovel+'&chapter='+chapterItem+'&chapterupdate='+ this.currentChapter
              
                    getAPI.put(url,{content:editedContent})
                        .then(response => {
                                console.log('Chapter API has recieved data')
                                    this.chapterContent = response.data
                        })
                        .catch(function (error) {
                            console.log(error);
                        })
            this.currentChapter = chapterItem
            for(var i=0; i < chapter_contents.length; i++){
                chapter_contents[i].style.display='none'
            }
            document.getElementById(chapterItem).style.display='block'
            
        },
        postChapterData(){
            
        }
    },
    created(){
        getAPI.get('/noveltitles')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.novelList = response.data
            console.log(response.data)
          })
          .catch(err => {
            console.log(err)
          })
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
#genre-selector{
display:none;
}
#editTable{
    width:70%;
    height:100%;
}
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
#completedEdit{
     background:none;
    border:none;
    -webkit-appearance: none;
}
#show-genres{
    background-color:white;
    border:none;
    color: inherit;
}
.toggle {
    --width: 100px;
    --height: 20px;
    position: relative;
    display: inline-block;
    width: var(--width);
    height: var(--height);
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.3);
    border-radius: var(--height);
    cursor: pointer;
}

/* hiding checkbox */
.toggle input {
    display: none;
}
.toggle .slider {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border-radius: var(--height);
    background-color: #ccc;
    transition: all 0.4s ease-in-out;
}
.toggle .slider::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 50px;
    height: calc(var(--height));
    background-color: #fff;
    box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.3);
    transition: all 0.4s ease-in-out;
    z-index:4;
}
.toggle input:checked + .slider::before {
    transform: translateX(50px);
}
/* Adding text in the toggle button */
.toggle .labels {
    position: absolute;
    top: 2px;
    left: 0;
    width: 100%;
    height: 100%;
    font-size: 12px;
    font-family: sans-serif;
    transition: all 0.4s ease-in-out;
}

.toggle .labels::after {
    content: attr(data-off);
    position: absolute;
    right: 5px;
    color: #4d4d4d;
    opacity: 1;
    transition: all 0.4s ease-in-out;
}

.toggle .labels::before {
    content: attr(data-on);
    position: absolute;
    left: 5px;
    color: #4d4d4d;
    transition: all 0.4s ease-in-out;
}
.chapter-list{
    background:none;
    border:none;
    border-bottom:1px solid lightgray;
    -webkit-appearance: none;
    width:100%;
    text-align:left;
    transition: all 0.4s ease-in-out;
}
#table{
text-decoration:none;
    list-style:none;
    width:100%;
    transition: all 0.4s ease-in-out;
    
}
.chapter-content{
    display:none;
    width:100%;
    white-space: pre-wrap;
    font-weight:lighter;
    overflow:hidden;
    transition: all 0.4s ease-in-out;
}
.table-list{
    height:fit-content;
    transition: height 0.4s linear;
    
}
#TableOfContents{
    height:fit-content;
     transition: all 0.4s ease-in-out;

}
@media (max-width: 775px) {
    #editTable{
        width:350px;
    }
    #novel-selector{
        width:350px;
    }
}
</style>