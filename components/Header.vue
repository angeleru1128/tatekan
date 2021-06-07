<template>
  <v-card class="overflow-hidden">

    <v-app-bar
      color="#6A76AB"
      dark
      shrink-on-scroll
      prominent
      src="tsukubatrees.png"
      fade-img-on-scroll
      scroll-target="#scrolling-techniques-3"
    >

    <!-- header画像引っ張ってくる -->
      <template v-slot:img="{ props }">
        <v-img
          v-bind="props"
          gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-app-bar-title>Find a tatekan</v-app-bar-title>

      <v-spacer></v-spacer>

<!-- <検索マーク、いいねのハート、三点マークのアイコン念のために表示できるように記載>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn> -->

    </v-app-bar>
    <v-sheet
      id="scrolling-techniques-3"
      class="overflow-y-auto"
      max-height="600"
    >
    
    </v-sheet>
  </v-card>
</template>


<script>
　export default {
    name: 'HeaderMenu'
　};
  
</script>


<style scoped>　
</style>