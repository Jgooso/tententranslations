"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[652],{1652:function(e,t,a){a.r(t),a.d(t,{default:function(){return h}});var d=a(6252),n=a(3577);const c=e=>((0,d.dD)("data-v-36258f02"),e=e(),(0,d.Cn)(),e),o={id:"feedback"},i=["id"],l=["onClick"],s=c((()=>(0,d._)("nav",{id:"page-navigation"},[(0,d._)("button",{class:"page-button",id:"left-arrow"},"←"),(0,d._)("button",{class:"page-button",id:"right-arrow"},"→")],-1)));function b(e,t,a,c,b,k){return(0,d.wg)(),(0,d.iD)("div",o,[((0,d.wg)(!0),(0,d.iD)(d.HY,null,(0,d.Ko)(b.feedback,(e=>((0,d.wg)(),(0,d.iD)("div",{key:e.id,class:"feedbackbox",id:e.id},[(0,d._)("p",null,(0,n.zw)(e.feedback),1),(0,d._)("button",{class:"delete-feedback",onClick:t=>k.deleteFeedback(e.id)},"X",8,l)],8,i)))),128)),s])}var k=a(9669),r=a.n(k),u={name:"Feedback",data(){return{page:1,feedback:[]}},methods:{getFeedback(e){this.page=this.page+e,r().get(`http://tententranslation.com/feedback?page=${this.page}`).then((e=>{this.feedback=e.data})).catch((e=>{console.log(e)}))},deleteFeedback(e){document.getElementById(e).style.display="none",r()["delete"](`/feedback?id=${e}`).then((e=>{console.log("Deleted Feedback")})).catch((e=>{console.log(e)}))}},created(){this.getFeedback(0)}},f=a(3744);const g=(0,f.Z)(u,[["render",b],["__scopeId","data-v-36258f02"]]);var h=g}}]);
//# sourceMappingURL=652.375b9b07.js.map