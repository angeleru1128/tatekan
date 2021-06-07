<template>
<div>
  <v-container>
    <!-- <左側のグリッド 筑波大学地図を表示> -->
    <v-row class="grey lighten-3" style="height: 600px;">
      <v-col cols="6" sm="6" md="6" lg="6" xl="6" style="height: 110%; text-align: center;">
        <SchoolImage />
      </v-col> 

    <!-- <右側のグリッド 背景ミントグリーンの場所> -->
        <v-col cols="6" sm="6" md="6" lg="6" xl="6" style="background-color: #AFDBC9" >
          <v-row style="height: 600px;" no-gutters>  
      
    <!-- <右側のグリッド　背景白の場所> -->
            <v-col>
              <v-card　:loading="loading"　class="mx-auto my-12"　max-width="600">
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  >
                  </v-progress-linear>
                </template>

    <!-- <タテカンの画像表示> -->
              <v-img
                height="520"
                src=""
              >タテカンの画像を表示させる場所 ・srcに画像リンク貼る
              </v-img>

              <v-divider class="mx-4"></v-divider>

    <!-- <Uploadボタンの表示> -->
              <v-col cols="12" sm="12" md="12" lg="12" xl="12" >
                <!-- <v-btn
                  color="deep-purple lighten-2"
                  text
                  @click="Upload"
                >
                Upload
                </v-btn> -->
                <!-- <imageInput /> -->
              </v-col> 
    
              <v-divider></v-divider>

      <!-- <x,y 入力> -->
              <v-col cols="12" sm="12" md="12" lg="12" xl="12" >
                <DetailInput />
              </v-col>
              
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</div>
</template>

<script>
import SchoolImage from "@/components/SchoolImage";
import UploadButton from "@/components/imageInput";
import DetailInput from "@/components/detailInput";
import TatekanImage from "@/components/TatekanImage";
import demos from "@/builds/tatekan-image-demo.json";
import HeaderMenu from "@/components/Header";

export default {
  methods: {
    onUpload: function() {
      //画像アップロード時の挙動
      let image = event.target.files; //どこかに保存
    },
    onSubmit: function() {}
  },
  data() {
    return{
    demos: demos
    }
  },
  components: {
    SchoolImage,
    UploadButton,
    DetailInput,
    TatekanImage,
    HeaderMenu,
  }
};
</script>


<style>
.components {
  background-color: #FFFFFF;
}
</style>
