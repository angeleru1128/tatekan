<template>
  <div>
    <v-container>
      <!-- <左側のグリッド 筑波大学地図を表示> -->
      <v-row class="grey lighten-3" style="height: 600px">
        <v-col
          cols="6"
          sm="6"
          md="6"
          lg="6"
          xl="6"
          style="height: 110%; text-align: center"
        >
          <SchoolImage v-bind:setCurrentTatekanTitle="setCurrentTatekanTitle" />
        </v-col>

        <!-- <右側のグリッド 背景ミントグリーンの場所> -->
        <v-col
          cols="6"
          sm="6"
          md="6"
          lg="6"
          xl="6"
          style="background-color: #afdbc9"
        >
          <v-row style="height: 600px" no-gutters>
            <!-- <右側のグリッド　背景白の場所> -->
            <v-col>
              <v-card class="mx-auto my-12" max-width="600">
                <template slot="progress">
                  <v-progress-linear
                    color="deep-purple"
                    height="10"
                    indeterminate
                  >
                  </v-progress-linear>
                </template>

                <!-- <タテカンの画像表示> -->
                <TatekanImage :tatekanImage="currentTatekanImage" />

                <v-divider class="mx-4"></v-divider>

                <!-- <Uploadボタンの表示> -->
                <v-col cols="12" sm="12" md="12" lg="12" xl="12">
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
                <v-col cols="12" sm="12" md="12" lg="12" xl="12">
                  <!-- <DetailInput /> -->
                </v-col>
                <div>{{ currentTatekanTitle }}</div>
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
import demos from "@/assets/tatekan-image-demo.json";
import HeaderMenu from "@/components/Header";
import axios from "axios";

export default {
  data() {
    return {
      demos: demos,
      currentTatekanTitle: "aaaa",
    };
  },
  computed: {
    currentTatekanImage: function () {
      let unsafeDemoObj = this.demos.find(
        (element) => element.title == this.currentTatekanTitle
      );
      if (unsafeDemoObj) {
        return unsafeDemoObj.image;
      }
      return "";
    },
  },
  methods: {
    onUpload: function () {
      //画像アップロード時の挙動
      let image = event.target.files; //どこかに保存
    },
    setCurrentTatekanTitle: function (newTatekanTitle) {
      console.log("currentTatekanTitle", this.currentTatekanTitle);
      console.log("newTatekanTitle", newTatekanTitle);
      this.currentTatekanTitle = newTatekanTitle;
    },
    onSubmit: function (uploadData) {
      axios.post("/upload", uploadData);
    },
  },
  data() {
    const axiosBase = require("axios");
    const axios = axiosBase.create({
      baseURL: "http://localhost:5000",
      headers: {
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
      },
      responseType: "json",
    });
    const data = axios.get("/topdata");
    console.log(data);
    return {
      demos: data, //demos
    };
  },
  mounted() {
    // console.log(this.$refs.preview)
  },
  components: {
    SchoolImage,
    UploadButton,
    DetailInput,
    TatekanImage,
    HeaderMenu,
  },
};
</script>

<style>
.components {
  background-color: #ffffff;
}
</style>
