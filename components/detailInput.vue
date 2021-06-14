<template>
  <div>
    <v-container>
      <!-- 入力ボタンsubmitの追加 -->
      <form v-on:submit.prevent>
        <v-row>
          <div id="target">
            <label for="xy">x,y 入力</label>
            <input
              type="number"
              name="pos_x"
              
              min="0"
              value="15"
              v-model="pos_x"
              placeholder="x"
            />
            <input
              type="number"
              name="pos_y"
              
              min="0"
              value="15"
              v-model="pos_y"
              placeholder="y"
            />
          </div>
        </v-row>
        <v-row>
        <div id="target">
            <label for="description">description</label>
            <input
              type="text"
              name="description"
              value="lorem iosum"
              v-model="description"
              placeholder="タテカンの説明"
            />
          </div>
                  <div id="target">
            <label for="title">title</label>
            <input
              type="text"
              name="title"
              value="hello"
              v-model="title"
              placeholder="lorem ipsum"
            />
          </div>
        </v-row>
        <v-row>
          <input type="file" name="uploadFile" v-on:change="select_file" />
          <v-btn color="#F0FFF0" class="ma-2 white--text" @click="send" type="submit">
            Upload
            <v-icon right dark> mdi-cloud-upload </v-icon>
          </v-btn>
        </v-row>
      </form>
    </v-container>
  </div>
</template>

<script>
export default {
  // documentgetElementById(target)
  // .addEventListener("click", function(event) {
  // 	var clickX = event.pageX ;
  // 	var clickY = event.pageY ;

  // 	// 要素の位置を取得
  // 	var clientRect = this.getBoundingClientRect() ;
  // 	var positionX = clientRect.left + window.pageXOffset ;
  // 	var positionY = clientRect.top + window.pageYOffset ;

  // 	// 要素内におけるクリック位置を計算
  // 	var x = clickX - positionX ;
  // 	var y = clickY - positionY ;
  // };)
  // }
  data() {
    return {
      file: null,
    };
  },
  methods: {
    select_file: function (e) {
      this.file = e.target.files[0];
    },
    send: function () {
      const axiosBase = require("axios");
      const axios = axiosBase.create({
        baseURL: "http://127.0.0.1:5000",
        headers: {
          'Content-type': 'multipart/form-data',
        }
      });
      let params = new FormData();
      params.append("image", this.file);
      params.append("description", this.description);
      params.append("title", this.title);
      params.append("pos_x", this.pos_x);
      params.append("pos_y", this.pos_y);
      axios.post("/upload", params).then((res) => {
        alert("送信完了");
        location.reload();
      }).catch(function (error) {
        if(error.message){
          console.log(error.message);
        }
        alert("Failed to upload.")
      });
    },
  },
};
</script>

<style scoped>
label {
  color: #000000;
  font: 1rem "Fira Sans", sans-serif;
}

/* x,y入力する場所の幅 */
input {
  border: 1px solid #000000;
  width: 15%;
}
</style>
