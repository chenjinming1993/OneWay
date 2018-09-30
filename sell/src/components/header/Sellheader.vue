<!--  -->
<template>
  <div class="header">
    <div class="content-wrapper">
      <div class="avatar">
        <img width="64px" height="64px" :src="seller.avatar">
      </div>
      <div class="content">
        <div class="title">
          <span class="brand"></span>
          <span class="name">{{seller.name}}</span>
        </div>
        <div class="description">{{seller.description}}/{{seller.deliveryTime}}分钟送达</div>
        <div v-if="seller.supports" class="support">
          <span class="icon"></span>
          <span class="text">{{seller.supports[0].description}}</span>
        </div>
      </div>
    </div>
    <div class="bulletin-wrapper"></div>
  </div>
</template>

<script>
export default {
  name: 'Sellheader',
  props: {
    seller: {
      type: Object
    }
  },
  data () {
      return {

      }
  }
}

</script>
<style lang="stylus">
  @import "../../common/stylus/mixin.styl";
  .header{
    background: blue;
    color: white;
  }
  .content-wrapper{
    padding: 24px 16px 18px 24px;
    font-size: 0;
  }
  .avatar{
    display: inline-block;
    vertical-align: top;
  }
  .avatar img{
    border-radius: 2px;
  }
  .content{
    display: inline-block;
    // font-size: 14px;
    margin-left: 16px;
  }
  .title{
    margin: 2px 0 8px 0;
  }
  .brand{
    width: 30px;
    height: 18px;
    display: inline-block;
    bg-image('brand');
    background-size: 30px 18px;
    background-repeat: no-repeat;
    vertical-align: top;
  }
  .name{
    font-size: 16px;
    font-weight: bold;
    line-height: 18px;
    margin-left: 6px;
  }
  .description{
    margin-bottom: 10px;
    font-size: 12px;
    // font-weight: 200;
    line-height: 12px;
  }
  .support{
    // margin: 10px 0 2px 0;
  }
</style>
