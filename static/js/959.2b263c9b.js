"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[959],{6393:function(e,t,n){n.d(t,{Z:function(){return h}});var l=n(6252),o=n(3577);const a={id:"genres"},s=["value","name","checked","onClick"];function i(e,t,n,i,c,r){return(0,l.wg)(),(0,l.iD)("div",a,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.genres.length,((e,t)=>((0,l.wg)(),(0,l.iD)("label",{key:t},[(0,l._)("input",{type:"checkbox",value:n.genres[t],name:"genre"+t,class:"genrecheckbox",checked:n.selectedgenres.includes(n.genres[t]),onClick:e=>r.changeGenre(n.genres[t])},null,8,s),(0,l.Uk)((0,o.zw)(n.genres[t]),1)])))),128))])}var c={name:"GenreSelector",props:["genres","selectedgenres"],methods:{changeGenre(e){if(this.selectedgenres.includes(e))for(var t=0;t<this.selectedgenres.length;t++)this.selectedgenres[t]===e&&(this.selectedgenres.splice(t,1),t--);else this.selectedgenres.push(e)}}},r=n(3744);const d=(0,r.Z)(c,[["render",i],["__scopeId","data-v-51abe6a6"]]);var h=d},9524:function(e,t,n){n.d(t,{Z:function(){return k}});var l=n(6252);const o={for:"tagfilter"},a=(0,l.Uk)("Filter "),s={id:"tagList"},i={class:"selectedtaglist"},c={id:"tagselector"},r=["id"],d=["value","name","onChange"],h=["innerHTML"];function p(e,t,n,p,u,g){const v=(0,l.up)("tagBox");return(0,l.wg)(),(0,l.iD)("div",null,[(0,l._)("label",o,[a,(0,l._)("input",{type:"text",id:"tagfilter",onKeyup:t[0]||(t[0]=e=>g.filterTag()),onFocusin:t[1]||(t[1]=e=>g.showtags())},null,32)]),(0,l._)("div",s,[(0,l._)("ul",i,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.selectedtags,(e=>((0,l.wg)(),(0,l.iD)("li",{key:e},[(0,l.Wm)(v,{tag:e,onRemove:g.removeTag},null,8,["tag","onRemove"])])))),128))]),(0,l._)("div",c,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.tags.length,(e=>((0,l.wg)(),(0,l.iD)("label",{key:e,class:"tagbutton unselected",id:n.tags[e]},[(0,l._)("input",{type:"checkbox",value:n.tags[e],name:"tag"+e,onChange:t=>g.addTag(n.tags[e])},null,40,d),(0,l._)("p",{innerHTML:n.tags[e]},null,8,h)],8,r)))),128))])])])}const u={class:"tagBox"},g=["innerHTML"];function v(e,t,n,o,a,s){return(0,l.wg)(),(0,l.iD)("div",u,[(0,l._)("p",{innerHTML:n.tag},null,8,g),(0,l._)("button",{onClick:t[0]||(t[0]=e=>s.remove())},"x")])}var m={name:"tagBox",props:["tag"],methods:{remove(){this.$emit("remove",this.tag)}}},y=n(3744);const _=(0,y.Z)(m,[["render",v],["__scopeId","data-v-6f470986"]]);var f=_,b={name:"TagSelector",props:["tags","selectedtags"],components:{tagBox:f},methods:{addTag(e){const t=document.getElementById(e);t.classList.remove("unselected");const n=e.replace(/[0-9]/g,"");this.selectedtags.includes(n)||this.selectedtags.push(n)},removeTag(e){const t=this.selectedtags.indexOf(e);this.selectedtags.splice(t-1,1),document.getElementById(e).classList.add("unselected")},filterTag(){var e,t,n;e=document.getElementById("tagfilter").value.toUpperCase(),t=document.getElementsByClassName("tagbutton");for(var l=0;l<t.length;l++)n=t[l].value||t[l].innerText,n.toUpperCase().indexOf(e)>-1?t[l].style.display="":t[l].style.display="none"},showtags(){document.getElementById("tagselector").style.display="flex"},hidetags(){document.getElementById("tagselector").style.display="none"}}};const C=(0,y.Z)(b,[["render",p],["__scopeId","data-v-5e24f6b4"]]);var k=C},85:function(e,t,n){n.d(t,{Z:function(){return p}});var l=n(6252);const o=e=>((0,l.dD)("data-v-71035fa8"),e=e(),(0,l.Cn)(),e),a={id:"box"},s=["innerHTML"],i=o((()=>(0,l._)("h3",{id:"point",class:"utf-shape"},"◆",-1)));function c(e,t,n,o,c,r){return(0,l.wg)(),(0,l.iD)("div",a,[(0,l._)("h3",{id:"star",class:"utf-shape",innerHTML:n.shape},null,8,s),i])}var r={name:"UtfBox",props:["shape"]},d=n(3744);const h=(0,d.Z)(r,[["render",c],["__scopeId","data-v-71035fa8"]]);var p=h},4959:function(e,t,n){n.r(t),n.d(t,{default:function(){return Ce}});var l=n(6252),o=n(3577);const a=e=>((0,l.dD)("data-v-6a9ead0c"),e=e(),(0,l.Cn)(),e),s={id:"editPage"},i={id:"confirmationBox"},c={style:{margin:"auto"}},r={style:{display:"flex","flex-direction":"row",margin:"auto",width:"220px"}},d=["value"],h={id:"cover",ref:"cover"},p={key:0},u=["textContent"],g={id:"inner"},v={id:"novel-information"},m={id:"data"},y=a((()=>(0,l._)("td",null,"Author",-1))),_={class:"info"},f=a((()=>(0,l._)("td",null,"URL",-1))),b={class:"info"},C=["href"],k=a((()=>(0,l._)("td",null,"Genres",-1))),D={class:"category"},w=a((()=>(0,l._)("td",null,"Tags",-1))),x={class:"category"},E=a((()=>(0,l._)("td",null,"Raw Status",-1))),T={class:"info"},B=["selected"],L=a((()=>(0,l._)("option",{value:"Ongoing"},"Ongoing",-1))),I=a((()=>(0,l._)("option",{value:"Completed"},"Completed",-1))),H=a((()=>(0,l._)("option",{value:"On Hold"},"On Hold",-1))),M=a((()=>(0,l._)("option",{value:"Dropped"},"Dropped",-1))),U=[L,I,H,M],$=a((()=>(0,l._)("td",null,"Novel Active",-1))),z={id:"genre-selector"},N=a((()=>(0,l._)("button",{style:{"background-color":"red","font-weight":"bold"}},"DELETE",-1))),S={id:"summary"},Z={key:0},G={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},A=a((()=>(0,l._)("h3",{id:"divider"},"SUMMARY",-1))),K=a((()=>(0,l._)("br",null,null,-1))),O=["innerHTML"],Y={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},R=a((()=>(0,l._)("h3",{id:"divider"},"CHAPTERS",-1))),P=a((()=>(0,l._)("br",null,null,-1))),W={id:"TableOfContents"},q={id:"table",ref:"tableofcontentlist"},F=a((()=>(0,l._)("tr",{class:"table-list"},[(0,l._)("td",{class:"chapter-title"},"Chapter Title"),(0,l._)("td",{class:"chapter-check-box",style:{"font-size":"15px"}},"Edited"),(0,l._)("td",{class:"chapter-check-box",style:{"font-size":"15px"}},"Uploaded"),(0,l._)("td",{style:{"font-size":"15px"}},"Upload Date")],-1))),X={style:{display:"flex","flex-direction":"column"}},j=["innerHTML","id"],J={style:{width:"100%"}},Q=["id"],V={class:"chapter-title"},ee=["value","onClick"],te=["onClick"],ne=["onClick"],le={key:2,style:{color:"lightgreen"},class:"chapter-check-box"},oe={key:3,style:{color:"red"},class:"chapter-check-box"},ae=["id","value","onChange"],se={id:"chapterEditor"},ie={key:0},ce=(0,l.Uk)("← "),re={key:1},de={contenteditable:"True",id:"chapter-title"},he=["textContent"];function pe(e,t,n,a,L,I){const H=(0,l.up)("GenreSelector"),M=(0,l.up)("TagSelector"),pe=(0,l.up)("UtfBox");return(0,l.wg)(),(0,l.iD)("div",s,[(0,l._)("div",i,[(0,l._)("h1",c,(0,o.zw)(0==L.novelData.novelactive?"Confirm Activate Novel":"Confirm Deactivate Novel"),1),(0,l._)("div",r,[(0,l._)("button",{onClick:t[0]||(t[0]=e=>I.confirm(2)),class:"confirmation-button"},"Confirm"),(0,l._)("button",{onClick:t[1]||(t[1]=e=>I.confirm(1)),class:"confirmation-button"},"Cancel")])]),(0,l._)("select",{id:"novel-selector",onChange:t[2]||(t[2]=e=>I.selectNovel())},[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(L.novelList,(e=>((0,l.wg)(),(0,l.iD)("option",{value:e.novelid},(0,o.zw)(e.title)+" "+(0,o.zw)(100*e.completed_percentage)+"%",9,d)))),256))],32),(0,l._)("div",h,[L.novelData.title?((0,l.wg)(),(0,l.iD)("div",p,[(0,l._)("p",{id:"noveltitle",textContent:(0,o.zw)(L.novelData.title),contenteditable:"true"},null,8,u),(0,l._)("div",g,[(0,l._)("div",v,[(0,l._)("div",m,[(0,l._)("table",null,[(0,l._)("tr",null,[y,(0,l._)("td",_,(0,o.zw)(L.novelData.author),1)]),(0,l._)("tr",null,[f,(0,l._)("td",b,[(0,l._)("a",{href:L.novelData.url,class:"selectable"},(0,o.zw)(L.novelData.url),9,C)])]),(0,l._)("tr",null,[k,(0,l._)("td",D,[(0,l._)("button",{class:"show",onClick:t[3]||(t[3]=e=>I.showGenres())},"Show")])]),(0,l._)("tr",null,[w,(0,l._)("td",x,[(0,l._)("button",{class:"show",onClick:t[4]||(t[4]=e=>I.showTags())},"Show")])])]),(0,l._)("table",null,[(0,l._)("tr",null,[E,(0,l._)("td",T,[(0,l._)("select",{id:"completedEdit",selected:e.value=L.novelData.novelstatus},U,8,B)])]),(0,l._)("tr",null,[$,(0,l._)("td",null,[(0,l._)("button",{onClick:t[5]||(t[5]=e=>I.confirm(0))},(0,o.zw)(0==L.novelData.novelactive?"Activate Novel":"Deactivate Novel"),1)])])])]),(0,l._)("div",z,[(0,l.Wm)(H,{genres:L.genres,selectedgenres:L.novelData.genres},null,8,["genres","selectedgenres"])]),(0,l.Wm)(M,{tags:L.tags,selectedtags:L.novelData.tags,id:"tag-selector"},null,8,["tags","selectedtags"])]),N]),(0,l._)("button",{onClick:t[6]||(t[6]=e=>I.uploadchapter())},"Uploadchapter"),(0,l._)("div",S,[L.novelData.title?((0,l.wg)(),(0,l.iD)("div",Z,[(0,l._)("div",G,[(0,l.Wm)(pe,{shape:"★"}),A]),K,(0,l._)("p",{id:"noveldescription",innerHTML:L.novelData.description,contenteditable:"true"},null,8,O)])):(0,l.kq)("",!0)]),(0,l._)("div",Y,[(0,l.Wm)(pe,{shape:"★"}),R]),P,(0,l._)("div",W,[(0,l._)("table",q,[F,((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(L.sectionList,(e=>((0,l.wg)(),(0,l.iD)("tr",X,[e.title?((0,l.wg)(),(0,l.iD)("p",{key:0,class:"section",innerHTML:e.title,id:"section"+e.section,contenteditable:"True"},null,8,j)):(0,l.kq)("",!0),(0,l._)("tr",J,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(L.chapterList.filter((t=>t.section==e.section)),(e=>((0,l.wg)(),(0,l.iD)("tr",{key:e.chapternumber,class:"table-list",id:"chapter"+e.chapternumber},[(0,l._)("td",V,[(0,l._)("label",null,[(0,l.Uk)((0,o.zw)(e.title)+" ",1),(0,l._)("input",{type:"button",class:"chapter-list",value:e.chapternumber,onClick:t=>I.displayChapter(e)},null,8,ee)])]),1==e.chapteredited?((0,l.wg)(),(0,l.iD)("td",{key:0,style:{color:"lightgreen"},class:"chapter-check-box edited-check",onClick:t=>I.chapteredit(e)},"✓",8,te)):((0,l.wg)(),(0,l.iD)("td",{key:1,style:{color:"red"},class:"chapter-check-box edited-check",onClick:t=>I.chapteredit(e)},"X",8,ne)),1==e.chapteractive?((0,l.wg)(),(0,l.iD)("td",le,"✓")):((0,l.wg)(),(0,l.iD)("td",oe,"X")),(0,l._)("td",null,[(0,l._)("input",{type:"datetime-local",id:"date"+e.chapterorder,value:e.uploaddate,onChange:t=>I.changeupload(e),min:"2023-01-01T00:00",style:{width:"fit-content","margin-right":"20px"}},null,40,ae)])],8,Q)))),128))])])))),256))],512),(0,l._)("div",se,[L.saved?((0,l.wg)(),(0,l.iD)("label",ie,[ce,(0,l._)("input",{type:"button",id:"back-button",onClick:t[7]||(t[7]=e=>I.hideChapter())})])):((0,l.wg)(),(0,l.iD)("p",re," Unsaved Changes")),(0,l._)("h3",de,(0,o.zw)(L.chapterTitle),1),(0,l._)("textarea",{textContent:(0,o.zw)(L.chapterContent),id:"chapter-content"},null,8,he)])])])):(0,l.kq)("",!0)],512),(0,l._)("button",{onClick:t[8]||(t[8]=e=>I.submit())},"Submit")])}var ue=n(9669),ge=n.n(ue),ve=n(6393),me=n(9524),ye=n(85),_e={data(){return{selectednovel:"",novelList:[],novelData:[],tags:[],genres:[],chapterList:[],sectionList:[],chapterContent:"",currentChapter:"",saved:"",chapterTitle:""}},components:{GenreSelector:ve.Z,TagSelector:me.Z,UtfBox:ye.Z},methods:{confirm(e){var t=document.getElementById("confirmationBox");0==e?t.style.display="flex":1==e?t.style.display="none":2==e&&(1==this.novelData.novelactive?this.novelData.novelactive=0:this.novelData.novelactive=1,t.style.display="none",ge().put(`http://tententranslation.com/activatenovel?novel=${this.novelData.novelid}'&active=${this.novelData.novelactive}`).then((e=>{console.log("sent")})).catch((e=>{console.log(e)})))},selectNovel(e){this.selectednovel=e||document.getElementById("novel-selector").value;const t=`http://tententranslation.com/novel/single?novel=${this.selectednovel}&tier=0&edit=True`;ge().get(t).then((e=>{console.log("Post Novel has recieved data"),this.novelData=e.data["Novel"];const t=e.data["Chapters"].filter((e=>0==e.chapternumber));t.length>0?this.sectionList=t:this.sectionList=[{section:0}],this.chapterList=e.data["Chapters"].filter((e=>0!=e.chapternumber)),this.genres=e.data["Genres"],this.tags=e.data["Tags"],this.currentChapter=null,this.chapterContent="",console.log(this.novelData)})).catch((e=>{console.log(e)})),this.saved=!0,this.hideChapter()},submit(){const e=document.getElementById("loadingscreen");e.style.display="block";const t=document.getElementsByClassName("genrecheckbox");var n=[];console.log(this.novelData.id);for(var l=0;l<t.length;l++)1==t[l].checked&&n.push(t[l].value);this.novelData.novelstatus=document.getElementById("completedEdit").value,this.novelData.description=document.getElementById("noveldescription").innerHTML,this.novelData.title=document.getElementById("noveltitle").innerHTML;const o=`http://tententranslation.com/novel/single?novel=${this.novelData.novelid}`;ge().put(o,{novelData:this.novelData,tags:this.novelData.tags,genres:n}).then((function(t){console.log(t),e.style.display="none"})).catch((function(t){console.log(t),e.style.display="none"}))},showGenres(){var e=document.getElementById("genre-selector");"flex"==e.style.display?e.style.display="none":e.style.display="flex"},showTags(){var e=document.getElementById("tag-selector");"flex"==e.style.display?e.style.display="none":e.style.display="flex"},save(e){"s"!=e.key&&(this.saved=!1),e.ctrlKey&&"s"===e.key&&(this.currentChapter.content=document.getElementById("chapter-content").value,this.currentChapter.title=document.getElementById("chapter-title").innerHTML,this.saved=!0,ge().put(`http://tententranslation.com/chapter?novel=${this.currentChapter.novelid}&chapter=${this.currentChapter.chapternumber}`,{title:this.currentChapter.title,content:this.currentChapter.content}).then((e=>{console.log(this.currentChapter)})).catch((e=>{console.log(e)})))},displayChapter(e){console.log(e),document.getElementById("chapterEditor").style.left="0px",document.getElementById("chapterEditor").style.width="100%",document.getElementById("table").style.width="0px",document.getElementById("chapter-content").addEventListener("keydown",this.save,!1);const t=`http://tententranslation.com/chapter?novel=${e.novelid}&chapter=${e.chapternumber}`;ge().get(t).then((t=>{console.log("Chapter API has recieved data"),this.chapterContent=t.data["content"],this.currentChapter=e,this.chapterTitle=t.data["title"]})).catch((e=>{console.log(e)}))},hideChapter(){if(1==this.saved){var e=document.getElementById("chapterEditor");e.style.left="100%",e.style.width="0px",this.chapterContent="",document.getElementById("table").style.width="100%",document.getElementById("chapter-content").removeEventListener("keyup",this.save)}},chapteredit(e){0==e.chapteredited?e.chapteredited=1:e.chapteredited=0,console.log(e);const t=`http://tententranslation.com/chaptereditchange?edit=${e.chapteredited}&novel=${e.novelid}&chapter=${e.chapterorder}`;ge().put(t).then((e=>{console.log("sent")})).catch((e=>{console.log(e)}))},changeupload(e){const t=document.getElementById("date"+e.chapterorder).value,n=`http://tententranslation.com/chapteruploadchange?novel=${e.novelid}&chapter=${e.chapterorder}`;ge().put(n,{date:t}).then((e=>{console.log("send")})).catch((e=>{console.log(e)}))},uploadchapter(){ge().put(`http://tententranslation.com/uploadchapter?novel=${this.novelData.novelid}`).then((e=>{console.log("send")})).catch((e=>{console.log(e)}))}},created(){ge().get("http://tententranslation.com/noveltitles").then((e=>{console.log("Chapter API has recieved data"),this.novelList=e.data,this.selectNovel(this.novelList[0].novelid)})).catch((e=>{console.log(e)}))},mounted(){}},fe=n(3744);const be=(0,fe.Z)(_e,[["render",pe],["__scopeId","data-v-6a9ead0c"]]);var Ce=be}}]);
//# sourceMappingURL=959.2b263c9b.js.map