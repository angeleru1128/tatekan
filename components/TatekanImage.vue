<template>
  <div>
    <img :src="require(`static/tatekan_images/${currentTatekanImage}`)" />
  </div>
</template>
<script>
export default {
  /*data() {
    return {
      currentTatekanImage: "hello.jpg"
    };
  },*/
  props: {
    currentTatekanImage: {
      type: String,
      required: true
    }
  },
  /*methods: {
    currentTatekanImage() {
      this.currentTatekanImage = this.getTatekanImage();
    }
  }*/
};
</script>

<style scoped>
img {
  /*height: 520px;*/
}
</style>
