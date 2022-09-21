<template>
    
</template>

<script>
export default{
    name:'UserBar',
    props:[
        'user'
    ]
}
</script>
<style scoped>
 #user-dropdown-box{
     border-bottom: 2px purple solid;
     background-color:lightgray;
     display:none;
 }
 #user-dropdown:hover+#user-dropdown-box{
     display:block
 }
 
</style>
