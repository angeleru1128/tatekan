<template>
  <div>
    <img :src="tatekan_image" />
  </div>
</template>
<script>
export default {
  props: {
    tatekan_image: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
img {
  /*height: 520px;*/
}
</style>
