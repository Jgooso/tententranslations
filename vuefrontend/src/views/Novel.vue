<template>
<div>
    <router-view v-if='isMounted'
      :novelData="novelData"
      :chapterList="chapterList"
      :sectionList='sectionList'
      :tier='tier'
      :key='$route.params.chapter'
    />
</div>
</template>
<script>
  import { getAPI } from '../axios-api'
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
    const url = '/novel/single?novel='+this.$route.params.title+'&tier='+this.tier
            getAPI.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelData=response.data['Novel']
            this.sectionList=response.data['Chapters'].filter(chapter => chapter.chapternumber == 0)
            this.chapterList=response.data['Chapters'].filter(chapter => chapter.chapternumber != 0)
            this.isMounted=true
          })
          .catch(err => {
            console.log(err)
          })
       console.log(this.$route.params)
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
    height:30px;
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
  }

</style>

