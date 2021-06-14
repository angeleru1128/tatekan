<template>
  <div style="position: relative;">
    <img src="tsukubamap.png" usemap="#tsukuba" />
    <map name="tsukuba">
      <div
        class="icon"
        style="position:absolute; top : 105px; left : 210px;"
        v-for="demo in demos"
        :key="demo.title"
      >
        <area
          style="color: #00ff00;"
          href="#"
          shape="circle"
          alt="円形"
          v-bind:coords="`${demo.pos_x}, ${demo.pos_y}, 20`"
          ref="preview"
          @click="() => gettitle(demo)"
        />
      </div>
    </map>
  </div>
</template>

<script>
//import demos from "@/assets/tatekan-image-demo.json";
export default {
  props: {
    setCurrentTatekanTitle: {
      type: Function,
      required: true
    },
    setCurrentTatekanImage: {
      type: Function,
      required: true
    }
  },
  data() {
    return {
      demos: []
    };
  },
  mounted() {
    // console.log(this.$refs.preview)
    const axiosBase = require("axios");
    const axios = axiosBase.create({
      baseURL: "http://127.0.0.1:5000",
      headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
      },
      responseType: "json"
    });
    axios.get("/topdata").then(response => {this.demos = response.data});
  },
  created() {
    console.log(this.demos);
  },
  methods: {
    gettitle(d) {
      console.log("debug1: ", d.title);
      this.setCurrentTatekanTitle(d.title);
      this.setCurrentTatekanImage();
    }
  }
};
</script>

<style scoped>
img {
  height: 100%;
}
</style>
