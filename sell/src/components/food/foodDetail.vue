<!--  -->
<template>
  <transition name="fadeFoodDetail">
    <div class="foodDetail" v-show="showFlag" ref="foodBS">
      <div class="food-content">
        <div class="image-header">
          <img :src="food.image">
          <div class="back" @click="showFlag=false">
            <i class="icon-arrow_lift"></i>
          </div>
        </div>
        <div class="content_fd">
          <h2 class="name_fd">{{food.name}}</h2>
          <div class="extra_fd">
            <span style="margin-right:12px">月售{{food.sellCount}}份</span>
            <span>好评率{{food.rating}}%</span>
          </div>
          <div class="price_fd">
            <span class="now_fd">￥{{food.price}}</span>
            <span v-show="food.oldPrice" class="old_fd">￥{{food.oldPrice}}</span>
          </div>
        </div>
        <div class="test">
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
          <div>1233554977</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import BScroll from 'better-scroll'
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
      this.$nextTick(() => {
        if (!this.scroll) {
          this.scroll = new BScroll(this.$refs.foodBS, {
            click: true
          })
        } else {
          this.scroll.refresh()
        }
      })
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
    .food-content
      border-bottom 1px solid rgba(7, 17, 27, 0.1)
      .image-header
        position relative
        width 100%
        height 0 // 从 0 改为 auto，避免图片拉伸
        padding-top 100%
        img
          position absolute
          top 0
          left 0
          width 100%
          height 100%
        .back
          position absolute
          top 10px
          left 5px
          height: 24px
          line-height: 24px
          border-radius: 7px
          background rgba(143, 165, 189, 0.3)
          text-align: center
          .icon-arrow_lift
            // display block
            padding 10px
            font-size: 16px
            line-height 24px
            vertical-align top
            color white
      .content_fd
        margin 18px
        .name_fd
          font-size 14px
          font-weight 700
          color rgb(7,17,27)
          line-height 14px
        .extra_fd
          font-size 10px
          font-weight 700
          margin 8px 0 18px 0
          color #93999f
          line-height 14px
        .price_fd
          font-weight 700
          line-height 24px
          .now_fd
            font-size 14px
            color rgb(240,20,20)
          .old_fd
            font-size 10px
            color rgb(147,153,159)
            text-decoration line-through
</style>
