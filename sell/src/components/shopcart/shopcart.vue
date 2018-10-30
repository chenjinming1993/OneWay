<!--  -->
<template>
  <div class="shopcart">
    <div class="content_sc">
      <div class="content-left">
        <div class="logo-wrapper">
          <div class="logo">
            <i class="icon-shopping_cart"></i>
          </div>
        </div>
        <div class="price">￥0</div>
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
    .content_sc
      display flex
      height 100%
      font-size 0
      background #141d27
      .content-left
        flex 1
        .logo-wrapper
          display inline-block
          position relative
          vertical-align top
          top -10px
          margin 0 12px
          padding 6px
          width 56px
          height 56px
          box-sizing border-box
          border-radius 50%
          background #141d27
          .logo
            width 100%
            height 100%
            border-radius 50%
            text-align center
            background #2b343c
            .icon-shopping_cart
              font-size 24px
              line-height 44px
              color rgba(255,255,255,0.4)
        .price
          display inline-block
          vertical-align top
          margin-top 12px
          line-height 24px
          padding-right 12px
          box-sizing border-box
          font-size 16px
          font-weight 700
          color rgba(255,255,255,0.4)
          border-right 1px solid rgba(255,255,255,0.4)

      .content-right
        flex 0 0 105px
        width 105px
        background blue
</style>
