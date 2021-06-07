<template>
 <div id="target">
  <label for="xy">x,y 入力</label>
  <input type="number" name="number" max="50" value="15">
  <input type="number" name="number" max="50" value="15">
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
}
</script>

<style scoped>
label {
    color: #000000;
    font: 1rem 'Fira Sans', sans-serif;

}

/* x,y入力する場所の幅 */
input {
    border: 1px solid #000000;
    width: 15%;
}

</style>