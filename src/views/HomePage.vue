<template>
<div id = 'homePage' v-if='popularNovels[0]'>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">Most Popular</h3>
</div><br>
<div id = 'popular'>
<HomePageNovelCard 
    :novelData='popularNovels[0]'
    type="main"
    id = 'mainPopular'/>
<div id = "popularList">
        <div v-for='novel in popularNovels.slice(1,popularNovels.length)' :key = 'novel.title'>
            <HomePageNovelCard 
                :novelData='novel' 
                class = 'popularnovel' 
                type = 'general'
            />
        </div>
</div>
</div>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">New Projects</h3>
</div><br>
<div class = "novelrow">
        <div v-for='novel in recentNovels' :key = 'novel.title'>
            <HomeCard :novelData='novel' type = "home"/>
        </div>
</div>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">Latest Releases</h3>
</div><br>
<div class = "novelrow">
        <div v-for='novel in latestNovels' :key = 'novel.title'>
            <HomeCard :novelData='novel' type = "home"/>
        </div>
</div>
</div>
</template>

<script>
import axios from 'axios'
import UtfBox from '../components/UtfBox'
import HomePageNovelCard from '../components/HomePageNovelCard'
import HomeCard from '../components/HomeCard'
export default{
    name:'HomePage',
    props:[
        'tier'
    ],
    components:{
        UtfBox,
        HomePageNovelCard,
        HomeCard
    },
    data(){
        return{
            popularNovels:[],
            recentNovels:[],
            latestNovels:[]
        }
    },
    created(){
        axios.get('http://tententranslation.com/home?tier='+this.tier)
          .then(response => {
            this.popularNovels = response.data['popular']
            this.recentNovels = response.data['recent']
            this.latestNovels = response.data['latest']
            console.log(response)
          })
          .catch(err => {
            console.log(err)
          })
    }
}

</script>
<style scoped>
#homePage{
    width:100%;
}
h3{
    font-size:20px;
    margin-left:10px;
}
.divide{
    display:flex;
    flex-direction:row;
    border-bottom:1px var(--borderColor) solid;
    height:30px;
    width:100%;
    padding-bottom:35px;
}
#popularList{
   display: grid;
   grid-template-columns: auto auto auto auto;
   margin-right:auto;
   height:fit-content;
   
}
.novelrow{
    display: flex;
    flex-direction:row;
    margin:auto;
    height:fit-content;
}
#popular{
    display:flex;
    flex-direction:row;
}
@media (max-width: 1200px){
     .novelrow{
         display:grid;
         grid-template-columns: auto auto auto;
    }
    #popular{
        flex-direction:column;
    }
    #popularList{
   grid-template-columns: auto auto;
   margin-right:auto;
   margin-left:auto;
   gap:50px;
   width:400px;
   padding-left:0px;
   transition: all .2s ease;
    }
    #mainPopular{
        margin-left:auto;
        margin-right:auto;
    }
  }
@media (max-width: 775px) {
    .novelrow{
         grid-template-columns: auto auto;
         margin:0px;
    }
    #popularList{
        grid-template-columns: auto;
       margin-left:10px;
    }
   
}
</style>