"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[4],{6004:function(t,e,n){n.r(e),n.d(e,{default:function(){return F}});var o=n(6252),a=n(3577),l=n(9963);const s=t=>((0,o.dD)("data-v-773a1647"),t=t(),(0,o.Cn)(),t),i={key:0},r={id:"navigator"},h=(0,o.Uk)("<"),d=(0,o.Uk)("Today"),u=(0,o.Uk)(">"),c={id:"calender"},m=["innerHTML"],g=["textContent"],y=["onContextmenu"],p=["innerHTML"],v={class:"novel"},_=["innerHTML"],f=["innerHTML"],w={id:"scheduleCreator",method:"formSubmit"},k=s((()=>(0,o._)("h6",null,"Novel",-1))),b={id:"novel-selector",name:"novel",form:"scheduleCreator"},C=["value"],D=s((()=>(0,o._)("h6",null,"Start Date",-1))),H=s((()=>(0,o._)("input",{type:"date",id:"start",name:"upload-start",min:"2022-01-01",max:"2030-12-31"},null,-1))),x=s((()=>(0,o._)("h6",null,"Upload Times",-1))),T=["name"],M=s((()=>(0,o._)("h6",null,"Days of the Week",-1))),S={style:{width:"100px"}},Y=["name","value"];function z(t,e,n,s,z,L){return z.dates[8]?((0,o.wg)(),(0,o.iD)("body",i,[(0,o._)("h1",null,(0,a.zw)(z.month_name)+", "+(0,a.zw)(z.year),1),(0,o._)("div",r,[(0,o._)("label",null,[h,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[0]||(e[0]=t=>L.change_month(1))})]),(0,o._)("label",null,[d,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[1]||(e[1]=t=>L.change_month("today"))})]),(0,o._)("label",null,[u,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[2]||(e[2]=t=>L.change_month(-1))})])]),(0,o._)("div",c,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.daysoftheWeek,((t,e)=>((0,o.wg)(),(0,o.iD)("div",{class:"weekday",innerHTML:t},null,8,m)))),256)),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.start_date,(t=>((0,o.wg)(),(0,o.iD)("div",{class:"cell other",textContent:(0,a.zw)(24+t)},null,8,g)))),256)),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.dates,((t,e)=>((0,o.wg)(),(0,o.iD)("div",{class:"cell",key:t,onContextmenu:(0,l.iM)((e=>L.print(t,e)),["right"])},[(0,o._)("p",{style:{color:"var(--borderColor)",align:"right"},innerHTML:e},null,8,p),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(t,(t=>((0,o.wg)(),(0,o.iD)("div",v,[(0,o._)("p",{class:"novel-title",innerHTML:t.novel},null,8,_),(0,o._)("p",{class:"hour",innerHTML:t.hour+n.timezoneOffset/60+":00"},null,8,f)])))),256))],40,y)))),128))]),(0,o._)("form",w,[k,(0,o._)("select",b,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.novels,(t=>((0,o.wg)(),(0,o.iD)("option",{value:t.novelid},(0,a.zw)(t.title),9,C)))),256))]),D,H,x,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.times,(t=>((0,o.wg)(),(0,o.iD)("input",{type:"time",name:"time"+t,min:"08:00",max:"20:00"},null,8,T)))),256)),(0,o._)("input",{type:"button",style:{background:"none",border:"none,border:1px solid black",height:"30px",width:"30px"},onClick:e[3]||(e[3]=t=>this.times++),value:"+"}),M,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(z.daysoftheWeek.length,(t=>((0,o.wg)(),(0,o.iD)("label",S,[(0,o.Uk)((0,a.zw)(z.daysoftheWeek[t-1]),1),(0,o._)("input",{type:"checkbox",name:z.daysoftheWeek[t-1],value:t-1},null,8,Y)])))),256))]),(0,o._)("button",{onClick:e[4]||(e[4]=t=>L.formSubmit())},"a")])):(0,o.kq)("",!0)}var L=n(9669),K=n.n(L),W={name:"Calender",data(){return{dates:[],daysoftheWeek:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],month_name:"",month:0,year:0,day:0,selectedDay:[],novels:[],times:1,start_date:0}},props:["schedule","timezoneOffset"],methods:{print(t,e){console.log(t);const n=e.clientX,o=e.clientY;console.log(n,o),K().get("http://tententranslation.com/noveltitles").then((t=>{console.log("Chapter API has recieved data"),this.novels=t.data,console.log(this.novels[0].novelid);var e=document.getElementById("scheduleCreator");e.style.display="flex",e.style.left=n+"px",e.style.top=150+o+"px"})).catch((t=>{console.log(t)}))},formSubmit(){console.log(document.getElementById("scheduleCreator"));const t=document.getElementById("scheduleCreator"),e=new FormData(t);K().post("http://tententranslation.com/schedule",e,{headers:{"Content-Type":"multipart/form-data"}}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},get_calender(t,e){K().get(`http://tententranslation.com/dates?offset=${this.timezoneOffset}&month=${t}&year=${e}`).then((t=>{console.log("Chapter API has recieved data"),this.dates=t.data["days"],console.log(t.data),this.start_date=t.data["weekday_start"],console.log(this.start_date),this.month_name=t.data["month"]})).catch((t=>{console.log(t)}))},change_month(t){if("today"==t){var e=new Date;return this.month=String(e.getMonth()+1).padStart(2,"0"),this.year=e.getFullYear(),void this.get_calender(this.month,this.year)}this.month-=t,this.month>12&&(this.month=1,this.year+=1),this.month<1&&(this.month=12,this.year-=1),this.get_calender(this.month,this.year)}},created(){var t=new Date;this.month=String(t.getMonth()+1).padStart(2,"0"),this.year=t.getFullYear(),this.get_calender(this.month,this.year)}},I=n(3744);const U=(0,I.Z)(W,[["render",z],["__scopeId","data-v-773a1647"]]);var F=U}}]);
//# sourceMappingURL=4.7c30afba.js.map