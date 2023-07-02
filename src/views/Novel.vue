<template>
<div class = 'novel'>
    <router-view v-if='isMounted'
      :novelData="novelData"
      :chapterList="chapterList"
      :sectionList='sectionList'
      :tier='tier'
      :key='$route.params.chapter'
      v-on:switchmode='$emit("switchmode")'
    />
</div>
</template>
<script>
  import axios from 'axios'
  export default {
    name: 'Novel',
    components: {
    },
    data () {
      return {
          chapterList:[],
          sectionList:[],
          novelData:[],
          isMounted:false
        }
    },
    props:[
      'tier'
    ],
    created () {
    const url = `http://127.0.0.1:5000/novel/single?novel=${this.$route.params.title}&tier=${this.tier}`
            axios.get(url)
          .then(response => {
            this.novelData=response.data['Novel']
           const sections = response.data['Chapters'].filter(chapter => chapter.chapter_number == 0)
            if(sections.length > 0){
                this.sectionList = sections
            }else{
                this.sectionList = [{'section':0}]
            }
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapter_number != 0)
            this.isMounted=true
          })
          .catch(err => {
            console.log(err)
          })
  },
  
 
  }
</script>

