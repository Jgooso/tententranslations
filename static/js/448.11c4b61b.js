"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[448],{9448:function(e,n,t){t.r(n),t.d(n,{default:function(){return D}});var s=t(6252);const a=e=>((0,s.dD)("data-v-27450f64"),e=e(),(0,s.Cn)(),e),l=a((()=>(0,s._)("h3",null,"Novel Release",-1))),r=["innerHTML"],u=a((()=>(0,s._)("h3",null,"Novel status",-1))),o=["innerHTML"],i=a((()=>(0,s._)("h3",null,"Upload status",-1))),c=["innerHTML"],d=a((()=>(0,s._)("h3",null,"Genres",-1))),g=["innerHTML"],p=a((()=>(0,s._)("h3",null,"Tags",-1))),v=["innerHTML"];function h(e,n,t,a,h,H){return(0,s.wg)(),(0,s.iD)("div",null,[l,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.novelrelease,(e=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:e.descriptor+":"+e["count"],class:"bar"},null,8,r)))),256)),u,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.novelstatus,(e=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:e.descriptor+":"+e["count"],class:"bar"},null,8,o)))),256)),i,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.uploadstatus,(e=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:e.descriptor+":"+e["count"],class:"bar"},null,8,c)))),256)),d,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.genres,(e=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:e.descriptor+":"+e["count"],class:"bar"},null,8,g)))),256)),p,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.tags,(e=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:e.descriptor+":"+e["count"],class:"bar"},null,8,v)))),256))])}var H=t(5992),w={name:"descriptorPage",data(){return{novelrelease:[],genres:[],tags:[],novelstatus:[],uploadstatus:[]}},created(){const e="/descriptorbution";H.K.get(e).then((e=>{this.novelrelease=e.data["novelrelease"],this.genres=e.data["genre"],this.tags=e.data["tag"],this.novelstatus=e.data["novelstatus"],this.uploadstatus=e.data["uploadstatus"]})).catch((e=>{console.log(e)}))},mounted(){setTimeout((()=>{for(var e=document.getElementsByClassName("bar"),n=0;n<e.length;n++){const t=e[n].innerHTML,s=parseInt(t.substring(t.indexOf(":")+1));e[n].style.width=10*s+"px"}}),500)}},T=t(3744);const f=(0,T.Z)(w,[["render",h],["__scopeId","data-v-27450f64"]]);var D=f}}]);
//# sourceMappingURL=448.11c4b61b.js.map