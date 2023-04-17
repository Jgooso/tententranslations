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
    const url = `http://tententranslation.com/novel/single?novel${this.$route.params.title}&tier=${this.tier}`
            getAPI.get(url)
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

<style>
button{
  border:none;
}
#chapter{
     display: flex;
     flex-direction:column;
}
#divider{
    font-size:18px;
    font-weight:bold;
    margin-left:15px;
    line-height:18px;
    padding-top:6px;
}
#cover {
    width: 100%;
    height: fit-content;
    display: flex;
    flex-direction: column;
    background-color: rgb(236, 237, 239);
    margin-top:0;
    padding-bottom:35px;
    min-height:500px;
    padding-left:20px;
    padding-right:20px;
  }

</style>

