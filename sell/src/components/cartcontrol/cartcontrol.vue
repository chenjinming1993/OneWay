<!--  -->
<template>
  <div class="cartcontrol">
    <div class="cart-decrease icon-remove_circle_outline" v-show="food.count>0" @click="decreaseCart"></div>
    <div class="cart-count" v-show="food.count>0">{{food.count}}</div>
    <div class="cart-add icon-add_circle" @click="addCart"></div>
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
