"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[599],{4476:function(t,e,n){n.d(e,{Z:function(){return g}});var o=n(6252);const a=t=>((0,o.dD)("data-v-0464c2c7"),t=t(),(0,o.Cn)(),t),r={id:"control-bar"},s={class:"control-buttons-container",selectable:"false"},c=a((()=>(0,o._)("br",null,null,-1))),i=a((()=>(0,o._)("br",null,null,-1))),l={id:"navigation"},u=a((()=>(0,o._)("p",{id:"selected-chapter"},"223 - Later Story",-1)));function p(t,e,n,a,p,h){const d=(0,o.up)("NavButton");return(0,o.wg)(),(0,o.iD)("div",r,[(0,o._)("div",s,[(0,o._)("button",{class:"controlbuttons",onClick:e[0]||(e[0]=t=>h.changeFontSize(1))},"＋"),(0,o._)("button",{class:"controlbuttons",onClick:e[1]||(e[1]=t=>h.changeFontSize(-1))},"－"),(0,o._)("button",{class:"controlbuttons",onClick:e[2]||(e[2]=t=>h.switchdarkmode())},"◐")]),c,i,(0,o._)("div",l,[u,(0,o.Wm)(d,{previous:1!=this.$route.params.chapter,next:this.$route.params.chapter<n.chapterList.length,onMove:e[3]||(e[3]=e=>t.moveChapters(e)),id:"NavButtons"},null,8,["previous","next"])])])}var h=n(9956),d={name:"ChapterSelector",props:["chapterList"],date(){return{darkmode:""}},components:{NavButton:h.Z},methods:{selectChapter(){const t=document.getElementById("myselect").value;this.$router.push({name:"chapterPage",params:{title:this.$route.params.title,chapter:t}})},changeFontSize(t){const e=document.getElementById("chapter-content"),n=parseInt(getComputedStyle(e).getPropertyValue("font-size").slice(0,2))+t;n>6&&(e.style.fontSize=n+"px",$cookies.set("font-size",n+"px"))},switchdarkmode(){this.$emit("switchmode")},handleClick(t){var e=document.getElementById("custom-select");e.contains(t.target)?e.style.backgroundColor="white":e.style.backgroundColor="red"}},created(){}},v=n(3744);const m=(0,v.Z)(d,[["render",p],["__scopeId","data-v-0464c2c7"]]);var g=m},9956:function(t,e,n){n.d(e,{Z:function(){return l}});var o=n(6252);const a={id:"MoveButton"};function r(t,e,n,r,s,c){return(0,o.wg)(),(0,o.iD)("div",null,[(0,o._)("div",a,[n.previous?((0,o.wg)(),(0,o.iD)("button",{key:0,onClick:e[0]||(e[0]=t=>c.go(this.$route.params.chapter-1))},"← Prev")):(0,o.kq)("",!0),n.next?((0,o.wg)(),(0,o.iD)("button",{key:1,onClick:e[1]||(e[1]=t=>c.go(parseInt(this.$route.params.chapter)+1))},"Next →")):(0,o.kq)("",!0)])])}var s={name:"NavButton",props:["previous","next"],methods:{go(t){this.$router.push({name:"chapterPage",params:{title:this.$route.params.title,chapter:t}})}}},c=n(3744);const i=(0,c.Z)(s,[["render",r],["__scopeId","data-v-e6c07720"]]);var l=i},1599:function(t,e,n){n.r(e),n.d(e,{default:function(){return y}});var o=n(6252),a=n(3577);const r=t=>((0,o.dD)("data-v-2a4149da"),t=t(),(0,o.Cn)(),t),s={id:"chapter"},c={id:"control-bar"},i={class:"control-buttons-container",selectable:"false"},l=r((()=>(0,o._)("br",null,null,-1))),u=r((()=>(0,o._)("br",null,null,-1))),p={id:"navigation"},h={style:{"font-size":"20px"}},d=["innerHTML"];function v(t,e,n,r,v,m){const g=(0,o.up)("router-link"),f=(0,o.up)("NavButton");return(0,o.wg)(),(0,o.iD)("div",s,[(0,o._)("div",null,[(0,o.Wm)(g,{to:{name:"coverPage",params:{title:n.novelData.novelid,chapter:v.chapter.chapternumber}},class:"novel-title",innerHTML:n.novelData.title},null,8,["to","innerHTML"]),(0,o._)("div",c,[(0,o._)("div",i,[(0,o._)("button",{class:"controlbuttons",onClick:e[0]||(e[0]=t=>m.changeFontSize(1))},"＋"),(0,o._)("button",{class:"controlbuttons",onClick:e[1]||(e[1]=t=>m.changeFontSize(-1))},"－"),(0,o._)("button",{class:"controlbuttons",onClick:e[2]||(e[2]=t=>m.switchdarkmode())},"◐")]),l,u,(0,o._)("div",p,[(0,o.Wm)(f,{previous:1!=this.$route.params.chapter,next:this.$route.params.chapter<n.chapterList.length,onMove:e[3]||(e[3]=e=>t.moveChapters(e)),id:"NavButtons"},null,8,["previous","next"])])]),(0,o._)("h1",h,(0,a.zw)(v.chapterTitle),1),(0,o._)("pre",{innerHTML:v.chapterContent,id:"chapter-content"},null,8,d),(0,o.Wm)(f,{previous:1!=this.$route.params.chapter,next:this.$route.params.chapter<n.chapterList.length,onMove:e[4]||(e[4]=e=>t.moveChapters(e)),style:{margin:"auto",float:"center",position:"relative",left:"0px"}},null,8,["previous","next"])])])}var m=n(4476),g=n(2311),f=n(9956),k=n(9669),b=n.n(k),C={name:"Chapter",components:{ChapterSelector:m.Z,KoFiButton:g.Z,NavButton:f.Z},props:["novelData","chapterList"],data(){return{chapter:[],chapterContent:null,error:null,chapterTitle:null}},methods:{changeFontSize(t){const e=document.getElementById("chapter-content"),n=parseInt(getComputedStyle(e).getPropertyValue("font-size").slice(0,2))+t;n>6&&(e.style.fontSize=n+"px",$cookies.set("font-size",n+"px"))},switchdarkmode(){this.$emit("switchmode")},setData(t,e){this.chapterContent=t,this.chapterTitle=e}},created(){const t=this.$route.params,e=`http://tententranslation.com/chapter?novel='${t.title}'&chapter='${t.chapter}`;b().get(e).then((t=>{this.chapterContent=t.data["content"],this.chapterTitle=t.data["title"]})).catch((t=>{console.log(t)}))},mounted(){const t=document.getElementById("chapter-content");null==$cookies.get("font-size")?($cookies.set("font-size","19px"),t.style.fontSize="19px"):t.style.fontSize=$cookies.get("font-size")}},_=n(3744);const $=(0,_.Z)(C,[["render",v],["__scopeId","data-v-2a4149da"]]);var y=$}}]);
//# sourceMappingURL=599.9f32cd83.js.map