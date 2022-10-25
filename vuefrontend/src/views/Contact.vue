<template>
    <div class = 'content'>
    <br>
        <h2>Contact Us</h2>
        <hr>
        <p>For any buisiness, advertisement, DMCA takedowns, please contact us at <a href = 'mailto:tententranslation@gmail.com'><b>tententranslation@gmail.com</b></a></p>
        <p>For any general feedback, please submit below.</p>
        
        <form name="feedbackForm" onsubmit='submitFeedback()'>
            <textarea id = 'feedbackbox' name = 'feedbackBox'></textarea>
            <input type = 'submit' @click='submitFeedback()' id = 'feedback-submit-button'>
        </form>
        <hr>
    </div>
</template>
<script>
import { getAPI } from '../axios-api'
export default{
    methods:{
        submitFeedback(){
                const feedback = document.getElementById('feedbackbox').value
                console.log('posted')
                getAPI.post('/feedback', {feedback:feedback})
                    .then(function (response) {
                        console.log(response);
                       
                }).catch(function (error) {
                    console.log(error);
        
                }); 
        }
    }
}
</script>
<style scoped>
#feedbackbox{
    width:100%;
    min-height:200px;
}
#feedback-submit-button{
    background-color:var(--backgroundColor);
    border:var(--borderColor) 1px solid;
}
</style>