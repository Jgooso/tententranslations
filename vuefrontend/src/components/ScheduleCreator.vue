<template>
<div class = 'schedule-creator'>
<div id = 'schedule-creator-selector'>
<select id = 'novel-selector'>
<option v-for='novel in novels'>{{novel.title}}</option>
</select>
<input type='time' id="appt" name="appt"
       min="8:00" max="20:00" required>
</div>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Sunday</label>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Monday</label>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Tuesday</label>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Thursday</label>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Friday</label>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Saturday</label>
<input type = 'submit' @click='submit()'>
</div>
</template>
<script>
import { getAPI } from '../axios-api'
export default{
    name:'ScheduleCreator',
    methods:{
        submit(){
            const time = document.getElementById('appt').value
            const novel = document.getElementById('novel-selector').value
            console.log(time)
            console.log(novel)
            const dates = document.getElementsByClassName('date-selector')
            console.log(dates[0].value)
            /*
            getAPI.post('/schedule', {novel:novel,time:time,dates:dates})
                .then(function (response) {
                    console.log(response);
                    loadingscreen.style.display = 'none'
            })
                .catch(function (error) {
                    console.log(error);
                    loadingscreen.style.display = 'none'
            }); 
            */
        }
    },
    data(){
        return{
            novels:[]
        }
    },
    created(){
        getAPI.get('/noveltitles')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.novels = response.data
            console.log(response.data)
          })
          .catch(err => {
            console.log(err)
          })
    }
}
</script>
<style scoped>
.schedule-creator{
position:fixed;
    background-color:lightgray;
    width:500px;
    height:500px;
    top:50%;
    left:50%;
    margin-top:-250px;
    margin-left:-250px;
    display:flex;
    flex-direction:column;
}
#novel-selector{
    background-color:white;
    border:none;
    margin-top:5px;
}
#appt{
    background:none;
    border:none;
    float:right;
    margin-right:50px;
    height:30px;
}
</style>
