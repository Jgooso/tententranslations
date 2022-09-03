<template>
<div class = 'content'>
<div id = 'managementnavigator'>
<router-link :to = "{name: 'uploadPage'}" class='nav'>Upload</router-link>
<router-link :to = "{name: 'schedulePage'}" class='nav'>Schedule</router-link>
<button>Edit</button>
<button>Manage Users</button>
</div>
<router-view/>

<ScheduleCreator/>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
export default{
    name:'Manage',
}
</script>

<style scoped>
.content{
    display:flex;
    flex-direction:row;
    height:1000px;
    margin-top:100px;
}
#managementnavigator{
    height:100%;
    background-color:lightgray;
    width:30%;
    display:flex;
    flex-direction:column;
}
.nav{
    color:black;
    margin:1px;
    text-align:center;
    width:100%;
    
}
</style>