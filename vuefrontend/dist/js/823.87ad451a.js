"use strict";(self["webpackChunkvuefrontend"]=self["webpackChunkvuefrontend"]||[]).push([[823],{1823:function(e,r,t){t.r(r),t.d(r,{default:function(){return w}});var a=t(3396);const o=(0,a._)("a",{href:"https://buy.stripe.com/test_7sI14ggPXa1WeEE6oo"},"Donate",-1);function n(e,r,t,n,s,c){const i=(0,a.up)("StripeCard");return(0,a.wg)(),(0,a.iD)("div",null,[o,(0,a.Wm)(i)])}var s=t(7139),c=t(9242);const i={class:"d-flex flex-column align-items-center"},l={class:"text-primary"},p={id:"payment-form",class:"w-75 px-5 d-flex flex-column align-items-center"},u={ref:"card",class:"form-control m-2"},d=["disabled"];function m(e,r,t,o,n,m){return(0,a.wg)(),(0,a.iD)("div",i,[(0,a._)("h2",l,(0,s.zw)(n.msg)+" "+(0,s.zw)(n.payAmount),1),(0,a._)("form",p,[(0,a._)("div",u,null,512),(0,a._)("input",{disabled:n.lockSubmit,class:"btn btn-primary shadow-sm",type:"submit",value:"Donate",onClick:r[0]||(r[0]=(0,c.iM)(((...e)=>m.purchase&&m.purchase(...e)),["prevent"]))},null,8,d)])])}t(1703);var h=t(6265),f=t.n(h),v={name:"StripeCard",data(){return{spk:"pk_test_51L5d0fHlYhKzvWmvoTeIQZRu94xVDT6rgJC9Lp9KZxoQaTM21qa8jahwmqFTBTB4h9p6bSp2gFGdbvakV0CpMNRf00KL6sxJNJ",stripe:void 0,card:void 0,msg:"Donate Here",payAmount:"$10.00",lockSubmit:!1,api:"http://localhost:8000/api"}},mounted:function(){var e=this;e.stripe=Stripe(e.spk),e.card=e.stripe.elements().create("card"),e.card.mount(e.$refs.card),console.log(e.stripe)},methods:{purchase(){var e=this;e.lockSubmit=!0,e.stripe.createToken(e.card).then((function(r){if(r.error)return alert(r.error.message),e.$forceUpdate(),void(e.lockSubmit=!1);e.processTransaction(r.token.id)})).catch((r=>{console.log("purchaseerror"),alert("error: "+r.message),e.lockSubmit=!1}))},processTransaction(e){var r=this,t={amount:r.stripCurrency(r.payAmount),currency:"USD",description:"something to say",token:e},a=r.api+"/charge/card";f().post(a,t,{headers:{}}).then((e=>{if(200!=e.status)throw new Error("failed donation");alert("Transaction succeeded"),r.lockSubmit=!1})).catch((e=>{console.log("processerror"),alert("error: "+e.message),r.lockSubmit=!1}))},stripCurrency(e){return e.replace(",","").replace("$","").replace(".","")}}},k=t(89);const g=(0,k.Z)(v,[["render",m]]);var b=g,S={components:{StripeCard:b}};const y=(0,k.Z)(S,[["render",n]]);var w=y}}]);
//# sourceMappingURL=823.87ad451a.js.map