<template>
<div  id = "navigation">
    <select id = "myselect" @change="selectChapter()">
        <option 
            v-for="chapter in chapterList" 
            :key="chapter.chapternumber"
            :value="chapter.chapternumber" 
            >
            {{chapter.chapternumber}} - {{chapter.title}}
        </option>
    </select>
    <NavButton 
            :previous='this.$route.params.chapter != 1'
            :next='this.$route.params.chapter<chapterList.length'
            v-on:move="moveChapters($event)"
            />
       
</div>
</template>
<script>
import NavButton from './Navbutton'
   export default{
        name: 'ChapterSelector',
        props:[
            'chapterList'
        ],components:{
            NavButton
        },
        methods:{
            selectChapter(){
                const x = document.getElementById("myselect").value
                this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:x}})
            },
            
            
        },
    }
</script>
<style scoped>
#navigation{
    display:flex;
    flex-direction:row;
    position: relative;
}
select{
    padding-left:10px;
    padding-right:10px;
    font-size:15px;
    width:355px;
    height:35px;
    background-color: rgb(235,235,235);
    border:none;
    border-radius:5px;
    font-weight:300;
}
</style>
