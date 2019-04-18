<!--  -->
<template>
  <div class="seller">
    <div class="overview">
      <h1 class="title">{{seller.name}}</h1>
      <div class="desc">
        <star :size="36" :score="seller.score"></star>
        <span class="text">({{seller.ratingCount}})</span>
        <span class="text">月售{{seller.sellCount}}</span>
      </div>
    </div>
  </div>
</template>

<script>
import star from '../../components/star/star'
export default {
  props: {
    seller: {
      type: Object
    }
  },
  data () {
    return {
    }
  },
  components: {
    star
  }
}

</script>
<style scoped>
</style>
