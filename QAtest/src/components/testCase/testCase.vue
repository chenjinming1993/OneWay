<!--  -->
<template>
  <div class="testCase">
    <div class="testList">
      <el-table
        :data="tableData3"
        height="250"
        border
        style="width: 100%"
        :row-style="testsOk">
        <el-table-column
          prop="tests"
          label="tests"
          width="180">
        </el-table-column>
        <el-table-column
          prop="result"
          label="result"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="地址">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">通过</el-button>
            <el-button @click="handleClick2(scope.row)" type="text" size="small">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="addTest">
        <el-tag>添加</el-tag>
        <el-input v-model="inputValue" placeholder="请输入内容"></el-input>
        <el-button class="inputAdd" type="primary" @click="handleSubmit">提交</el-button>
      </div>
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
      inputValue: '',
      inputTest: {}
    }
  },
  methods: {
    handleSubmit() {
      if (this.inputValue === '') {
        alert('请输入信息')
        return
      }
      this.inputTest.tests = this.inputValue
      this.tableData3.push(this.inputTest)
      console.log(this.tableData3)
      this.inputTest = {}
      this.inputValue = ''
    },
    handleClick(row) {
      console.log(row)
      row.result = 'OK'
    },
    handleClick2(row) {
      console.log(row)
      row.result = 'noOK'
    },
    testsOk({row, rowIndex}) { // 如何改变行的样式？(3月7日成功实现)
      if (row.result === 'OK') {
        return 'background:pink'
      } else if (row.result === 'noOK') {
        return 'background:red'
      }
      return ''
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
      .addTest
        .inputAdd
          font-size 10px
          padding 8px 12px
</style>
