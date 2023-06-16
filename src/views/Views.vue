<template>
{{data}}
</template>

<script>
import axios from 'axios'
export default{
    name:'Views',
    data(){
        return{
            novel:[],
            data:[]
        }
    },
    created(){
        this.novel = 'JVJSF6F'
        axios.get(`http://tententranslation.com/views?novel=${this.novel}`).then(response => {
            this.data = response
          })
          .catch(err => {
            console.log(err)
          })
    }
}
</script>