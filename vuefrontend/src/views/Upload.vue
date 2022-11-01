<template>
<div id = 'download'>
    <div id = 'loadingscreen'><div class="loader"></div></div>
     <h1 id = "noveltitle">Lorem Ipsum</h1>
    <form id = 'upload' method='postData'>
        <div id = 'upload_tables'>
            <div  id = 'image-border' v-if='imageSelected'>
            <button id = 'remove-image' @click='this.imageSelected=false'>&#9747;</button>
            <img src='#' id = 'output'>
            <input type = 'file' id = 'image-selector' @change='showFile()'>
            </div>
            <table>
                <tr>
                    <td class='category'>Views</td>
                    <td class = 'info  unselectable'>0</td>
                </tr>
                <tr>
                    <td class='category'>Alternative</td>
                    <td class='info  unselectable'>ロレム・イプサム</td>
                </tr>
                <tr>
                    <td class='category'>URL</td>
                    <td class='info'><input type = "url" id = 'urltextbox' name = 'url' maxlength="34" style='border:none;' placeholder='Enter novel URL'></td>
                </tr>
                <tr>
                    <td class = 'category'>Authors</td>
                    <td class='info'>Author-san</td>
                </tr>
                <tr>
                    <td class='category'>Genres</td>
                    <td  @click='showGenres()' class='info' v-if='selectedgenres.length>0'>{{selectedgenres}}</td>
                    <td v-else style='color:red'  @click='showGenres()' class='info'>Select Genres</td>
                </tr>
                <tr>
                    <td class='category'>Tags</td>
                    <td @click='showTags()' class='info'  v-if='selectedtags.length>0'></td>
                    <td v-else style='color:red'  @click='showTags()' class='info'>Select Tags</td>
                    </tr>
            </table>
            <table>
                <tr>
                    <td class='category'>Release</td>
                    <td class='info unselectable'>20XX</td>
                </tr>
                <tr>
                    <td class='category'>Status</td>
                    <td class='info'>Unreleased</td>
                </tr>
                <tr>
                    <td class='category'>Novel</td>
                    <td class='info'>
                        <select id = 'completedEdit' placeholder='SELECT' style='color:red;' onfocus='this.style.color="rgb(136,136,136)"' form = 'upload' name = 'novelstatus'>
                            <option value="" disabled selected>Select your option</option>
                            <option value = 'Ongoing'>Ongoing</option>
                            <option value = 'Completed'>Completed</option>
                            <option value = 'On Hold'>On Hold</option>
                            <option value = 'Dropped'>Dropped</option>
                        </select>
                     </td>
                </tr>
       
            </table>
        </div>
        <div id = 'genre-selector'>
             <GenreSelector
                :genres='genres'
                :selectedgenres='selectedgenres'
                
                />
        </div>
        <TagSelector
            :tags='tags'
            :selectedtags='selectedtags'
            id = 'tag-selector'
        />
        
    </form>
    <div id = "summary">
        <div>
           <div style = "display:flex;flex-direction:row;border-bottom:2px lightgray solid;height:30px;"><UtfBox shape = '&#9733;'/><h3 id = "divider">SUMMARY</h3></div><br>
            <p id="noveldescription">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
    </div>
    <button @click='postData()' style='width:100%;margin-top:30px;'>Submit</button>

</div>
</template>
<script>
import { getAPI } from '../axios-api'
import GenreSelector from '../components/GenreSelector'
import TagSelector from '../components/TagSelector'
import UtfBox from '../components/UtfBox'
export default{
    data(){
        return{
            genres:[],
            tags:[],
            selectedtags:[],
            selectedgenres:[],
            imageSelected:true,
        }
    },
    components:{
        GenreSelector,
        TagSelector,
        UtfBox
    },
methods:{
        postData(){
            const loadingscreen = document.getElementById('loadingscreen')
            loadingscreen.style.display = 'block'
            const form = document.getElementById('upload')
            const formData = new FormData(form)
            try{
                const file = document.getElementById('image-selector').files[0]
                formData.append('file',file,file.name)
            }catch{
                console.log('no file')
            }
            console.log()
            getAPI.post('/novel/single',formData, {headers: {"Content-Type": "multipart/form-data"}}).then((res) => {
                console.log(res);
                loadingscreen.style.display = 'none'
            })
            .catch((err) => {
                console.log(err);
                loadingscreen.style.display = 'none'
            })
            /*
            getAPI.post('/novel/single', {url:url,tags:this.selectedtags,genres:selectedGenres,image:upload})
                .then(function (response) {
                    console.log(response);
                    loadingscreen.style.display = 'none'
            })
                .catch(function (error) {
                    console.log(error);
                    loadingscreen.style.display = 'none'
            }); 
            */
        },
        showFile(){
            
            const file = document.getElementById('image-selector').files[0]
            var image = document.getElementById('output')
	        image.src = URL.createObjectURL(file);
            image.style.display='block'
            console.log(file)
            console.log(image.src)
            this.imageSelected=true
            /*
            let data = new FormData()
            data.append('file', file, file.name)
            
            getAPI.post('/test',data, {headers: {"Content-Type": "multipart/form-data"}}).then((res) => {
                console.log(res);
            })
            .catch((err) => {
                console.log(err);
            })
            */

            
        },
        showGenres(){
            var genre_selector = document.getElementById('genre-selector')
            document.getElementById('tag-selector').style.display='none'
            if(genre_selector.style.display=='flex'){
                genre_selector.style.display = 'none'
            }else{
                genre_selector.style.display = 'flex'
            }
        },
        showTags(){
            var tag_selector = document.getElementById('tag-selector')
            document.getElementById('genre-selector').style.display='none'
            if(tag_selector.style.display=='flex'){
                tag_selector.style.display = 'none'
            }else{
                tag_selector.style.display = 'flex'
            }
        },
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
table{
    height:fit-content;
}
button{
    background:none;
    border-right:none
}
::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: red;
  opacity: 1; /* Firefox */
}
#upload{
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
     border-radius:20px;
     padding:20px;
}
input{
    margin-right:5px;
}
.unselectable{
      font-size:14px;
      color:rgb(136,136,136);
  }
#download{
    width:100%;
    height:fit-content;
}
#genre-selector{
    display:none;
}
#tag-selector{
    display:none;
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
#upload_tables{
    display:flex;
    flex-direction:row;
}
#image-selector{
    margin:auto;
    width:100px;
}
.category{
    font-weight: bold;
      padding-bottom: 10px;
      padding-right:20px;
      width:15%;
      min-width:125px;
      vertical-align: top;
      color:black;
   
}
#completedEdit{
     background-color:transparent;
    border:none;
    appearance: none;
}
.info{
    font-weight:normal;
      width: 85%;
      line-height: 20px;
      font-size:14px;
      vertical-align:top;
}
#output{
    margin:auto;
    width:100%;
    height:100%;
    display:none;
}
#image-border{
    height:300px;
    width:200px;
    border:1px solid black;
    margin-right:20px;
    border-radius:10px;
    background-color: var(--backgroundColor));
    float:left;
    transition: all .2s ease;
    overflow:hidden;
    display:flex
}
#remove-image{
    color:rgb(136,136,136);
    position:relative;
    top:0px;
    left:170px;
    height:30px;
    width:30px;
    border:none;
    font-size:20px;
}
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