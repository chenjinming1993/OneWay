<!--  -->
<template>
  <div class="architecture">
    <ul>
      <li v-for="(user,index) in users" :key="index">
        {{user.name}}
      </li>
    </ul>
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
    this.$axios.get('/api/name', {}).then(function (response) {
      response.data.forEach(function(item, index) {
        this.users.push({
          'name': item.name
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
