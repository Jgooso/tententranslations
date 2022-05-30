<template>
<div>
    <router-view
      :novelData="novelData"
      :chapterList="chapterList"
      :sectionList='sectionList'
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
          novelData: [],
          chapterList:[],
          sectionList:[],
        }
    },
    props:[
      'tier'
    ],
    created () {
    const url = '/singlenovel/?novel='+this.$route.params.title+'&tier='+this.tier
    
       getAPI.get(url)
          .then(response => {
            console.log('Post API has recieved data')
        this.novelData=response.data['Novel'][0]
        this.sectionList=response.data['Chapter'].filter(chapter => !chapter.content)
        this.chapterList=response.data['Chapter'].filter(chapter => chapter.content)
          })
          .catch(err => {
            console.log(err)
          })
  }
 
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

