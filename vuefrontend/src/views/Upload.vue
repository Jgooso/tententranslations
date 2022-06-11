<template>
<div class = 'content'>
<div id = 'managementnavigator'>
<button>Upload</button>
<button>Schedule</button>
<button>Edit</button>
<button>Manage Users</button>
</div>
<form>
<label for="fname">URL:</label>
<input type="text" id = 'urltextbox' maxlength="34" style='width:280px'>
<div id = 'genres'>
<label v-for='genre in genres' :key = 'genre'><input type='checkbox' :value='genre' class = 'genrecheckbox'>{{genre}}</label>
</div>

</form>
<button @click='getGenres()'>Submit</button>
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
        var selectedGenres = ''
        const genreelements = document.getElementsByClassName('genrecheckbox')
        const url = document.getElementById('urltextbox').value
        for(var i=0; i<genreelements.length;i++){
            if(genreelements[i].checked == true){
                selectedGenres +=genreelements[i].value+","
            }
        }
        selectedGenres = selectedGenres.replace(/(^,)|(,$)/g, '')
        console.log(selectedGenres)
        console.log(url)

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
@media (max-width: 775px) {
    #genres{
        grid-template-rows: auto auto auto auto auto auto auto auto auto auto auto auto;
    }
}
</style>