"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[246],{881:function(e,t,a){a.d(t,{Z:function(){return c}});var n=a(6252);const o=e=>((0,n.dD)("data-v-3eb7aad7"),e=e(),(0,n.Cn)(),e),l={id:"box"},r=["innerHTML"],i=o((()=>(0,n._)("h3",{id:"point"},"◆",-1)));function s(e,t,a,o,s,d){return(0,n.wg)(),(0,n.iD)("div",l,[(0,n._)("h3",{id:"star",innerHTML:a.shape},null,8,r),i])}var d={name:"UtfBox",props:["shape"]},p=a(3744);const v=(0,p.Z)(d,[["render",s],["__scopeId","data-v-3eb7aad7"]]);var c=v},4246:function(e,t,a){a.r(t),a.d(t,{default:function(){return S}});var n=a(6252);const o=e=>((0,n.dD)("data-v-9b53f304"),e=e(),(0,n.Cn)(),e),l={key:0,id:"homePage"},r={class:"divide"},i=o((()=>(0,n._)("h3",{id:"divider"},"Most Popular",-1))),s=o((()=>(0,n._)("br",null,null,-1))),d={id:"popular"},p={id:"popularList"},v={class:"divide"},c=o((()=>(0,n._)("h3",{id:"divider"},"New Projects",-1))),u=o((()=>(0,n._)("br",null,null,-1))),m={class:"novelrow"},h={class:"divide"},g=o((()=>(0,n._)("h3",{id:"divider"},"Latest Releases",-1))),D=o((()=>(0,n._)("br",null,null,-1))),_={class:"novelrow"};function C(e,t,a,o,C,w){const f=(0,n.up)("UtfBox"),x=(0,n.up)("HomePageNovelCard"),y=(0,n.up)("HomeCard");return C.popularNovels[0]?((0,n.wg)(),(0,n.iD)("div",l,[(0,n._)("div",r,[(0,n.Wm)(f,{shape:"⬤"}),i]),s,(0,n._)("div",d,[(0,n.Wm)(x,{novelData:C.popularNovels[0],type:"main",id:"mainPopular"},null,8,["novelData"]),(0,n._)("div",p,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(C.popularNovels.slice(1,C.popularNovels.length),(e=>((0,n.wg)(),(0,n.iD)("div",{key:e.title},[(0,n.Wm)(x,{novelData:e,class:"popularnovel",type:"general"},null,8,["novelData"])])))),128))])]),(0,n._)("div",v,[(0,n.Wm)(f,{shape:"⬤"}),c]),u,(0,n._)("div",m,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(C.recentNovels,(e=>((0,n.wg)(),(0,n.iD)("div",{key:e.title},[(0,n.Wm)(y,{novelData:e,type:"home"},null,8,["novelData"])])))),128))]),(0,n._)("div",h,[(0,n.Wm)(f,{shape:"⬤"}),g]),D,(0,n._)("div",_,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(C.latestNovels,(e=>((0,n.wg)(),(0,n.iD)("div",{key:e.title},[(0,n.Wm)(y,{novelData:e,type:"home"},null,8,["novelData"])])))),128))])])):(0,n.kq)("",!0)}var w=a(9669),f=a.n(w),x=a(881),y=a(3577);const b={id:"rank"},N={key:0},k=["innerHTML"],P=(0,n.Uk)("Continue Reading");function H(e,t,a,o,l,r){const i=(0,n.up)("router-link");return(0,n.wg)(),(0,n.iD)("div",{class:(0,y.C_)(a.type)},[(0,n._)("div",b,(0,y.zw)(a.novelData.row_num),1),(0,n.Wm)(i,{to:{name:"coverPage",params:{title:a.novelData.novelid}},textContent:(0,y.zw)(a.novelData.title),id:"title"},null,8,["to","textContent"]),"main"==a.type?((0,n.wg)(),(0,n.iD)("div",N,[(0,n.Wm)(i,{to:{name:"explorePage",params:{browsetype:"novel-genres",identifier:a.novelData.genre}},textContent:(0,y.zw)(a.novelData.genre),id:"main-genre"},null,8,["to","textContent"]),(0,n._)("p",{innerHTML:a.novelData.description,id:"description"},null,8,k),(0,n.Wm)(i,{to:{name:"coverPage",params:{title:a.novelData.novelid}},id:"continue"},{default:(0,n.w5)((()=>[P])),_:1},8,["to"])])):((0,n.wg)(),(0,n.j4)(i,{key:1,to:{name:"explorePage",params:{browsetype:"novel-genres",identifier:a.novelData.genre}},textContent:(0,y.zw)(a.novelData.genre),id:"general-genre"},null,8,["to","textContent"]))],2)}var W={name:"HomePageNovelCard",props:["novelData","type"],methods:{goTo(e){this.$router.push({name:"coverPage",params:{title:e}})}}},z=a(3744);const L=(0,z.Z)(W,[["render",H],["__scopeId","data-v-0d944904"]]);var T=L;const Z=e=>((0,n.dD)("data-v-092cf320"),e=e(),(0,n.Cn)(),e),M={id:"HomeCard"},j=["textContent"],I={id:"chapter-box"},U=Z((()=>(0,n._)("p",{id:"recent-chapters"},"Recent Chapters",-1))),B={class:"chapter"},K=["textContent"],R=["textContent"],Y=Z((()=>(0,n._)("hr",{style:{margin:"0px"}},null,-1))),q={class:"chapter"},$=["textContent"],A=["textContent"];function E(e,t,a,o,l,r){const i=(0,n.up)("router-link");return(0,n.wg)(),(0,n.j4)(i,{to:{name:"coverPage",params:{title:a.novelData.novelid}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",M,[(0,n._)("p",{textContent:(0,y.zw)(a.novelData.title),id:"title"},null,8,j),(0,n._)("div",I,[U,(0,n.Wm)(i,{to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.firstChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",B,[(0,n._)("p",{textContent:(0,y.zw)(a.novelData.firstChapter["chapternumber"]),class:"chapterNumber"},null,8,K),(0,n._)("p",{class:"date",textContent:(0,y.zw)(a.novelData.firstChapter["uploaddate"])},null,8,R)])])),_:1},8,["to"]),Y,a.novelData.secondChapter?((0,n.wg)(),(0,n.j4)(i,{key:0,to:{name:"chapterPage",params:{title:a.novelData.novelid,chapter:a.novelData.secondChapter["chapternumber"]}},style:{"text-decoration":"none"}},{default:(0,n.w5)((()=>[(0,n._)("div",q,[(0,n._)("p",{textContent:(0,y.zw)(a.novelData.secondChapter["chapternumber"]),class:"chapterNumber"},null,8,$),(0,n._)("p",{class:"date",textContent:(0,y.zw)(a.novelData.secondChapter["uploaddate"])},null,8,A)])])),_:1},8,["to"])):(0,n.kq)("",!0)])])])),_:1},8,["to"])}var F={name:"HomeCard",props:["novelData"],methods:{goTo(e){this.$router.push({name:"coverPage",params:{title:e}})}}};const G=(0,z.Z)(F,[["render",E],["__scopeId","data-v-092cf320"]]);var J=G,O={name:"HomePage",props:["tier"],components:{UtfBox:x.Z,HomePageNovelCard:T,HomeCard:J},data(){return{popularNovels:[],recentNovels:[],latestNovels:[]}},created(){f().get("http://127.0.0.1:5000/home?tier="+this.tier).then((e=>{this.popularNovels=e.data["popular"],this.recentNovels=e.data["recent"],this.latestNovels=e.data["latest"],console.log(e)})).catch((e=>{console.log(e)}))}};const Q=(0,z.Z)(O,[["render",C],["__scopeId","data-v-9b53f304"]]);var S=Q}}]);
//# sourceMappingURL=246.e54f43cb.js.map