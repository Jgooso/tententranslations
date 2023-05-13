"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[487],{7541:function(t,e,n){n.d(e,{Z:function(){return c}});var o=n(6252);const a={id:"MoveButton"};function l(t,e,n,l,i,s){return(0,o.wg)(),(0,o.iD)("div",null,[(0,o._)("div",a,[n.previous?((0,o.wg)(),(0,o.iD)("button",{key:0,onClick:e[0]||(e[0]=t=>s.go(this.$route.params.chapter-1))},"← Prev")):(0,o.kq)("",!0),n.next?((0,o.wg)(),(0,o.iD)("button",{key:1,onClick:e[1]||(e[1]=t=>s.go(parseInt(this.$route.params.chapter)+1))},"Next →")):(0,o.kq)("",!0)])])}var i={name:"NavButton",props:["first","last","previous","next"],methods:{go(t){this.$router.push({name:"chapterPage",params:{title:this.$route.params.title,chapter:t}})}}},s=n(3744);const r=(0,s.Z)(i,[["render",l],["__scopeId","data-v-dc2180d8"]]);var c=r},1771:function(t,e,n){n.d(e,{Z:function(){return p}});var o=n(6252),a=n(3577);const l={id:"navigator"},i=(0,o.Uk)("Home"),s=(0,o.Uk)("/ "),r=(0,o.Uk)("/ ");function c(t,e,n,c,d,u){const v=(0,o.up)("router-link");return(0,o.wg)(),(0,o.iD)("div",l,[(0,o.Wm)(v,{to:{name:"homePage"}},{default:(0,o.w5)((()=>[i])),_:1}),s,(0,o.Wm)(v,{to:{name:"coverPage",params:{novel:n.novelid}},textContent:(0,a.zw)(n.novel)},null,8,["to","textContent"]),r,n.chapter?((0,o.wg)(),(0,o.j4)(v,{key:0,to:{name:"chapterPage",params:{novel:n.novelid,chapter:n.chapter.chapternumber}},textContent:(0,a.zw)(n.chapter.title+" - "+n.chapter.chapternumber)},null,8,["to","textContent"])):(0,o.kq)("",!0)])}var d={name:"Navigator",props:["novel","novelid","chapter"]},u=n(3744);const v=(0,u.Z)(d,[["render",c],["__scopeId","data-v-dfffece0"]]);var p=v},881:function(t,e,n){n.d(e,{Z:function(){return v}});var o=n(6252);const a=t=>((0,o.dD)("data-v-3eb7aad7"),t=t(),(0,o.Cn)(),t),l={id:"box"},i=["innerHTML"],s=a((()=>(0,o._)("h3",{id:"point"},"◆",-1)));function r(t,e,n,a,r,c){return(0,o.wg)(),(0,o.iD)("div",l,[(0,o._)("h3",{id:"star",innerHTML:n.shape},null,8,i),s])}var c={name:"UtfBox",props:["shape"]},d=n(3744);const u=(0,d.Z)(c,[["render",r],["__scopeId","data-v-3eb7aad7"]]);var v=u},9487:function(t,e,n){n.r(e),n.d(e,{default:function(){return nt}});var o=n(6252),a=n(3577);const l=t=>((0,o.dD)("data-v-0f871711"),t=t(),(0,o.Cn)(),t),i={id:"cover",ref:"cover"},s={key:0},r=["textContent"],c={id:"inner"},d=["src"],u={id:"novel-test"},v=l((()=>(0,o._)("div",{class:"column1 label"},"Views",-1))),p=["textContent"],m=l((()=>(0,o._)("div",{class:"column1 label"},"Alternative",-1))),h=["textContent"],g=l((()=>(0,o._)("div",{class:"column1 label"},"Raw",-1))),w={class:"column2 info"},f=["href"],_=l((()=>(0,o._)("div",{class:"column1 label"},"Author",-1))),b={class:"column2 info"},D=l((()=>(0,o._)("div",{class:"column1 label"},"Genres",-1))),x={class:"column2 info"},k={class:"comma-list"},y=l((()=>(0,o._)("div",{class:"column1 label"},"Tags",-1))),C={class:"column2 info"},L={class:"comma-list"},z=l((()=>(0,o._)("div",{class:"column3 label",style:{"grid-row":"1/span 1"}},"Release",-1))),M=["textContent"],T=l((()=>(0,o._)("div",{class:"column3 label",style:{"grid-row":"2/span 1"}},"Status",-1))),H={class:"column4 info",style:{"grid-row":"2/span 1"}},P=l((()=>(0,o._)("div",{class:"column3 label",style:{"grid-row":"3/span 1"}},"Novel",-1))),Z=["textContent"],q={id:"summary"},B={key:0},W=l((()=>(0,o._)("p",{style:{"font-weight":"bold"}},"SUMMARY",-1))),U=["innerHTML"],I=l((()=>(0,o._)("br",null,null,-1))),N={id:"TableOfContents"},K={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},Y=l((()=>(0,o._)("h3",{id:"divider"},"Table Of Contents",-1))),$={id:"tableofcontentList",ref:"tableofcontentlist"},A={key:0,class:"section"},R=["textContent"],S=l((()=>(0,o._)("br",null,null,-1))),O=["id"],j={class:"title"},E={class:"date"};function F(t,e,n,l,F,G){const V=(0,o.up)("router-link"),J=(0,o.up)("UtfBox");return(0,o.wg)(),(0,o.iD)("div",null,[(0,o._)("div",i,[n.novelData.title?((0,o.wg)(),(0,o.iD)("div",s,[(0,o._)("p",{id:"noveltitle",textContent:(0,a.zw)(n.novelData.title)},null,8,r),(0,o._)("div",c,[n.novelData.imageurl?((0,o.wg)(),(0,o.iD)("img",{key:0,id:"image-border",src:n.novelData.imageurl},null,8,d)):(0,o.kq)("",!0),(0,o._)("div",u,[v,(0,o._)("div",{class:"column2 info",textContent:(0,a.zw)(n.novelData.views)},null,8,p),m,(0,o._)("div",{class:"column2 info",textContent:(0,a.zw)(n.novelData.alternativetitle)},null,8,h),g,(0,o._)("div",w,[(0,o._)("a",{href:n.novelData.url,class:"selectable"},(0,a.zw)(n.novelData.url),9,f)]),_,(0,o._)("div",b,[(0,o.Wm)(V,{to:{name:"explorePage",params:{browsetype:"novel-authors",identifier:n.novelData.authors}},class:"selectable",textContent:(0,a.zw)(n.novelData.authors)},null,8,["to","textContent"])]),D,(0,o._)("div",x,[(0,o._)("ul",k,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(n.novelData.genres,(t=>((0,o.wg)(),(0,o.iD)("li",{key:t},[(0,o.Wm)(V,{to:{name:"explorePage",params:{browsetype:"novel-genres",identifier:t}},class:"selectable",textContent:(0,a.zw)(t)},null,8,["to","textContent"])])))),128))])]),y,(0,o._)("div",C,[(0,o._)("ul",L,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(n.novelData.tags,(t=>((0,o.wg)(),(0,o.iD)("li",{key:t},[(0,o.Wm)(V,{to:{name:"explorePage",params:{browsetype:"novel-tags",identifier:t}},class:"selectable",innerHTML:t},null,8,["to","innerHTML"])])))),128))])]),z,(0,o._)("div",{class:"column4 info",style:{"grid-row":"1/span 1"},textContent:(0,a.zw)(n.novelData.novelrelease)},null,8,M),T,(0,o._)("div",H,[(0,o.Wm)(V,{to:{name:"explorePage",params:{browsetype:"novel-status",identifier:"u"+n.novelData.uploadstatus}},class:"selectable",textContent:(0,a.zw)(n.novelData.uploadstatus)},null,8,["to","textContent"])]),P,F.editable?(0,o.kq)("",!0):((0,o.wg)(),(0,o.iD)("div",{key:0,class:"column4 info",style:{"grid-row":"3/span 1"},textContent:(0,a.zw)(n.novelData.novelstatus)},null,8,Z))]),(0,o._)("div",q,[n.novelData.title?((0,o.wg)(),(0,o.iD)("div",B,[W,(0,o._)("p",{id:"description",innerHTML:n.novelData.description},null,8,U)])):(0,o.kq)("",!0)])])])):(0,o.kq)("",!0)],512),I,(0,o._)("div",N,[(0,o._)("div",K,[(0,o.Wm)(J,{shape:""}),Y,(0,o._)("button",{id:"switcher",onClick:e[0]||(e[0]=(...t)=>G.sortToc&&G.sortToc(...t))},"⇅")]),(0,o._)("ul",$,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(n.sectionList,(t=>((0,o.wg)(),(0,o.iD)("li",{key:t.section},[t.title?((0,o.wg)(),(0,o.iD)("button",A,[(0,o._)("h3",{textContent:(0,a.zw)(t.title)},null,8,R)])):(0,o.kq)("",!0),S,(0,o._)("ul",{id:t.section},[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(n.chapterList.filter((e=>e.section==t.section)),(t=>((0,o.wg)(),(0,o.iD)("li",{key:t.chapterorder},[(0,o.Wm)(V,{to:{name:"chapterPage",params:{title:n.novelData.novelid,chapter:t.chapternumber,id:t.id}},class:"group"},{default:(0,o.w5)((()=>[(0,o._)("p",j,(0,a.zw)(t.title),1),(0,o._)("p",E,(0,a.zw)(t.uploaddate),1)])),_:2},1032,["to"])])))),128))],8,O)])))),128))],512),n.chapterList.length+n.sectionList.length>25?((0,o.wg)(),(0,o.iD)("button",{key:0,onClick:e[1]||(e[1]=t=>G.showMore()),id:"showMore"},"Show More ▾")):(0,o.kq)("",!0)])])}var G=n(1771),V=n(881),J=n(7541),Q=n(2311),X=(n(5992),{name:"CoverPage",components:{UtfBox:V.Z,Navigator:G.Z,NavButton:J.Z,KoFiButton:Q.Z},props:["novelData","sectionList","chapterList","tier"],data(){return{editable:!1}},methods:{trigger(t){var e=document.getElementById(t);"none"==e.style.display?e.style.display="block":e.style.display="none"},sortToc(){this.chapterList.reverse(),this.sectionList.reverse()},showMore(){}},created(){this.chapterList.sort(((t,e)=>t.chapternumber>e.chapternumber?-1:1)),this.sectionList.sort(((t,e)=>t.section>e.section?-1:1))}}),tt=n(3744);const et=(0,tt.Z)(X,[["render",F],["__scopeId","data-v-0f871711"]]);var nt=et}}]);
//# sourceMappingURL=487.cc074793.js.map