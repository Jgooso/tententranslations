"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[108],{8108:function(t,e,n){n.r(e),n.d(e,{default:function(){return A}});var o=n(6252),a=n(3577),l=n(9963);const s=t=>((0,o.dD)("data-v-86bc8084"),t=t(),(0,o.Cn)(),t),i={key:0},h={id:"navigator"},d=(0,o.Uk)("<"),r=(0,o.Uk)("Today"),c=(0,o.Uk)(">"),u={id:"calender"},m={class:"weekday"},g=["textContent"],y=["onContextmenu"],p={style:{color:"var(--borderColor)",align:"right"}},v={class:"novel"},_={class:"novel-title"},w={class:"hour"},f={id:"scheduleCreator",method:"formSubmit"},k=s((()=>(0,o._)("h6",null,"Novel",-1))),b={id:"novel-selector",name:"novel",form:"scheduleCreator"},D=["value"],C=s((()=>(0,o._)("h6",null,"Start Date",-1))),x=s((()=>(0,o._)("input",{type:"date",id:"start",name:"upload-start",min:"2022-01-01",max:"2030-12-31"},null,-1))),z=s((()=>(0,o._)("h6",null,"Upload Times",-1))),S=["name"],Y=s((()=>(0,o._)("h6",null,"Days of the Week",-1))),H={style:{width:"100px"}},I=["name","value"];function K(t,e,n,s,K,W){return K.dates[8]?((0,o.wg)(),(0,o.iD)("body",i,[(0,o._)("h1",null,(0,a.zw)(K.month_name)+", "+(0,a.zw)(K.year),1),(0,o._)("div",h,[(0,o._)("label",null,[d,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[0]||(e[0]=t=>W.change_month(1))})]),(0,o._)("label",null,[r,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[1]||(e[1]=t=>W.change_month("today"))})]),(0,o._)("label",null,[c,(0,o._)("input",{type:"button",class:"navigation-button",onClick:e[2]||(e[2]=t=>W.change_month(-1))})])]),(0,o._)("div",u,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.daysoftheWeek,((t,e)=>((0,o.wg)(),(0,o.iD)("div",m,(0,a.zw)(t),1)))),256)),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.start_date,(t=>((0,o.wg)(),(0,o.iD)("div",{class:"cell other",textContent:(0,a.zw)(24+t)},null,8,g)))),256)),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.dates,((t,e)=>((0,o.wg)(),(0,o.iD)("div",{class:"cell",key:t,onContextmenu:(0,l.iM)((e=>W.print(t,e)),["right"])},[(0,o._)("p",p,(0,a.zw)(e),1),((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(t,(t=>((0,o.wg)(),(0,o.iD)("div",v,[(0,o._)("p",_,(0,a.zw)(t.novel),1),(0,o._)("p",w,(0,a.zw)(t.hour)+":00",1)])))),256))],40,y)))),128))]),(0,o._)("form",f,[k,(0,o._)("select",b,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.novels,(t=>((0,o.wg)(),(0,o.iD)("option",{value:t.novelid},(0,a.zw)(t.title),9,D)))),256))]),C,x,z,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.times,(t=>((0,o.wg)(),(0,o.iD)("input",{type:"time",name:"time"+t,min:"08:00",max:"20:00"},null,8,S)))),256)),(0,o._)("input",{type:"button",style:{background:"none",border:"none,border:1px solid black",height:"30px",width:"30px"},onClick:e[3]||(e[3]=t=>this.times++),value:"+"}),Y,((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(K.daysoftheWeek.length,(t=>((0,o.wg)(),(0,o.iD)("label",H,[(0,o.Uk)((0,a.zw)(K.daysoftheWeek[t-1]),1),(0,o._)("input",{type:"checkbox",name:K.daysoftheWeek[t-1],value:t-1},null,8,I)])))),256))]),(0,o._)("button",{onClick:e[4]||(e[4]=t=>W.formSubmit())},"a")])):(0,o.kq)("",!0)}var W=n(9669),T=n.n(W),U={name:"Calender",data(){return{dates:[],daysoftheWeek:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],month_name:"",month:0,year:0,day:0,selectedDay:[],novels:[],times:1,start_date:0}},props:["schedule"],methods:{print(t,e){console.log(t);const n=e.clientX,o=e.clientY;console.log(n,o),T().get("http://tententranslation.com/noveltitles").then((t=>{console.log("Chapter API has recieved data"),this.novels=t.data,console.log(this.novels[0].novelid);var e=document.getElementById("scheduleCreator");e.style.display="flex",e.style.left=n+"px",e.style.top=150+o+"px"})).catch((t=>{console.log(t)}))},formSubmit(){console.log(document.getElementById("scheduleCreator"));const t=document.getElementById("scheduleCreator"),e=new FormData(t);T().post("http://tententranslation.com/schedule",e,{headers:{"Content-Type":"multipart/form-data"}}).then((t=>{console.log(t)})).catch((t=>{console.log(t)}))},get_calender(t,e){const n=(new Date).getTimezoneOffset();getAPI.get(`http://tententranslation.com/dates?offset=${n}&month=${t}&year=${e}`).then((t=>{console.log("Chapter API has recieved data"),this.dates=t.data["days"],console.log(t.data),this.start_date=t.data["weekday_start"],console.log(this.start_date),this.month_name=t.data["month"]})).catch((t=>{console.log(t)}))},change_month(t){if("today"==t){var e=new Date;return this.month=String(e.getMonth()+1).padStart(2,"0"),this.year=e.getFullYear(),void this.get_calender(this.month,this.year)}this.month-=t,this.month>12&&(this.month=1,this.year+=1),this.month<1&&(this.month=12,this.year-=1),this.get_calender(this.month,this.year)}},created(){var t=new Date;this.month=String(t.getMonth()+1).padStart(2,"0"),this.year=t.getFullYear(),this.get_calender(this.month,this.year)}},F=n(3744);const M=(0,F.Z)(U,[["render",K],["__scopeId","data-v-86bc8084"]]);var A=M}}]);
//# sourceMappingURL=108.0a57dbc7.js.map