<template>
  <div class="components">
    
    <v-container>
  <v-row class="grey lighten-3" style="height: 600px;">
    <v-col cols="6" sm="6" md="6" lg="6" xl="6" style="background-color: #FFCDD2">
      column 1
    </v-col>
    
    <v-col cols="6" sm="6" md="6" lg="6" xl="6" style="background-color: #F8BBD0">
       <v-container　class="pa-8">
          <v-row style="height: 600px;" no-gutters >
            <v-col cols="12" sm="12" md="12" lg="12" xl="12">
               <v-card color="red" style="height: 400px"> 
               <v-card color="red" style="height: 110%">hi</v-card>
              </v-card>
            </v-col>
            <v-col cols="12" sm="12" md="12" lg="12" xl="12" style="background-color: #ffb6c1" class="pa-2">
                <v-card class="pa-2" style="#FFFFFF;">column 3 </v-card>
            </v-col>
            <v-col cols="12" sm="12" md="12" lg="12" xl="12" style="background-color: #00FF00">
              <v-card class="pa-2">column ３</v-card>
            </v-col>
          </v-row>
      </v-container>
           </v-col>
         </v-row>
         <!-- <v-row>
            <v-card  class="pa-5" style="background-color: #000000">
              カラム2
            </v-card>
            <v-card  style="background-color: #0000FF">
              カラム3
              </v-card>
         </v-row> -->
       </v-container>
   
    </v-col>



  </v-row>
</v-container>
  
    <!-- <v-container>
      <v-row rows="6" style="height: 600px;">
        <v-col cols="6" md="6" style="background-color: blue;">
          左だよ -->
          <!-- <SchoolImage /> -->
        <!-- </v-col>
        <v-col cols="6" md="6">
          <!-- <v-row rows="6" md="6" class="align-stretch" style="background-color: red;">  -->
             <!-- <TatekanImage />  -->
              <!-- <v-card class="md-2 align-stretch" >
              右上 -->
             <!-- </v-card>  -->
              
             
          <!-- </v-row>  -->
          <!-- <v-row rows="6" md="3" style="background-color: green;"> -->
            <!-- <UploadButton /> -->
            <!-- 右真ん中 -->
          <!-- </v-row>
          <v-row rows="6" md="3" class="align-stretch" style="background-color: yellow;"> -->
             <!-- <DetailInput /> -->
             <!-- 右の下
          </v-row>
        </v-col> -->
      <!-- </v-row> -->
    <!-- </v-container>  -->
  </div>
 </template>






<script>
import SchoolImage from "@/components/SchoolImage";
import UploadButton from "@/components/imageInput";
import DetailInput from "@/components/detailInput";
import TatekanImage from "@/components/TatekanImage";
import HeaderMenu from "@/components/Header";

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
