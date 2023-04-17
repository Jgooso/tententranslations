"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[570],{881:function(t,e,a){a.d(e,{Z:function(){return u}});var n=a(6252);const o=t=>((0,n.dD)("data-v-3eb7aad7"),t=t(),(0,n.Cn)(),t),s={id:"box"},r=["innerHTML"],l=o((()=>(0,n._)("h3",{id:"point"},"◆",-1)));function i(t,e,a,o,i,d){return(0,n.wg)(),(0,n.iD)("div",s,[(0,n._)("h3",{id:"star",innerHTML:a.shape},null,8,r),l])}var d={name:"UtfBox",props:["shape"]},c=a(3744);const p=(0,c.Z)(d,[["render",i],["__scopeId","data-v-3eb7aad7"]]);var u=p},7570:function(t,e,a){a.r(e),a.d(e,{default:function(){return q}});var n=a(6252),o=a(3577),s=a(9963);const r=t=>((0,n.dD)("data-v-302ce6fd"),t=t(),(0,n.Cn)(),t),l={id:"Browse"},i=["innerHTML"],d={id:"top"},c={id:"count"},p={id:"resultCount"},u=r((()=>(0,n._)("label",{class:"category"}," Order By",-1))),v={id:"sortButtons"},h={id:"pageNumber"},g={class:"novelList"},C={id:"pageNav"};function m(t,e,a,r,m,f){const _=(0,n.up)("UtfBox"),b=(0,n.up)("NovelCard");return(0,n.wg)(),(0,n.iD)("div",l,[(0,n._)("h1",{id:"sortCategory",innerHTML:this.$route.params.identifier?this.$route.params.identifier:"All Novels"},null,8,i),(0,n._)("header",d,[(0,n._)("div",c,[(0,n.Wm)(_,{shape:"★"}),(0,n._)("p",p,(0,o.zw)(m.novelCount)+" RESULTS",1),u]),(0,n._)("div",v,[(0,n._)("input",{type:"button",class:"category selectable",style:{"border-left":"1px solid var(--borderColor)"},onClick:e[0]||(e[0]=t=>f.sort("lastupload")),value:"Latest",id:"sort-lastupload"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[1]||(e[1]=t=>f.sort("title")),value:"A-Z",id:"sort-title"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[2]||(e[2]=t=>f.sort("length")),value:"Length",id:"sort-length"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[3]||(e[3]=t=>f.sort("views")),value:"Trending",id:"sort-views"}),(0,n._)("input",{type:"button",class:"category selectable",onClick:e[4]||(e[4]=t=>f.sort("firstupload")),value:"New",id:"sort-firstupload"}),(0,n._)("h6",h,"Page "+(0,o.zw)(m.page)+" of "+(0,o.zw)(m.pageCount),1)])]),(0,n._)("div",g,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(m.novelData,(t=>((0,n.wg)(),(0,n.iD)("div",{key:t.title,id:"novels"},[(0,n.Wm)(s.uT,null,{default:(0,n.w5)((()=>[(0,n.Wm)(b,{novelData:t,type:"browse",class:"novelcard"},null,8,["novelData"])])),_:2},1024)])))),128))]),(0,n._)("div",C,[m.page>1?((0,n.wg)(),(0,n.iD)("button",{key:0,class:"navigationButton",id:"prev",onClick:e[5]||(e[5]=t=>f.changePage(-1))},"←Previous Page")):(0,n.kq)("",!0),m.page<m.pageCount?((0,n.wg)(),(0,n.iD)("button",{key:1,class:"navigationButton",id:"next",onClick:e[6]||(e[6]=t=>f.changePage(1))},"Next Page→")):(0,n.kq)("",!0)])])}var f=a(5992);const _=t=>((0,n.dD)("data-v-7536af57"),t=t(),(0,n.Cn)(),t),b={class:"NovelCard"},w=["textContent"],y={id:"chapter-box"},D=_((()=>(0,n._)("p",{id:"recent-chapters"},"Recent Chapters",-1))),x={class:"chapter"},k=["textContent"],N=["textContent"],P=_((()=>(0,n._)("hr",{style:{margin:"0px"}},null,-1))),B={class:"chapter"},L=["textContent"],$=["textContent"];function z(t,e,a,s,r,l){const i=(0,n.up)("router-link");return(0,n.wg)(),(0,n.j4)(i,{to:{name:"coverPage",params:{title:a.novelData.novelid}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",b,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.title),id:"title"},null,8,w),(0,n._)("div",y,[D,(0,n.Wm)(i,{to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.firstChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",x,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.firstChapter["chapternumber"]),class:"chapterNumber"},null,8,k),(0,n._)("p",{class:"date",textContent:(0,o.zw)(a.novelData.firstChapter["uploaddate"])},null,8,N)])])),_:1},8,["to"]),P,a.novelData.secondChapter?((0,n.wg)(),(0,n.j4)(i,{key:0,to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.secondChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",B,[(0,n._)("p",{textContent:(0,o.zw)(a.novelData.secondChapter["chapternumber"]),class:"chapterNumber"},null,8,L),(0,n._)("p",{class:"date",textContent:(0,o.zw)(a.novelData.secondChapter["uploaddate"])},null,8,$)])])),_:1},8,["to"])):(0,n.kq)("",!0)])])])),_:1},8,["to"])}var T={name:"NovelCard",props:["novelData"],methods:{goTo(t){this.$router.push({name:"coverPage",params:{title:t}})}}},Z=a(3744);const H=(0,Z.Z)(T,[["render",z],["__scopeId","data-v-7536af57"]]);var j=H,E=a(881),I=a(9669),M=a.n(I),U={name:"Browser",components:{NovelCard:j,UtfBox:E.Z},data(){return{novelData:[],chapterList:[],attributesort:"lastupload",page:1,pageCount:0,novelCount:0}},props:["tier"],methods:{getNovels(t){void 0!=t&&(t=t.replace(/&nbsp;/g,"|"));const e="/novel/multiple?tier="+this.tier+"&identifier="+t+"&order="+this.attributesort+"&page="+this.page;f.K.get(e).then((t=>{this.novelData=t.data,console.log(this.novelData[0])})).catch((t=>{console.log(t)}))},sort(t){const e=document.getElementsByClassName("selected");this.attributesort=t;for(var a=0;a<e.length;a++)e[a].classList.remove("selected");document.getElementById("sort-"+t).classList.add("selected"),this.getNovels(this.$route.params.identifier)},changePage(t){this.page=this.page+t,this.getNovels(this.$route.params.identifier)},getPages(t){M().get("http://127.0.0.1:5000/novels-page-count?tier="+this.tier+"&identifier="+t).then((e=>{this.pageCount=e.data["page_count"],this.novelCount=e.data["novel_count"],this.getNovels(t)})).catch((t=>{console.log(t)}))}},created(){var t=this.$route.params.identifier;this.getPages(t),this.$watch((()=>this.$route.params),((t,e)=>{var a=this.$route.params.identifier;if(void 0!=a&&(a=a.replace(/&nbsp;/g,"|")),Object.keys(e).includes("browsetype")&&0==Object.keys(t).length){const t=document.getElementsByClassName("selected");this.getNovels(a),this.getPages(a);for(var n=0;n<t.length;n++)t[n].classList.remove("selected")}}))}};const W=(0,Z.Z)(U,[["render",m],["__scopeId","data-v-302ce6fd"]]);var q=W}}]);
//# sourceMappingURL=570.aaaf0762.js.map