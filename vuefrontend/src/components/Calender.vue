<template>
<body v-if='dates[8]'>
<h1>
{{month}}
</h1>
<div id = 'calender'>
    <div class = 'weekday' v-for='(day,v) in daysoftheWeek'>
    {{day}}
    </div>
    <div v-for='n in start_date'/>
    <div class = 'cell' v-for='(date,k) in dates' :key = 'date' @click.right='print(date,$event)'>
       <p>{{
           k
           }}
       </p>
       <div v-for='d in date'><p>{{d.novel}}</p><p>{{d.hour}}</p></div>
    </div>
</div>
<form id = 'scheduleCreator' method='formSubmit'>
<h6>Novel</h6>
<select id = 'novel-selector' name = 'novel' form = 'scheduleCreator'>
<option v-for='novel in novels' :value='novel.novelid'>{{novel.title}}</option>
</select>
<h6>Start Date</h6>
<input type="date" id="start" name="upload-start"
       min="2022-01-01" max="2030-12-31">
<h6>Upload Times</h6>
<input type="time" :name='"time"+t'
       min="08:00" max="20:00" v-for='t in times'>
<input type = 'button' style = 'background:none;border:none,border:1px solid black; height:30px; width:30px;' @click='this.times++' value = '+'>
<h6>Days of the Week</h6>
<label v-for='i in daysoftheWeek.length' style='width:100px;'>{{daysoftheWeek[i-1]}}<input type = 'checkbox' :name = 'daysoftheWeek[i-1]' :value = 'i-1'></label>
</form>
<button @click='formSubmit()'>a</button>
</body>
</template>

<script>
import { getAPI } from '../axios-api'
export default{
    name:'Calender',
    data(){
        return {
            dates:[],
            daysoftheWeek:['Sunday','Monday','Tuesady','Wednesday','Thursday','Friday','Saturday'],
            month:'',
            day:0,
            selectedDay:[],
            novels:[],
            times:1,
            start_date:0
        }
    },
    props:[
        'schedule'
    ],

    methods:{
        print(a,event){
            console.log(a)
            const x = event.clientX;
            const y= event.clientY;
            console.log(x,y)
            getAPI.get('/noveltitles')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.novels = response.data
            console.log(this.novels[0].novelid)
            //this.selectNovel(this.novels[0].novelid)
            var menu = document.getElementById('scheduleCreator')
            menu.style.display = 'flex'
            menu.style.left= x + 'px'
            menu.style.top = 50+y + 'px'
          })
          .catch(err => {
            console.log(err)
          })
            

        },
        formSubmit(){
            console.log(document.getElementById('scheduleCreator'))
            const form = document.getElementById('scheduleCreator')
            const formData = new FormData(form)
            getAPI.post('/schedule',formData, {headers: {"Content-Type": "multipart/form-data"}}).then((res) => {
                console.log(res);
            })
            .catch((err) => {
                console.log(err);
            })
            
        }
    },
    created(){
        var today = new Date();
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        console.log(mm + '/' + yyyy)
        getAPI.get('/dates')
          .then(response => {
            console.log('Chapter API has recieved data')
            this.dates = response.data['days']
            console.log(response.data)
            this.start_date = response.data["weekday_start"]
            console.log(this.start_date)
            this.month = response.data['month']
          })
          .catch(err => {
            console.log(err)
          })
          
    }

}
</script>
<style scoped>
.cell{
    border:1px black solid;
    width:100%;
    height:100%;
    margin:0px;
}
#calender{
    width:100%;
    height:100%;
    min-height:700px;
    display:grid;
    grid-template-columns: auto auto auto auto auto auto auto;
    gap:0px;
    border:1px solid black;
}
.weekday{
    text-align:center;
    width:100px;
    margin:0px;
    height:20px;
}
#scheduleCreator{
    display:none;
    background-color:lightgray;
    position:absolute;
    width:300px;
    height:500px;
    flex-direction:column;
    padding:20px;
    border-radius:20px;
}
#novel-selector{
    width:100%;
}
h6{
    margin-top:10px;
    margin-bottom:10px;
}
</style>

