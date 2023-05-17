(function(){"use strict";var e={6653:function(e,t,n){var o=n(9963),r=n(6252);const a={id:"app"},i={id:"sidemenu"},s={id:"sidebar"},d=(0,r.Uk)("Browse"),c=(0,r.Uk)("About"),l=(0,r.Uk)("Contact"),u={id:"header",class:"view-header"},f=(0,r.Uk)("TenTenTranslations"),m={id:"header-navigation-bar"},h=(0,r.Uk)("Browse"),p=(0,r.Uk)("About"),b=(0,r.Uk)("Contact"),v=(0,r.Uk)("Manage"),g=(0,r._)("div",{class:"menu-btn__burger"},null,-1),y=[g],k=(0,r._)("div",{class:"view-border-one border"},null,-1),w=(0,r._)("div",{class:"view-border-two border"},null,-1),P={id:"footer",class:"view-footer"},C={id:"footer-navigation"},_=(0,r.Uk)("About"),x=(0,r._)("p",{id:"footer-divider",style:{"font-size":"15px"}},"|",-1),A=(0,r.Uk)("Contact"),O=(0,r._)("br",null,null,-1);function j(e,t,n,o,g,j){const E=(0,r.up)("router-link"),B=(0,r.up)("KoFiButton"),T=(0,r.up)("router-view");return(0,r.wg)(),(0,r.iD)("div",a,[(0,r._)("div",i,[(0,r._)("div",s,[(0,r._)("h3",{onClick:t[0]||(t[0]=t=>e.swap()),id:"close-sidebar-button"},"╳"),(0,r.Wm)(E,{to:{name:"Browse"},class:"sidebar-nav",onClick:t[1]||(t[1]=e=>j.changesidebar()),style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[d])),_:1}),(0,r.Wm)(E,{to:{name:"aboutPage"},class:"sidebar-nav",onClick:t[2]||(t[2]=e=>j.changesidebar()),style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[c])),_:1}),(0,r.Wm)(E,{to:{name:"contactPage"},class:"sidebar-nav",onClick:t[3]||(t[3]=e=>j.changesidebar()),style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[l])),_:1}),(0,r.Wm)(B,{class:"nav",id:"KoFi-sidebar"})]),(0,r._)("div",{id:"shade",onClick:t[4]||(t[4]=e=>j.changesidebar())})]),(0,r._)("header",u,[(0,r.Wm)(E,{to:{name:"homePage"},id:"home-button"},{default:(0,r.w5)((()=>[f])),_:1}),(0,r._)("div",m,[(0,r.Wm)(E,{to:{name:"Browse"},class:"header-nav",style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[h])),_:1}),(0,r.Wm)(E,{to:{name:"aboutPage"},class:"header-nav",style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[p])),_:1}),(0,r.Wm)(E,{to:{name:"contactPage"},class:"header-nav",style:{"text-decoration":"none"}},{default:(0,r.w5)((()=>[b])),_:1}),0==g.user.tier?((0,r.wg)(),(0,r.j4)(E,{key:0,to:{name:"uploadPage"},class:"header-nav"},{default:(0,r.w5)((()=>[v])),_:1})):((0,r.wg)(),(0,r.j4)(B,{key:1,id:"KoFi"})),(0,r._)("div",{class:"menu-btn",onClick:t[5]||(t[5]=e=>j.changesidebar()),id:"menubutton"},y)])]),k,(0,r.Wm)(T,{tier:g.user.tier,class:"view-content",onSwitchmode:t[6]||(t[6]=e=>j.switchdarkmode())},null,8,["tier"]),w,(0,r._)("footer",P,[(0,r._)("div",C,[(0,r.Wm)(E,{to:{name:"aboutPage"},class:"footer-nav"},{default:(0,r.w5)((()=>[_])),_:1}),x,(0,r.Wm)(E,{to:{name:"contactPage"},class:"footer-nav"},{default:(0,r.w5)((()=>[A])),_:1})]),O])])}var E={name:"App",data(){return{darkmode:"true"==$cookies.get("darkmode"),user:[],url:"http://ipinfo.io/json",status:1}},methods:{changesidebar(){const e=document.getElementById("menubutton"),t=document.getElementById("sidebar"),n=document.getElementByID("shade");"0px"==t.style.left?(t.style.left="-300px",n.style.opacity="0",e.classList.remove("open")):(t.style.left="0px",n.style.opacity="0.5",e.classList.add("open"))},setdarkmode(){var e=document.querySelector(":root");this.darkmode?(e.style.setProperty("--backgroundColor","#262626"),e.style.setProperty("--textColor","#959595"),e.style.setProperty("--shadowColor","rgba(255,255,255,0.19)"),e.style.setProperty("--borderColor","white"),e.style.setProperty("--styleColor","#A837AF")):(e.style.setProperty("--backgroundColor","white"),e.style.setProperty("--textColor","black"),e.style.setProperty("--shadowColor","rgba(0,0,0,0.19)"),e.style.setProperty("--borderColor","black"),e.style.setProperty("--styleColor","#A837AF"))},switchdarkmode(){this.darkmode=!this.darkmode,this.setdarkmode(),$cookies.set("darkmode",this.darkmode)}},created(){this.setdarkmode(),this.user={id:838383,status:"a",fontsize:19,tier:this.status}},mounted(){}},B=n(3744);const T=(0,B.Z)(E,[["render",j]]);var S=T,U=n(2119);const W=[{path:"/novel/:title",children:[{path:"",name:"coverPage",component:()=>n.e(153).then(n.bind(n,3153))},{path:":chapter",name:"chapterPage",component:()=>Promise.all([n.e(669),n.e(42)]).then(n.bind(n,7042))}],component:()=>Promise.all([n.e(669),n.e(249)]).then(n.bind(n,1249))},{path:"",name:"homePage",component:()=>Promise.all([n.e(669),n.e(964)]).then(n.bind(n,7964))},{path:"/novel/",name:"Browse",component:()=>Promise.all([n.e(669),n.e(7)]).then(n.bind(n,4007))},{path:"/:browsetype/:identifier/",name:"explorePage",component:()=>Promise.all([n.e(669),n.e(7)]).then(n.bind(n,4007))},{path:"/about",name:"aboutPage",component:()=>n.e(15).then(n.bind(n,3015))},{path:"/contact",name:"contactPage",component:()=>Promise.all([n.e(669),n.e(136)]).then(n.bind(n,6136))},{path:"/manage",children:[{path:"upload",name:"uploadPage",component:()=>Promise.all([n.e(669),n.e(344)]).then(n.bind(n,2344))},{path:"schedule",name:"schedulePage",component:()=>Promise.all([n.e(669),n.e(797)]).then(n.bind(n,2797))},{path:"edit",name:"editPage",component:()=>Promise.all([n.e(669),n.e(959)]).then(n.bind(n,4959))},{path:"feedback",name:"feedbackPage",component:()=>Promise.all([n.e(669),n.e(652)]).then(n.bind(n,1652))},{path:"descriptorbution",name:"descriptorPage",component:()=>Promise.all([n.e(669),n.e(698)]).then(n.bind(n,6698))}],name:"managePage",component:()=>n.e(684).then(n.bind(n,4684))},{path:"/:pathmatch(.*)*",name:"not-found",component:()=>n.e(99).then(n.bind(n,1099))}],F=(0,U.p7)({history:(0,U.PO)(),routes:W,mode:"hash"});F.resolve({name:"not-found",params:{pathMatch:["not","found"]}}).href;var L=F,N=n(6123);$cookies.config("1m"),(0,o.ri)(S).use(L,N.VueCookies).mount("#app")}},t={};function n(o){var r=t[o];if(void 0!==r)return r.exports;var a=t[o]={exports:{}};return e[o](a,a.exports,n),a.exports}n.m=e,function(){var e=[];n.O=function(t,o,r,a){if(!o){var i=1/0;for(l=0;l<e.length;l++){o=e[l][0],r=e[l][1],a=e[l][2];for(var s=!0,d=0;d<o.length;d++)(!1&a||i>=a)&&Object.keys(n.O).every((function(e){return n.O[e](o[d])}))?o.splice(d--,1):(s=!1,a<i&&(i=a));if(s){e.splice(l--,1);var c=r();void 0!==c&&(t=c)}}return t}a=a||0;for(var l=e.length;l>0&&e[l-1][2]>a;l--)e[l]=e[l-1];e[l]=[o,r,a]}}(),function(){n.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return n.d(t,{a:t}),t}}(),function(){n.d=function(e,t){for(var o in t)n.o(t,o)&&!n.o(e,o)&&Object.defineProperty(e,o,{enumerable:!0,get:t[o]})}}(),function(){n.f={},n.e=function(e){return Promise.all(Object.keys(n.f).reduce((function(t,o){return n.f[o](e,t),t}),[]))}}(),function(){n.u=function(e){return"../static/js/"+e+"."+{7:"54c587c1",15:"8790d749",42:"bab2b4a8",99:"712e5113",136:"fe181c29",153:"0d5baeb5",249:"e2dc4d63",344:"1a6b988a",652:"375b9b07",669:"a2705867",684:"826c2c95",698:"ed03f31f",797:"d97edd6a",959:"2b263c9b",964:"7dc9e1a0"}[e]+".js"}}(),function(){n.miniCssF=function(e){return"../static/css/"+e+"."+{7:"7ea73f1c",42:"9e0c2c96",99:"864c3d1d",136:"b3b8e6b8",153:"63377036",344:"9716699b",652:"efe2246f",684:"27e84fef",698:"6021a068",797:"63bd84e3",959:"911b68d6",964:"b22e7168"}[e]+".css"}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){var e={},t="vuefrontend:";n.l=function(o,r,a,i){if(e[o])e[o].push(r);else{var s,d;if(void 0!==a)for(var c=document.getElementsByTagName("script"),l=0;l<c.length;l++){var u=c[l];if(u.getAttribute("src")==o||u.getAttribute("data-webpack")==t+a){s=u;break}}s||(d=!0,s=document.createElement("script"),s.charset="utf-8",s.timeout=120,n.nc&&s.setAttribute("nonce",n.nc),s.setAttribute("data-webpack",t+a),s.src=o),e[o]=[r];var f=function(t,n){s.onerror=s.onload=null,clearTimeout(m);var r=e[o];if(delete e[o],s.parentNode&&s.parentNode.removeChild(s),r&&r.forEach((function(e){return e(n)})),t)return t(n)},m=setTimeout(f.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=f.bind(null,s.onerror),s.onload=f.bind(null,s.onload),d&&document.head.appendChild(s)}}}(),function(){n.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){n.p="../static/"}(),function(){var e=function(e,t,n,o){var r=document.createElement("link");r.rel="stylesheet",r.type="text/css";var a=function(a){if(r.onerror=r.onload=null,"load"===a.type)n();else{var i=a&&("load"===a.type?"missing":a.type),s=a&&a.target&&a.target.href||t,d=new Error("Loading CSS chunk "+e+" failed.\n("+s+")");d.code="CSS_CHUNK_LOAD_FAILED",d.type=i,d.request=s,r.parentNode.removeChild(r),o(d)}};return r.onerror=r.onload=a,r.href=t,document.head.appendChild(r),r},t=function(e,t){for(var n=document.getElementsByTagName("link"),o=0;o<n.length;o++){var r=n[o],a=r.getAttribute("data-href")||r.getAttribute("href");if("stylesheet"===r.rel&&(a===e||a===t))return r}var i=document.getElementsByTagName("style");for(o=0;o<i.length;o++){r=i[o],a=r.getAttribute("data-href");if(a===e||a===t)return r}},o=function(o){return new Promise((function(r,a){var i=n.miniCssF(o),s=n.p+i;if(t(i,s))return r();e(o,s,r,a)}))},r={143:0};n.f.miniCss=function(e,t){var n={7:1,42:1,99:1,136:1,153:1,344:1,652:1,684:1,698:1,797:1,959:1,964:1};r[e]?t.push(r[e]):0!==r[e]&&n[e]&&t.push(r[e]=o(e).then((function(){r[e]=0}),(function(t){throw delete r[e],t})))}}(),function(){var e={143:0};n.f.j=function(t,o){var r=n.o(e,t)?e[t]:void 0;if(0!==r)if(r)o.push(r[2]);else{var a=new Promise((function(n,o){r=e[t]=[n,o]}));o.push(r[2]=a);var i=n.p+n.u(t),s=new Error,d=function(o){if(n.o(e,t)&&(r=e[t],0!==r&&(e[t]=void 0),r)){var a=o&&("load"===o.type?"missing":o.type),i=o&&o.target&&o.target.src;s.message="Loading chunk "+t+" failed.\n("+a+": "+i+")",s.name="ChunkLoadError",s.type=a,s.request=i,r[1](s)}};n.l(i,d,"chunk-"+t,t)}},n.O.j=function(t){return 0===e[t]};var t=function(t,o){var r,a,i=o[0],s=o[1],d=o[2],c=0;if(i.some((function(t){return 0!==e[t]}))){for(r in s)n.o(s,r)&&(n.m[r]=s[r]);if(d)var l=d(n)}for(t&&t(o);c<i.length;c++)a=i[c],n.o(e,a)&&e[a]&&e[a][0](),e[a]=0;return n.O(l)},o=self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[];o.forEach(t.bind(null,0)),o.push=t.bind(null,o.push.bind(o))}();var o=n.O(void 0,[998],(function(){return n(6653)}));o=n.O(o)})();
//# sourceMappingURL=app.20b6bc31.js.map