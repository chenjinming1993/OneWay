<!--  -->
<template>
  <div class="ratings" ref="ratings">
    <div class="ratings-content">
      <div class="overview">
        <div class="overview-left">
          <h1 class="score">{{seller.score}}</h1>
          <div class="title">综合评分</div>
          <div class="rank">高于周边商家{{seller.rankRate}}</div>
        </div>
        <div class="overview-right">
          <div class="score-wrapper">
            <span class="title">服务态度</span>
            <star :size="36" :score="seller.serviceScore"></star>
            <span class="score">{{seller.serviceScore}}</span>
          </div>
          <div class="score-wrapper">
            <span class="title">商品评分</span>
            <star :size="36" :score="seller.foodScore"></star>
            <span class="score">{{seller.foodScore}}</span>
          </div>
          <div class="delivery-wrapper">
            <span class="title">送达时间</span>
            <span class="delivery">{{seller.deliveryTime}}分钟</span>
          </div>
        </div>
      </div>
      <div class="rating-detail">
        <ratingselect :select-type="selectType" :only-content="onlyContent" :ratings="ratings"></ratingselect>
        <div class="rating-wrapper">
          <ul>
            <li v-for="(rating,index) in ratings" :key="index">
              <div class="avatar">
                <img :src="rating.avatar" alt="" width="28px" height="28px">
              </div>
              <div class="content">
                <h1 class="name">{{rating.username}}</h1>
                <div class="star-wrapper">
                  <star :size="24" :score="rating.score"></star>
                  <span class="delivery" v-show="rating.deliveryTime">{{rating.deliveryTime}}分钟送达</span>
                </div>
                <p class="text">{{rating.text}}</p>
                <div class="recommend" v-show="rating.recommend && rating.recommend.length">
                  <i class="icon-thumb_up"></i>
                  <span class="item" v-for="(item,index) in rating.recommend" :key="index">{{item}}</span>
                </div>
                <div class="time">{{rating.rateTime | formatDate}}</div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BScroll from 'better-scroll'
import star from '../../components/star/star'
import ratingselect from '../../components/ratingselect/ratingselect'
import {formatDate} from '../../common/js/date'
const ALL = 2
const ERR_OK = 0
export default {
  name: 'ratings',
  props: {
    seller: {
      type: Object
    }
  },
  data () {
    return {
      ratings: [],
      // showFlag: false,
      selectType: ALL,
      onlyContent: true
    }
  },
  created () {
    this.$http.get('/api/ratings').then((response) => {
      response = response.body
      if (response.errno === ERR_OK) {
        this.ratings = response.data
        this.$nextTick(() => {
          this.scroll = new BScroll(this.$refs.ratings, {
            click: true
          })
        })
      }
    })
  },
  filters: {
    formatDate(time) {
      let date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm')
    }
  },
  components: {
    star,
    ratingselect
  }
}

</script>
<style lang='stylus' scoped>
  .ratings
    position absolute
    top 174px
    bottom 0
    left 0
    width 100%
    overflow hidden
    .overview
      display flex
      padding 18px 0
      border-bottom 1px solid rgba(7, 17, 27, 0.1)
      .overview-left
        flex 0 0 137px
        width 137px
        border-right 1px solid rgba(7, 17, 27, 0.1)
        text-align center
        padding-bottom 6px
        @media only screen and (max-width 320px)
          flex 0 0 110px
          width 110px
        .score
          font-size 24px
          line-height 28px
          color rgb(255,153,0)
          margin-bottom 6px
        .title
          font-size 12px
          line-height 12px
          margin-bottom 8px
          color rgb(7,17,27)
        .rank
          font-size 10px
          line-height 10px
          color rgb(147,153,159)
      .overview-right
        flex 1
        padding-left 24px
        @media only screen and (max-width 320px)
          padding-left 6px
        .score-wrapper
          margin-bottom 8px
          .title
            display inline-block
            font-size 12px
            color rgb(7,17,27)
            vertical-align top
          .star
            display inline-block
            margin 0 12px
            line-height 18px
            vertical-align top
          .score
            display inline-block
            font-size 12
            color rgb(255,153,0)
            vertical-align top
        .delivery-wrapper
          .title
            display inline-block
            font-size 12px
            color rgb(7,17,27)
            margin-right 12px
            vertical-align top
          .delivery
            display inline-block
            font-size 13px
            line-height 18px
            color rgb(147,153,159)
            vertical-align top
</style>
