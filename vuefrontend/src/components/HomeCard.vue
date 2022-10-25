<template>
<div id = "HomeCard">
    <!--
    <div  class = "cover_image"  @click='goTo(novelData.id)'>
        <img :src="novelData.imageurl" v-if='novelData.imageurl'/>
        <span class='overlay'></span>
    </div>
    -->
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" v-text='novelData.title' id = 'title'/>
    <div class = 'chapter'> 
        <router-link 
         :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.firstChapter['chapternumber']}}" 
         v-text='novelData.firstChapter["chapternumber"]' 
         class = 'chapterNumber'/>
        <p class = 'date' v-text = "novelData.firstChapter['uploaddate']"/>
        
    </div>
    <div class = 'chapter'>
        <router-link 
         :to = "{name: 'chapterPage', params:{title:novelData.novelid, chapter:novelData.secondChapter['chapternumber']}}" 
         v-text='novelData.secondChapter["chapternumber"]' 
         class = 'chapterNumber'/>
        <p class = 'date' v-text = "novelData.secondChapter['uploaddate']"/>
    </div>
</div>
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
    margin-left:50px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:10px;
    border:var(--borderColor) 1px solid;
    border-radius:5px;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);

}
#HomeCard:hover{
    width:200px;
      transition: all .3s ease;
}
#HomeCard:hover #title{
    -webkit-line-clamp: 8;
     transition: all .3s ease;
}
#HomeCard:hover .chapter{
    flex-direction:row;
}
.home{
    width:100px;;
}
.cover_image{
    overflow:hidden;
    width:100%;
   
}
.chapter{
    width:100%;
    height:fit-content;
    display:flex;
    flex-direction:column;
    margin-top:10px;
    border-radius:20px;
}
.chapter:hover{
    background-color:purple;
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
    margin-bottom:5px;
    
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
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
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
    .browse{
        height:fit-content;
        width:320px;
        margin-bottom:20px;
        border-bottom:2px black solid;
    }
}
</style>