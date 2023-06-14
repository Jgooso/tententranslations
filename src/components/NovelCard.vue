<template>
<router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" style="text-decoration:none">
<div class = 'NovelCard' >
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
    <div class = 'chapter' >
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
    name:'NovelCard',
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
.NovelCard{
    width:250px;
    min-height:250px;
    max-height:515px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:10px;
    border:var(--borderColor) 1px solid;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    border-radius:10px;
    text-decoration:none;


}
.NovelCard:hover{
    text-decoration:none;
    transition: all .2s ease;
    box-shadow: 0 4px 8px 0 var(--styleColor), 0 6px 20px 0 var(--styleColor);
}
#recent-chapters{
    font-size:14px;
    color:gray;
    font-weight:300;
    text-decoration:underline;
    margin-bottom:5px;
}
.chapter{
    height:40px;
    display:flex;
    flex-direction:row;
    vertical-align: middle;
    border-radius:10px;
    -webkit-border-radius:10px;
    overflow:hidden;
}
.chapter:hover{
    outline:1px solid var(--styleColor);
}
#chapter-box{
    width:70%;
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
    overflow:hidden;
    
}

#title{
    font-weight:bold;
    color:var(--textColor);
    text-decoration:none;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
    height:100px;
    margin-bottom:10px;
}

.date{
    color:rgb(146,146,146);
    font-size: 12px;
    margin-left:5px;
    height:24px;
    line-height:24px;
    vertical-align: middle;
    margin-top:auto;
    margin-bottom:auto;
    overflow:hidden;

}

@media (max-width: 775px) {
    .NovelCard{
        height:fit-content;
        width:100%;
        margin:auto;
        margin-bottom:20px;

    }
}
</style>