<template>
<div class = 'content'>
<div id = 'managementnavigator'>
<button>Upload</button>
<button>Schedule</button>
<button>Edit</button>
<button>Manage Users</button>
</div>
<form id = 'download' >
<label for="fname">URL:</label>
<input type = "text" id = 'urltextbox' name = 'url' maxlength="34" style='width:280px' >
<div id = 'genres'>
<label v-for='genre in genres' :key = 'genre'><input type='checkbox' :value='genre' name = 'genres' class = 'genrecheckbox'>{{genre}}</label>
</div>
<br><br>
<label id = 'tags'>Tags:<input type = 'text' name = 'tags' @focusin="showHideTagList(1)" @change ='showHideTagList(2)' id = 'tagtextbox'></label>
<select id = 'tagSelect' @change='addTag()' size = '20'>
    <option v-for='tag in tags' :key = 'tag' v-html = 'tag'></option>
</select>
<input type = 'submit' @click='postData()'>
</form>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
export default{
    name:'Upload',
    data(){
        return{
            genres:[],
            tags:[],
        }
    },
    methods:{
        showHideTagList(display){
            const x = document.getElementById('tagSelect')
            if(!x)return null
            if (display==1) {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
            
        },
        addTag(){
            const x = document.getElementById('tagtextbox')
            const tag = document.getElementById('tagSelect').value
            x.value += tag+","
        },
        postData(){
            var selectedGenres = ''
            const form = document.getElementById('download');
            const genreelements = form['genres'].value
            const url = form['url'].value
            const selectedtags = form['tags'].value
            console.log('selectedgenres')
            getAPI.post('/novel/single', {url:url,tags:selectedtags,genres:selectedGenres})
                .then(function (response) {
                    console.log(response);
            })
                .catch(function (error) {
                    console.log(error);
            }); 
        }
    },
    created(){
        getAPI.get('/uploaddata')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.genres = response.data['genres']
            this.tags = response.data['tags']
          })
          .catch(err => {
            console.log(err)
          })
    }
}
</script>

<style scoped>
.content{
    display:flex;
    flex-direction:row;
    height:1000px;
    margin-top:100px;
}
#managementnavigator{
    height:100%;
    background-color:lightgray;
    width:30%;
    display:flex;
    flex-direction:column;
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
    display:none;
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
@media (max-width: 775px) {
    #genres{
        grid-template-rows: auto auto auto auto auto auto auto auto auto auto auto auto;
    }
}
</style>