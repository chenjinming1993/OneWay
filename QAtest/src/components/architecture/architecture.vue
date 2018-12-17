<!--  -->
<template>
  <div class="architecture">
    <ul>
      <li v-for="(user,index) in users" :key="index">
        {{user.name}}
        {{user.id}}
        {{user.area}}
        {{user.level}}
        {{user.cost_stone}}
        {{user.cost_metal}}
        {{user.cost_water}}
        {{user.cost_plastic}}
        {{user.cost_nuclear}}
        {{user.cost_tech}}
        {{user.cost_time}}
      </li>
    </ul>
    {{users[0]}}
  </div>
</template>

<script>
export default {
  data () {
    return {
      users: []
    }
  },
  created() {
    var _this = this
    this.$axios.get('/api/list', {}).then(function (response) {
      response.data.forEach(function(item, index) {
        _this.users.push({
          'name': item.name,
          'id': item.id,
          'area': item.area,
          'level': item.level,
          'cost_stone': item.cost_stone,
          'cost_metal': item.cost_metal,
          'cost_water': item.cost_water,
          'cost_plastic': item.cost_plastic,
          'cost_nuclear': item.cost_nuclear,
          'cost_tech': item.cost_tech,
          'cost_time': item.cost_time
        })
      })
    }).catch(function (error) {
      console.log(error)
    })
  }
}

</script>
<style lang='stylus' scoped>
  .architecture
    font-size 15px
</style>
