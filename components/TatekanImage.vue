<template>
  <div>
    <img :src="tatekanImage" />
  </div>
</template>
<script>
export default {
  props: {
    tatekanImage: {
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
