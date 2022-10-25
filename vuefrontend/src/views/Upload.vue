<template>
<div id = 'download'>
    <div id = 'loadingscreen'><div class="loader"></div></div>
    <label for="fname">URL:
        <input type = "text" id = 'urltextbox' name = 'url' maxlength="34" style='width:280px' >
    </label>
    <input type="file"
       id="cover-image" name="cover_image"
       accept="image/png, image/jpeg">
    <GenreSelector
    :genres='genres'
    :selectedgenres='selectedgenres'
    />
    <br><br>
    <input type = 'submit' @click='postData()'>
    <TagSelector
    :tags='tags'
    :selectedtags='selectedtags'
    />
</div>

</template>
<script>
import { getAPI } from '../axios-api'
import tagBox from '../components/TagBox'
import GenreSelector from '../components/GenreSelector'
import TagSelector from '../components/TagSelector'
export default{
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
        GenreSelector,
        TagSelector
    },
methods:{
        postData(){
            const loadingscreen = document.getElementById('loadingscreen')
            loadingscreen.style.display = 'block'
            const url = document.getElementById('urltextbox').value;
            const genres = document.getElementsByClassName('genrecheckbox')
            var selectedGenres = []
            for(var i=0; i < genres.length; i++){
                if(genres[i].checked==true){
                    selectedGenres.push(genres[i].value)
                }
            }
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
        getAPI.get('/uploaddata')
          .then(response => {
            console.log('Descriptor API has recieved data')
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
button{
    background:none;
    border-right:none
}

input{
    margin-right:5px;
}
#download{
    width:100%;
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
    width:100%;
    height:100%;
    background-color:rgba(0,0,0,0.5)
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
@media (max-width: 775px) {
    #genres{
        grid-template-rows: auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto;
        width:300px;
        margin-left:20px;
    }
    #tagList{
        width:350px;
    }
    #tagselector{
        width:350px;
    }
}
</style>