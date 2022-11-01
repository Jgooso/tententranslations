<template>
<body v-if='dates[8]'>
<h1>
{{month}}
</h1>
<div id = 'calender'>
    <div class = 'weekday' v-for='(day,v) in daysoftheWeek'>
    {{day}}
    </div>
    <div v-for='n in start_date' class='cell other' v-text='24+n'/>
    <div class = 'cell' v-for='(date,k) in dates' :key = 'date' @click.right='print(date,$event)'>
       <p style='color:var(--borderColor);align:right'>{{
           k
           }}
       </p>
       <div v-for='d in date' class = 'novel'><p class='novel-title'>{{d.novel}}</p><p class='hour'>{{d.hour}}:00</p></div>
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
            menu.style.top = 150+y + 'px'
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
        const diff = new Date().getTimezoneOffset()
        console.log(diff)
        getAPI.get('/dates?offset='+diff)
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
    height:150px;
    margin:0px;
    padding:10px;
    background-color:var(--backgroundColor);
    
    
}
.other{
    color:rgb(120,120,120)
}
#calender{
    width:100%;
    height:930px;
    min-height:700px;
    display:grid;
    gap:1px;
    grid-template-columns: repeat(7, minmax(0, 1fr));
    background-color: var(--borderColor);
}
.weekday{
    text-align:left;
    margin:0px;
    height:30px;
    padding:5px;
     background-color:var(--backgroundColor);
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
label{
     color:black;
}
#novel-selector{
    width:100%;
}
h6{
    margin-top:10px;
    margin-bottom:10px;
    color:black;
}
.novel-title{
    width:75%;
    height:20px;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    font-size:12px;
     vertical-align:middle;
}
.novel{
    display:flex;
    flex-direction:row;
    margin:0px;
    height:20px;
}
.hour{
    height:20px;
    font-size:11px;
    text-align:left;
    width:22%;
    margin-left:auto;
    vertical-align:middle;

}
@media (max-width: 775px) {
  .hour{
      display:none;
  }
  .novel-title{
      width:100%;
  }
  .cell{
      padding:5px;
  }
}
</style>

