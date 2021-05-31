<template>
 <div>
  <label for="xy">x,y　入力</label>
  <input type="number" name="number" max="50" value="15">
  <input type="number" name="number" max="50" value="51">

  
 </div>
</template>


<script>
export default {

}
</script>



<style scoped>
.label {
    color: #000000;
    font: 1rem 'Fira Sans', sans-serif;
}

input {
    border: 2px solid #000000;
    width: 15%;
}


label,
input {
  margin: .4rem 0;
  color: #000000;
  position: relative;
  left: 600px;
  bottom: 40px;
}



</style>



 