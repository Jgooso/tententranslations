<template>
<router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" style="text-decoration:none">
    <div id = 'HomeCard' >
        <p v-text='novelData.title' id = 'title' />
        <div id = 'chapter-box'>
            <p id = "recent-chapters">Recent Chapters</p>
            <router-link :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.firstChapter['chapternumber']}}" style='text-decoration:none'>
                <div class = 'chapter'> 
                    <p v-text='novelData.firstChapter["chapternumber"]' class = 'chapterNumber'/>
                    <p class = 'date' v-text = "novelData.firstChapter['uploaddate']"/>
                </div>
            </router-link>
            <hr style='margin:0px'>
            <router-link v-if='novelData.secondChapter' :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.secondChapter['chapternumber']}}" style='text-decoration:none'>
                <div class = 'chapter'>
                    <p v-text='novelData.secondChapter["chapternumber"]' class = 'chapterNumber'/>
                    <p class = 'date' v-text = "novelData.secondChapter['uploaddate']"/>
                </div>
            </router-link>
        </div>
    </div>
</router-link>
</template>

<script>
export default{
    name:'HomeCard',
    props:[
        'novelData'
    ],
        methods:{
            goTo(novel){
                this.$router.push({name: 'coverPage', params:{title:novel}})
            }
        }
}
</script>
<style scoped>
#HomeCard{
    width:120px;
    height:280px;
    margin:auto;
    margin-left:50px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:10px;
    border-radius:5px;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
}
#HomeCard:hover{
    box-shadow: 0 4px 8px 0 var(--styleColor), 0 6px 20px 0 var(--styleColor);
}
.home{
    width:100px;;
}
.chapter{
    height:40px;
    display:flex;
    flex-direction:column;
    vertical-align: middle;
    width:100%;
    border-radius:10px;
}
.chapter:hover{
    outline:1px solid purple;    
}
#chapter-box{
    border-radius:5px;
    position:relative;
    bottom:10px;
    margin-bottom:auto;
}
.chapterNumber{
    text-align:center;
    font-size:15px;
    line-height:12px;
    color:var(--textColor);
    width:43px;
    height:24px;
    font-weight:bold;
    padding-top:6px;
    margin-top:auto;
    margin-bottom:auto;
    text-decoration:none;
    margin-right:0px;
    
}
#title{
    font-weight:bold;
    font-size:17px;
    color:var(--textColor);
    text-decoration:none;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    height:40%;
}
.date{
    color:rgb(146,146,146);
    font-size: 12px;
    height:24px;
    line-height:24px;
    vertical-align: middle;
    margin-top:auto;
    margin-bottom:auto;
    margin-left:7px;
    margin-right:1px;

}

@media (max-width: 775px) {
    #HomeCard{
        margin-left:0px;
    }
    #HomeCard:hover{
        width:120px;
}
#chapter-box{
    width:100%;
}
}
</style>