<template>
<div class = 'manager'>
    <div id = 'loadingscreen'><div class="loader"></div></div>
    <div id = 'management-navigator'>
        <router-link :to = "{name: 'uploadPage'}" class='manage-nav'>Upload</router-link>
        <router-link :to = "{name: 'schedulePage'}" class='manage-nav'>Schedule</router-link>
        <router-link :to = "{name: 'editPage'}" class='manage-nav'>Edit</router-link>
        <router-link :to = "{name: 'feedbackPage'}" class='manage-nav'>Feedback</router-link>
        <router-link :to = "{name: 'descriptorPage'}" class='manage-nav'>Descriptors</router-link>
    </div>
    <router-view
        :editable='true'
        id = 'editView'
        v-if='verified'
    />
    <div v-else id ='password-protection'>
        <label for='password'>Password:
            <input type = 'password' id = 'manage-password-input'>
        </label>
        <input type = 'submit' @click='submit()'>
    </div>
</div>
</template>

<script>
import { getAPI } from '../axios-api'
export default{
    name:'Manage',
    data(){
        return{
            verified:$cookies.get('verified')
        }
    },
    methods:{
        submit(){
            const pass = document.getElementById('manage-password-input').value
            if(pass == 'jeg4Novel'){
                this.verified = true;
                $cookies.set('verified',true)
            }
            
        }
    }
}
</script>

<style scoped>
.manager{
    display:flex;
    flex-direction:row;
    height:100%;
    min-height:1000px;
    margin-top:50px;
    margin-left:0px;
    width:100%;
}
#management-navigator{
    height:500px;
    background-color:lightgray;
    width:13%;
    display:flex;
    flex-direction:column;
    min-width:200px;
    margin-right:10px;
    left:0;
    position:fixed;
}
.manage-nav{
    color:black;
    text-align:center;
    width:200px;
    font-size:15px;
    padding-top:10px;
    padding-bottom:10px;
    border-bottom: 1px solid black;
    text-decoration:none;

    
}
#password-protection{
    width:87%;
position:relative;
align:right;
margin-left:200px;
display:flex;
flex-direction:column;
}
input[type='password']{
    width:300px;
    margin:auto;
    position:relative;
    float:right;
}
#editView{
    width:100%;
    align:right;
    margin-left:90px;
}
.loader {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
  margin:auto;
  margin-top:170px;

}
#loadingscreen{
    display:none;
    position:absolute;
    z-index:5;
    width:100%;
    height:100%;
    background-color:rgba(0,0,0,0.5)
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
@media (max-width: 775px) {
  #editView{
      margin-left:0px;
  }
}
</style>