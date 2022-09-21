<template>
<div id = 'signin' ref = 'signin'>
<div id = 'sign-in-card'>
<p id = 'error-message'/>
<button @click='$emit("closesignin")'>X</button>
<form>
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username">
    <br>
    <label for='email'>Email:</label><br>
    <input type='email'>
    <br>
    <label for='password'>Password:</label><br>
    <input type='password'>
    <br><br>
    <div>
    <input type = 'submit' value='Log In'>
    <input type='checkbox' name = 'remember'>
    <label for='checkbox'>Remember Me</label>
    </div>
</form>
</div>
</div>
</template>
<script>
import {getAPI} from '../axios-api'
export default{
    name:'SignIn',
    methods:{
        submit(){

        }
    }
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
#sign-in-card{
    position:fixed;
    background-color:lightgray;
    width:500px;
    height:500px;
    top:50%;
    left:50%;
    margin-top:-250px;
    margin-left:-250px;
}
form{
    position:absolute;
    top:50px;
    left:100px;
}
input{
    width:300px;
    margin-bottom:20px;
    height:50px;
    border-radius:5px;
    border:none;
}
input[type=submit]{
    background-color:var(--styleColor);
    width:100px;
    border-radius:20px;
    height:40px;
    color:white;
    font-size:14px;
    font-weight:400px;
}

</style>