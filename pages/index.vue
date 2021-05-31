<template>
  <div class="components">
    <v-container>
      <v-row>
        <v-col>
          <SchoolImage />
        </v-col>
        <v-col>
          <TatekanImage />
          <UploadButton />
          <DetailInput />
        </v-col>
      </v-row>
    </v-container>
          <div v-for="demo in demos" v-bind:key="demo.description">
          {{demo.description}}
        </div>
  </div>
</template>

<script>
import SchoolImage from "@/components/SchoolImage";
import UploadButton from "@/components/imageInput";
import DetailInput from "@/components/detailInput";
import TatekanImage from "@/components/TatekanImage";
import demos from "@/builds/tatekan-image-demo.json";

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
    TatekanImage
  }
};
</script>

<style>
.components {
  background-color: #ffffff;
}
</style>
