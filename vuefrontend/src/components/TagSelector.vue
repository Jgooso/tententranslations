<template>
<div>
<label for='tagfilter'>Filter
        <input id = 'tagfilter' @keyup='filterTag()' @focus='showtags()'>
    </label>
    <div  id = 'tagList'>
        <ul class = 'selectedtaglist' >
            <li v-for='tag in selectedtags' :key = 'tag'>
                <tagBox :tag='tag' @remove='removeTag'/>
            </li>
        </ul>
        <div id = 'tagselector'>
            <button v-for='tag in tags' :key='tag' class = 'tagbutton unselected' :id = 'tag' v-html='tag' @click='addTag(tag)'/>
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
            const tagbutton = document.getElementById(tag)
            tagbutton.classList.remove('unselected')
            if(!this.selectedtags.includes(tag)){
                this.selectedtags.push(tag)
            }
            console.log(this.selectedtags)
           
        },
        removeTag(removetag){
            const index = this.selectedtags.indexOf(removetag)
            this.selectedtags.splice(index,1)
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
border: 2px rgb(244,244,244) solid;
width:500px;
height:fit-content;
min-height:50px;
float:left;

}
#tagfilter{
    height:30px;
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
}
.tagbutton{
    border:none;
    color:lightgray;
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
@media (max-width: 775px) {
    #tagList{
        width:350px;
    }
    #tagselector{
        width:350px;
    }
}
</style>