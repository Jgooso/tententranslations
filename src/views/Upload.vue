<template>
<div id = 'download'>
    <h1 id = "noveltitle">Lorem Ipsum</h1>
    <form id = 'upload' method='postData'>
        <div id = "novel-test">
            <div class = 'column1 label'>Views</div>
            <div class = 'column2 unselectable'>0</div>
            <div class = 'column1 label'>Alternative</div>
            <div class = 'column2 unselectable'>ロレム・イプサム</div>
            <div class = 'column1 label'>Raw</div>
            <div class = 'column2 info' ><input type = "url" id = 'urltextbox' name = 'url' maxlength="34" style='border:none;' placeholder='Enter novel URL'></div>
            <div class = 'column1 label'>Author</div>
            <div class = 'column2 info' >Author-san</div>
            <div class = 'column1 label'>Genres</div>
            <div class = 'column2 info'>
                <div @click='showGenres()' class='info' v-if='selectedgenres.length>0'>
                    <ul class='comma-list'>
                        <li v-for='genre in selectedgenres' :key='genre' v-html='genre'/>
                    </ul>
                </div>
                <div v-else style='color:red'  @click='showGenres()' class='info'>Select Genres</div>
            </div>
            <div class = 'column1 label'>Tags</div>
            <div class = 'column2 info'>
                <div @click='showTags()' class='info'  v-if='selectedtags.length>0'>
                    <ul class='comma-list'>
                        <li v-for='tag in selectedtags' :key='tag'  v-html='tag'/>
                    </ul>
                </div>
                 <div v-else style='color:red'  @click='showTags()' class='info'>Select Tags</div>
                    <TagSelector
                        :tags='tags'
                        :selectedtags='selectedtags'
                        id = 'tag-selector'
                    />
                </div>
                <div class = 'column3 label' style='grid-row:1/span 1'>Release</div>
                <div class = 'column4 unselectable' style='grid-row:1/span 1'>20XX</div>
                <div class = 'column3 label' style='grid-row:2/span 1'>Status</div>
                <div class = 'column4 unselectable' style='grid-row:2/span 1'>Unreleased</div>
                <div class = 'column3 label' style='grid-row:3/span 1'>Novel</div>
                <div class = 'column4 info' style='grid-row:3/span 1'>
                    <select id = 'completedEdit' placeholder='SELECT' style='color:red;' onfocus='this.style.color="rgb(136,136,136)"' form = 'upload' name = 'novelstatus'>
                        <option value="" disabled selected>Select your option</option>
                        <option value = 'Ongoing'>Ongoing</option>
                        <option value = 'Completed'>Completed</option>
                        <option value = 'On Hold'>On Hold</option>
                        <option value = 'Dropped'>Dropped</option>
                    </select>
                </div>
        </div>
        <div id = 'genre-selector'>
             <GenreSelector
                :genres='genres'
                :selectedgenres='selectedgenres'
                />
        </div>
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
import axios from 'axios'
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
    props:[
        'url'
    ],
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
            axios.post(`http://${url}/novel/single`,formData, {headers: {"Content-Type": "multipart/form-data"}}).then((res) => {
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
        getAPI.get(`http://${url}/uploaddata`)
          .then(response => {
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
  #novel-test{
     display:grid;
    grid-template-columns: 7.5% 60% 10% 10%;
    align-self:center;
    column-gap:20px;
    row-gap:10px;
    width:100%;
    transition: all .2s ease;
    margin-top:20px;
    padding:20px;
  }
.column1{
     grid-column:1 / span 1;
 }
 .column2{
     grid-column:2 / span 1
 }
 .column3{
     grid-column:3/ span 1;
 }
 .column4{
     grid-column:4/ span 1
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
    #novel-test{
        display:flex;
        flex-direction:column;
    }
}
</style>