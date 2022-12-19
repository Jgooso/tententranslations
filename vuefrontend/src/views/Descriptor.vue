<template>
<div>
    <h3>Novel Release</h3>
        <p v-for='p in novelrelease' v-html='p.descriptor+":"+p["count"]' class = 'bar'/>
    <h3>Novel status</h3>
        <p v-for='p in novelstatus' v-html='p.descriptor+":"+p["count"]' class = 'bar'/>
     <h3>Upload status</h3>
        <p v-for='p in uploadstatus' v-html='p.descriptor+":"+p["count"]' class = 'bar'/>
    <h3>Genres</h3>
        <p v-for='p in genres' v-html='p.descriptor+":"+p["count"]' class = 'bar'/>
    <h3>Tags</h3>
        <p v-for='p in tags' v-html='p.descriptor+":"+p["count"]' class = 'bar'/>
</div>
</template>

<script>
  import { getAPI } from '../axios-api'
export default{
    name:'descriptorPage',
    data(){
        return {
            novelrelease:[],
            genres:[],
            tags:[],
            novelstatus:[],
        }
    },
        created(){
            const url = '/descriptorbution'
            getAPI.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelrelease = response.data['novelrelease']
            this.genres = response.data['genre']
            this.tags = response.data['tag']
            this.novelstatus = response.data['novelstatus']
            this.uploadstatus = response.data['uploadstatus']
          })
          .catch(err => {
            console.log(err)
          })
        },
        mounted(){
            setTimeout(() => {
            var bars = document.getElementsByClassName('bar')
            for (var i = 0; i < bars.length;i++){
                const text = bars[i].innerHTML
                const length = parseInt(text.substring((text.indexOf(":")+1)))
                bars[i].style.width = (10*length)+'px'
                console.log(text.substring((text.indexOf(":")+1)))
            }
             }, 500);
        }
}
</script>

<style scoped>
.bar{
    background-color:lightblue;
}
</style>