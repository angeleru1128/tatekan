<template>
 <div>
  <label for="xy">x,y 入力</label>
  <input type="number" name="number" max="50" value="15">
  <input type="number" name="number" max="50" value="15">
 </div>
</template>


<script>
export default {

}
</script>

<style scoped>
label {
    color: #000000;
    font: 1rem 'Fira Sans', sans-serif;

}

/* x,y入力する場所の幅 */
input {
    border: 1px solid #000000;
    width: 15%;
}

</style>