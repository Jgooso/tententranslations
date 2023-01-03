<template>
<div>
<label for='tagfilter'>Filter
        <input type='text' id = 'tagfilter' @keyup='filterTag()' @focusin='showtags()'>
    </label>
    <div  id = 'tagList'>
        <ul class = 'selectedtaglist' >
            <li v-for='tag in selectedtags' :key = 'tag'>
                <tagBox :tag='tag' @remove='removeTag'/>
            </li>
        </ul>
        <div id = 'tagselector'>
            <label v-for='i in tags.length' :key='i' class = 'tagbutton unselected'  :id = 'tags[i]'>
                <input type='checkbox' :value='tags[i]' :name = '"tag"+i' @change='addTag(tags[i])'>
                <p v-html='tags[i]'/>
            </label>
        </div>
    </div>
</div>
</template>

<script>
import tagBox from '../components/TagBox'
    export default{
        name:'TagSelector',
        props:[
            'tags',
            'selectedtags'
        ],
        components:{
            tagBox
        },
        methods:{
            addTag(tag){
                console.log(tag)
            const tagbutton = document.getElementById(tag)
            tagbutton.classList.remove('unselected')
            const tagvalue = tag.replace(/[0-9]/g, '')
            if(!this.selectedtags.includes(tagvalue)){
                this.selectedtags.push(tagvalue)
            }
            console.log(this.selectedtags)
           
        },
        removeTag(removetag){
            const index = this.selectedtags.indexOf(removetag)
            this.selectedtags.splice(index-1,1)
            console.log(this.selectedtags)
            document.getElementById(removetag).classList.add('unselected')
        },
        filterTag(){
            var input, tagbuttons, txtValue
            input = document.getElementById('tagfilter').value.toUpperCase()
            tagbuttons = document.getElementsByClassName('tagbutton')
            for(var i = 0; i < tagbuttons.length; i++){
                txtValue = tagbuttons[i].value || tagbuttons[i].innerText;
                if (txtValue.toUpperCase().indexOf(input) > -1) {
                    tagbuttons[i].style.display = "";
                } else {
                    tagbuttons[i].style.display = "none";
                }
            }
        },
        showtags(){
           document.getElementById('tagselector').style.display = 'flex'
        },
        hidetags(){
            document.getElementById('tagselector').style.display = 'none'
        },
        }
    }
</script>

<style scoped>
#tagList{
border: 2px black solid;
width:500px;
height:fit-content;
min-height:50px;
float:left;
padding:20px;
box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) inset, 0 6px 20px 0 rgba(0, 0, 0, 0.19) inset;
}
#tagfilter{
    height:30px;
    border:none;
}
.selectedtaglist{
    display:inline;
    list-style: none;
    padding:0px;
   
}

.selectedtaglist li{
    display:inline;
    float:left;
    margin-left:10px;
}

#tagselector{
    display:none;
    flex-direction:column;
    overflow:scroll;
    width:100%;
    max-height:500px;
    height:100%;
    background-color:white;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2) inset, 0 6px 20px 0 rgba(0, 0, 0, 0.19) inset;
}
.tagbutton{
    border:none;
    color:lightgray;
    background:none;
}
.unselected{
    color:black;
}
.unselected:hover{
    background-color:blue;
    color:white;
}
#tagSelect{
    background:lightgray;
    border:none;
    -webkit-appearance: none;
}
#tags{
    width:100%
}
#tagtextbox{
    width:500px;
    text-align:left;
    overflow-wrap: break-word
}
input[type="checkbox"]  {
   display: none;
}
@media (max-width: 775px) {
    #tagList{
        width:350px;
    }
    #tagselector{
        width:350px;
    }
}
</style>