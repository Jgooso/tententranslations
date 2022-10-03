<template>
<div class = 'content' >
    <br>
    <p id = 'sortCategory' v-html='this.$route.params.identifier ? this.$route.params.identifier : "All Novels"'/>
    <div id = 'top'>
        <div id = 'count'>
            <UtfBox shape = '&#9733;'/>
            <p id = 'resultCount'>{{novelData.length}} RESULTS</p>
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
        <div v-for='novel in novelData.sort(sort)' :key = 'novel.title' id = 'novels'>
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
            /*
            slugify(text) {
            return text          
                .normalize('NFKD')            
                .replace(/[^a-zA-Z0-9 ]/g, "")//remove nonletter chars             
                .trim()                                  
                .replace(/\s+/g, '-')//replace - with space 
        },*/
        sort(a,b){
            switch (this.attributesort){
                case 'latest':
                    if(Date.parse(a.last_updated) < Date.parse(b.last_updated)) { return 1; }
                    if(Date.parse(a.last_updated) > Date.parse(b.last_updated)) { return -1; }
                    return 0;
                case 'alphabetical':
                    if(a.title < b.title) { return -1; }
                    if(a.title > b.title) { return 1; }
                    return 0;
                case 'length':
                    if(a.firstChapter[0] < b.firstChapter[0]) { return 1; }
                    if(a.firstChapter[0] > b.firstChapter[0]) { return -1; }
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
        //document.title='Browse'
        var identifier = this.$route.params.identifier
        console.log(identifier)
        if(identifier != undefined){
            identifier = identifier.replace(/&nbsp;/g,'-')
        }
       getAPI.get('/novel/multiple?tier=5&category='+this.$route.params.browsetype+'&identifier='+identifier)
          .then(response => {
            console.log('Post API has recieved data')
            this.novelData=response.data
            console.log(this.novelData[0])
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
    color:var(--styleColor);
    border-bottom:4px solid var(--styleColor);
}

.category:focus{
    color:var(--styleColor);
    border-bottom:4px solid var(--styleColor);
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
