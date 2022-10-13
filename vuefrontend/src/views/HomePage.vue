<template>
<div id = 'homePage'>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">Most Popular</h3>
</div><br>
<div id = 'popular'>
<HomePageNovelCard 
    :novelData='popularNovels[0]'
    type="main"/>
<div class = "novelList">
        <div v-for='novel in popularNovels' :key = 'novel.title' id = 'novels'>
            <HomePageNovelCard :novelData='novel'/>
        </div>
</div>
</div>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">New Projects</h3>
</div><br>
<div class = "novelrow">
        <div v-for='novel in recentNovels' :key = 'novel.title' id = 'novels'>
            <NovelCard :novelData='novel'/>
        </div>
</div>
<div class = 'divide'>
    <UtfBox shape = '&#x2B24;'/><h3 id = "divider">Latest Releases</h3>
</div><br>
<div class = "novelrow">
        <div v-for='novel in latestNovels' :key = 'novel.title' id = 'novels'>
            <NovelCard :novelData='novel'/>
        </div>
</div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
import UtfBox from '../components/UtfBox'
import HomePageNovelCard from '../components/HomePageNovelCard'
import NovelCard from '../components/NovelCard'
export default{
    name:'HomePage',
    props:[
        'tier'
    ],
    components:{
        UtfBox,
        HomePageNovelCard,
        NovelCard
    },
    data(){
        return{
            popularNovels:[],
            recentNovels:[],
            latestNovels:[]
        }
    },
    created(){
        getAPI.get('/home?tier='+this.tier)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.popularNovels = response.data['popular']
            this.recentNovels = response.data['recent']
            this.latestNovels = response.data['latest']
            console.log(this.recentNovels)
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
    border-bottom:2px lightgray solid;
    height:30px;
    width:100%;
}
.novelList{
   display: grid;
   grid-template-columns: auto auto auto auto;
   margin:auto;
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
</style>