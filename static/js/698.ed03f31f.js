"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[698],{6698:function(n,e,t){t.r(e),t.d(e,{default:function(){return M}});var s=t(6252);const a=n=>((0,s.dD)("data-v-52926408"),n=n(),(0,s.Cn)(),n),l=a((()=>(0,s._)("h3",null,"Novel Release",-1))),r=["innerHTML"],u=a((()=>(0,s._)("h3",null,"Novel status",-1))),o=["innerHTML"],i=a((()=>(0,s._)("h3",null,"Upload status",-1))),c=["innerHTML"],d=a((()=>(0,s._)("h3",null,"Genres",-1))),g=["innerHTML"],p=a((()=>(0,s._)("h3",null,"Tags",-1))),v=["innerHTML"];function h(n,e,t,a,h,H){return(0,s.wg)(),(0,s.iD)("div",null,[l,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.novelrelease,(n=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:n.descriptor+":"+n["count"],class:"bar"},null,8,r)))),256)),u,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.novelstatus,(n=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:n.descriptor+":"+n["count"],class:"bar"},null,8,o)))),256)),i,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.uploadstatus,(n=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:n.descriptor+":"+n["count"],class:"bar"},null,8,c)))),256)),d,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.genres,(n=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:n.descriptor+":"+n["count"],class:"bar"},null,8,g)))),256)),p,((0,s.wg)(!0),(0,s.iD)(s.HY,null,(0,s.Ko)(h.tags,(n=>((0,s.wg)(),(0,s.iD)("p",{innerHTML:n.descriptor+":"+n["count"],class:"bar"},null,8,v)))),256))])}var H=t(9669),w=t.n(H),T={name:"descriptorPage",data(){return{novelrelease:[],genres:[],tags:[],novelstatus:[],uploadstatus:[]}},created(){const n="http://tententranslation.com/descriptorbution";w().get(n).then((n=>{this.novelrelease=n.data["novelrelease"],this.genres=n.data["genre"],this.tags=n.data["tag"],this.novelstatus=n.data["novelstatus"],this.uploadstatus=n.data["uploadstatus"]})).catch((n=>{console.log(n)}))},mounted(){setTimeout((()=>{for(var n=document.getElementsByClassName("bar"),e=0;e<n.length;e++){const t=n[e].innerHTML,s=parseInt(t.substring(t.indexOf(":")+1));n[e].style.width=10*s+"px"}}),500)}},D=t(3744);const L=(0,D.Z)(T,[["render",h],["__scopeId","data-v-52926408"]]);var M=L}}]);
//# sourceMappingURL=698.ed03f31f.js.map