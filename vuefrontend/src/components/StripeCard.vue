<template>
  <div class="d-flex flex-column align-items-center">
    <h2 class="text-primary">{{msg}} {{payAmount}}</h2>
    <form id="payment-form" class="w-75 px-5 d-flex flex-column align-items-center" >
        <div ref="card" class="form-control m-2">
          <!-- A Stripe Element will be inserted here. -->
        </div>
        <input :disabled="lockSubmit" class="btn btn-primary shadow-sm" type="submit" value="Donate" v-on:click.prevent="purchase" />
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'StripeCard',
    data(){
        return {
      spk:"pk_test_51L5d0fHlYhKzvWmvoTeIQZRu94xVDT6rgJC9Lp9KZxoQaTM21qa8jahwmqFTBTB4h9p6bSp2gFGdbvakV0CpMNRf00KL6sxJNJ",
      stripe:undefined,
      card:undefined,
      msg: 'Donate Here',
      payAmount:"$10.00",
      lockSubmit:false,
      api:"http://localhost:8000/api"
    }
    },mounted: function () {
    var self=this;
    self.stripe= Stripe(self.spk);
    self.card = self.stripe.elements().create('card');
    self.card.mount(self.$refs.card);
    console.log(self.stripe)
  },
  methods:{
    purchase() {
      var self = this;
      self.lockSubmit=true
      self.stripe.createToken(self.card).then(function(result) {
        if (result.error) {
          alert(result.error.message)
          self.$forceUpdate(); // Forcing the DOM to update so the Stripe Element can update.
          self.lockSubmit=false
          return;
        }
        else{ 
          self.processTransaction(result.token.id)
        }
      })
      .catch((err) => {
        console.log('purchaseerror')
        alert("error: "+err.message)
        self.lockSubmit=false
      });
    },
    processTransaction(transactionToken){
      var self=this;
      var dt= {
          amount:self.stripCurrency(self.payAmount), //stripe uses an int [with shifted decimal place] so we must convert our payment amount
          currency:"USD",
          description:"something to say",
          token:transactionToken
      }
      
      var route=self.api+"/charge/card"
      axios.post(route,dt, {
          headers: {
          }
      }).then(response => {
          if(response.status==200){
              alert("Transaction succeeded")
              self.lockSubmit=false
          }
          else{
              throw new Error("failed donation")
          }
      }).catch((err) => {
          console.log('processerror')
          alert("error: "+err.message)
          self.lockSubmit=false
      });
      
    },
    stripCurrency(val){
      return val.replace(',','').replace('$','').replace('.','')
    }
  },

}
</script>

<style>
</style>