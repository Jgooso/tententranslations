"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[633],{85:function(t,e,a){a.d(e,{Z:function(){return u}});var n=a(6252);const o=t=>((0,n.dD)("data-v-71035fa8"),t=t(),(0,n.Cn)(),t),s={id:"box"},r=["innerHTML"],l=o((()=>(0,n._)("h3",{id:"point",class:"utf-shape"},"◆",-1)));function i(t,e,a,o,i,c){return(0,n.wg)(),(0,n.iD)("div",s,[(0,n._)("h3",{id:"star",class:"utf-shape",innerHTML:a.shape},null,8,r),l])}var c={name:"UtfBox",props:["shape"]},d=a(3744);const p=(0,d.Z)(c,[["render",i],["__scopeId","data-v-71035fa8"]]);var u=p},633:function(t,e,a){a.r(e),a.d(e,{default:function(){return U}});var n=a(6252),o=a(3577);const s=t=>((0,n.dD)("data-v-4ef92960"),t=t(),(0,n.Cn)(),t),r={id:"Browse"},l=["innerHTML"],i={id:"top"},c={id:"count"},d=s((()=>(0,n._)("p",{id:"resultCount"},null,-1))),p=s((()=>(0,n._)("label",{class:"category"}," Order By",-1))),u={id:"sortButtons"},v={id:"pageNumber"},h={class:"novelList"},g={id:"pageNav"};function m(t,e,a,s,m,C){const f=(0,n.up)("UtfBox"),_=(0,n.up)("NovelCard");return(0,n.wg)(),(0,n.iD)("div",r,[(0,n._)("h1",{id:"sortCategory",innerHTML:this.$route.params.identifier?this.$route.params.identifier:"All Novels"},null,8,l),(0,n._)("div",i,[(0,n._)("div",c,[(0,n.Wm)(f,{shape:"★"}),d,p]),(0,n._)("div",u,[(0,n._)("input",{type:"button",class:"category selectable",style:{"border-left":"1px solid var(--borderColor)"},onClick:e[0]||(e[0]=t=>C.sort("lastupload")),value:"Latest",id:"sort-lastupload"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[1]||(e[1]=t=>C.sort("title")),value:"A-Z",id:"sort-title"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[2]||(e[2]=t=>C.sort("length")),value:"Length",id:"sort-length"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[3]||(e[3]=t=>C.sort("views")),value:"Trending",id:"sort-views"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[4]||(e[4]=t=>C.sort("firstupload")),value:"New",id:"sort-firstupload"}),(0,n._)("h6",v,"Page "+(0,o.zw)(m.page)+" of "+(0,o.zw)(m.pageCount),1)])]),(0,n._)("div",h,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(m.novelData,(t=>((0,n.wg)(),(0,n.iD)("div",{key:t.title,id:"novels"},[(0,n.Wm)(_,{novelData:t,type:"browse",class:"novelcard"},null,8,["novelData"])])))),128))]),(0,n._)("div",g,[m.page>1?((0,n.wg)(),(0,n.iD)("button",{key:0,class:"navigationButton",id:"prev",onClick:e[5]||(e[5]=t=>C.changePage(-1))},"←Previous Page")):(0,n.kq)("",!0),m.page<m.pageCount?((0,n.wg)(),(0,n.iD)("button",{key:1,class:"navigationButton",id:"next",onClick:e[6]||(e[6]=t=>C.changePage(1))},"Next Page→")):(0,n.kq)("",!0)])])}const C=t=>((0,n.dD)("data-v-2cc98570"),t=t(),(0,n.Cn)(),t),f={class:"NovelCard"},_=["textContent"],b={id:"chapter-box"},y=C((()=>(0,n._)("p",{id:"recent-chapters"},"Recent Chapters",-1))),w={class:"chapter"},D=["textContent"],x=["textContent"],k=C((()=>(0,n._)("hr",{style:{margin:"0px"}},null,-1))),N={class:"chapter"},$=["textContent"],P=["textContent"];function B(t,e,a,s,r,l){const i=(0,n.up)("router-link");return(0,n.wg)(),(0,n.j4)(i,{to:{name:"coverPage",params:{title:a.novelData.novelid}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",f,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.title),id:"title"},null,8,_),(0,n._)("div",b,[y,(0,n.Wm)(i,{to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.firstChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",w,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.firstChapter["chapternumber"]),class:"chapterNumber"},null,8,D),(0,n._)("p",{class:"date",textContent:(0,o.zw)(a.novelData.firstChapter["uploaddate"])},null,8,x)])])),_:1},8,["to"]),k,a.novelData.secondChapter?((0,n.wg)(),(0,n.j4)(i,{key:0,to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.secondChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",N,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.secondChapter["chapternumber"]),class:"chapterNumber"},null,8,$),(0,n._)("p",{class:"date",textContent:(0,o.zw)(a.novelData.secondChapter["uploaddate"])},null,8,P)])])),_:1},8,["to"])):(0,n.kq)("",!0)])])])),_:1},8,["to"])}var L={name:"NovelCard",props:["novelData"],methods:{goTo(t){this.$router.push({name:"coverPage",params:{title:t}})}}},T=a(3744);const z=(0,T.Z)(L,[["render",B],["__scopeId","data-v-2cc98570"]]);var H=z,Z=a(85),E=a(9669),I=a.n(E),M={name:"Browser",components:{NovelCard:H,UtfBox:Z.Z},data(){return{novelData:[],chapterList:[],attributesort:"lastupload",page:1,pageCount:0}},props:["tier"],methods:{getNovels(t){void 0!=t&&(t=t.replace(/&nbsp;/g,"|"));const e=`http://127.0.0.1:5000/novel/multiple?tier=${this.tier}&identifier=${t}&order=${this.attributesort}&page=${this.page}`;I().get(e).then((t=>{this.novelData=t.data})).catch((t=>{console.log(t)}))},sort(t){const e=document.getElementsByClassName("selected");this.attributesort=t;for(var a=0;a<e.length;a++)e[a].classList.remove("selected");document.getElementById("sort-"+t).classList.add("selected"),this.getNovels(this.$route.params.identifier)},changePage(t){this.page=this.page+t,this.getNovels(this.$route.params.identifier)},getPages(t){I().get(`http://tententranslation.com/novels-page-count?tier=${this.tier}&identifier=${t}`).then((e=>{this.pageCount=e.data["page_count"],this.getNovels(t),document.getElementById("resultCount").innerHTML=`${e.data["novel_count"]} RESULTS`})).catch((t=>{console.log(t)}))}},created(){var t=this.$route.params.identifier;this.getPages(t),this.$watch((()=>this.$route.params),((t,e)=>{var a=this.$route.params.identifier;if(void 0!=a&&(a=a.replace(/&nbsp;/g,"|")),Object.keys(e).includes("browsetype")&&0==Object.keys(t).length){const t=document.getElementsByClassName("selected");this.getNovels(a),this.getPages(a);for(var n=0;n<t.length;n++)t[n].classList.remove("selected")}}))}};const j=(0,T.Z)(M,[["render",m],["__scopeId","data-v-4ef92960"]]);var U=j}}]);
//# sourceMappingURL=633.39c86fc5.js.map