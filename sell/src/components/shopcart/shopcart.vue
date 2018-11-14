<!--  -->
<template>
  <div class="shopcart">
    <div class="content_sc">
      <div class="content-left" @click="toggleList">
        <div class="logo-wrapper">
          <div class="logo" :class="{'highlight':totalCount>0}">
            <i class="icon-shopping_cart" :class="{'highlight':totalCount>0}"></i>
            <div class="select-num" v-show="totalCount>0">{{totalCount}}</div>
          </div>
        </div>
        <div class="price" :class="{'highlight':totalPrice>0}">￥{{totalPrice}}</div>
        <div class="desc">另需配送费￥{{deliveryPrice}}元</div>
      </div>
      <div class="content-right" @click="pay">
        <div class="pay" :class="{'highlight':totalPrice>=minPrice}">{{payDesc}}</div>
      </div>
      <div class="ball-container">
        <div v-for="(ball,index) in balls" :key="index">
          <transition name="drop" @before-enter="beroreEnter" @enter="enter" @after-enter="afterEnter">
            <div v-show="ball.show" class="ball">
              <div class="inner"></div>
            </div>
          </transition>
        </div>
      </div>
      <transition name="fade">
        <div class="shopcart-list" v-show="listShow">
          <div class="list-header">
            <div class="title_sc">购物车</div>
            <div class="empty_sc" @click="empty">清空</div>
          </div>
          <div class="list-content" ref="listContent">
            <ul>
              <li v-for="(food,index) in selectFoods" :key="index" class="food_sc">
                <h2 class="name">{{food.name}}</h2>
                <div class="price">
                  <span>￥{{food.price*food.count}}</span>
                </div>
                <div class="cartcontrol-wrapper">
                    <cartcontrol :food="food"></cartcontrol>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </transition>
    </div>
    <transition name="fadeBG">
      <div class="list-mask" v-show="listShow" @click="hideList"></div>
    </transition>
  </div>
</template>

<script>
// import BScroll from 'better-scroll'
import cartcontrol from '../../components/cartcontrol/cartcontrol'
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
      balls: [{
        show: false
      },
      {
        show: false
      },
      {
        show: false
      },
      {
        show: false
      },
      {
        show: false
      }],
      dropBalls: [],
      fold: true // 购物车详情列表默认折叠。ture时隐藏，false时显示
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
    },
    listShow() { // 决定是否可以显示已选商品列表
      if (!this.totalCount) {
        // eslint-disable-next-line
        this.fold = true
        return false
      }
      let show = !this.fold
      // if (show) {
      //   this.$nextTick(() => {
      //     this.scroll = new BScroll(this.$refs.listContent, {
      //       click: true
      //     })
      //   })
      // }
      return show
    }
  },
  methods: {
    drop(el) {
      // 遍历balls，拿到第一个show为false的球，做一个动画
      for (let i = 0; i < this.balls.length; i++) {
        let ball = this.balls[i]
        // console.log(this.balls[i].show)
        // console.log(this.balls[0].show)
        // console.log(this.balls[1].show)
        if (!ball.show) {
          ball.show = true
          ball.el = el // 保留当前的DOM对象，用来计算位置
          this.dropBalls.push(ball) // dropBalls存的是已经下落的小球,后续要对已经下落的小球进行处理
          // console.log(this.balls[i].show)
          // console.log(this.balls[0].show)
          // console.log(this.balls[1].show)
          return
        }
      }
    },
    toggleList() { // 用户打开或关闭已选商品列表
      if (!this.totalCount) {
        return
      }
      this.fold = !this.fold
    },
    empty() {
      this.selectFoods.forEach((food) => {
        food.count = 0
      })
    },
    hideList() {
      this.fold = true
    },
    pay() {
      if (this.totalPrice < this.minPrice) {
        return
      }
      alert(`请支付${this.totalPrice}元`)
    },
    // 定义三个钩子函数实现动画
    beroreEnter(el) { // el为当前执行transition动画的DOM对象
    // 先找到所有为true的小球（连续点击的情况）
      let count = this.balls.length
      while (count--) {
        let ball = this.balls[count]
        // console.log(this.balls[0].show)
        if (ball.show) { // 这个是要运动的小球true
          let rect = ball.el.getBoundingClientRect(); // 获得元素相当于视口的位置
          let x = rect.left - 32
          let y = -(window.innerHeight - rect.top - 22)
          el.style.display = ''
          el.style.webkitTransform = `translate3d(0,${y}px,0)`
          el.style.transform = `tranlate3d(0,${y}px,0)`
          let inner = el.getElementsByClassName('inner')[0]
          // console.log(inner)
          inner.style.webkitTransform = `translate3d(${x}px,0,0)`
          inner.style.transform = `translate3d(${x}px,0,0)`
          // console.log(inner.style.transform)
        }
      }
    },
    enter(el) {
      /* 触发浏览器重绘，重绘之后才可以设置transform */
      /* eslint-disable no-unused-vars */
      let rf = el.offsetHeight
      this.$nextTick(() => {
        el.style.webKitTransform = 'translate3d(0,0,0)' // 设置小球掉落后最终的位置
        el.style.transform = 'translate3d(0,0,0)'
        let inner = el.getElementsByClassName('inner')[0]
        inner.style.webKitTransform = `translate3d(0,0,0)`
        inner.style.transform = `translate3d(0,0,0)`
      })
    },
    afterEnter(el) {
      let ball = this.dropBalls.shift() // 完成一次动画就删除一个dropBalls的小球
      if (ball) {
        ball.show = false
        el.style.display = 'none'
      }
    }
  },
  components: {
    cartcontrol
  }
}

