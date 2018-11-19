<!--  -->
<template>
  <transition name="fadeFoodDetail">
    <div class="foodDetail" v-show="showFlag">
      <div class="image-header">
        <img :src="food.image">
        <div class="back" @click="showFlag=false">
          <i class="icon-arrow_lift"></i>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    food: {
      type: Object
    }
  },
  data () {
    return {
      showFlag: false
    }
  },
  methods: {
    show() {
      this.showFlag = true
    }
  }
}

</script>
<style lang='stylus' scoped>
  .fadeFoodDetail-enter-active, .fadeFoodDetail-leave-active
    transition all 0.3s linear
  .fadeFoodDetail-enter, .fadeFoodDetail-leave-to
    transform translateX(100%)
    opacity 0
  .foodDetail
    position fixed
    top 0
    left 0
    width 100%
    height 100%
    z-index 40
    background #fff
  .image-header
    position relative
    width 100%
    height auto // 从 0 改为 auto，避免图片拉伸
    padding-top 100%
    img
      position absolute
      top 0
      left 0
      width 100%
      height auto
    .back
      position absolute
      top 10px
      left 5px
      height: 24px
      line-height: 24px
      border-radius: 7px
      background rgba(20,29,39,0.3)
      text-align: center
      .icon-arrow_lift
        padding 10px
        font-size: 16px
        vertical-align top
</style>
