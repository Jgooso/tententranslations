<template>
    <div id = "box">
        <h3 id = "star" class = "utf-shape" v-html = 'shape'/>
        <h3 id = "point" class = "utf-shape">&#9670;</h3>
    </div>
</template>
<script>
    export default{
        name: 'UtfBox',
        props:[
            'shape',
        ]
    }
</script>
<style scoped>

.utf-shape{
    font-size:18px;
    padding:0;
    margin:0;
    font-weight:bold;
    color:var(--styleColor);
}
#star{
    background-color:var(--styleColor);
    color:white;
    width:30px;
    padding-top:4px;
    padding-left:6px;
    margin:0px;
    height:30px;
    z-index:2;
    border-radius:5px;
}
#point{
    margin:0px;
    height:30px;
    padding:0;
    padding-top:4px;
    width:15px;
    position:absolute;
    left:20px;
    
}
#box{
    display:flex;
    flex-direction:row;
    position:relative;
    user-select: none;
    -webkit-user-select: none;
    -webkit-touch-callout: none; 
}
</style>