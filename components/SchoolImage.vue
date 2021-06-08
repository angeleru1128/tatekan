<template>
  <div style="position: relative;">
    <img src="tsukubamap.png" usemap="#tsukuba" />
    <map name="tsukuba">
      <div class="icon"  style="position:absolute; top : 105px; left : 210px;" v-for="demo in demos" :key="demo.title" >
        <area style="color: #00ff00;"
          href="#"
          shape="circle"
          alt="円形"
          v-bind:coords="demo.pos"
          ref="preview"
          @click="()=>gettitle(demo)"
        />
        <!-- <img src="/tatekan_images/icon.png" width="12" /> -->
      </div>
    </map>

    <div v-for="demo in demos" :key="demo.title">{{demo.pos_x}}</div>
    
  </div>
</template>

<script>
import demos from "@/assets/tatekan-image-demo.json";
export default {
  props: {
    setCurrentTatekanTitle: {
      type: Function,
      required: true
    }
  },
 data() {
    return{
    demos: demos
    }
  },
  created() {
    console.log(this.demos)
  },
  methods:{
    gettitle(d){
      console.log("debug1: ",d.title)
      this.setCurrentTatekanTitle(d.title)
    }
  }
};
</script>

<style scoped>
img {
  height: 100%;
}

</style>
