<template>
<div>
  <a href="#" class="UploadButton" role="button">Upload</a>
  <label for="avatar">タテカン写真選択</label>
  <input type="file" id="avatar" name="avatar" accept="image/png, image/jpeg">
</div>
</template>


<script>
export default {

}
</script>


<style> 
.UploadButton {
  background-color: #00a656;
  border-radius: 1.5em;
  box-shadow: 0 0.2em 0.5em rgba(0, 0, 0, 0.2);
  padding: 1em 2em;
  color: #ffffff;
  font-weight: bold;
  text-decoration: none;
  /* position: relative;
  left: 1000px;
  bottom: 40px; */
}

.avater {
  color: #000000;
}

label {
  display: block;
  font: 1rem 'Fira Sans', sans-serif;
  color: #000000;
}

input,
label {
  margin: .4rem 0;
  color: #000000;
  /* position: relative;
  left: 1000px;
  bottom: 40px; */
}

</style>




