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
          <span class="icon" :class="classMap[seller.supports[2].type]"></span>
          <span class="text">{{seller.supports[0].description}}</span>
        </div>
      </div>
      <div v-if="seller.supports" class="support-count" @click="showDetail">
        <span class="count">{{seller.supports.length}}个</span>
        <i class="icon-keyboard_arrow_right"></i>
      </div>
    </div>
    <div class="bulletin-wrapper" @click="showDetail">
      <span class="bulletin-title"></span><span class="bulletin-text">{{seller.bulletin}}</span>
      <i class="icon-keyboard_arrow_right"></i>
    </div>
    <div class="background">
      <img :src="seller.avatar" width="100%" height="100%">
    </div>
    <div v-show="detailShow" class="detail">
      <div class="detail-wrapper clearfix">
        <div class="detail-main">
          <h1 class="name">{{seller.name}}</h1>
        </div>
      </div>
      <div class="detail-close" @click="closeDetail">
        <i class="icon-close"></i>
      </div>
    </div>
  </div>
</template>

<script>
import star from '../../components/star/star'
export default {
  name: 'Sellheader',
  props: {
    seller: {
      type: Object
    }
  },
  data() {
    return {
      detailShow: false
    }
  },
  methods: {
    showDetail() {
      this.detailShow = true
    },
    closeDetail() {
      this.detailShow = false
    }
  },
  created() {
    this.classMap = ['decrease', 'discount', 'special', 'invoice', 'guarantee']
  },
  components: {
    star
  }
}

</script>
<style lang="stylus">
  @import "../../common/stylus/mixin.styl";
  .header{
    position: relative;
    overflow: hidden;
    background: rgba(7,17,27,0.5);
    color: white;
  }
  .content-wrapper{
    padding: 24px 16px 18px 24px;
    font-size: 0;
    position: relative;
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
    margin-bottom: 2px;
  }
  .icon{
    width: 12px;
    height: 12px;
    display: inline-block;
    // bg-image('decrease_1');
    background-size: 12px 12px;
    margin-right: 4px;
    vertical-align: top;
    &.decrease{
      bg-image('decrease_1');
    }
    &.discount{
      bg-image('discount_1');
    }
    &.guarantee{
      bg-image('guarantee_1')
    }
    &.invoice{
      bg-image('invoice_1')
    }
    &.special{
      bg-image('special_1')
    }
  }
  .text{
    font-size: 10px;
    line-height: 12px;
  }
  .support-count{
    position: absolute;
    right: 12px;
    bottom: 14px;
    padding: 0 8px;
    height: 24px;
    line-height: 24px;
    border-radius: 7px;
    background: rgba(0,0,0,0.2);
    text-align: center;
  }
  .count{
    font-size: 10px;
    vertical-align top;
  }
  .icon-keyboard_arrow_right{
    font-size:10px;
    margin-left: 2px;
    line-height: 24px;
  }
  .bulletin-wrapper{
    position relative;
    height: 28px;
    // line-height 28px;
    padding: 0 22px 0 12px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    background: rgba(7,17,27,0.2);
  }
  .bulletin-title{
    width: 22px;
    height: 12px;
    display: inline-block;
    bg-image('bulletin');
    background-size: 22px 12px;
    background-repeat: no-repeat;
    margin-right: 4px;
    vertical-align: middle;
  }
  .bulletin-text{
    font-size: 10px;
    line-height: 28px;
    margin-right: 4px;
    vertical-align: middle;
  }
  .bulletin-wrapper .icon-keyboard_arrow_right{
    position absolute;
    font-size: 10px;
    right: 12px;
    top: 3px;
  }
  .background{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    filter: blur(10px);
  }
  .detail{
    position: fixed;
    z-index: 100;
    overflow: auto;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(7,17,27,0.8);
  }
  .detail-wrapper{
    min-height: 100%;
    width: 100%;
  }
  .detail-main{
    margin-top: 64px;
    padding-bottom: 64px;
  }
  .detail-main .name{
    font-size: 16px;
    font-weight: 700;
    line-height: 16px;
    text-align: center;
  }
  .detail-close{
    position: relative;
    width: 32px;
    height: 32px;
    margin: -64px auto 0 auto;
    clear: both;
    font-size: 32px;
  }
</style>
