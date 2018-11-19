<!--  -->
<template>
  <transition name="fadeFoodDetail">
    <div class="foodDetail" v-show="showFlag" @click="showFlag=false">
      你好么!
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
</style>
