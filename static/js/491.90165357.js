"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[491],{4491:function(t,e,n){n.r(e),n.d(e,{default:function(){return y}});var o=n(6252),a=n(3577);const r=t=>((0,o.dD)("data-v-d52fc8ac"),t=t(),(0,o.Cn)(),t),s={id:"chapter"},c={id:"control-bar"},i={id:"control-buttons-container",selectable:"false"},l=r((()=>(0,o._)("br",null,null,-1))),p=r((()=>(0,o._)("br",null,null,-1))),h={style:{"font-size":"20px"}},u=["innerHTML"];function d(t,e,n,r,d,v){const m=(0,o.up)("router-link"),f=(0,o.up)("NavButton");return(0,o.wg)(),(0,o.iD)("div",s,[(0,o.Wm)(m,{to:{name:"coverPage",params:{title:n.novelData.novelid}},class:"novel-title",innerHTML:n.novelData.title},null,8,["to","innerHTML"]),(0,o._)("div",c,[(0,o._)("div",i,[(0,o._)("button",{class:"controlbuttons",onClick:e[0]||(e[0]=t=>v.changeFontSize(1))},"＋"),(0,o._)("button",{class:"controlbuttons",onClick:e[1]||(e[1]=t=>v.changeFontSize(-1))},"－"),(0,o._)("button",{class:"controlbuttons",onClick:e[2]||(e[2]=t=>v.switchdarkmode())},"◐")]),l,p,(0,o.Wm)(f,{previous:1!=this.chapter.chapter,next:this.chapter.chapter<n.chapterList.length,onMove:e[3]||(e[3]=e=>t.moveChapters(e)),id:"NavButtons"},null,8,["previous","next"])]),(0,o._)("h1",h,(0,a.zw)(d.chapterTitle),1),(0,o._)("pre",{innerHTML:d.chapterContent,id:"chapter-content"},null,8,u),(0,o.Wm)(f,{previous:1!=this.chapter.chapter,next:this.chapter.chapter<n.chapterList.length,onMove:e[4]||(e[4]=e=>t.moveChapters(e)),style:{margin:"auto",float:"center",position:"relative",left:"0px"}},null,8,["previous","next"])])}var v=n(245);const m={id:"MoveButton"};function f(t,e,n,a,r,s){return(0,o.wg)(),(0,o.iD)("div",null,[(0,o._)("div",m,[n.previous?((0,o.wg)(),(0,o.iD)("button",{key:0,onClick:e[0]||(e[0]=t=>s.go(this.$route.params.chapter-1))},"← Prev")):(0,o.kq)("",!0),n.next?((0,o.wg)(),(0,o.iD)("button",{key:1,onClick:e[1]||(e[1]=t=>s.go(parseInt(this.$route.params.chapter)+1))},"Next →")):(0,o.kq)("",!0)])])}var g={name:"NavButton",props:["previous","next"],methods:{go(t){this.$router.push({name:"chapterPage",params:{title:this.$route.params.title,chapter:t}})}}},k=n(3744);const b=(0,k.Z)(g,[["render",f],["__scopeId","data-v-e6bfddd4"]]);var C=b,_=n(9669),x=n.n(_),z={name:"Chapter",components:{KoFiButton:v.Z,NavButton:C},props:["novelData","chapterList"],data(){return{chapter:[],chapterContent:null,error:null,chapterTitle:null}},methods:{changeFontSize(t){const e=document.getElementById("chapter-content"),n=parseInt(getComputedStyle(e).getPropertyValue("font-size").slice(0,2))+t;n>6&&(e.style.fontSize=n+"px",$cookies.set("font-size",n+"px"))},switchdarkmode(){this.$emit("switchmode")},setData(t,e){this.chapterContent=t,this.chapterTitle=e}},created(){this.chapter=this.$route.params;const t=`http://tententranslation.com/chapter?novel=${this.chapter.title}&chapter=${this.chapter.chapter}`;x().get(t).then((t=>{this.chapterContent=t.data["content"],this.chapterTitle=t.data["title"]})).catch((t=>{console.log(t)}))},mounted(){const t=document.getElementById("chapter-content");null==$cookies.get("font-size")?($cookies.set("font-size","19px"),t.style.fontSize="19px"):t.style.fontSize=$cookies.get("font-size")}};const $=(0,k.Z)(z,[["render",d],["__scopeId","data-v-d52fc8ac"]]);var y=$}}]);
//# sourceMappingURL=491.90165357.js.map