"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[668],{6668:function(t,e,n){n.r(e),n.d(e,{default:function(){return B}});var o=n(6252),a=n(3577);const r=t=>((0,o.dD)("data-v-e756723c"),t=t(),(0,o.Cn)(),t),c={id:"chapter"},s={id:"control-bar"},i={id:"control-buttons-container",selectable:"false"},p=r((()=>(0,o._)("br",null,null,-1))),l=r((()=>(0,o._)("br",null,null,-1))),h={style:{"font-size":"20px"}},u=["innerHTML"];function d(t,e,n,r,d,m){const f=(0,o.up)("router-link"),g=(0,o.up)("NavButton");return(0,o.wg)(),(0,o.iD)("div",c,[(0,o.Wm)(f,{to:{name:"coverPage",params:{title:n.novelData.novelid}},class:"novel-title",innerHTML:n.novelData.title},null,8,["to","innerHTML"]),(0,o._)("div",s,[(0,o._)("div",i,[(0,o._)("button",{class:"controlbuttons",onClick:e[0]||(e[0]=t=>m.changeFontSize(1))},"＋"),(0,o._)("button",{class:"controlbuttons",onClick:e[1]||(e[1]=t=>m.changeFontSize(-1))},"－"),(0,o._)("button",{class:"controlbuttons",onClick:e[2]||(e[2]=t=>m.switchdarkmode())},"◐")]),p,l,(0,o.Wm)(g,{previous:1!=this.chapter.chapter,next:this.chapter.chapter<n.chapterList.length,onMove:e[3]||(e[3]=e=>t.moveChapters(e)),id:"NavButtons"},null,8,["previous","next"])]),(0,o._)("h1",h,(0,a.zw)(d.chapterTitle),1),(0,o._)("pre",{innerHTML:d.chapterContent,id:"chapter-content"},null,8,u),(0,o.Wm)(g,{previous:1!=this.chapter.chapter,next:this.chapter.chapter<n.chapterList.length,onMove:e[4]||(e[4]=e=>t.moveChapters(e)),style:{margin:"auto",float:"center",position:"relative",left:"0px"}},null,8,["previous","next"])])}var m="data:image/png;base64,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";const f={href:"https://ko-fi.com/K3K4FC3HF",target:"_blank"},g=(0,o._)("img",{height:"36",style:{border:"0px",height:"36px"},src:m,border:"0",alt:"Buy Me a Coffee at ko-fi.com"},null,-1),v=[g];function H(t,e,n,a,r,c){return(0,o.wg)(),(0,o.iD)("a",f,v)}var x={name:"KoFiButton"},A=n(3744);const O=(0,A.Z)(x,[["render",H]]);var k=O;const X={id:"MoveButton"};function z(t,e,n,a,r,c){return(0,o.wg)(),(0,o.iD)("div",null,[(0,o._)("div",X,[n.previous?((0,o.wg)(),(0,o.iD)("button",{key:0,onClick:e[0]||(e[0]=t=>c.go(this.$route.params.chapter-1))},"← Prev")):(0,o.kq)("",!0),n.next?((0,o.wg)(),(0,o.iD)("button",{key:1,onClick:e[1]||(e[1]=t=>c.go(parseInt(this.$route.params.chapter)+1))},"Next →")):(0,o.kq)("",!0)])])}var w={name:"NavButton",props:["previous","next"],methods:{go(t){this.$router.push({name:"chapterPage",params:{title:this.$route.params.title,chapter:t}})}}};const b=(0,A.Z)(w,[["render",z],["__scopeId","data-v-e6bfddd4"]]);var G=b,W=n(9669),I=n.n(W),P={name:"Chapter",components:{KoFiButton:k,NavButton:G},props:["novelData","chapterList"],data(){return{chapter:[],chapterContent:null,error:null,chapterTitle:null}},methods:{changeFontSize(t){const e=document.getElementById("chapter-content"),n=parseInt(getComputedStyle(e).getPropertyValue("font-size").slice(0,2))+t;n>6&&(e.style.fontSize=n+"px",$cookies.set("font-size",n+"px"))},switchdarkmode(){this.$emit("switchmode")},setData(t,e){this.chapterContent=t,this.chapterTitle=e}},created(){this.chapter=this.$route.params;const t=`http://tententranslation.com/chapter?novel=${this.chapter.title}&chapter=${this.chapter.chapter}`;I().get(t).then((t=>{this.chapterContent=t.data["content"],this.chapterTitle=t.data["title"]})).catch((t=>{console.log(t)}))},mounted(){const t=document.getElementById("chapter-content");null==$cookies.get("font-size")?($cookies.set("font-size","19px"),t.style.fontSize="19px"):t.style.fontSize=$cookies.get("font-size")}};const Z=(0,A.Z)(P,[["render",d],["__scopeId","data-v-e756723c"]]);var B=Z}}]);
//# sourceMappingURL=668.2aa0ec39.js.map