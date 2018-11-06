<!--  -->
<template>
  <div class="shopcart">
    <div class="content_sc">
      <div class="content-left">
        <div class="logo-wrapper">
          <div class="logo" :class="{'highlight':totalCount>0}">
            <i class="icon-shopping_cart" :class="{'highlight':totalCount>0}"></i>
            <div class="select-num" v-show="totalCount>0">{{totalCount}}</div>
          </div>
        </div>
        <div class="price" :class="{'highlight':totalPrice>0}">￥{{totalPrice}}</div>
        <div class="desc">另需配送费￥{{deliveryPrice}}元</div>
      </div>
      <div class="content-right">
        <div class="pay" :class="{'highlight':totalPrice>=minPrice}">{{payDesc}}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectFoods: {
      type: Array,
      default() {
        return [
          // {
          //   price: 30,
          //   count: 1
          // }
        ]
      }
    },
    deliveryPrice: {
      type: Number,
      default: 0
    },
    minPrice: {
      type: Number,
      default: 0
    }
  },
  data () {
    return {
    }
  },
  computed: {
    totalPrice() { // 选中商品的总价格
      let total = 0
      this.selectFoods.forEach((food) => {
        total += food.price * food.count
      });
      return total
    },
    totalCount() { // 总选中的商品数量
      let count = 0
      this.selectFoods.forEach((food) => {
        count += food.count
      })
      return count
    },
    payDesc() {
      if (this.totalPrice === 0) {
        return `￥${this.minPrice}起送`
      } else if (this.totalPrice < this.minPrice) {
        let diff = this.minPrice - this.totalPrice
        return `还差￥${diff}起送`
      } else {
        return '去结算'
      }
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
            &.highlight
              background rgb(0,160,220)
            .icon-shopping_cart
              font-size 24px
              line-height 44px
              color rgba(255,255,255,0.4)
              &.highlight
                color #fff
            .select-num
              position absolute
              top 0
              right 0
              width 24px
              height 16px
              line-height 16px
              font-size 9px
              font-weight 700
              color rgb(255,255,255)
              background rgb(240,20,20)
              box-shadow 0 4px 8px 0 rgba(0,0,0,0.4)
              border-radius 16px
              // z-z-index 50
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
          &.highlight
            color #fff
        .desc
          display inline-block
          vertical-align top
          margin-top 12px
          margin-left 12px
          box-sizing border-box
          font-size 10px
          // font-weight 700
          line-height 24px
          color rgba(255,255,255,0.4)
      .content-right
        flex 0 0 105px
        width 105px
        .pay
          text-align center
          font-size 15px
          font-weight 700
          height 48px
          line-height 48px
          color rgba(255,255,255,0.4)
          background #2b333b
          &.highlight
            background #00b43c
            color white
</style>
