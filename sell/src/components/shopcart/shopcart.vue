<!--  -->
<template>
  <div class="shopcart">
    <div class="content">
      <div class="content-left">
        <div class="logo-wrapper">
          <div class="logo">
            <span class="icon-shopping_cart"></span>
          </div>
        </div>
        <div class="price"></div>
        <div class="desc"></div>
      </div>
      <div class="content-right"></div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}

</script>
<style lang="stylus" rel="stylesheet/stylus">
  .shopcart
    position: fixed
    left 0
    bottom 0
    width 100%
    height 48px
    z-index 50
    .content
      display flex
      height 100%
      .content-left
        flex 1
        .logo-wrapper
          display inline-block
      .content-right
        flex 0 0 105px
        width 105px
        background blue
</style>
