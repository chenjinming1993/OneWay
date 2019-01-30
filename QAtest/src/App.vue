<template>
  <div id="app">
    <qaHeader></qaHeader>
    <div class="tab border-1px">
      <div class="tab-item"><router-link to="/architecture">建筑</router-link></div>
      <div class="tab-item"><router-link to="/testCase">测试用例</router-link></div>
      <!-- <div class="tab-item"><router-link to="">待定</router-link></div> -->
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import qaHeader from './components/qaHeader/qaHeader'

export default {
  name: 'App',
  components: {
    qaHeader
  }
}
</script>

<style lang='stylus' scoped>
  @import "./common/stylus/mixin.styl"
  .tab
    display: flex
    width: 100%;
    height: 40px
    line-height: 40px
    border-1px(rgba(7, 17, 27, 0.1))
    .tab-item
      flex: 1;
      text-align: center;
</style>
