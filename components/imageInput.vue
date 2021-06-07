<template>
  <v-container>
    <v-row>
      <input type="file" v-on:change="select_file" />
      <v-btn
      color=#F0FFF0
      class="ma-2 white--text"
      @click="send"
    >
      Upload
      <v-icon
        right
        dark
      >
        mdi-cloud-upload
      </v-icon>
    </v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  
}
</script>


<style scoped> 
</style>




