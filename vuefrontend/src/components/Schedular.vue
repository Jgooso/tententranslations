<template>
<div class = 'schedular'>
<button @click='showCreator()'>New</button>
<select id = 'novel-selector' @change="selectNovel()">
<option v-for='novel in novels' :value='novel.novelid'>{{novel.title}}</option>
</select>

<ul>

<li v-for='(scheduleDay,day) in scheduleList' :key='day'>
{{day}}
<ul>
    <li v-for='schedule in scheduleDay' :key='schedule.day+schedule.time'>
        <div>
            {{timeConverter(schedule.time)}}
            {{schedule.title}}
        </div>
    </li>
    </ul>
</li>
</ul>

<div id = 'schedule-creator'>
<div id = 'schedule-creator-selector'>
<input type='time' id="appt" name="appt"
       min="8:00" max="20:00" required>
</div>
<label><input type = 'checkbox' value = 'Sunday' class = 'date-selector'>Sunday</label>
<label><input type = 'checkbox' value = 'Monday' class = 'date-selector'>Monday</label>
<label><input type = 'checkbox' value = 'Tuesday' class = 'date-selector'>Tuesday</label>
<label><input type = 'checkbox' value = 'Wednesday' class = 'date-selector'>Wednesday</label>
<label><input type = 'checkbox' value = 'Thursday' class = 'date-selector'>Thursday</label>
<label><input type = 'checkbox' value = 'Friday' class = 'date-selector'>Friday</label>
<label><input type = 'checkbox' value = 'Saturday' class = 'date-selector'>Saturday</label>
<input type = 'submit' @click='submit()'>

</div>
</div>
</template>

<script>
import {getAPI} from '../axios-api'
export default{
    name:'Schedular',
    data(){
        return{
            scheduleList:[],
            novels:[],
            novel:[]
        }
    },
    methods:{
        timeConverter(time){
            var convertedTime = parseInt(time)
            if((convertedTime % 12) == convertedTime){
                convertedTime = (convertedTime %= 12).toString() + ':00 AM'
            }else{
                convertedTime = (convertedTime %= 12).toString() + ':00 PM'
            }
            return convertedTime
        },
        selectNovel(){
            this.novel = document.getElementById("novel-selector").value
            console.log(this.novel)
            getAPI.get('/schedule?novel='+this.novel)
          .then(response => {
            console.log('Schedule API has recieved data')
            console.log(response)
            this.scheduleList=response.data
          })
          .catch(err => {
            console.log(err)
          })
        },
        showCreator(){
            document.getElementById('schedule-creator').style.display='flex'
        },
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
            document.getElementById('schedule-creator').style.display='none'
            
            
        },
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
.schedular{
    width:100%
}
#schedule-creator{
position:fixed;
    background-color:lightgray;
    width:500px;
    height:500px;
    top:50%;
    left:50%;
    margin-top:-250px;
    margin-left:-250px;
    display:none;
    flex-direction:column;
}
#appt{
    background:none;
    border:none;
    float:right;
    margin-right:50px;
    height:30px;
}
@media (max-width: 775px) {
    #novel-selector{
        width:350px;
    }
}
</style>