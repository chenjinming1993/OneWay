<!--  -->
<template>
  <div class="foodDetail" v-show="showFlag"></div>
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
  .foodDetail
    position fixed
    top 0
    left 0
    width 100%
    height 100%
    z-index 40
    background #fff
</style>
