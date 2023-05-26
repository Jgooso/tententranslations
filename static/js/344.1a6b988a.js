"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[344],{6393:function(e,t,l){l.d(t,{Z:function(){return u}});var n=l(6252),s=l(3577);const a={id:"genres"},o=["value","name","checked","onClick"];function i(e,t,l,i,d,c){return(0,n.wg)(),(0,n.iD)("div",a,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.genres.length,((e,t)=>((0,n.wg)(),(0,n.iD)("label",{key:t},[(0,n._)("input",{type:"checkbox",value:l.genres[t],name:"genre"+t,class:"genrecheckbox",checked:l.selectedgenres.includes(l.genres[t]),onClick:e=>c.changeGenre(l.genres[t])},null,8,o),(0,n.Uk)((0,s.zw)(l.genres[t]),1)])))),128))])}var d={name:"GenreSelector",props:["genres","selectedgenres"],methods:{changeGenre(e){if(this.selectedgenres.includes(e))for(var t=0;t<this.selectedgenres.length;t++)this.selectedgenres[t]===e&&(this.selectedgenres.splice(t,1),t--);else this.selectedgenres.push(e)}}},c=l(3744);const r=(0,c.Z)(d,[["render",i],["__scopeId","data-v-51abe6a6"]]);var u=r},9524:function(e,t,l){l.d(t,{Z:function(){return x}});var n=l(6252);const s={for:"tagfilter"},a=(0,n.Uk)("Filter "),o={id:"tagList"},i={class:"selectedtaglist"},d={id:"tagselector"},c=["id"],r=["value","name","onChange"],u=["innerHTML"];function g(e,t,l,g,m,v){const p=(0,n.up)("tagBox");return(0,n.wg)(),(0,n.iD)("div",null,[(0,n._)("label",s,[a,(0,n._)("input",{type:"text",id:"tagfilter",onKeyup:t[0]||(t[0]=e=>v.filterTag()),onFocusin:t[1]||(t[1]=e=>v.showtags())},null,32)]),(0,n._)("div",o,[(0,n._)("ul",i,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.selectedtags,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e},[(0,n.Wm)(p,{tag:e,onRemove:v.removeTag},null,8,["tag","onRemove"])])))),128))]),(0,n._)("div",d,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(l.tags.length,(e=>((0,n.wg)(),(0,n.iD)("label",{key:e,class:"tagbutton unselected",id:l.tags[e]},[(0,n._)("input",{type:"checkbox",value:l.tags[e],name:"tag"+e,onChange:t=>v.addTag(l.tags[e])},null,40,r),(0,n._)("p",{innerHTML:l.tags[e]},null,8,u)],8,c)))),128))])])])}const m={class:"tagBox"},v=["innerHTML"];function p(e,t,l,s,a,o){return(0,n.wg)(),(0,n.iD)("div",m,[(0,n._)("p",{innerHTML:l.tag},null,8,v),(0,n._)("button",{onClick:t[0]||(t[0]=e=>o.remove())},"x")])}var y={name:"tagBox",props:["tag"],methods:{remove(){this.$emit("remove",this.tag)}}},h=l(3744);const f=(0,h.Z)(y,[["render",p],["__scopeId","data-v-6f470986"]]);var _=f,w={name:"TagSelector",props:["tags","selectedtags"],components:{tagBox:_},methods:{addTag(e){const t=document.getElementById(e);t.classList.remove("unselected");const l=e.replace(/[0-9]/g,"");this.selectedtags.includes(l)||this.selectedtags.push(l)},removeTag(e){const t=this.selectedtags.indexOf(e);this.selectedtags.splice(t-1,1),document.getElementById(e).classList.add("unselected")},filterTag(){var e,t,l;e=document.getElementById("tagfilter").value.toUpperCase(),t=document.getElementsByClassName("tagbutton");for(var n=0;n<t.length;n++)l=t[n].value||t[n].innerText,l.toUpperCase().indexOf(e)>-1?t[n].style.display="":t[n].style.display="none"},showtags(){document.getElementById("tagselector").style.display="flex"},hidetags(){document.getElementById("tagselector").style.display="none"}}};const b=(0,h.Z)(w,[["render",g],["__scopeId","data-v-5e24f6b4"]]);var x=b},85:function(e,t,l){l.d(t,{Z:function(){return g}});var n=l(6252);const s=e=>((0,n.dD)("data-v-71035fa8"),e=e(),(0,n.Cn)(),e),a={id:"box"},o=["innerHTML"],i=s((()=>(0,n._)("h3",{id:"point",class:"utf-shape"},"◆",-1)));function d(e,t,l,s,d,c){return(0,n.wg)(),(0,n.iD)("div",a,[(0,n._)("h3",{id:"star",class:"utf-shape",innerHTML:l.shape},null,8,o),i])}var c={name:"UtfBox",props:["shape"]},r=l(3744);const u=(0,r.Z)(c,[["render",d],["__scopeId","data-v-71035fa8"]]);var g=u},2344:function(e,t,l){l.r(t),l.d(t,{default:function(){return M}});var n=l(6252);const s=e=>((0,n.dD)("data-v-a061774a"),e=e(),(0,n.Cn)(),e),a={id:"download"},o=s((()=>(0,n._)("h1",{id:"noveltitle"},"Lorem Ipsum",-1))),i={id:"upload",method:"postData"},d={id:"novel-test"},c=(0,n.uE)('<div class="column1 label" data-v-a061774a>Views</div><div class="column2 unselectable" data-v-a061774a>0</div><div class="column1 label" data-v-a061774a>Alternative</div><div class="column2 unselectable" data-v-a061774a>ロレム・イプサム</div><div class="column1 label" data-v-a061774a>Raw</div><div class="column2 info" data-v-a061774a><input type="url" id="urltextbox" name="url" maxlength="34" style="border:none;" placeholder="Enter novel URL" data-v-a061774a></div><div class="column1 label" data-v-a061774a>Author</div><div class="column2 info" data-v-a061774a>Author-san</div><div class="column1 label" data-v-a061774a>Genres</div>',9),r={class:"column2 info"},u={class:"comma-list"},g=["innerHTML"],m=s((()=>(0,n._)("div",{class:"column1 label"},"Tags",-1))),v={class:"column2 info"},p={class:"comma-list"},y=["innerHTML"],h=(0,n.uE)('<div class="column3 label" style="grid-row:1/span 1;" data-v-a061774a>Release</div><div class="column4 unselectable" style="grid-row:1/span 1;" data-v-a061774a>20XX</div><div class="column3 label" style="grid-row:2/span 1;" data-v-a061774a>Status</div><div class="column4 unselectable" style="grid-row:2/span 1;" data-v-a061774a>Unreleased</div><div class="column3 label" style="grid-row:3/span 1;" data-v-a061774a>Novel</div>',5),f=s((()=>(0,n._)("div",{class:"column4 info",style:{"grid-row":"3/span 1"}},[(0,n._)("select",{id:"completedEdit",placeholder:"SELECT",style:{color:"red"},onfocus:'this.style.color="rgb(136,136,136)"',form:"upload",name:"novelstatus"},[(0,n._)("option",{value:"",disabled:"",selected:""},"Select your option"),(0,n._)("option",{value:"Ongoing"},"Ongoing"),(0,n._)("option",{value:"Completed"},"Completed"),(0,n._)("option",{value:"On Hold"},"On Hold"),(0,n._)("option",{value:"Dropped"},"Dropped")])],-1))),_={id:"genre-selector"},w={id:"summary"},b={style:{display:"flex","flex-direction":"row","border-bottom":"2px lightgray solid",height:"30px"}},x=s((()=>(0,n._)("h3",{id:"divider"},"SUMMARY",-1))),k=s((()=>(0,n._)("br",null,null,-1))),D=s((()=>(0,n._)("p",{id:"noveldescription"},"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",-1)));function T(e,t,l,s,T,B){const E=(0,n.up)("TagSelector"),C=(0,n.up)("GenreSelector"),I=(0,n.up)("UtfBox");return(0,n.wg)(),(0,n.iD)("div",a,[o,(0,n._)("form",i,[(0,n._)("div",d,[c,(0,n._)("div",r,[T.selectedgenres.length>0?((0,n.wg)(),(0,n.iD)("div",{key:0,onClick:t[0]||(t[0]=e=>B.showGenres()),class:"info"},[(0,n._)("ul",u,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(T.selectedgenres,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e,innerHTML:e},null,8,g)))),128))])])):((0,n.wg)(),(0,n.iD)("div",{key:1,style:{color:"red"},onClick:t[1]||(t[1]=e=>B.showGenres()),class:"info"},"Select Genres"))]),m,(0,n._)("div",v,[T.selectedtags.length>0?((0,n.wg)(),(0,n.iD)("div",{key:0,onClick:t[2]||(t[2]=e=>B.showTags()),class:"info"},[(0,n._)("ul",p,[((0,n.wg)(!0),(0,n.iD)(n.HY,null,(0,n.Ko)(T.selectedtags,(e=>((0,n.wg)(),(0,n.iD)("li",{key:e,innerHTML:e},null,8,y)))),128))])])):((0,n.wg)(),(0,n.iD)("div",{key:1,style:{color:"red"},onClick:t[3]||(t[3]=e=>B.showTags()),class:"info"},"Select Tags")),(0,n.Wm)(E,{tags:T.tags,selectedtags:T.selectedtags,id:"tag-selector"},null,8,["tags","selectedtags"])]),h,f]),(0,n._)("div",_,[(0,n.Wm)(C,{genres:T.genres,selectedgenres:T.selectedgenres},null,8,["genres","selectedgenres"])])]),(0,n._)("div",w,[(0,n._)("div",null,[(0,n._)("div",b,[(0,n.Wm)(I,{shape:"★"}),x]),k,D])]),(0,n._)("button",{onClick:t[4]||(t[4]=e=>B.postData()),style:{width:"100%","margin-top":"30px"}},"Submit")])}var B=l(9669),E=l.n(B),C=l(6393),I=l(9524),L=l(85),H={data(){return{genres:[],tags:[],selectedtags:[],selectedgenres:[],imageSelected:!0}},components:{GenreSelector:C.Z,TagSelector:I.Z,UtfBox:L.Z},methods:{postData(){const e=document.getElementById("loadingscreen");e.style.display="block";const t=document.getElementById("upload"),l=new FormData(t);try{const e=document.getElementById("image-selector").files[0];l.append("file",e,e.name)}catch{console.log("no file")}E().post("http://tententranslation.com/novel/single",l,{headers:{"Content-Type":"multipart/form-data"}}).then((t=>{console.log(t),e.style.display="none"})).catch((t=>{console.log(t),e.style.display="none"}))},showFile(){const e=document.getElementById("image-selector").files[0];var t=document.getElementById("output");t.src=URL.createObjectURL(e),t.style.display="block",console.log(e),console.log(t.src),this.imageSelected=!0},showGenres(){var e=document.getElementById("genre-selector");document.getElementById("tag-selector").style.display="none","flex"==e.style.display?e.style.display="none":e.style.display="flex"},showTags(){var e=document.getElementById("tag-selector");document.getElementById("genre-selector").style.display="none","flex"==e.style.display?e.style.display="none":e.style.display="flex"}},created(){getAPI.get("http://tententranslation.com/uploaddata").then((e=>{this.genres=e.data["genres"],this.tags=e.data["tags"]})).catch((e=>{console.log(e)}))}},S=l(3744);const U=(0,S.Z)(H,[["render",T],["__scopeId","data-v-a061774a"]]);var M=U}}]);
//# sourceMappingURL=344.1a6b988a.js.map