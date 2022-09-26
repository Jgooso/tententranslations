<template>
<div class = 'schedule-creator'>
<div id = 'schedule-creator-selector'>
<input type='time' id="appt" name="appt"
       min="8:00" max="20:00" required>
</div>
{{novel}}
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Sunday</label>
<label><input type = 'checkbox' value = 'Monday' class = 'date-selector'>Monday</label>
<label><input type = 'checkbox' value = 'Tuesday' class = 'date-selector'>Tuesday</label>
<label><input type = 'checkbox' value = 'Wednesday' class = 'date-selector'>Wednesday</label>
<label><input type = 'checkbox' value = 'Thursday' class = 'date-selector'>Thursday</label>
<label><input type = 'checkbox' value = 'Friday' class = 'date-selector'>Friday</label>
<label><input type = 'checkbox' value = 'Saturday' class = 'date-selector'>Saturday</label>
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
            console.log(time)
            console.log(this.novel)
            const dates = document.getElementsByClassName('date-selector')
            var selecteddates = []
            console.log(dates.length)
            for(var i=0; i < dates.length; i++){
                if(dates[i].checked==true){
                    selecteddates.push(dates[i].value)
                }
            }
            console.log(selecteddates)
            getAPI.post('/schedule', {novel:this.novel,time:time,dates:selecteddates})
                .then(function (response) {
                    console.log(response);
            })
                .catch(function (error) {
                    console.log(error);
            }); 
            console.log('what')
            
            
            
        },
        props:[
            'novel'
        ]
    },
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
#appt{
    background:none;
    border:none;
    float:right;
    margin-right:50px;
    height:30px;
}
</style>
