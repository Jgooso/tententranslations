<template>
    <div id = "navigator">
        <!--<a href = "index.html">Home</a>/-->
        <router-link :to = "{name: 'coverPage', params:{novel:novelid}}" v-text='novel'/>/
        <router-link :to = "{name: 'chapterPage', params:{novel:novelid,chapter:chapter.chapternumber}}" v-if='chapter' v-text='chapter.title+" - "+chapter.chapternumber'/>
    </div> 
</template>
<script>
    export default{
        name: 'Navigator',
        props:[
            'novel',
            'novelid',
            'chapter'
        ],
        
    }
</script>
<style scoped>
*{
      color:rgb(139, 139, 139);
      font-size: 12px;
  }
*:hover{
      color:var(--styleColor)
}
</style>