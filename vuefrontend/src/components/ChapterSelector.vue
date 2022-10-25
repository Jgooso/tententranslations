<template>
<div id = 'control-bar'>
            <div class='control-buttons-container' selectable='false'>
             
                <button class = 'controlbuttons' @click='changeFontSize(1)'>+</button>
                <button class = 'controlbuttons' @click='changeFontSize(-1)'>-</button>
                  <!--
                <button class = 'controlbuttons'><font-awesome-icon icon="fa-solid fa-bookmark" /></button>
                <button class = 'controlbuttons'>&#xF288;</button> -->
             
            </div>
        <br><br>
        <div  id = "navigation">
        
            <select id = "myselect" @change="selectChapter()">
                <option 
                    v-for="chapter in chapterList" 
                    :key="chapter.chapternumber"
                    :value="chapter.chapternumber"
                    :selected ='this.$route.params.chapter==chapter.chapternumber'
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
            changeFontSize(change){
            var r = document.querySelector(':root');
            const new_font_size =parseInt(r.style.getPropertyValue('--fontsize').slice(0,2))+change
            if(new_font_size > 5){
            r.style.setProperty('--fontsize',  new_font_size+ 'px')
            }
            console.log(r.style.getPropertyValue('--fontsize'))
            }
            
            
        },
    }
</script>
<style scoped>
#navigation{
    display:flex;
    flex-direction:row;
    position: relative;
}
#myselect{
    padding-left:10px;
    padding-right:10px;
    font-size:15px;
    height:35px;
    background-color: var(--backgroundColor);
    border:none;
    border-radius:5px;
    font-weight:300;
    width:50%;
}
#control-bar{
    position: -webkit-sticky;
    position:sticky;
    top: 0;
    background-color: var(--backgroundColor);
    padding-top:10px;
    padding-bottom:20px;
    border-bottom:2px black solid
}
#editButton{
    width:170px;
    background-color:var(--styleColor);
    color:white;
    float:right;
    border-radius:5px;
}
.control-buttons-container{
    float:right;
    
}
button.controlbuttons{
    border-radius:15px;
    background-color:lightgray;
    height:30px;
    width:30px;
    font-size:20px;
    text-align:center;
    vertical-align:middle;
    line-height:20px;
    margin-left:17px;
    margin-right:10px;
    color:var(--styleColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
button.controlbuttons:hover{
    color:white;
    background-color:var(--styleColor);
    transition: all .2s ease;
}
#myselect.items{
    background-color:red;
}
@media (max-width:1000px) {
   #myselect{
       min-width:200px;
   }
  }
</style>
