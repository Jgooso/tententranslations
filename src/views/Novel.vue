<template>
<div class = 'novel'>
    <router-view v-if='isMounted'
      :novelData="novelData"
      :chapterList="chapterList"
      :sectionList='sectionList'
      :tier='tier'
      :key='$route.params.chapter'
      :url='url'
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
      'tier',
      'url'
    ],
    created () {
    const get_url = `http://${url}/novel/single?novel=${this.$route.params.title}&tier=${this.tier}`
            axios.get(get_url)
          .then(response => {
            this.novelData=response.data['Novel']
           const sections = response.data['Chapters'].filter(chapter => chapter.chapternumber == 0)
            if(sections.length > 0){
                this.sectionList = sections
            }else{
                this.sectionList = [{'section':0}]
            }
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapternumber != 0)
            this.isMounted=true
          })
          .catch(err => {
            console.log(err)
          })
  },
  
 
  }
</script>

