<!--  -->
<template>
  <div class="header">
    <div class="content-wrapper">
      <div class="avatar">
        <img width="64px" height="64px" :src="seller.avatar">
      </div>
    </div>
    <div class="bulletin-wrapper"></div>
  </div>
</template>

<script>
export default {
  name: 'Sellheader',
  props: {
    seller: {
      type: Object
    }
  },
  data () {
      return {

      }
  }
}

</script>
<style scoped>
</style>
