<template>
<div :class = 'type'>
    <div id = 'rank' v-html = 'novelData.row_num'/>
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
    border-radius:10px;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
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
    border-radius:5px;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
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
    font-size:17px;
    color:var(--textColor);
    text-decoration:none;
    height:fit-content;
    margin-top:0px;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow:hidden;
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
@media (max-width: 700px) {
    .main{
        width:300px;
    }
}
</style>