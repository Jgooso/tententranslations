<template>
<div class = 'schedular'>
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
</div>
</template>

<script>
import {getAPI} from '../axios-api'
export default{
    name:'Schedular',
    data(){
        return{
            scheduleList:[],
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
        }
    },
    created(){
        getAPI.get('/schedule')
          .then(response => {
            console.log('Schedule API has recieved data')
            console.log(response)
            this.scheduleList=response.data
          })
          .catch(err => {
            console.log(err)
          })
}
}
</script>

<style scoped>
</style>