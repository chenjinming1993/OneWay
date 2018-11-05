<!--  -->
<template>
  <div class="cartcontrol">
    <div class="cart-decrease icon-remove_circle_outline"></div>
    <div class="cart-count">1</div>
    <div class="cart-add icon-add_circle"></div>
  </div>
</template>

<script>
export default {
  data () {
    return {
    };
  }

}

</script>
<style lang='stylus' scoped>
  .cartcontrol
    font-size 0
    .cart-decrease
      display inline-block
      line-height 24px
      font-size 24px
      // padding 6px
      color rgb(0,160,220)
    .cart-count
      display inline-block
      vertical-align top
      text-align center
      width 24px
      line-height 24px
      font-size 10px
      color rgb(147,153,159)
    .cart-add
      display inline-block
      line-height 24px
      font-size 24px
      // padding 6px
      color rgb(0,160,220)
</style>
