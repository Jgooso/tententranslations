<template>
<div id = 'control-bar'>
            <div class='control-buttons-container' selectable='false'>
             
                <button class = 'controlbuttons' @click='changeFontSize(1)'>&#65291;</button>
                <button class = 'controlbuttons' @click='changeFontSize(-1)'>&#65293;</button>
                  <!--
                <button class = 'controlbuttons'><font-awesome-icon icon="fa-solid fa-bookmark" /></button>-->
                <button class = 'controlbuttons' @click='switchdarkmode()'>&#9680;</button> 
             
            </div>
        <br><br>
        <div  id = "navigation">
            <p id = 'selected-chapter'>223 - Later Story</p>
    <NavButton 
            :previous='this.$route.params.chapter != 1'
            :next='this.$route.params.chapter<chapterList.length'
            v-on:move="moveChapters($event)"
            id ='NavButtons'
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
        ],
        date(){
            return{
                darkmode:''
            }
        },components:{
            NavButton
        },
        methods:{
            selectChapter(){
                const x = document.getElementById("myselect").value
                this.$router.push({name: 'chapterPage', params:{title:this.$route.params.title,chapter:x}})
            },
            changeFontSize(change){
                 const v = document.getElementById('chapter-content')
                 const newFontSize = parseInt(getComputedStyle(v).getPropertyValue('font-size').slice(0,2))+change
                 if(newFontSize > 6){
                    v.style.fontSize=newFontSize+'px'
                    $cookies.set('font-size',newFontSize+'px')
                 }
                 
            },
            switchdarkmode(){
                this.$emit("switchmode")
        },
            handleClick(event){
                var box = document.getElementById('custom-select')
                if (!box.contains(event.target)) {
                   box.style.backgroundColor = 'red';
                }else{
                    box.style.backgroundColor = 'white';
                }
            }
        
            
            
        },
        mounted(){
            const v = document.getElementById('chapter-content')
            document.addEventListener('click', this.handleClick)
            if($cookies.get('font-size') == null){
                $cookies.set('font-size','19px')
                v.style.fontSize='19px'
            }else[
                v.style.fontSize = $cookies.get('font-size')
            ]
        }
    }
</script>
<style scoped>
#navigation{
    display:flex;
    flex-direction:row;
}
#custom-select{
    display:flex;
    flex-direction:column;
    position:absolute;
    background-color:white;
    max-height:500px;
    overflow:scroll;
    border:1px solid black;
    border-bottom:2px solid black;
    top:307px;
    width:50%;
    display:none;
}
.chapter-link{
    color:black;
    border-left:1px solid black;
    border-right:1px solid black;
    border-bottom:1px solid black;
    position:relative;
    padding:5px;
    width:100%;
    z-index: 1000;
}
.chapter-link:hover{
    color:var(--styleColor);
    font-weight:bold;
}
#selected-chapter{
    border:1px solid black;
    vertical-align:middle;
    padding-top:12.5px;
    margin-bottom:-5px;
    padding-left:5px;
    font-size:15px;
    height:50px;
    border-radius:5px;
    width:50%;
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
    color:var(--borderColor);
}
#NavButtons{
    position:relative;
    width:180px;
    height:50px;
    padding:5px;
    margin-left:35%;
}
#control-bar{
    top: 0;
    background-color: var(--backgroundColor);
    padding-top:10px;
    padding-bottom:20px;
    
}

.control-buttons-container{
    float:right;
    box-shadow: 0 4px 8px 0 var(--shadowColor), 0 6px 20px 0 var(--shadowColor);
    padding:5px;
    border-radius:5px;
    position:sticky;
    top:10px;
}
button.controlbuttons{
    border-radius:15px;
    height:30px;
    width:30px;
    font-size:20px;
    text-align:center;
    vertical-align:middle;
    font-weight:bold;
    background-color:var(--backgroundColor);
    line-height:20px;
    margin-left:17px;
    margin-right:10px;
    color:var(--styleColor);
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
#myselect.items{
    background-color:red;
}

@media (max-width:1000px) {
   #myselect{
       min-width:200px;
   }
  }
html:not([data-scroll='0']) {
    #chapter-content{
        background-color:blue;
    }

}
</style>
