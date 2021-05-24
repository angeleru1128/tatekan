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
  </div>
</template>

<script>
import SchoolImage from "@/components/SchoolImage";
import UploadButton from "@/components/imageInput";
import DetailInput from "@/components/detailInput";
import TatekanImage from "@/components/TatekanImage";

export default {
  methods: {
    onUpload: function() {
      //画像アップロード時の挙動
      let image = event.target.files; //どこかに保存
    },
    onSubmit: function() {}
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
