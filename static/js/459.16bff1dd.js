"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[459],{8514:function(e,t,l){l.d(t,{Z:function(){return g}});var n=l(6252),s=l(3577);const a={id:"genres"},o=["value","name","checked","onClick"];function d(e,t,l,d,i,c){return(0,n.wg)(),(0,n.iD)("div",a,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.genres.length,((e,t)=>((0,n.wg)(),(0,n.iD)("label",{key:t},[(0,n._)("input",{type:"checkbox",value:l.genres[t],name:"genre"+t,class:"genrecheckbox",checked:l.selectedgenres.includes(l.genres[t]),onClick:e=>c.changeGenre(l.genres[t])},null,8,o),(0,n.Uk)((0,s.zw)(l.genres[t]),1)])))),128))])}var i={name:"GenreSelector",props:["genres","selectedgenres"],methods:{changeGenre(e){if(this.selectedgenres.includes(e))for(var t=0;t<this.selectedgenres.length;t++)this.selectedgenres[t]===e&&(this.selectedgenres.splice(t,1),t--);else this.selectedgenres.push(e)}}},c=l(3744);const r=(0,c.Z)(i,[["render",d],["__scopeId","data-v-b6809f84"]]);var g=r},9524:function(e,t,l){l.d(t,{Z:function(){return x}});var n=l(6252);const s={for:"tagfilter"},a=(0,n.Uk)("Filter "),o={id:"tagList"},d={class:"selectedtaglist"},i={id:"tagselector"},c=["id"],r=["value","name","onChange"],g=["innerHTML"];function u(e,t,l,u,v,m){const p=(0,n.up)("tagBox");return(0,n.wg)(),(0,n.iD)("div",null,[(0,n._)("label",s,[a,(0,n._)("input",{type:"text",id:"tagfilter",onKeyup:t[0]||(t[0]=e=>m.filterTag()),onFocusin:t[1]||(t[1]=e=>m.showtags())},null,32)]),(0,n._)("div",o,[(0,n._)("ul",d,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.selectedtags,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e},[(0,n.Wm)(p,{tag:e,onRemove:m.removeTag},null,8,["tag","onRemove"])])))),128))]),(0,n._)("div",i,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.tags.length,(e=>((0,n.wg)(),(0,n.iD)("label",{key:e,class:"tagbutton unselected",id:l.tags[e]},[(0,n._)("input",{type:"checkbox",value:l.tags[e],name:"tag"+e,onChange:t=>m.addTag(l.tags[e])},null,40,r),(0,n._)("p",{innerHTML:l.tags[e]},null,8,g)],8,c)))),128))])])])}const v={class:"tagBox"},m=["innerHTML"];function p(e,t,l,s,a,o){return(0,n.wg)(),(0,n.iD)("div",v,[(0,n._)("p",{innerHTML:l.tag},null,8,m),(0,n._)("button",{onClick:t[0]||(t[0]=e=>o.remove())},"x")])}var f={name:"tagBox",props:["tag"],methods:{remove(){this.$emit("remove",this.tag)}}},y=l(3744);const h=(0,y.Z)(f,[["render",p],["__scopeId","data-v-6f470986"]]);var b=h,_={name:"TagSelector",props:["tags","selectedtags"],components:{tagBox:b},methods:{addTag(e){const t=document.getElementById(e);t.classList.remove("unselected");const l=e.replace(/[0-9]/g,"");this.selectedtags.includes(l)||this.selectedtags.push(l)},removeTag(e){const t=this.selectedtags.indexOf(e);this.selectedtags.splice(t-1,1),document.getElementById(e).classList.add("unselected")},filterTag(){var e,t,l;e=document.getElementById("tagfilter").value.toUpperCase(),t=document.getElementsByClassName("tagbutton");for(var n=0;n<t.length;n++)l=t[n].value||t[n].innerText,l.toUpperCase().indexOf(e)>-1?t[n].style.display="":t[n].style.display="none"},showtags(){document.getElementById("tagselector").style.display="flex"},hidetags(){document.getElementById("tagselector").style.display="none"}}};const w=(0,y.Z)(_,[["render",u],["__scopeId","data-v-5e24f6b4"]]);var x=w},881:function(e,t,l){l.d(t,{Z:function(){return u}});var n=l(6252);const s=e=>((0,n.dD)("data-v-3eb7aad7"),e=e(),(0,n.Cn)(),e),a={id:"box"},o=["innerHTML"],d=s((()=>(0,n._)("h3",{id:"point"},"◆",-1)));function i(e,t,l,s,i,c){return(0,n.wg)(),(0,n.iD)("div",a,[(0,n._)("h3",{id:"star",innerHTML:l.shape},null,8,o),d])}var c={name:"UtfBox",props:["shape"]},r=l(3744);const g=(0,r.Z)(c,[["render",i],["__scopeId","data-v-3eb7aad7"]]);var u=g},2459:function(e,t,l){l.r(t),l.d(t,{default:function(){return U}});var n=l(6252);const s=e=>((0,n.dD)("data-v-fcfb2dc8"),e=e(),(0,n.Cn)(),e),a={id:"download"},o=s((()=>(0,n._)("h1",{id:"noveltitle"},"Lorem Ipsum",-1))),d={id:"upload",method:"postData"},i={id:"novel-test"},c=(0,n.uE)('<div class="column1 label" data-v-fcfb2dc8>Views</div><div class="column2 unselectable" data-v-fcfb2dc8>0</div><div class="column1 label" data-v-fcfb2dc8>Alternative</div><div class="column2 unselectable" data-v-fcfb2dc8>ロレム・イプサム</div><div class="column1 label" data-v-fcfb2dc8>Raw</div><div class="column2 info" data-v-fcfb2dc8><input type="url" id="urltextbox" name="url" maxlength="34" style="border:none;" placeholder="Enter novel URL" data-v-fcfb2dc8></div><div class="column1 label" data-v-fcfb2dc8>Author</div><div class="column2 info" data-v-fcfb2dc8>Author-san</div><div class="column1 label" data-v-fcfb2dc8>Genres</div>',9),r={class:"column2 info"},g={class:"comma-list"},u=["innerHTML"],v=s((()=>(0,n._)("div",{class:"column1 label"},"Tags",-1))),m={class:"column2 info"},p={class:"comma-list"},f=["innerHTML"],y=(0,n.uE)('<div class="column3 label" style="grid-row:1/span 1;" data-v-fcfb2dc8>Release</div><div class="column4 unselectable" style="grid-row:1/span 1;" data-v-fcfb2dc8>20XX</div><div class="column3 label" style="grid-row:2/span 1;" data-v-fcfb2dc8>Status</div><div class="column4 unselectable" style="grid-row:2/span 1;" data-v-fcfb2dc8>Unreleased</div><div class="column3 label" style="grid-row:3/span 1;" data-v-fcfb2dc8>Novel</div>',5),h=s((()=>(0,n._)("div",{class:"column4 info",style:{"grid-row":"3/span 1"}},[(0,n._)("select",{id:"completedEdit",placeholder:"SELECT",style:{color:"red"},onfocus:'this.style.color="rgb(136,136,136)"',form:"upload",name:"novelstatus"},[(0,n._)("option",{value:"",disabled:"",selected:""},"Select your option"),(0,n._)("option",{value:"Ongoing"},"Ongoing"),(0,n._)("option",{value:"Completed"},"Completed"),(0,n._)("option",{value:"On Hold"},"On Hold"),(0,n._)("option",{value:"Dropped"},"Dropped")])],-1))),b={id:"genre-selector"},_={id:"summary"},w={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},x=s((()=>(0,n._)("h3",{id:"divider"},"SUMMARY",-1))),k=s((()=>(0,n._)("br",null,null,-1))),D=s((()=>(0,n._)("p",{id:"noveldescription"},"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",-1)));function T(e,t,l,s,T,B){const E=(0,n.up)("TagSelector"),C=(0,n.up)("GenreSelector"),I=(0,n.up)("UtfBox");return(0,n.wg)(),(0,n.iD)("div",a,[o,(0,n._)("form",d,[(0,n._)("div",i,[c,(0,n._)("div",r,[T.selectedgenres.length>0?((0,n.wg)(),(0,n.iD)("div",{key:0,onClick:t[0]||(t[0]=e=>B.showGenres()),class:"info"},[(0,n._)("ul",g,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(T.selectedgenres,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e,innerHTML:e},null,8,u)))),128))])])):((0,n.wg)(),(0,n.iD)("div",{key:1,style:{color:"red"},onClick:t[1]||(t[1]=e=>B.showGenres()),class:"info"},"Select Genres"))]),v,(0,n._)("div",m,[T.selectedtags.length>0?((0,n.wg)(),(0,n.iD)("div",{key:0,onClick:t[2]||(t[2]=e=>B.showTags()),class:"info"},[(0,n._)("ul",p,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(T.selectedtags,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e,innerHTML:e},null,8,f)))),128))])])):((0,n.wg)(),(0,n.iD)("div",{key:1,style:{color:"red"},onClick:t[3]||(t[3]=e=>B.showTags()),class:"info"},"Select Tags")),(0,n.Wm)(E,{tags:T.tags,selectedtags:T.selectedtags,id:"tag-selector"},null,8,["tags","selectedtags"])]),y,h]),(0,n._)("div",b,[(0,n.Wm)(C,{genres:T.genres,selectedgenres:T.selectedgenres},null,8,["genres","selectedgenres"])])]),(0,n._)("div",_,[(0,n._)("div",null,[(0,n._)("div",w,[(0,n.Wm)(I,{shape:"★"}),x]),k,D])]),(0,n._)("button",{onClick:t[4]||(t[4]=e=>B.postData()),style:{width:"100%","margin-top":"30px"}},"Submit")])}var B=l(5992),E=l(8514),C=l(9524),I=l(881),L={data(){return{genres:[],tags:[],selectedtags:[],selectedgenres:[],imageSelected:!0}},components:{GenreSelector:E.Z,TagSelector:C.Z,UtfBox:I.Z},methods:{postData(){const e=document.getElementById("loadingscreen");e.style.display="block";const t=document.getElementById("upload"),l=new FormData(t);try{const e=document.getElementById("image-selector").files[0];l.append("file",e,e.name)}catch{console.log("no file")}B.K.post("/novel/single",l,{headers:{"Content-Type":"multipart/form-data"}}).then((t=>{console.log(t),e.style.display="none"})).catch((t=>{console.log(t),e.style.display="none"}))},showFile(){const e=document.getElementById("image-selector").files[0];var t=document.getElementById("output");t.src=URL.createObjectURL(e),t.style.display="block",console.log(e),console.log(t.src),this.imageSelected=!0},showGenres(){var e=document.getElementById("genre-selector");document.getElementById("tag-selector").style.display="none","flex"==e.style.display?e.style.display="none":e.style.display="flex"},showTags(){var e=document.getElementById("tag-selector");document.getElementById("genre-selector").style.display="none","flex"==e.style.display?e.style.display="none":e.style.display="flex"}},created(){B.K.get("/uploaddata").then((e=>{this.genres=e.data["genres"],this.tags=e.data["tags"]})).catch((e=>{console.log(e)}))}},H=l(3744);const S=(0,H.Z)(L,[["render",T],["__scopeId","data-v-fcfb2dc8"]]);var U=S}}]);
//# sourceMappingURL=459.16bff1dd.js.map