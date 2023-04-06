<template>
<div id = 'genres'>
        <label v-for='(n,i) in genres.length' :key = 'i'>
            <input type='checkbox' :value='genres[i]' 
                                :name = '"genre"+i' class = 'genrecheckbox' :checked='selectedgenres.includes(genres[i])' @click='changeGenre(genres[i])'>{{genres[i]}}
        </label>
    </div>
</template>

<script>
export default{
    name:'GenreSelector',
    props:[
        'genres',
        'selectedgenres'
    ],
    methods:{
        changeGenre(genre){
            if(this.selectedgenres.includes(genre)){
               for( var i = 0; i < this.selectedgenres.length; i++){ 
                    if ( this.selectedgenres[i] === genre) { 
                        this.selectedgenres.splice(i, 1); 
                        i--; 
                    }
    
                }
            }else{
                this.selectedgenres.push(genre)
            }        
        }
    }
}
</script>
<style scoped>
#genres{
    position:relative;
    display:grid;
    grid-template-rows: auto auto auto auto auto auto auto auto auto;
    grid-auto-flow: column;
    column-gap: 30px;
    row-gap:10px;
    margin:auto;
    width:100%
}
@media (max-width: 775px) {
    #genres{
        grid-template-rows: auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto auto;
        width:300px;
        margin-left:20px;
    }
}
</style>