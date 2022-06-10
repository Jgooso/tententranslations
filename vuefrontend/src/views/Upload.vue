<template>
<div class = 'content'>
<div id = 'managementnavigator'>
<button>Upload</button>
<button>Schedule</button>
</div>
<form>
<label for="fname">URL:</label>
<input type="text">
<div id = 'genres'>
<label v-for='genre in genres' :key = 'genre'><input type='checkbox' :value='genre' class = 'genrecheckbox'>{{genre}}</label>
</div>
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
        getGenres(){
        const genres = document.getElementsByClassName('genrecheckbox')
        for(var i=0; i<genres.length;i++){
            console.log(i)
        }
        console.log(genres)
        }
    },
    created(){
        getAPI.get('/uploaddata')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.genres = response.data['genres']
          })
          .catch(err => {
            console.log(err)
          })
    this.getGenres()
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
</style>