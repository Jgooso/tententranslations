<template>
<div>
<select>

</select>
<table>
<tr>
<td>Title</td>
<td></td>
</tr>
</table>
</div>
</template>

<script>
export default{
    name: 'NovelInformation',
    props:[
        'novel'
    ],
    data(){
        return{
            novelData:[]
        }
    },
    created(){
        
    },
    methods:{
        getNovel(){
            const url = '/novel/single?novel='+this.novel+'&tier='+5
            getAPI.get(url)
          .then(response => {
            console.log('Post Novel has recieved data')
            this.novelData=response.data['Novel']
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
}
</script>
