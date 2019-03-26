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
        <div class="content_wrapper">
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
          <div class="cart-wrapper">
            <cartcontrol :food="food"></cartcontrol>
          </div>
          <div class="addShop" v-show="!food.count || food.count===0" @click="addFirst">加入购物车</div>
        </div>
        <div class="info-wrapper" v-show="food.info">
          <h2 class="info-title">商品介绍</h2>
          <div class="info">{{food.info}}</div>
        </div>
        <div class="rating">
          <h1 class="title">商品评价</h1>
          <ratingselect @ratingevent="ratingevent" :select-type="selectType" :only-content="onlyContent" :desc="desc" :ratings="food.ratings"></ratingselect>
          <div class="rating-wrapper">
            <ul v-show="food.ratings && food.ratings.length">
              <li v-show="needShow(rating.rateType,rating.text)" v-for="(rating,index) in food.ratings" :key="index" class="rating-item border-1px">
                <div class="user">
                  <span class="name">{{rating.username}}</span>
                  <img class="avatar" width="12" height="12" :src="rating.avatar" alt="">
                </div>
                <div class="time">{{rating.rateTime | formatDate}}</div>
                <p class="text">
                  <span :class="{'icon-thumb_up':rating.rateType===0,'icon-thumb_down':rating.rateType===1}"></span>{{rating.text}}
                </p>
              </li>
            </ul>
            <div class="no-rating" v-show="!food.ratings || !food.ratings.length">暂无评价</div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import Vue from 'vue'
import BScroll from 'better-scroll'
import {formatDate} from '../../common/js/date'
import cartcontrol from '../../components/cartcontrol/cartcontrol'
import ratingselect from '../../components/ratingselect/ratingselect'
// const POSITIVE = 0
// const NEGATIVE = 1
const ALL = 2
export default {
  props: {
    food: {
      type: Object
    }
  },
  data () {
    return {
      showFlag: false,
      selectType: ALL,
      onlyContent: true,
      desc: {
        all: '全部',
        positive: '推荐',
        negative: '吐槽'
      }
    }
  },
  methods: {
    show() {
      this.showFlag = true
      this.selectType = ALL
      this.onlyContent = true
      this.$nextTick(() => {
        if (!this.scroll) {
          this.scroll = new BScroll(this.$refs.foodBS, {
            click: true
          })
        } else {
          this.scroll.refresh()
        }
      })
    },
    addFirst() {
      Vue.set(this.food, 'count', 1) // 为单件商品添加'count'(选中商品数量)数据。第一次时数据中没有count属性
    },
    ratingevent(type, data) {
      this[type] = data
      this.$nextTick(() => {
        this.scroll.refresh()
      })
    },
    needShow(type, text) {
      if (this.onlyContent && !text) {
        return false
      }
      if (this.selectType === 2) {
        return true
      } else {
        return type === this.selectType
      }
    }
  },
  filters: {
    formatDate(time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm')
    }
  },
  components: {
    cartcontrol,
    ratingselect
  }
}

</script>
<style lang='stylus' scoped>
  @import "../../common/stylus/mixin.styl"
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
      padding-bottom 60px
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
      .content_wrapper
        position relative
        border-bottom 1px solid rgba(7, 17, 27, 0.1)
        margin-bottom 16px
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
        .cart-wrapper
          position absolute
          right 12px
          bottom 12px
        .addShop
          position absolute
          right 18px
          bottom 18px
          z-index 10
          // width 74px
          height 24px
          line-height 24px
          padding 0 12px
          box-sizing border-box
          border-radius 12px
          font-size 10px
          // text-align center
          color #ffffff
          background rgb(0,160,220)
      .info-wrapper
        border-top 1px solid rgba(7, 17, 27, 0.1)
        border-bottom 1px solid rgba(7, 17, 27, 0.1)
        .info-title
          margin 18px 0 6px 18px
          font-size 15px
          font-weight 550
        .info
          margin 0 26px 18px 26px
          font-size 12px
          font-weight 200
          color rgb(77,85,93)
          line-height 24px
      .rating
        margin-top 16px
        border-top 1px solid rgba(7, 17, 27, 0.1)
        .title
          margin 18px 0 6px 18px
          font-size 15px
          font-weight 550
        .rating-wrapper
          padding 0 18px
          .rating-item
            position relative
            padding 16px 0
            border-1px(rgba(7, 17, 27, 0.1))
            .user
              position absolute
              right 0
              line-height 12px
              top 16px
              font-size 0
              .name
                display inline-block
                margin-right 6px
                vertical-align top
                font-size 10px
                line-height 12px
                color rgb(147,153,159)
              .avatar
                border-radius 50%
            .time
              margin-bottom 6px
              line-height 12px
              font-size 10px
              color rgb(147,153,159)
            .text
              line-height 16px
              font-size 12px
              color rgb(7,17,27)
              .icon-thumb_up, .icon-thumb_down
                line-height 16px
                margin-right 4px
                font-size 12px
              .icon-thumb_up
                color rgb(0,160,220)
              .icon-thumb_down
                color rgb(147,153,159)
          .no-rating
            padding 16px 0
            font-size 12px
            color rgb(147,153,159)

</style>
