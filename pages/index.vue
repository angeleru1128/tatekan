<template>
  <div class="components">
    <SchoolImage />
    <UploadButton />
    <DetailInput />
  </div>
</template>

<script>
import SchoolImage from "@/components/SchoolImage";
import UploadButton from "@/components/imageInput";
import DetailInput from "@/components/detailInput";
export class TatekanData {
  constructor(title, image, description, pos_x, pos_y) {
    this.title = title;
    this.image = image;
    this.description = description;
    this.pos_x = pos_x;
    this.pos_y = pos_y;
  }
}

export default {
  data() {
    return {
      post: TatekanData()
    };
  },
  methods: {
    onUpload: function() {
      //画像アップロード時の挙動
      let image = event.target.files; //どこかに保存
    },
    onSubmit: function() {
      //投稿ボタンクリック時の挙動
      //画像形式変換？（必要？）
      //ファイルネーム：数字。最大のファイルネーム+1の値で登録？
      //ファイルネーム生成処理
      //SQL問い合わせ(save)
    }
  },
  components: {
    SchoolImage,
    UploadButton,
    DetailInput
  }
}
</script>

<style>
.components {
  background-color: #ffffff;
}
</style>
