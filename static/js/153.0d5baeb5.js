"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[153],{85:function(e,t,l){l.d(t,{Z:function(){return v}});var n=l(6252);const a=e=>((0,n.dD)("data-v-71035fa8"),e=e(),(0,n.Cn)(),e),o={id:"box"},s=["innerHTML"],i=a((()=>(0,n._)("h3",{id:"point",class:"utf-shape"},"◆",-1)));function r(e,t,l,a,r,c){return(0,n.wg)(),(0,n.iD)("div",o,[(0,n._)("h3",{id:"star",class:"utf-shape",innerHTML:l.shape},null,8,s),i])}var c={name:"UtfBox",props:["shape"]},d=l(3744);const u=(0,d.Z)(c,[["render",r],["__scopeId","data-v-71035fa8"]]);var v=u},3153:function(e,t,l){l.r(t),l.d(t,{default:function(){return $}});var n=l(6252),a=l(3577);const o=e=>((0,n.dD)("data-v-ccea3dc2"),e=e(),(0,n.Cn)(),e),s={id:"cover",ref:"cover"},i={key:0},r=["textContent"],c={id:"inner"},d=["src"],u={id:"novel-cover"},v=o((()=>(0,n._)("div",{class:"column1 label"},"Views",-1))),p=["textContent"],m=o((()=>(0,n._)("div",{class:"column1 label"},"Alternative",-1))),w=["textContent"],_=o((()=>(0,n._)("div",{class:"column1 label"},"Raw",-1))),f={class:"column2 info"},g=["href"],b=o((()=>(0,n._)("div",{class:"column1 label"},"Author",-1))),h={class:"column2 info"},D=o((()=>(0,n._)("div",{class:"column1 label"},"Genres",-1))),y={class:"column2 info"},x={class:"comma-list"},C=o((()=>(0,n._)("div",{class:"column1 label"},"Tags",-1))),k={class:"column2 info"},L={class:"comma-list"},z=o((()=>(0,n._)("div",{class:"column3 label",style:{"grid-row":"1/span 1"}},"Release",-1))),T=["textContent"],H=o((()=>(0,n._)("div",{class:"column3 label",style:{"grid-row":"2/span 1"}},"Status",-1))),M={class:"column4 info",style:{"grid-row":"2/span 1"}},P=o((()=>(0,n._)("div",{class:"column3 label",style:{"grid-row":"3/span 1"}},"Novel",-1))),W=["textContent"],q={id:"summary"},Y={key:0},B=o((()=>(0,n._)("p",{style:{"font-weight":"bold"}},"SUMMARY",-1))),K=["innerHTML"],U=o((()=>(0,n._)("br",null,null,-1))),Z={id:"TableOfContents"},A={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},I=o((()=>(0,n._)("h3",{id:"divider"},"Table Of Contents",-1))),R={id:"tableofcontentList",ref:"tableofcontentlist"},O={key:0,class:"section"},S=["textContent"],E=o((()=>(0,n._)("br",null,null,-1))),G=["id"],N={class:"title"},V={class:"date"};function j(e,t,l,o,j,F){const J=(0,n.up)("router-link"),Q=(0,n.up)("UtfBox");return(0,n.wg)(),(0,n.iD)("div",null,[(0,n._)("div",s,[l.novelData.title?((0,n.wg)(),(0,n.iD)("div",i,[(0,n._)("p",{id:"noveltitle",textContent:(0,a.zw)(l.novelData.title)},null,8,r),(0,n._)("div",c,[l.novelData.imageurl?((0,n.wg)(),(0,n.iD)("img",{key:0,id:"image-border",src:l.novelData.imageurl},null,8,d)):(0,n.kq)("",!0),(0,n._)("div",u,[v,(0,n._)("div",{class:"column2 info",textContent:(0,a.zw)(l.novelData.views)},null,8,p),m,(0,n._)("div",{class:"column2 info",textContent:(0,a.zw)(l.novelData.alternativetitle)},null,8,w),_,(0,n._)("div",f,[(0,n._)("a",{href:l.novelData.url,class:"selectable"},(0,a.zw)(l.novelData.url),9,g)]),b,(0,n._)("div",h,[(0,n.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-authors",identifier:l.novelData.authors}},class:"selectable",textContent:(0,a.zw)(l.novelData.authors)},null,8,["to","textContent"])]),D,(0,n._)("div",y,[(0,n._)("ul",x,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.novelData.genres,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e},[(0,n.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-genres",identifier:e}},class:"selectable",textContent:(0,a.zw)(e)},null,8,["to","textContent"])])))),128))])]),C,(0,n._)("div",k,[(0,n._)("ul",L,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.novelData.tags,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e},[(0,n.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-tags",identifier:e}},class:"selectable",innerHTML:e},null,8,["to","innerHTML"])])))),128))])]),z,(0,n._)("div",{class:"column4 info",style:{"grid-row":"1/span 1"},textContent:(0,a.zw)(l.novelData.novelrelease)},null,8,T),H,(0,n._)("div",M,[(0,n.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-status",identifier:"u"+l.novelData.uploadstatus}},class:"selectable",textContent:(0,a.zw)(l.novelData.uploadstatus)},null,8,["to","textContent"])]),P,j.editable?(0,n.kq)("",!0):((0,n.wg)(),(0,n.iD)("div",{key:0,class:"column4 info",style:{"grid-row":"3/span 1"},textContent:(0,a.zw)(l.novelData.novelstatus)},null,8,W))]),(0,n._)("div",q,[l.novelData.title?((0,n.wg)(),(0,n.iD)("div",Y,[B,(0,n._)("p",{id:"description",innerHTML:l.novelData.description},null,8,K)])):(0,n.kq)("",!0)])])])):(0,n.kq)("",!0)],512),U,(0,n._)("div",Z,[(0,n._)("div",A,[(0,n.Wm)(Q,{shape:""}),I,(0,n._)("button",{id:"switcher",onClick:t[0]||(t[0]=(...e)=>F.sortToc&&F.sortToc(...e))},"⇅")]),(0,n._)("ul",R,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.sectionList,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e.section},[e.title?((0,n.wg)(),(0,n.iD)("button",O,[(0,n._)("h3",{textContent:(0,a.zw)(e.title)},null,8,S)])):(0,n.kq)("",!0),E,(0,n._)("ul",{id:e.section},[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.chapterList.filter((t=>t.section==e.section)),(e=>((0,n.wg)(),(0,n.iD)("li",{key:e.chapterorder},[(0,n.Wm)(J,{to:{name:"chapterPage",params:{title:l.novelData.novelid,chapter:e.chapternumber,id:e.id}},class:"group"},{default:(0,n.w5)((()=>[(0,n._)("p",N,(0,a.zw)(e.title),1),(0,n._)("p",V,(0,a.zw)(e.uploaddate),1)])),_:2},1032,["to"])])))),128))],8,G)])))),128))],512)])])}var F=l(85),J={name:"CoverPage",components:{UtfBox:F.Z},props:["novelData","sectionList","chapterList","tier"],data(){return{editable:!1}},methods:{trigger(e){var t=document.getElementById(e);"none"==t.style.display?t.style.display="block":t.style.display="none"},sortToc(){this.chapterList.reverse(),this.sectionList.reverse()}},created(){this.chapterList.sort(((e,t)=>e.chapternumber>t.chapternumber?-1:1)),this.sectionList.sort(((e,t)=>e.section>t.section?-1:1))}},Q=l(3744);const X=(0,Q.Z)(J,[["render",j],["__scopeId","data-v-ccea3dc2"]]);var $=X}}]);
//# sourceMappingURL=153.0d5baeb5.js.map