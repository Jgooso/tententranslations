<template>
<div  id = "navigation">
    <select id = "myselect" @change="selectChapter()">
        <option 
            v-for="chapter in chapterList" 
            :key="chapter.chapterNumber"
            :value="chapter.chapterNumber" 
            :selected = "{'selected':($route.params.chapter===5)}">
            {{chapter.chapterNumber}} - {{chapter.title}}
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
                this.$emit('changeChapter', x)
                document.getElementsByTagName('option')[8].selected='selected'
                console.log(document.getElementsByTagName('option')[8].selected)
                this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:x}})
                

            },
            moveChapters(direction){
                const x = parseInt(this.$route.params.chapter)+direction
                this.$emit('changeChapter', x)
                this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:x}})
                
            },
            
        }
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
