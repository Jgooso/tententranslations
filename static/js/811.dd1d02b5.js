"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[811],{7811:function(t,e,n){n.r(e),n.d(e,{default:function(){return u}});var s=n(6252);const i={class:"novel"};function a(t,e,n,a,o,r){const c=(0,s.up)("router-view");return(0,s.wg)(),(0,s.iD)("div",i,[o.isMounted?((0,s.wg)(),(0,s.j4)(c,{novelData:o.novelData,chapterList:o.chapterList,sectionList:o.sectionList,tier:n.tier,key:t.$route.params.chapter,onSwitchmode:e[0]||(e[0]=e=>t.$emit("switchmode"))},null,8,["novelData","chapterList","sectionList","tier"])):(0,s.kq)("",!0)])}var o=n(9669),r=n.n(o),c={name:"Novel",components:{},data(){return{chapterList:[],sectionList:[],novelData:[],isMounted:!1}},props:["tier"],created(){const t=`http://127.0.0.1:5000/novel/single?novel=${this.$route.params.title}&tier=${this.tier}`;r().get(t).then((t=>{this.novelData=t.data["Novel"];const e=t.data["Chapters"].filter((t=>0==t.chapternumber));e.length>0?this.sectionList=e:this.sectionList=[{section:0}],this.chapterList=t.data["Chapters"].filter((t=>0!=t.chapternumber)),console.log(t.data["Chapters"]),this.isMounted=!0})).catch((t=>{console.log(t)}))}},h=n(3744);const l=(0,h.Z)(c,[["render",a]]);var u=l}}]);
//# sourceMappingURL=811.dd1d02b5.js.map