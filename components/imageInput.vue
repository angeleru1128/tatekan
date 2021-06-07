<template>

  <v-container>
    <v-row>
      <input type="file" v-on:change="select_file" />
      <v-btn
      :loading="loading3"
      :disabled="loading3"
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
  data(){
    return{
      file: null
    }
  },
  methods:{
    select_file:function(e){
        this.file = e.target.files[0]
    },
    send:function(){
        let params = new FormData();
        params.append("image",this.file)
        this.$axios.$post("url",params)
        .then(res=>{
            alert("送信完了")
        })
    }
}
}
</script>


<style scoped> 
</style>




