<template>
<div class = 'NovelCard'>
    <div  class = "cover_image"  @click='goTo(novelData.id)'>
        <img :src="novelData.image" v-if='novelData.image'/>
        <span class='overlay'></span>
    </div>
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" v-text='novelData.title' id = 'title'/>
    <div class = 'chapter'> 
        <router-link 
         :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.firstChapter[0]}}" 
         v-text='novelData.firstChapter[0]' 
         class = 'chapterNumber'/>
        <p class = 'date' v-text = "new Date(novelData.firstChapter[1]).toLocaleString('default', { month: 'long', day:'numeric', year:'numeric' })"/>
        
    </div>
    <div class = 'chapter'>
        <router-link 
         :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.secondChapter[0]}}" 
         v-text='novelData.secondChapter[0]' 
         class = 'chapterNumber'/>
        <p class = 'date' v-text = "new Date(novelData.secondChapter[1]).toLocaleString('default', { month: 'long', day:'numeric', year:'numeric' })"/>
    </div>
</div>
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
    width:170px;
    max-height:515px;
    margin-left:50px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:0;

}
.cover_image{
    overflow:hidden;
    width:100%;
   
}
.chapter{
    width:100%;
    height:fit-content;
    display:flex;
    flex-direction:row;
    margin-top:10px;
}
.chapterNumber{
    background-color:rgb(221,221,221);
    border-radius:10px;
    text-align:center;
    font-size:12px;
    line-height:12px;
    color:rgb(102,102,102);
    width:43px;
    height:24px;
    font-weight:bold;
    padding-top:6px;
    
}
.chapterNumber:hover{
    background-color:var(--styleColor);
    color:white;
    transition: all .3s ease;
    text-decoration:none;
}
#title{
    font-weight:bold;
    color:var(--textColor);
    text-decoration:none;
    height:fit-content;
}
#title:hover{
    color:var(--styleColor);
     transition: all .3s ease;
}
.date{
    color:rgb(146,146,146);
    font-size: 12px;
    margin-left:5px;
    height:24px;
    line-height:24px;
    vertical-align: middle;

}
.cover_image img{
     transition: all .2s ease;
     width:100%;
}
.cover_image:hover img{
    transform:scale(1.1);
    
}
.cover_image:hover{
    color:rgba(250,250,250,0.5);
    z-index: 4;
}
span.overlay {
background: rgba(0,0,0,0.2);
display: none;
height: 100%;
width: 100%;
position: relative;
bottom: 100%;
margin-top: 0px;
}
.cover_image:hover span.overlay {
display:block;


}
@media (max-width: 775px) {
    .NovelCard{
        height:fit-content;
        width:320px;
        margin-bottom:20px;
        border-bottom:2px black solid;
    }
}
</style>