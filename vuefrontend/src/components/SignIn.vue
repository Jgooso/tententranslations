<template>
<div id = 'signin'>
<form>
    <label for='text'>Username:</label><br>
    <input type='text'>
    <br>
    <label for='email'>Email:</label><br>
    <input type='email'>
    <br>
    <label for='password'>Password:</label><br>
    <input type='password'>
    <br><br>
    <input type = 'submit' value='Register'>
</form>
</div>
</template>
<script>
export default{
    name:'SignIn'
}
</script>

<style scoped>
#signin{
    position:fixed;
    width:100%;
    height:100%;
    z-index:5;
    background-color:rgba(0,0,0,0.95);
    display:none;
}
form{
    position:fixed;
    background-color:lightgray;
    width:500px;
    height:500px;
    top:50%;
    left:50%;
    margin-top:-250px;
    margin-left:-250px;
}
</style>