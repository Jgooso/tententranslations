<template>
<div class = 'content'>
<div id = 'managementnavigator'>
<button>Upload</button>
<button>Schedule</button>
<button>Edit</button>
<button>Manage Users</button>
</div>
<!--
<form id = 'download' >
<div id = 'loadingscreen'><div class="loader"></div></div>
<label for="fname">URL:</label>
<input type = "text" id = 'urltextbox' name = 'url' maxlength="34" style='width:280px' >
<div id = 'genres'>
<label v-for='genre in genres' :key = 'genre'><input type='checkbox' :value='genre' :name = 'genre' class = 'genrecheckbox'>{{genre}}</label>
</div>
<br><br>
<input type = 'submit' @click='postData()'>

</form>
<div  id = 'tagList'>
<ul class = 'selectedtaglist' >
    <li v-for='tag in selectedtags' :key = 'tag'><tagBox :tag='tag' @remove='removeTag'/></li>
</ul>
<input id = 'tagfilter' v-on:keyup='filterTag()'>
</div>
<div id = 'tagselector'>
    <button v-for='tag in tags' :key='tag' class = 'tagbutton unselected' :id = 'tag' v-html='tag' @click='addTag(tag)'/>

</div>
-->
<NovelInformation/>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import tagBox from '../components/TagBox'
import schedular from '../components/Schedular'
import ScheduleCreator from '../components/ScheduleCreator'
import NovelInformation from './NovelInformation'
export default{
    name:'Upload',
    data(){
        return{
            genres:[],
            tags:[],
            selectedtags:[],
            selectedgenres:[]
        }
    },
    components:{
        tagBox,
        schedular,
        ScheduleCreator,
        NovelInformation
    },
    methods:{
        addTag(tag){
            const tagbutton = document.getElementById(tag)
            tagbutton.classList.remove('unselected')
            if(!this.selectedtags.includes(tag)){
                this.selectedtags.push(tag)
            }
           
        },
        removeTag(removetag){
            const index = this.selectedtags.indexOf(removetag)
            this.selectedtags.splice(index,1)
            document.getElementById(removetag).classList.add('unselected')
        },
        filterTag(){
            var input, tagbuttons, txtValue
            input = document.getElementById('tagfilter').value.toUpperCase()
            tagbuttons = document.getElementsByClassName('tagbutton')
            for(var i = 0; i < tagbuttons.length; i++){
                txtValue = tagbuttons[i].value || tagbuttons[i].innerText;
                if (txtValue.toUpperCase().indexOf(input) > -1) {
                    tagbuttons[i].style.display = "";
                } else {
                    tagbuttons[i].style.display = "none";
                }
            }
        },
        postData(){
            const loadingscreen = document.getElementById('loadingscreen')
            loadingscreen.style.display = 'block'
            const form = document.getElementById('download');
            const selectedGenres = 'Fantasy, Comedy'//form['genres'].value
            const url = form['url'].value
            console.log('posted')
            getAPI.post('/novel/single', {url:url,tags:this.selectedtags,genres:selectedGenres})
                .then(function (response) {
                    console.log(response);
                    loadingscreen.style.display = 'none'
            })
                .catch(function (error) {
                    console.log(error);
                    loadingscreen.style.display = 'none'
            }); 
        }
    },
    created(){
        /*
        getAPI.get('/uploaddata')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.genres = response.data['genres']
            this.tags = response.data['tags']
          })
          .catch(err => {
            console.log(err)
          })
          */
    }
}
</script>

<style scoped>
#tagList{
border: 2px rgb(244,244,244) solid;
width:800px;
height:fit-content;
min-height:50px;

}
.content{
    display:flex;
    flex-direction:row;
    height:1000px;
    margin-top:100px;
}
.selectedtaglist{
    display:inline;
    list-style: none;
    padding:0px;
}
.selectedtaglist li{
    display:inline;
    float:left;
    margin-left:10px;
}
#managementnavigator{
    height:100%;
    background-color:lightgray;
    width:30%;
    display:flex;
    flex-direction:column;
}
#tagselector{
    display:flex;
    flex-direction:column;
    overflow:scroll;
    height:500px;
    width:500px;
}
.tagbutton{
    border:none;
    color:lightgray;
}
.unselected{
    color:black;
}
.unselected:hover{
    background-color:blue;
    color:white;
}
button{
    background:none;
    border-right:none
}
#genres{
    position:relative;
    display:grid;
    grid-template-rows: auto auto auto auto auto auto auto auto auto;
    grid-auto-flow: column;
    column-gap: 30px;
    row-gap:10px;
    margin:auto;
    width:100%
}
input{
    margin-right:5px;
}
#tagSelect{
    background:lightgray;
    border:none;
    -webkit-appearance: none;
}
#tags{
    width:100%
}
#tagtextbox{
    width:500px;
    text-align:left;
    overflow-wrap: break-word
}
#download{
    width:1000px;
    height:fit-content;
}
.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
  margin:auto;
  margin-top:170px;

}
#loadingscreen{
    display:none;
    position:absolute;
    z-index:5;
    width:1000px;
    height:500px;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
@media (max-width: 775px) {
    #genres{
        grid-template-rows: auto auto auto auto auto auto auto auto auto auto auto auto;
    }
}
</style>