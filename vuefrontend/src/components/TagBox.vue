<template>
<div class = 'tagBox'>
    <p v-html='tag'/>
    <button @click = 'remove()'>x</button>
</div>
</template>

<script>
export default{
    name:'tagBox',
    props:[
        'tag'
    ],
    methods:{
        remove(){
            console.log(this.tag)
            this.$emit('remove',this.tag)
        }
    }
}
</script>
<style scoped>
.tagBox{
    display:flex;
    flex-direction:row;
    height:20px;
    font-size:15px;
    background-image:linear-gradient(rgb(244,244,244),rgb(236,236,236));
    border: 1px rgb(170,170,170) solid;
    border-radius:5px;
    width:fit-content;
    align-items:center;
    vertical-align:middle;
}
button{
    background:none;
    border:none;
    height:20px;
    margin-left:5px;
    margin:auto;
    font-weight:bold;
    margin-top:0px;
    margin-bottom:6px;
}
p{
    margin-top:15px;
}
</style>