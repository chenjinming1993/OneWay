<template>
  <div id="app">
    <router-view/>
    <div class="tab">
      <div class="tab-item"><a router-link="{path:'/goods'}">商品</a></div>
      <div class="tab-item"><a router-link="{path:'/ratings'}">评价</a></div>
      <div class="tab-item"><a router-link="{path:'/seller'}">商家</a></div>
      <!-- <div class="tab-item"><router-link to="/goods">商品</router-link></div>
      <div class="tab-item"><router-link to="/goods">评价</router-link></div>
      <div class="tab-item"><router-link to="/goods">商家</router-link></div> -->
    </div>
  </div>
</template>

<script>
  export default {
    name: 'App'
  }
</script>

<style scoped>
  .tab{
    display: flex;
    width: 100%;
    height: 40px;
    line-height: 40px;
  }
  .tab-item{
    flex: 1;
    text-align: center;
  }
</style>
