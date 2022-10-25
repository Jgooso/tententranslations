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
            <input type='button' class = 'category' @click='print("lastupload")' value = 'Latest' id = 'sort-lastupload'>
            <input type ='button' class = 'category' @click='print("title")' value = 'A-Z' id = 'sort-title'>
            <input type ='button' class = 'category' @click='print("length")' value = 'Length' id = 'sort-length'>
            <input type ='button' class = 'category' @click='print("views")' value = 'Views' id = 'sort-views'>
            <input type ='button' class = 'category' @click='print("firstupload")' value = 'New' id = 'sort-firstupload'>
        </div>
        <h6>Page {{page}} of {{(pageCount)}}</h6>
    </header>

    <div class = "novelList">
        <div v-for='novel in novelData' :key = 'novel.title' id = 'novels'>
            <NovelCard 
                :novelData='novel'
                type="browse"
                />
        </div>
    </div>
    <div id = 'pageNav'>
    <button v-if='page> 1'  @click='changePage(-1)'>Previous Page</button>
    <button v-if='page < pageCount' @click='changePage(1)'>Next Page</button>
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
        sort(a,b){
            switch (this.attributesort){
                case 'Latest':
                    if(Date.parse(a.lastupload) < Date.parse(b.lastupload)) { return 1; }
                    if(Date.parse(a.lastupload) > Date.parse(b.lastupload)) { return -1; }
                    return 0;
                case 'alphabetical':
                    if(a.title < b.title) { return -1; }
                    if(a.title > b.title) { return 1; }
                    return 0;
                case 'length':
                    if(a.firstChapter['chapternumber'] < b.firstChapter['chapternumber']) { return 1; }
                    if(a.firstChapter['chapternumber'] > b.firstChapter['chapternumber']) { return -1; }
                    return 0;
                case 'views':
                    const view_a = parseInt(a.views)
                    const view_b = parseInt(b.views)
                    if(view_a < view_b) { return 1; }
                    if(view_a > view_b) { return -1; }
                    return 0;
                case 'new':
                    if(Date.parse(a.firstupload) < Date.parse(b.firstupload)) { return 1; }
                    if(Date.parse(a.firstupload) > Date.parse(b.firstupload)) { return -1; }
                    return 0;

            }

        },
        getNovels(){
            var identifier = this.$route.params.identifier
        console.log(identifier)
        if(identifier != undefined){
            identifier = identifier.replace(/&nbsp;/g,'|')
        }
        const url = '/novel/multiple?tier='+this.tier+'&identifier='+identifier+'&order='+this.attributesort+'&page='+this.page
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
        print(p){
            const selected = document.getElementsByClassName('selected')
            this.attributesort = p
            for(var i=0; i < selected.length; i++){
                selected[i].classList.remove('selected')
            }
            document.getElementById('sort-'+p).classList.add('selected')
            console.log(p)
            this.getNovels()
        },
        changePage(change){
            this.page = this.page + change
            this.getNovels()
        }
        
    },
    created(){
         var identifier = this.$route.params.identifier
         if(identifier != undefined){
            identifier = identifier.replace(/&nbsp;/g,'|')
        }
        getAPI.get('/novels-page-count?tier='+this.tier+'&identifier='+identifier)
          .then(response => {
            console.log('Post API has recieved data')
            console.log(response.data)
            this.pageCount = response.data['page_count']
            this.novelCount = response.data['novel_count']
            this.getNovels('lastupload',1)  
          })
          .catch(err => {
            console.log(err)
          })
        this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        // react to route changes...

            if(Object.keys(previousParams).includes('browsetype') && Object.keys(toParams).length == 0){
                const selected = document.getElementsByClassName('selected')
                this.getNovels('lastupload',1)
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
     padding:10px;
 
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
