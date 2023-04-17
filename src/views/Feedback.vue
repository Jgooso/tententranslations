<template>
    <div id = 'feedback'>
        <div v-for='f in feedback'  :key = 'f.id' class = 'feedbackbox' :id = 'f.id'>
            <p>{{f.feedback}}</p>
            <button class = 'delete-feedback' @click='deleteFeedback(f.id)'>X</button>
        </div>
        <nav id = 'page-navigation'>
         <button class = 'page-button' id = 'left-arrow'>&larr;</button>
        <button class = 'page-button' id = 'right-arrow'>&rarr;</button>
        </nav>
    </div>
</template>

<script>
import axios from 'axios'
export default{
    name:'Feedback',
    data(){
        return{
            page:1,
            feedback:[]
        }
    },
    methods:{
        getFeedback(change){
            this.page = this.page + change
            axios.get(`http://tententranslation.com/feedback?page=${this.page}`)
          .then(response => {
            this.feedback = response.data
          })
          .catch(err => {
            console.log(err)
          })
        },
        deleteFeedback(id){
            document.getElementById(id).style.display='none'
            axios.delete(`/feedback?id=${id}`).then(response =>{
                console.log('Deleted Feedback')
            }).catch(err =>{
                console.log(err)

            })
        }
    },
    created(){
        this.getFeedback(0)
    }
}
</script>
<style scoped>
#feedback{
    display:flex;
    flex-direction:row;
}
.feedbackbox{
    border: 1px solid var(--borderColor);
    width: 100%;
    margin-bottom:50px;
    height:200px;
    overflow:scroll;
    margin-left:20px;
    margin-right:20px;
}
.delete-feedback{
    border:none;
    background:transparent;
    position:relative;
    bottom:30px;
    left:97%;
}
.page-button{
    border:none;
    background-color:rgba(200,200,200,0.2);
    width: 50px;
    height:50px;
}
#page-navigation{
    margin:auto;
    width:200px;
}

#right-arrow{
    margin-left:100px;
}
</style>