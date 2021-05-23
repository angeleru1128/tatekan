<template>
<div class = 'components'>
  <SchoolImage />
  <UploadButton />
  <DetailInput />

</div>
</template>




<script>
import SchoolImage from '@/components/SchoolImage'
import UploadButton from '@/components/imageInput'
import DetailInput from '@/components/detailInput'

export default {
  components: {
    SchoolImage,
    UploadButton,
    DetailInput,
  }
}
</script>

<style>
.components {
  background-color: #FFFFFF;
}
</style>
