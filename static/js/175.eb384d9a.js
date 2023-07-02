"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[175],{6393:function(e,t,n){n.d(t,{Z:function(){return h}});var l=n(6252),o=n(3577);const a={id:"genres"},s=["value","name","checked","onClick"];function i(e,t,n,i,c,r){return(0,l.wg)(),(0,l.iD)("div",a,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.genres.length,((e,t)=>((0,l.wg)(),(0,l.iD)("label",{key:t},[(0,l._)("input",{type:"checkbox",value:n.genres[t],name:"genre"+t,class:"genrecheckbox",checked:n.selectedgenres.includes(n.genres[t]),onClick:e=>r.changeGenre(n.genres[t])},null,8,s),(0,l.Uk)((0,o.zw)(n.genres[t]),1)])))),128))])}var c={name:"GenreSelector",props:["genres","selectedgenres"],methods:{changeGenre(e){if(this.selectedgenres.includes(e))for(var t=0;t<this.selectedgenres.length;t++)this.selectedgenres[t]===e&&(this.selectedgenres.splice(t,1),t--);else this.selectedgenres.push(e)}}},r=n(3744);const d=(0,r.Z)(c,[["render",i],["__scopeId","data-v-51abe6a6"]]);var h=d},9524:function(e,t,n){n.d(t,{Z:function(){return D}});var l=n(6252);const o={for:"tagfilter"},a=(0,l.Uk)("Filter "),s={id:"tagList"},i={class:"selectedtaglist"},c={id:"tagselector"},r=["id"],d=["value","name","onChange"],h=["innerHTML"];function u(e,t,n,u,p,g){const v=(0,l.up)("tagBox");return(0,l.wg)(),(0,l.iD)("div",null,[(0,l._)("label",o,[a,(0,l._)("input",{type:"text",id:"tagfilter",onKeyup:t[0]||(t[0]=e=>g.filterTag()),onFocusin:t[1]||(t[1]=e=>g.showtags())},null,32)]),(0,l._)("div",s,[(0,l._)("ul",i,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.selectedtags,(e=>((0,l.wg)(),(0,l.iD)("li",{key:e},[(0,l.Wm)(v,{tag:e,onRemove:g.removeTag},null,8,["tag","onRemove"])])))),128))]),(0,l._)("div",c,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(n.tags.length,(e=>((0,l.wg)(),(0,l.iD)("label",{key:e,class:"tagbutton unselected",id:n.tags[e]},[(0,l._)("input",{type:"checkbox",value:n.tags[e],name:"tag"+e,onChange:t=>g.addTag(n.tags[e])},null,40,d),(0,l._)("p",{innerHTML:n.tags[e]},null,8,h)],8,r)))),128))])])])}const p={class:"tagBox"},g=["innerHTML"];function v(e,t,n,o,a,s){return(0,l.wg)(),(0,l.iD)("div",p,[(0,l._)("p",{innerHTML:n.tag},null,8,g),(0,l._)("button",{onClick:t[0]||(t[0]=e=>s.remove())},"x")])}var m={name:"tagBox",props:["tag"],methods:{remove(){this.$emit("remove",this.tag)}}},y=n(3744);const _=(0,y.Z)(m,[["render",v],["__scopeId","data-v-6f470986"]]);var f=_,b={name:"TagSelector",props:["tags","selectedtags"],components:{tagBox:f},methods:{addTag(e){const t=document.getElementById(e);t.classList.remove("unselected");const n=e.replace(/[0-9]/g,"");this.selectedtags.includes(n)||this.selectedtags.push(n)},removeTag(e){const t=this.selectedtags.indexOf(e);this.selectedtags.splice(t-1,1),document.getElementById(e).classList.add("unselected")},filterTag(){var e,t,n;e=document.getElementById("tagfilter").value.toUpperCase(),t=document.getElementsByClassName("tagbutton");for(var l=0;l<t.length;l++)n=t[l].value||t[l].innerText,n.toUpperCase().indexOf(e)>-1?t[l].style.display="":t[l].style.display="none"},showtags(){document.getElementById("tagselector").style.display="flex"},hidetags(){document.getElementById("tagselector").style.display="none"}}};const C=(0,y.Z)(b,[["render",u],["__scopeId","data-v-5e24f6b4"]]);var D=C},85:function(e,t,n){n.d(t,{Z:function(){return u}});var l=n(6252);const o=e=>((0,l.dD)("data-v-71035fa8"),e=e(),(0,l.Cn)(),e),a={id:"box"},s=["innerHTML"],i=o((()=>(0,l._)("h3",{id:"point",class:"utf-shape"},"◆",-1)));function c(e,t,n,o,c,r){return(0,l.wg)(),(0,l.iD)("div",a,[(0,l._)("h3",{id:"star",class:"utf-shape",innerHTML:n.shape},null,8,s),i])}var r={name:"UtfBox",props:["shape"]},d=n(3744);const h=(0,d.Z)(r,[["render",c],["__scopeId","data-v-71035fa8"]]);var u=h},4175:function(e,t,n){n.r(t),n.d(t,{default:function(){return ke}});var l=n(6252),o=n(3577);const a=e=>((0,l.dD)("data-v-6ba52c29"),e=e(),(0,l.Cn)(),e),s={id:"editPage"},i={id:"confirmationBox"},c={style:{margin:"auto"}},r={style:{display:"flex","flex-direction":"row",margin:"auto",width:"220px"}},d=["value"],h={id:"cover",ref:"cover"},u={key:0},p=["textContent"],g={id:"inner"},v={id:"novel-information"},m={id:"data"},y=a((()=>(0,l._)("td",null,"Author",-1))),_={class:"info"},f=a((()=>(0,l._)("td",null,"URL",-1))),b={class:"info"},C=["href"],D=a((()=>(0,l._)("td",null,"Genres",-1))),k={class:"category"},w=a((()=>(0,l._)("td",null,"Tags",-1))),x={class:"category"},E=a((()=>(0,l._)("td",null,"Release Date",-1))),T={class:"info",contenteditable:"true",id:"releaseDate"},B=a((()=>(0,l._)("td",null,"Raw Status",-1))),L={class:"info"},I=["selected"],H=a((()=>(0,l._)("option",{value:"Ongoing"},"Ongoing",-1))),$=a((()=>(0,l._)("option",{value:"Completed"},"Completed",-1))),z=a((()=>(0,l._)("option",{value:"On Hold"},"On Hold",-1))),M=a((()=>(0,l._)("option",{value:"Dropped"},"Dropped",-1))),U=[H,$,z,M],S=a((()=>(0,l._)("td",null,"Novel Active",-1))),N={id:"genre-selector"},Z=a((()=>(0,l._)("button",{style:{"background-color":"red","font-weight":"bold"}},"DELETE",-1))),G={id:"summary"},A={key:0},K={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},O=a((()=>(0,l._)("h3",{id:"divider"},"SUMMARY",-1))),R=a((()=>(0,l._)("br",null,null,-1))),Y=["innerHTML"],P={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},W=a((()=>(0,l._)("h3",{id:"divider"},"CHAPTERS",-1))),q=a((()=>(0,l._)("br",null,null,-1))),F={id:"TableOfContents"},X={id:"table",ref:"tableofcontentlist"},j=a((()=>(0,l._)("tr",{class:"table-list"},[(0,l._)("td",{class:"chapter-title"},"Chapter Title"),(0,l._)("td",{class:"chapter-check-box",style:{"font-size":"15px"}},"Edited"),(0,l._)("td",{class:"chapter-check-box",style:{"font-size":"15px"}},"Uploaded"),(0,l._)("td",{style:{"font-size":"15px"}},"Upload Date")],-1))),J={style:{display:"flex","flex-direction":"column"}},Q=["innerHTML","id"],V={style:{width:"100%"}},ee=["id"],te={class:"chapter-title"},ne=["value","onClick"],le=["onClick"],oe=["onClick"],ae={key:2,style:{color:"lightgreen"},class:"chapter-check-box"},se={key:3,style:{color:"red"},class:"chapter-check-box"},ie=["id","value","onChange"],ce={id:"chapterEditor"},re={key:0},de=(0,l.Uk)("← "),he={key:1},ue={contenteditable:"True",id:"chapter-title"},pe=["textContent"];function ge(e,t,n,a,H,$){const z=(0,l.up)("GenreSelector"),M=(0,l.up)("TagSelector"),ge=(0,l.up)("UtfBox");return(0,l.wg)(),(0,l.iD)("div",s,[(0,l._)("div",i,[(0,l._)("h1",c,(0,o.zw)(0==H.novelData.novelactive?"Confirm Activate Novel":"Confirm Deactivate Novel"),1),(0,l._)("div",r,[(0,l._)("button",{onClick:t[0]||(t[0]=e=>$.confirm(2)),class:"confirmation-button"},"Confirm"),(0,l._)("button",{onClick:t[1]||(t[1]=e=>$.confirm(1)),class:"confirmation-button"},"Cancel")])]),(0,l._)("select",{id:"novel-selector",onChange:t[2]||(t[2]=e=>$.selectNovel())},[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(H.novelList,(e=>((0,l.wg)(),(0,l.iD)("option",{value:e.novelid},(0,o.zw)(e.title)+" "+(0,o.zw)(100*e.completed_percentage)+"%",9,d)))),256))],32),(0,l._)("div",h,[H.novelData.title?((0,l.wg)(),(0,l.iD)("div",u,[(0,l._)("p",{id:"noveltitle",textContent:(0,o.zw)(H.novelData.title),contenteditable:"true"},null,8,p),(0,l._)("div",g,[(0,l._)("div",v,[(0,l._)("div",m,[(0,l._)("table",null,[(0,l._)("tr",null,[y,(0,l._)("td",_,(0,o.zw)(H.novelData.author),1)]),(0,l._)("tr",null,[f,(0,l._)("td",b,[(0,l._)("a",{href:H.novelData.url,class:"selectable"},(0,o.zw)(H.novelData.url),9,C)])]),(0,l._)("tr",null,[D,(0,l._)("td",k,[(0,l._)("button",{class:"show",onClick:t[3]||(t[3]=e=>$.showGenres())},"Show")])]),(0,l._)("tr",null,[w,(0,l._)("td",x,[(0,l._)("button",{class:"show",onClick:t[4]||(t[4]=e=>$.showTags())},"Show")])])]),(0,l._)("table",null,[(0,l._)("tr",null,[E,(0,l._)("td",T,(0,o.zw)(H.novelData.novelrelease),1)]),(0,l._)("tr",null,[B,(0,l._)("td",L,[(0,l._)("select",{id:"completedEdit",selected:e.value=H.novelData.novelstatus},U,8,I)])]),(0,l._)("tr",null,[S,(0,l._)("td",null,[(0,l._)("button",{onClick:t[5]||(t[5]=e=>$.confirm(0))},(0,o.zw)(0==H.novelData.novelactive?"Activate Novel":"Deactivate Novel"),1)])])])]),(0,l._)("div",N,[(0,l.Wm)(z,{genres:H.genres,selectedgenres:H.novelData.genres},null,8,["genres","selectedgenres"])]),(0,l.Wm)(M,{tags:H.tags,selectedtags:H.novelData.tags,id:"tag-selector"},null,8,["tags","selectedtags"])]),Z]),(0,l._)("button",{onClick:t[6]||(t[6]=e=>$.uploadchapter()),id:"upload-button"},"Upload chapter"),(0,l._)("button",{onClick:t[7]||(t[7]=e=>$.resetschedule()),id:"reset-button"},"Reset Schedule"),(0,l._)("div",G,[H.novelData.title?((0,l.wg)(),(0,l.iD)("div",A,[(0,l._)("div",K,[(0,l.Wm)(ge,{shape:"★"}),O]),R,(0,l._)("p",{id:"noveldescription",innerHTML:H.novelData.description,contenteditable:"true"},null,8,Y)])):(0,l.kq)("",!0)]),(0,l._)("div",P,[(0,l.Wm)(ge,{shape:"★"}),W]),q,(0,l._)("div",F,[(0,l._)("table",X,[j,((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(H.sectionList,(e=>((0,l.wg)(),(0,l.iD)("tr",J,[e.title?((0,l.wg)(),(0,l.iD)("p",{key:0,class:"section",innerHTML:e.title,id:"section"+e.section,contenteditable:"True"},null,8,Q)):(0,l.kq)("",!0),(0,l._)("tr",V,[((0,l.wg)(!0),(0,l.iD)(l.HY,null,(0,l.Ko)(H.chapterList.filter((t=>t.section==e.section)),(e=>((0,l.wg)(),(0,l.iD)("tr",{key:e.chapternumber,class:"table-list",id:"chapter"+e.chapternumber},[(0,l._)("td",te,[(0,l._)("label",null,[(0,l.Uk)((0,o.zw)(e.title)+" ",1),(0,l._)("input",{type:"button",class:"chapter-list",value:e.chapternumber,onClick:t=>$.displayChapter(e)},null,8,ne)])]),1==e.chapteredited?((0,l.wg)(),(0,l.iD)("td",{key:0,style:{color:"lightgreen"},class:"chapter-check-box edited-check",onClick:t=>$.chapteredit(e)},"✓",8,le)):((0,l.wg)(),(0,l.iD)("td",{key:1,style:{color:"red"},class:"chapter-check-box edited-check",onClick:t=>$.chapteredit(e)},"X",8,oe)),1==e.chapteractive?((0,l.wg)(),(0,l.iD)("td",ae,"✓")):((0,l.wg)(),(0,l.iD)("td",se,"X")),(0,l._)("td",null,[(0,l._)("input",{type:"datetime-local",id:"date"+e.chapterorder,value:e.uploaddate,onChange:t=>$.changeupload(e),min:"2023-01-01T00:00",style:{width:"fit-content","margin-right":"20px"}},null,40,ie)])],8,ee)))),128))])])))),256))],512),(0,l._)("div",ce,[H.saved?((0,l.wg)(),(0,l.iD)("label",re,[de,(0,l._)("input",{type:"button",id:"back-button",onClick:t[8]||(t[8]=e=>$.hideChapter())})])):((0,l.wg)(),(0,l.iD)("p",he," Unsaved Changes")),(0,l._)("h3",ue,(0,o.zw)(H.chapterTitle),1),(0,l._)("textarea",{textContent:(0,o.zw)(H.chapterContent),id:"chapter-content"},null,8,pe)])])])):(0,l.kq)("",!0)],512),(0,l._)("button",{onClick:t[9]||(t[9]=e=>$.submit())},"Submit")])}var ve=n(9669),me=n.n(ve),ye=n(6393),_e=n(9524),fe=n(85),be={data(){return{selectednovel:"",novelList:[],novelData:[],tags:[],genres:[],chapterList:[],sectionList:[],chapterContent:"",currentChapter:"",saved:"",chapterTitle:""}},components:{GenreSelector:ye.Z,TagSelector:_e.Z,UtfBox:fe.Z},methods:{confirm(e){var t=document.getElementById("confirmationBox");0==e?t.style.display="flex":1==e?t.style.display="none":2==e&&(1==this.novelData.novelactive?this.novelData.novelactive=0:this.novelData.novelactive=1,t.style.display="none",me().put(`http://tententranslation.com/activatenovel?novel=${this.novelData.novelid}'&active=${this.novelData.novelactive}`).then((e=>{console.log("sent")})).catch((e=>{console.log(e)})))},selectNovel(e){this.selectednovel=e||document.getElementById("novel-selector").value;const t=`http://tententranslation.com/novel/single?novel=${this.selectednovel}&tier=0&edit=True`;me().get(t).then((e=>{console.log("Post Novel has recieved data"),this.novelData=e.data["Novel"];const t=e.data["Chapters"].filter((e=>0==e.chapternumber));t.length>0?this.sectionList=t:this.sectionList=[{section:0}],this.chapterList=e.data["Chapters"].filter((e=>0!=e.chapternumber)),this.genres=e.data["Genres"],this.tags=e.data["Tags"],this.currentChapter=null,this.chapterContent="",console.log(this.novelData)})).catch((e=>{console.log(e)})),this.saved=!0,this.hideChapter()},submit(){const e=document.getElementById("loadingscreen");e.style.display="block";const t=document.getElementsByClassName("genrecheckbox");var n=[];console.log(this.novelData.id);for(var l=0;l<t.length;l++)1==t[l].checked&&n.push(t[l].value);this.novelData.novelstatus=document.getElementById("completedEdit").value,this.novelData.description=document.getElementById("noveldescription").innerHTML,this.novelData.title=document.getElementById("noveltitle").innerHTML,this.novelData.novelrelease=document.getElementById("releaseDate").innerHTML;const o=`http://tententranslation.com/novel/single?novel=${this.novelData.novelid}`;me().put(o,{novelData:this.novelData,tags:this.novelData.tags,genres:n}).then((function(t){console.log(t),e.style.display="none"})).catch((function(t){console.log(t),e.style.display="none"}))},showGenres(){var e=document.getElementById("genre-selector");"flex"==e.style.display?e.style.display="none":e.style.display="flex"},showTags(){var e=document.getElementById("tag-selector");"flex"==e.style.display?e.style.display="none":e.style.display="flex"},save(e){"s"!=e.key&&(this.saved=!1),e.ctrlKey&&"s"===e.key&&(this.currentChapter.content=document.getElementById("chapter-content").value,this.currentChapter.title=document.getElementById("chapter-title").innerHTML,this.saved=!0,me().put(`http://tententranslation.com/chapter?novel=${this.currentChapter.novelid}&chapter=${this.currentChapter.chapternumber}`,{title:this.currentChapter.title,content:this.currentChapter.content}).then((e=>{console.log(this.currentChapter)})).catch((e=>{console.log(e)})))},displayChapter(e){console.log(e),document.getElementById("chapterEditor").style.left="0px",document.getElementById("chapterEditor").style.width="100%",document.getElementById("table").style.width="0px",document.getElementById("chapter-content").addEventListener("keydown",this.save,!1);const t=`http://tententranslation.com/chapter?novel=${e.novelid}&chapter=${e.chapternumber}`;me().get(t).then((t=>{console.log("Chapter API has recieved data"),this.chapterContent=t.data["content"],this.currentChapter=e,this.chapterTitle=t.data["title"]})).catch((e=>{console.log(e)}))},hideChapter(){if(1==this.saved){var e=document.getElementById("chapterEditor");e.style.left="100%",e.style.width="0px",this.chapterContent="",document.getElementById("table").style.width="100%",document.getElementById("chapter-content").removeEventListener("keyup",this.save)}},chapteredit(e){0==e.chapteredited?e.chapteredited=1:e.chapteredited=0,console.log(e);const t=`http://tententranslation.com/chaptereditchange?edit=${e.chapteredited}&novel=${e.novelid}&chapter=${e.chapterorder}`;me().put(t).then((e=>{console.log("sent")})).catch((e=>{console.log(e)}))},changeupload(e){const t=document.getElementById("date"+e.chapterorder).value,n=`http://tententranslation.com/chapteruploadchange?offset=${timezoneOffset}&novel=${e.novelid}&chapter=${e.chapterorder}`;me().put(n,{date:t}).then((e=>{console.log("send")})).catch((e=>{console.log(e)}))},uploadchapter(){me().put(`http://tententranslation.com/uploadchapter?novel=${this.novelData.novelid}`).then((e=>{console.log("send")})).catch((e=>{console.log(e)}))},resetschedule(){me().put(`http://tententranslation.com/resetschedule?novel=${this.novelData.novelid}`).then((e=>{console.log("send")})).catch((e=>{console.log(e)}))}},created(){me().get("http://tententranslation.com/noveltitles").then((e=>{console.log("Chapter API has recieved data"),this.novelList=e.data,this.selectNovel(this.novelList[0].novelid)})).catch((e=>{console.log(e)}))},mounted(){}},Ce=n(3744);const De=(0,Ce.Z)(be,[["render",ge],["__scopeId","data-v-6ba52c29"]]);var ke=De}}]);
//# sourceMappingURL=175.eb384d9a.js.map