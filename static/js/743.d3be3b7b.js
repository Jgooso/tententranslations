"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[743],{881:function(e,t,n){n.d(t,{Z:function(){return v}});var l=n(6252);const o=e=>((0,l.dD)("data-v-3eb7aad7"),e=e(),(0,l.Cn)(),e),a={id:"box"},s=["innerHTML"],i=o((()=>(0,l._)("h3",{id:"point"},"◆",-1)));function r(e,t,n,o,r,c){return(0,l.wg)(),(0,l.iD)("div",a,[(0,l._)("h3",{id:"star",innerHTML:n.shape},null,8,s),i])}var c={name:"UtfBox",props:["shape"]},d=n(3744);const u=(0,d.Z)(c,[["render",r],["__scopeId","data-v-3eb7aad7"]]);var v=u},4743:function(e,t,n){n.r(t),n.d(t,{default:function(){return $}});var l=n(6252),o=n(3577);const a=e=>((0,l.dD)("data-v-8c7565d0"),e=e(),(0,l.Cn)(),e),s={id:"cover",ref:"cover"},i={key:0},r=["textContent"],c={id:"inner"},d=["src"],u={id:"novel-test"},v=a((()=>(0,l._)("div",{class:"column1 label"},"Views",-1))),p=["textContent"],m=a((()=>(0,l._)("div",{class:"column1 label"},"Alternative",-1))),w=["textContent"],g=a((()=>(0,l._)("div",{class:"column1 label"},"Raw",-1))),_={class:"column2 info"},h=["href"],b=a((()=>(0,l._)("div",{class:"column1 label"},"Author",-1))),f={class:"column2 info"},D=a((()=>(0,l._)("div",{class:"column1 label"},"Genres",-1))),y={class:"column2 info"},x={class:"comma-list"},C=a((()=>(0,l._)("div",{class:"column1 label"},"Tags",-1))),k={class:"column2 info"},L={class:"comma-list"},z=a((()=>(0,l._)("div",{class:"column3 label",style:{"grid-row":"1/span 1"}},"Release",-1))),M=["textContent"],T=a((()=>(0,l._)("div",{class:"column3 label",style:{"grid-row":"2/span 1"}},"Status",-1))),H={class:"column4 info",style:{"grid-row":"2/span 1"}},q=a((()=>(0,l._)("div",{class:"column3 label",style:{"grid-row":"3/span 1"}},"Novel",-1))),P=["textContent"],W={id:"summary"},Y={key:0},B=a((()=>(0,l._)("p",{style:{"font-weight":"bold"}},"SUMMARY",-1))),K=["innerHTML"],U=a((()=>(0,l._)("br",null,null,-1))),Z={id:"TableOfContents"},A={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},I=a((()=>(0,l._)("h3",{id:"divider"},"Table Of Contents",-1))),R={id:"tableofcontentList",ref:"tableofcontentlist"},S={key:0,class:"section"},O=["textContent"],E=a((()=>(0,l._)("br",null,null,-1))),G=["id"],N={class:"title"},V={class:"date"};function j(e,t,n,a,j,F){const J=(0,l.up)("router-link"),Q=(0,l.up)("UtfBox");return(0,l.wg)(),(0,l.iD)("div",null,[(0,l._)("div",s,[n.novelData.title?((0,l.wg)(),(0,l.iD)("div",i,[(0,l._)("p",{id:"noveltitle",textContent:(0,o.zw)(n.novelData.title)},null,8,r),(0,l._)("div",c,[n.novelData.imageurl?((0,l.wg)(),(0,l.iD)("img",{key:0,id:"image-border",src:n.novelData.imageurl},null,8,d)):(0,l.kq)("",!0),(0,l._)("div",u,[v,(0,l._)("div",{class:"column2 info",textContent:(0,o.zw)(n.novelData.views)},null,8,p),m,(0,l._)("div",{class:"column2 info",textContent:(0,o.zw)(n.novelData.alternativetitle)},null,8,w),g,(0,l._)("div",_,[(0,l._)("a",{href:n.novelData.url,class:"selectable"},(0,o.zw)(n.novelData.url),9,h)]),b,(0,l._)("div",f,[(0,l.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-authors",identifier:n.novelData.authors}},class:"selectable",textContent:(0,o.zw)(n.novelData.authors)},null,8,["to","textContent"])]),D,(0,l._)("div",y,[(0,l._)("ul",x,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.novelData.genres,(e=>((0,l.wg)(),(0,l.iD)("li",{key:e},[(0,l.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-genres",identifier:e}},class:"selectable",textContent:(0,o.zw)(e)},null,8,["to","textContent"])])))),128))])]),C,(0,l._)("div",k,[(0,l._)("ul",L,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.novelData.tags,(e=>((0,l.wg)(),(0,l.iD)("li",{key:e},[(0,l.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-tags",identifier:e}},class:"selectable",innerHTML:e},null,8,["to","innerHTML"])])))),128))])]),z,(0,l._)("div",{class:"column4 info",style:{"grid-row":"1/span 1"},textContent:(0,o.zw)(n.novelData.novelrelease)},null,8,M),T,(0,l._)("div",H,[(0,l.Wm)(J,{to:{name:"explorePage",params:{browsetype:"novel-status",identifier:"u"+n.novelData.uploadstatus}},class:"selectable",textContent:(0,o.zw)(n.novelData.uploadstatus)},null,8,["to","textContent"])]),q,j.editable?(0,l.kq)("",!0):((0,l.wg)(),(0,l.iD)("div",{key:0,class:"column4 info",style:{"grid-row":"3/span 1"},textContent:(0,o.zw)(n.novelData.novelstatus)},null,8,P))]),(0,l._)("div",W,[n.novelData.title?((0,l.wg)(),(0,l.iD)("div",Y,[B,(0,l._)("p",{id:"description",innerHTML:n.novelData.description},null,8,K)])):(0,l.kq)("",!0)])])])):(0,l.kq)("",!0)],512),U,(0,l._)("div",Z,[(0,l._)("div",A,[(0,l.Wm)(Q,{shape:""}),I,(0,l._)("button",{id:"switcher",onClick:t[0]||(t[0]=(...e)=>F.sortToc&&F.sortToc(...e))},"⇅")]),(0,l._)("ul",R,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.sectionList,(e=>((0,l.wg)(),(0,l.iD)("li",{key:e.section},[e.title?((0,l.wg)(),(0,l.iD)("button",S,[(0,l._)("h3",{textContent:(0,o.zw)(e.title)},null,8,O)])):(0,l.kq)("",!0),E,(0,l._)("ul",{id:e.section},[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.chapterList.filter((t=>t.section==e.section)),(e=>((0,l.wg)(),(0,l.iD)("li",{key:e.chapterorder},[(0,l.Wm)(J,{to:{name:"chapterPage",params:{title:n.novelData.novelid,chapter:e.chapternumber,id:e.id}},class:"group"},{default:(0,l.w5)((()=>[(0,l._)("p",N,(0,o.zw)(e.title),1),(0,l._)("p",V,(0,o.zw)(e.uploaddate),1)])),_:2},1032,["to"])])))),128))],8,G)])))),128))],512),n.chapterList.length+n.sectionList.length>25?((0,l.wg)(),(0,l.iD)("button",{key:0,onClick:t[1]||(t[1]=e=>F.showMore()),id:"showMore"},"Show More ▾")):(0,l.kq)("",!0)])])}var F=n(881),J={name:"CoverPage",components:{UtfBox:F.Z},props:["novelData","sectionList","chapterList","tier"],data(){return{editable:!1}},methods:{trigger(e){var t=document.getElementById(e);"none"==t.style.display?t.style.display="block":t.style.display="none"},sortToc(){this.chapterList.reverse(),this.sectionList.reverse()},showMore(){}},created(){this.chapterList.sort(((e,t)=>e.chapternumber>t.chapternumber?-1:1)),this.sectionList.sort(((e,t)=>e.section>t.section?-1:1))}},Q=n(3744);const X=(0,Q.Z)(J,[["render",j],["__scopeId","data-v-8c7565d0"]]);var $=X}}]);
//# sourceMappingURL=743.d3be3b7b.js.map