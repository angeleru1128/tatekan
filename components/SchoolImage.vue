<template>
  <div style="position: relative;">
    <img src="tsukubamap.png" usemap="#tsukuba" />
    <map name="tsukuba">
      <div class="icon" style="position:absolute; top : 105px; left : 210px;">
        <area style="color: #00ff00;"
          href="http://www.cman.jp"
          shape="circle"
          alt="円形"
          coords="210,105,40"
        />
        <img src="/tatekan_images/icon.png" width="12" />
      </div>
    </map>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
img {
  height: 100%;
}

</style>
