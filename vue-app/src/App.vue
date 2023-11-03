<template>
 {{ data }}text23

</template>

<script setup>
import { ref,onMounted } from "vue";
const data = ref();
onMounted( ()=>{
//   const response = await fetch('http://127.0.0.1:8000/api');
// const json = await response.json();
// data.value = json;
fetch('http://127.0.0.1:8000/api')
.then(res=> res.json())
.then(json=> data.value = json)
  .catch(error => console.log(error) )
})
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