</script>
<style lang="stylus" rel="stylesheet/stylus" scoped>
  @import "../../common/stylus/mixin.styl"
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
      .ball-container
        .ball
          position fixed
          left 32px
          bottom  22px
          z-index 200
          transition: all 0.6s cubic-bezier(0.49, -0.29, 0.75, 0.41)
          // transition: all 0.6s cubic-bezier(.82,.07,.84,.78)
          .inner
            width 16px
            height 16px
            border-radius 50%
            background rgb(0,160,220)
            transition all 0.4s linear  //x轴做一个线性的过渡即可
      .shopcart-list
        position absolute
        left 0
        top 0
        width 100%
        z-index -1
        // background pink
        transform translate3d(0,-100%,0)
        &.fade-enter-active, &.fade-leave-active
          transition all 0.5 linear
          transform translate3d(0,-100%,0)
        &.fade-enter, &.fade-leave-active
          transform translate3d(0,0,0)
        .list-header
          height 40px
          line-height 40px
          padding 0 18px
          background #f3f5f7
          border-bottom 1px solid rgba(7,17,27,0.1)
          .title_sc
            float left
            font-size 14px
            font-weight 200
            color rgb(7,17,27)
          .empty_sc
            float right
            font-size 12px
            color rgb(0,160,220)
        .list-content
          padding 0 18px
          background #fff
          max-height 217px
          overflow hidden
          overflow-y scroll
          .food_sc
            position relative
            padding 12px 0
            box-sizing border-box
            border-1px(rgba(7,17,27,0.1))
            .name
              line-height 24px
              font-size 14px
              color rgb(7,17,27)
            .price
              position absolute
              right 100px
              bottom 12px
              line-height 24px
              font-size 14px
              font-weight 700
              color rgb(240,20,20)
            .cartcontrol-wrapper
              position absolute
              right 0
              bottom 6px
    .list-mask
      position fixed
      top 0
      left 0
      width 100%
      height 100%
      z-index -2
      background rgba(7,17,27,0.6)
      backdrop-filter blur(10px) // 模糊效果
      -webkit-backdrop-filter blur(10px)
      opacity 1
      &.fadeBG-enter-active, &.fadeBG-leave-active
        opacity 1
        transition all 0.5s
        background rgba(7,17,27,0.6)
      &.fadeBG-enter, &.fadeBG-leave-to
        opacity 0
        background rgba(7,17,27,0)
</style>
