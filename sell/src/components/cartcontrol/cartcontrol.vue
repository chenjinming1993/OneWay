<!--  -->
<template>
  <div class="cartcontrol">
    <div class="cart-decrease icon-remove_circle_outline" v-show="food.count>0" @click.stop.prevent="decreaseCart"></div>
    <div class="cart-count" v-show="food.count>0">{{food.count}}</div>
    <div class="cart-add icon-add_circle" @click.stop.prevent="addCart"></div>
  </div>
</template>

<script>
import Vue from 'vue'
export default {
  props: {
    food: {
      type: Object
    }
  },
  methods: {
    addCart() {
      console.log('click')
      if (!this.food.count) {
        Vue.set(this.food, 'count', 1) // 为单件商品添加'count'(选中商品数量)数据
      } else {
        this.food.count++
      }
      // 设置滚动对象时，点击加号，设置一个派发事件，将DOM对象传出去,将target（DOM）作为cart.add事件的对象传入
      this.$emit('cart-add', event.target) // $emit, $on, $off 分别来分发、监听、取消监听事件：
    },
    decreaseCart() {
      if (this.food.count > 0) {
        this.food.count--
      }
    }
  },
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
      padding 6px
      color rgb(0,160,220)
    .cart-count
      display inline-block
      vertical-align top
      text-align center
      width 12px
      line-height 24px
      font-size 10px
      padding 6px
      color rgb(147,153,159)
    .cart-add
      display inline-block
      line-height 24px
      font-size 24px
      padding 6px
      color rgb(0,160,220)
</style>
