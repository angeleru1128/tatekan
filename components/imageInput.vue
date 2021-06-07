<template>

  <v-container>
    <v-row>
      <v-btn
      :loading="loading3"
      :disabled="loading3"
      color=#F0FFF0
      class="ma-2 white--text"
      @click="loader = 'loading3'"
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




