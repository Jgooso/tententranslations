(function(){"use strict";var e={5992:function(e,t,n){n.d(t,{K:function(){return r}});var o=n(9669),a=n.n(o);const r=a().create({baseURL:"127.0.0.1:5000"})},1829:function(e,t,n){var o=n(9963),a=n(6252);const r={id:"app"},i=(0,a._)("div",{class:"view-border-one bord"},null,-1),s=(0,a._)("div",{class:"view-border-two bord"},null,-1);function d(e,t,n,o,d,u){const c=(0,a.up)("sidebar"),l=(0,a.up)("SignIn"),f=(0,a.up)("Header"),m=(0,a.up)("router-view"),p=(0,a.up)("Footer");return(0,a.wg)(),(0,a.iD)("div",r,[(0,a.Wm)(c,{ref:"sidemenu",onChangesidebar:t[0]||(t[0]=e=>u.changesidebar()),onClosesignin:t[1]||(t[1]=e=>u.close_signin())},null,512),(0,a.Wm)(l,{ref:"signin"},null,512),(0,a.Wm)(f,{ref:"header",onChangesidebar:t[2]||(t[2]=e=>u.changesidebar()),onSignin:t[3]||(t[3]=e=>u.open_signin()),onSignup:t[4]||(t[4]=e=>u.signup()),status:d.user.status,class:"view-header"},null,8,["status"]),i,(0,a.Wm)(m,{tier:d.user.tier,class:"view-content",onSwitchmode:t[5]||(t[5]=e=>u.switchdarkmode())},null,8,["tier"]),s,(0,a.Wm)(p,{class:"view-footer"})])}const u=e=>((0,a.dD)("data-v-14317c66"),e=e(),(0,a.Cn)(),e),c={id:"header-top"},l=(0,a.Uk)("TenTenTranslations"),f={id:"header-navigation"},m=(0,a.Uk)("Browse"),p=(0,a.Uk)("About"),b=(0,a.Uk)("Contact"),h=(0,a.Uk)("Manage"),g=u((()=>(0,a._)("div",{class:"menu-btn__burger"},null,-1))),v=[g];function y(e,t,n,o,r,i){const s=(0,a.up)("router-link"),d=(0,a.up)("KoFiButton");return(0,a.wg)(),(0,a.iD)("header",null,[(0,a._)("div",c,[(0,a.Wm)(s,{to:{name:"homePage"},id:"home-button"},{default:(0,a.w5)((()=>[l])),_:1}),(0,a._)("div",f,[(0,a.Wm)(s,{to:{name:"Browse"},class:"nav",style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[m])),_:1}),(0,a.Wm)(s,{to:{name:"aboutPage"},class:"nav",style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[p])),_:1}),(0,a.Wm)(s,{to:{name:"contactPage"},class:"nav",style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[b])),_:1}),n.status.includes("Moderator")?((0,a.wg)(),(0,a.j4)(s,{key:0,to:{name:"uploadPage"},class:"nav"},{default:(0,a.w5)((()=>[h])),_:1})):((0,a.wg)(),(0,a.j4)(d,{key:1,id:"KoFi"})),(0,a._)("div",{class:"menu-btn",onClick:t[0]||(t[0]=t=>e.$emit("changesidebar")),ref:"menubutton"},v,512)])])])}var w=n(2311),k={name:"Header",props:{status:String},components:{KoFiButton:w.Z}},P=n(3744);const A=(0,P.Z)(k,[["render",y],["__scopeId","data-v-14317c66"]]);var O=A;const x=e=>((0,a.dD)("data-v-67ff1177"),e=e(),(0,a.Cn)(),e),H={id:"footer"},C={id:"navigation"},W=(0,a.Uk)("About"),j=x((()=>(0,a._)("p",{style:{"font-size":"15px"}},"|",-1))),X=(0,a.Uk)("Contact"),E=x((()=>(0,a._)("br",null,null,-1)));function Z(e,t,n,o,r,i){const s=(0,a.up)("router-link");return(0,a.wg)(),(0,a.iD)("footer",H,[(0,a._)("div",C,[(0,a.Wm)(s,{to:{name:"aboutPage"},class:"footer-nav"},{default:(0,a.w5)((()=>[W])),_:1}),j,(0,a.Wm)(s,{to:{name:"contactPage"},class:"footer-nav"},{default:(0,a.w5)((()=>[X])),_:1})]),E])}var G={name:"Footer"};const I=(0,P.Z)(G,[["render",Z],["__scopeId","data-v-67ff1177"]]);var U=I;const B={id:"sidemenu"},F={id:"sidebar",ref:"sidebar"},L=(0,a.Uk)("Browse"),K=(0,a.Uk)("About"),z=(0,a.Uk)("Contact");function Q(e,t,n,o,r,i){const s=(0,a.up)("router-link"),d=(0,a.up)("KoFiButton");return(0,a.wg)(),(0,a.iD)("div",B,[(0,a._)("div",F,[(0,a._)("h3",{onClick:t[0]||(t[0]=e=>i.swap())},"╳"),(0,a.Wm)(s,{to:{name:"Browse"},class:"nav",onClick:t[1]||(t[1]=e=>i.swap()),style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[L])),_:1}),(0,a.Wm)(s,{to:{name:"aboutPage"},class:"nav",onClick:t[2]||(t[2]=e=>i.swap()),style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[K])),_:1}),(0,a.Wm)(s,{to:{name:"contactPage"},class:"nav",onClick:t[3]||(t[3]=e=>i.swap()),style:{"text-decoration":"none"}},{default:(0,a.w5)((()=>[z])),_:1}),(0,a.Wm)(d,{class:"nav",id:"KoFi"})],512),(0,a._)("div",{id:"shade",onClick:t[4]||(t[4]=e=>i.swap()),ref:"shade"},null,512)])}var D={name:"sidebar",components:{KoFiButton:w.Z},methods:{swap(){this.$emit("changesidebar")}}};const T=(0,P.Z)(D,[["render",Q],["__scopeId","data-v-399e3934"]]);var N=T;const Y=e=>((0,a.dD)("data-v-1eb79b86"),e=e(),(0,a.Cn)(),e),M={id:"signin",ref:"signin"},q={id:"sign-in-card"},R=Y((()=>(0,a._)("p",{id:"error-message"},null,-1))),S=(0,a.uE)('<form data-v-1eb79b86><label for="username" data-v-1eb79b86>Username:</label><br data-v-1eb79b86><input type="text" id="username" name="username" data-v-1eb79b86><br data-v-1eb79b86><label for="email" data-v-1eb79b86>Email:</label><br data-v-1eb79b86><input type="email" data-v-1eb79b86><br data-v-1eb79b86><label for="password" data-v-1eb79b86>Password:</label><br data-v-1eb79b86><input type="password" data-v-1eb79b86><br data-v-1eb79b86><br data-v-1eb79b86><div data-v-1eb79b86><input type="submit" value="Log In" data-v-1eb79b86><input type="checkbox" name="remember" data-v-1eb79b86><label for="checkbox" data-v-1eb79b86>Remember Me</label></div></form>',1);function J(e,t,n,o,r,i){return(0,a.wg)(),(0,a.iD)("div",M,[(0,a._)("div",q,[R,(0,a._)("button",{onClick:t[0]||(t[0]=t=>e.$emit("closesignin"))},"X"),S])],512)}n(5992);var V={name:"SignIn",methods:{submit(){}}};const _=(0,P.Z)(V,[["render",J],["__scopeId","data-v-1eb79b86"]]);var $=_,ee={name:"App",components:{Header:O,Footer:U,sidebar:N,SignIn:$},data(){return{darkmode:"true"===$cookies.get("darkmode"),testing:[],user:[],url:"http://ipinfo.io/json",status:1}},methods:{changesidebar(){const e=this.$refs.header.$refs.menubutton;"0px"==this.$refs.sidemenu.$refs.sidebar.style.left?(this.$refs.sidemenu.$refs.sidebar.style.left="-300px",this.$refs.sidemenu.$refs.shade.style.opacity="0",e.classList.remove("open")):(this.$refs.sidemenu.$refs.sidebar.style.left="0px",this.$refs.sidemenu.$refs.shade.style.opacity="0.5",e.classList.add("open"))},open_signin(){this.switchdarkmode()},close_signin(){this.$refs.signin.$refs.signin.style.display="none"},signup(){this.$refs.signin.$refs.signin.style.display="block"},setdarkmode(){var e=document.querySelector(":root");this.darkmode?(e.style.setProperty("--backgroundColor","#262626"),e.style.setProperty("--textColor","#959595"),e.style.setProperty("--shadowColor","rgba(255,255,255,0.19)"),e.style.setProperty("--borderColor","white"),e.style.setProperty("--styleColor","#A837AF")):(e.style.setProperty("--backgroundColor","white"),e.style.setProperty("--textColor","black"),e.style.setProperty("--shadowColor","rgba(0,0,0,0.19)"),e.style.setProperty("--borderColor","black"),e.style.setProperty("--styleColor","#A837AF"))},switchdarkmode(){this.darkmode=!this.darkmode,this.setdarkmode(),$cookies.set("darkmode",this.darkmode)},errorCaptured:function(e){}},created(){this.setdarkmode(),this.user={id:838383,status:"a",fontsize:19,tier:this.status}},mounted(){}};const te=(0,P.Z)(ee,[["render",d]]);var ne=te,oe=n(2119);const ae=[{path:"/novel/:title",children:[{path:"",name:"coverPage",component:()=>n.e(487).then(n.bind(n,9487))},{path:":chapter",name:"chapterPage",component:()=>n.e(726).then(n.bind(n,3726)),props:!0}],component:()=>n.e(880).then(n.bind(n,3880))},{path:"",name:"homePage",component:()=>n.e(148).then(n.bind(n,9148))},{path:"/novel/",name:"Browse",component:()=>n.e(277).then(n.bind(n,6277))},{path:"/:browsetype/:identifier/",name:"explorePage",component:()=>n.e(277).then(n.bind(n,6277))},{path:"/about",name:"aboutPage",component:()=>n.e(80).then(n.bind(n,4080))},{path:"/contact",name:"contactPage",component:()=>n.e(106).then(n.bind(n,106))},{path:"/manage",children:[{path:"upload",name:"uploadPage",component:()=>n.e(459).then(n.bind(n,2459))},{path:"schedule",name:"schedulePage",component:()=>n.e(99).then(n.bind(n,2099))},{path:"edit",name:"editPage",component:()=>n.e(352).then(n.bind(n,1352))},{path:"feedback",name:"feedbackPage",component:()=>n.e(865).then(n.bind(n,7865))},{path:"descriptorbution",name:"descriptorPage",component:()=>n.e(448).then(n.bind(n,9448))}],name:"managePage",component:()=>n.e(428).then(n.bind(n,5428))},{path:"/:pathmatch(.*)*",name:"not-found",component:()=>n.e(153).then(n.bind(n,9153))}],re=(0,oe.p7)({history:(0,oe.PO)(),routes:ae,mode:"history"});re.resolve({name:"not-found",params:{pathMatch:["not","found"]}}).href;var ie=re,se=n(6123);$cookies.config("1m"),(0,o.ri)(ne).use(ie,se.VueCookies).mount("#app")},2311:function(e,t,n){n.d(t,{Z:function(){return f}});var o=n(6252),a="data:image/png;base64,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";const r={href:"https://ko-fi.com/K3K4FC3HF",target:"_blank"},i=(0,o._)("img",{height:"36",style:{border:"0px",height:"36px"},src:a,border:"0",alt:"Buy Me a Coffee at ko-fi.com"},null,-1),s=[i];function d(e,t,n,a,i,d){return(0,o.wg)(),(0,o.iD)("a",r,s)}var u={name:"KoFiButton"},c=n(3744);const l=(0,c.Z)(u,[["render",d]]);var f=l}},t={};function n(o){var a=t[o];if(void 0!==a)return a.exports;var r=t[o]={exports:{}};return e[o](r,r.exports,n),r.exports}n.m=e,function(){var e=[];n.O=function(t,o,a,r){if(!o){var i=1/0;for(c=0;c<e.length;c++){o=e[c][0],a=e[c][1],r=e[c][2];for(var s=!0,d=0;d<o.length;d++)(!1&r||i>=r)&&Object.keys(n.O).every((function(e){return n.O[e](o[d])}))?o.splice(d--,1):(s=!1,r<i&&(i=r));if(s){e.splice(c--,1);var u=a();void 0!==u&&(t=u)}}return t}r=r||0;for(var c=e.length;c>0&&e[c-1][2]>r;c--)e[c]=e[c-1];e[c]=[o,a,r]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var o in t)n.o(t,o)&&!n.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,o){return n.f[o](e,t),t}),[]))}}(),function(){n.u=function(e){return"../static/js/"+e+"."+{80:"235b1a19",99:"0ed622eb",106:"591dad1c",148:"020f079b",153:"4a271e6b",277:"3c36d0d5",352:"9c8d7487",428:"94241c3a",448:"32f1d6e9",459:"b14c8c0d",487:"fe1fe7d4",726:"7cab367a",865:"92c1ff2a",880:"3fd3b7ce"}[e]+".js"}}(),function(){n.miniCssF=function(e){return"../static/css/"+e+"."+{99:"939030af",106:"3616b489",148:"17ea2ce5",153:"1940294c",277:"3ee96d3a",352:"c0883e7d",428:"fe5a4e36",448:"e47d87a1",459:"6b9939df",487:"55a99041",726:"98436ec0",865:"c8e40e66",880:"d218aaf4"}[e]+".css"}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="vuefrontend:";n.l=function(o,a,r,i){if(e[o])e[o].push(a);else{var s,d;if(void 0!==r)for(var u=document.getElementsByTagName("script"),c=0;c<u.length;c++){var l=u[c];if(l.getAttribute("src")==o||l.getAttribute("data-webpack")==t+r){s=l;break}}s||(d=!0,s=document.createElement("script"),s.charset="utf-8",s.timeout=120,n.nc&&s.setAttribute("nonce",n.nc),s.setAttribute("data-webpack",t+r),s.src=o),e[o]=[a];var f=function(t,n){s.onerror=s.onload=null,clearTimeout(m);var a=e[o];if(delete e[o],s.parentNode&&s.parentNode.removeChild(s),a&&a.forEach((function(e){return e(n)})),t)return t(n)},m=setTimeout(f.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=f.bind(null,s.onerror),s.onload=f.bind(null,s.onload),d&&document.head.appendChild(s)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="../static/"}(),function(){var e=function(e,t,n,o){var a=document.createElement("link");a.rel="stylesheet",a.type="text/css";var r=function(r){if(a.onerror=a.onload=null,"load"===r.type)n();else{var i=r&&("load"===r.type?"missing":r.type),s=r&&r.target&&r.target.href||t,d=new Error("Loading CSS chunk "+e+" failed.\n("+s+")");d.code="CSS_CHUNK_LOAD_FAILED",d.type=i,d.request=s,a.parentNode.removeChild(a),o(d)}};return a.onerror=a.onload=r,a.href=t,document.head.appendChild(a),a},t=function(e,t){for(var n=document.getElementsByTagName("link"),o=0;o<n.length;o++){var a=n[o],r=a.getAttribute("data-href")||a.getAttribute("href");if("stylesheet"===a.rel&&(r===e||r===t))return a}var i=document.getElementsByTagName("style");for(o=0;o<i.length;o++){a=i[o],r=a.getAttribute("data-href");if(r===e||r===t)return a}},o=function(o){return new Promise((function(a,r){var i=n.miniCssF(o),s=n.p+i;if(t(i,s))return a();e(o,s,a,r)}))},a={143:0};n.f.miniCss=function(e,t){var n={99:1,106:1,148:1,153:1,277:1,352:1,428:1,448:1,459:1,487:1,726:1,865:1,880:1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=o(e).then((function(){a[e]=0}),(function(t){throw delete a[e],t})))}}(),function(){var e={143:0};n.f.j=function(t,o){var a=n.o(e,t)?e[t]:void 0;if(0!==a)if(a)o.push(a[2]);else{var r=new Promise((function(n,o){a=e[t]=[n,o]}));o.push(a[2]=r);var i=n.p+n.u(t),s=new Error,d=function(o){if(n.o(e,t)&&(a=e[t],0!==a&&(e[t]=void 0),a)){var r=o&&("load"===o.type?"missing":o.type),i=o&&o.target&&o.target.src;s.message="Loading chunk "+t+" failed.\n("+r+": "+i+")",s.name="ChunkLoadError",s.type=r,s.request=i,a[1](s)}};n.l(i,d,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,o){var a,r,i=o[0],s=o[1],d=o[2],u=0;if(i.some((function(t){return 0!==e[t]}))){for(a in s)n.o(s,a)&&(n.m[a]=s[a]);if(d)var c=d(n)}for(t&&t(o);u<i.length;u++)r=i[u],n.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return n.O(c)},o=self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))}();var o=n.O(void 0,[998],(function(){return n(1829)}));o=n.O(o)})();
//# sourceMappingURL=app.f3115dd1.js.map