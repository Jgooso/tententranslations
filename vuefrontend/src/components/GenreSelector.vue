<template>
<div id = 'genres'>
        <label v-for='genre in genres' :key = 'genre'>
            <input type='checkbox' :value='genre' :name = 'genre' class = 'genrecheckbox' :checked='selectedgenres.includes(genre)'>{{genre}}
        </label>
    </div>
</template>

<script>
export default{
    name:'GenreSelector',
    props:[
        'genres',
        'selectedgenres'
    ]
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