<!--  -->
<template>
  <div class="testCase">
    <div class="testList">
      <el-table
        :data="tableData3"
        height="250"
        border
        style="width: 100%">
        <el-table-column
          prop="tests"
          label="测试点"
          width="180">
        </el-table-column>
        <el-table-column
          prop="result"
          label="测试结果"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
      </el-table>
      <div>添加</div>
      <el-input v-model="input" placeholder="请输入内容"></el-input>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData3: [{
        tests: '2016-05-03',
        result: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      },
      {
        tests: '2016-05-03',
        result: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }],
      input: ''
    }
  }
}

</script>
<style lang='stylus' scoped>
  .testCase
    position fixed
    top 0
    left 0
    width 100%
    height 100%
    z-index 10
    background #fff
    .testList
      width 800px
      height auto
      margin 0 auto
</style>
