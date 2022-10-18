<template>
<div :class = 'type'>
    <!--
    <div  class = "cover_image"  @click='goTo(novelData.id)'>
        <img :src="novelData.imageurl" v-if='novelData.imageurl'/>
        <span class='overlay'></span>
    </div>
    -->
    <div id = 'rank'>1</div>
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" v-text='novelData.title' id = 'title'/>
    <div v-if='type=="main"'>
    <router-link :to = "{name: 'explorePage', params:{browsetype:'novel-genres',identifier:novelData.genre}}" v-text='novelData.genre' id = 'main-genre'/>
    <p v-html='novelData.description' id="description"/>
    <router-link :to = "{name: 'coverPage', params:{title:novelData.novelid}}" id = 'continue'>Continue Reading</router-link>
    </div>
     <router-link v-else :to = "{name: 'explorePage', params:{browsetype:'novel-genres',identifier:novelData.genre}}" v-text='novelData.genre' id = 'general-genre'/>
</div>

</template>

<script>
export default{
    name:'HomePageNovelCard',
    props:[
        'novelData',
        'type'
    ],
        methods:{
            goTo(novel){
                this.$router.push({name: 'coverPage', params:{title:novel}})
            }
        }
}
</script>
<style scoped>
.main{
    width:400px;
    max-height:500px;
    margin-left:50px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:10px;
    border:black 1px solid;
    border-radius:5px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius:10px;
    position:relative;

}
.general{
    width:170px;
    height:200px;
    margin-left:50px;
    margin-bottom:50px;
    display:flex;
    flex-direction:column;
    padding:10px;
    border:black 1px solid;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border-radius:5px;
    position:relative;

}
#rank{
    height:30px;
    width:30px;
    border-radius:15px;
    background-color:red;
    font-size:16px;
    color:white;
    position:absolute;
    left:-15px;
    top:-15px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    border: 1px solid black;
    text-align:center;
    padding:1px;
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
    margin-top:0px;
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
#general-genre{
    color:var(--textColor);
    text-decoration:none;
    font-weight:300;
}
#main-genre{
    color:rgb(136,136,136);
    text-decoration:none;
    font-weight:300;
    font-size:14px;
}
#general-genre:hover{
    color:var(--styleColor);
    transition: all .2s ease;
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
#description{
    overflow:hidden;
    max-height:300px;
    width:100%;
    font-size:15px;
    line-height:30px;
    font-weight:300;
}
#continue{
    color:rgb(153,153,153);
    text-decoration:none;
}
#continue:hover{
    color:var(--styleColor);
    transition: all .2s ease;
}
@media (max-width: 1200px) {
    .general{
        margin-left:0px;
        transition: all .2s ease;

    }
}
</style>