<template>
<div id = 'Browse' >
    <h1 id = 'sortCategory' v-html='this.$route.params.identifier ? this.$route.params.identifier : "All Novels"'/>
    <div id = 'top'>
        <div id = 'count'>
            <UtfBox shape = '&#9733;'/>
            <p id = 'resultCount'/>
            <label class = 'category'> Order By</label>
        </div>
        <div id = 'sortButtons'>
            <input type='button' class = 'category selectable' style="border-left:1px solid var(--borderColor)" @click='sort("latest_upload")' value = 'Latest' id = 'sort-lastupload'>
            <input type ='button' class = 'category selectable' @click='sort("title")' value = 'A-Z' id = 'sort-title'>
            <input type ='button' class = 'category selectable' @click='sort("length")' value = 'Length' id = 'sort-length'>
            <input type ='button' class = 'category selectable' @click='sort("views")' value = 'Trending' id = 'sort-views'>
            <input type ='button' class = 'category selectable' @click='sort("first_upload")' value = 'New' id = 'sort-firstupload'>
            <h6 id = 'pageNumber'>Page {{page}} of {{(pageCount)}}</h6>
        </div> 
    </div>

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
import NovelCard from '../components/NovelCard'
import UtfBox from '../components/UtfBox'
import axios from 'axios'
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
            attributesort:'latest_upload',
            page:1,
            pageCount:0,
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
        const url = (`http://127.0.0.1:5000/novel/multiple?tier=${this.tier}&identifier=${identifier}&order=${this.attributesort}&page=${this.page}`)
        axios.get(url)
          .then(response => {
            this.novelData=response.data
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
            this.getNovels(this.$route.params.identifier)
        },
        changePage(change){
            this.page = this.page + change
            this.getNovels(this.$route.params.identifier)
        },
        getPages(identifier){
            axios.get(`http://tententranslation.com/novels-page-count?tier=${this.tier}&identifier=${identifier}`)
                .then(response => {
                    this.pageCount = response.data['page_count']
                    this.getNovels(identifier)
                    document.getElementById('resultCount').innerHTML = `${response.data['novel_count']} RESULTS`  
                })
                .catch(err => {
                    console.log(err)
                })
        }
        
    },
    created(){
        var identifier = this.$route.params.identifier
        this.getPages(identifier)
        this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        // react to route changes...
            var identifier = this.$route.params.identifier
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
   min-height:900px;
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
