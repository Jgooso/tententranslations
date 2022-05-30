<template>
<div class = 'content' >
    <br>
    <p id = 'sortCategory'>{{ this.$route.params.identifier ? this.$route.params.identifier : 'All Novels' }}</p>
    <div id = 'top'>
        <div id = 'count'>
            <UtfBox shape = '&#9733;'/>
            <p id = 'resultCount'>{{novelData.filter(contains).length}} RESULTS</p>
            <label class = 'category'> Order By</label>
        </div>
        <div id = 'sortButtons'>
            <button class = 'category' @click='attributesort="latest"'>Latest</button>
            <button class = 'category' @click='attributesort="alphabetical"'>A-Z</button>
            <button class = 'category' @click='attributesort="length"'>Length</button>
            <button class = 'category' @click='attributesort="views"'>Most Views</button>
            <button class = 'category' @click='attributesort="new"'>New</button>
        </div>
    </div>
    <div class = "novelList">
        <div v-for='novel in novelData.filter(contains).sort(sort)' :key = 'novel.title' id = 'novels'>
            <NovelCard :novelData='novel'/>
        </div>
    </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import NovelCard from '../components/NovelCard'
import UtfBox from '../components/UtfBox'
    export default{
        name: 'Browser',
        components:{
            NovelCard,
            UtfBox,
        },
        data(){
            return{
            novelData:[],
            chapterList:[],
            attributesort:'latest'
            }
        },
        methods:{
            slugify(text) {
            return text          
                .normalize('NFKD')            
                .replace(/[^a-zA-Z0-9 ]/g, "")//remove nonletter chars             
                .trim()                                  
                .replace(/\s+/g, '-')//replace - with space 
            },
            contains(novel){
                if(!this.$route.params.browsetype){
                    return true
                }
                const identifier = this.$route.params.identifier;
                if(this.$route.params.browsetype.includes('author')){
                    return novel.author==identifier;
                }else if(this.$route.params.browsetype.includes('tag')){
                    return novel.tags.includes(identifier);
                }
                else if(this.$route.params.browsetype.includes('genre')){
                    return novel.genres.includes(identifier);
            }else{
                return true
            }
        },
        sort(a,b){
            switch (this.attributesort){
                case 'latest':
                    if(a.last_updated < b.last_updated) { return 1; }
                    if(a.last_updated > b.last_updated) { return -1; }
                    return 0;
                case 'alphabetical':
                    if(a.title < b.title) { return -1; }
                    if(a.title > b.title) { return 1; }
                    return 0;
                case 'length':
                    if(a.firstchapter.chapterNum < b.firstchapter.chapterNum) { return 1; }
                    if(a.firstchapter.chapterNum > b.firstchapter.chapterNum) { return -1; }
                    return 0;
                case 'views':
                    if(a.views < b.views) { return 1; }
                    if(a.views > b.views) { return -1; }
                    return 0;
                case 'new':
                    if(a.first_release < b.first_release) { return 1; }
                    if(a.first_release > b.first_release) { return -1; }
                    return 0;

            }

        }
        
    },
    created(){
       getAPI.get('/novels/?tier=2')
          .then(response => {
            console.log('Post API has recieved data')
        this.novelData=response.data['Novel']
        this.chapterList=response.data['Chapter']
        for (let i = 0; i < this.novelData.length; i++) { 
            var novel=this.novelData[i]
            novel['firstchapter']=this.chapterList.filter(chapter => chapter.novel==novel.id)[1]
            novel['secondchapter']=this.chapterList.filter(chapter => chapter.novel==novel.id)[0]
        }
        console.log(this.attributesort)
          })
          .catch(err => {
            console.log(err)
          })
         
    }
    
    }
</script>

<style scoped>
#novels{
    display:flex;
    flex-direction:row;
}
#top{
    display:flex;
    flex-direction:row;
    border-bottom:gray 2px solid;
    margin-bottom:30px;
    position:relative;
    height:37px;
}
.novelList{
   display: grid;
   grid-template-columns: auto auto auto auto;
   margin:auto;
   height:fit-content;
 
}
#count{
    width:275px;
    display:flex;
    flex-direction:row;
   

}
#sortButtons{
    width:400px;
}
.category{
    background:none;
    border:none;
    color:gray;
    position:relative;
    margin-bottom:-3px;
    padding-bottom:10px;
    font-size:15px;
    min-width:75px;
}
button.category:hover{
    color:purple;
    border-bottom:4px solid purple;
}

button.category:focus{
    color:purple;
    border-bottom:4px solid purple;
   outline: none;
    }
#sortCategory{
    font-size:18px;
    font-weight:bold;
    margin-bottom:28px;
    letter-spacing: 0.5px;
}
#resultCount{
    margin-left:20px;
    font-size:18px;
    font-weight:600;
    width:200px;
}

@media (max-width: 1200px){
     .novelList{
         grid-template-columns: auto auto auto;
    }
    #top{
        flex-direction:column;
        height: 79px;
    }
  }
@media (max-width: 775px) {
    .novelList{
         grid-template-columns: auto;
    }
   
}
</style>
