<template>
<div id = 'Browse' >

    <h1 id = 'sortCategory' v-html='this.$route.params.identifier ? this.$route.params.identifier : "All Novels"'/>

    <header id = 'top'>
        <div id = 'count'>
            <UtfBox shape = '&#9733;'/>
            <p id = 'resultCount'>{{novelCount}} RESULTS</p>
            <label class = 'category'> Order By</label>
        </div>

        <div id = 'sortButtons'>
            <input type='button' class = 'category selectable' style="border-left:1px solid var(--borderColor)" @click='sort("lastupload")' value = 'Latest' id = 'sort-lastupload'>
            <input type ='button' class = 'category selectable' @click='sort("title")' value = 'A-Z' id = 'sort-title'>
            <input type ='button' class = 'category selectable' @click='sort("length")' value = 'Length' id = 'sort-length'>
            <input type ='button' class = 'category selectable' @click='sort("views")' value = 'Trending' id = 'sort-views'>
            <input type ='button' class = 'category selectable' @click='sort("firstupload")' value = 'New' id = 'sort-firstupload'>
            <h6 id = 'pageNumber'>Page {{page}} of {{(pageCount)}}</h6>
        </div>
        
    </header>

    <div class = "novelList">
        <div v-for='novel in novelData' :key = 'novel.title' id = 'novels'>
            <NovelCard 
                :novelData='novel'
                type="browse"
                class = 'novelcard'
                />
        </div>
    </div>
    <div id = 'pageNav'>
    <button v-if='page > 1' class = 'navigationButton'  id = 'prev' @click='changePage(-1)'>&#8592;Previous Page</button>
    <button v-if='page < pageCount' class = 'navigationButton' id = 'next' @click='changePage(1)'>Next Page&#8594;</button>
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
            attributesort:'lastupload',
            page:1,
            pageCount:0,
            novelCount:0,
            }
        },
        props:[
            'tier'
        ],
        methods:{
        getNovels(identifier){  
            if(identifier != undefined){
                identifier = identifier.replace(/&nbsp;/g,'|')
            }
        const url = '/novel/multiple?tier='+this.tier+'&identifier='+identifier+'&order='+this.attributesort+'&page='+this.page
        console.log(identifier)
       getAPI.get(url)
          .then(response => {
            console.log('Post API has recieved data')
            this.novelData=response.data
            console.log(this.novelData[0])
          })
          .catch(err => {
            console.log(err)
          })
        },
        sort(p){
            const selected = document.getElementsByClassName('selected')
            this.attributesort = p
            for(var i=0; i < selected.length; i++){
                selected[i].classList.remove('selected')
            }
            document.getElementById('sort-'+p).classList.add('selected')
            console.log(p)
            this.getNovels(this.$route.params.identifier)
        },
        changePage(change){
            this.page = this.page + change
            this.getNovels(this.$route.params.identifier)
        },
        getPages(identifier){
            getAPI.get('/novels-page-count?tier='+this.tier+'&identifier='+identifier)
                .then(response => {
                    console.log('Post API has recieved data')
                    console.log(response.data)
                    this.pageCount = response.data['page_count']
                    this.novelCount = response.data['novel_count']
                    this.getNovels(identifier)  
                })
                .catch(err => {
                    console.log(err)
                })
        }
        
    },
    created(){
        var identifier = this.$route.params.identifier
            console.log(identifier)
        this.getPages(identifier)
        this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        // react to route changes...
            var identifier = this.$route.params.identifier
            console.log(identifier)
            if(identifier != undefined){
                identifier = identifier.replace(/&nbsp;/g,'|')
            }
            if(Object.keys(previousParams).includes('browsetype') && Object.keys(toParams).length == 0){
                const selected = document.getElementsByClassName('selected')
                this.getNovels(identifier)
                this.getPages(identifier)
                for(var i=0; i < selected.length; i++){
                selected[i].classList.remove('selected')
            }
            }
      }
    )     
    
    }
    
    }
</script>

<style scoped>
#Browse{
    width:100%;
}
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
    transition: all .3s ease;
     /*box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) inset , 0 6px 20px 0 rgba(0, 0, 0, 0.19) inset;*/
     padding:20px;
     border-radius:20px;
     padding-left:20px;
     padding-right:0px;
 
}
#count{
    width:275px;
    display:flex;
    flex-direction:row;
}
#sortButtons{
    width:100%;
    display:block;
}
#pageNumber{
    position:relative;
    vertical-align: middle;
    margin-bottom:-3px;
    padding:10px;
    padding-bottom:10px;
    padding-top:4px;
    font-size:15px;
    min-width:75px;
    float:right;
    margin-right:30px;
    border-radius:10px;
  
}
.category{
    background:none;
    border-bottom:none;
    color:gray;
    position:relative;
    margin-bottom:-3px;
    padding-bottom:10px;
    font-size:15px;
    min-width:75px;
    
}
.selectable{
    border:1px solid var(--borderColor);
    border-top-left-radius:5px;
    border-top-right-radius:5px;
    border-left:0px;
}
input[type='button'].category:hover{
    color:var(--styleColor);
    border-bottom:4px solid var(--styleColor);
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
.selected{
    color:var(--styleColor);
    border-bottom:4px solid var(--styleColor);
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    transition: all .3s ease;
    
}
.navigationButton{
    border:1px solid var(--borderColor);
    background:none;
}
#next{
    width:150px;
    margin-right:30px;
    float:right;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) , 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius:10px;
}
#prev{
    width:150px;
    float:left;
    margin-left:30px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) , 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius:10px;

}
#pageNav{
    width:100%;
    display:block;
}
@media (max-width: 1200px){
     .novelList{
         grid-template-columns: auto auto auto;
    }
    #top{
        flex-direction:column;
        height: 80px;
        
    }
  }
@media (max-width: 775px) {
    .novelList{
         grid-template-columns: auto;
    }
    .novelcard{
        width:100%;
    }
   
}
@media (max-width: 700px) {
    #top{
        height: 111px;
        
    }
    #next{
    width:150px;
    margin-right:0px;
    float:right;
}
#prev{
    width:150px;
    float:left;
    margin-left:0px;

}
   
}
</style>
