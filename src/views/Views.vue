<template>
<body id = 'view'>
    <div v-for='d in data' id = 'novels'>
        <p>{{d[1]}}   </p>
        <p>{{d[2]}}   </p><br>
        <p>{{d[3]}}</p>
    </div>
</body>
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
            this.data = response.data
          })
          .catch(err => {
            console.log(err)
          })
    }
}
</script>
<style>
#view{
    display:flex;
    flex-direction:column;
}
#novels{
 display:flex;
flex-direction:row;
}
</style>