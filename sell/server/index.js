const express = require('express')
const app = express()// 请求server
var appData = require('../data.json')// 加载本地数据文件
var seller = appData.seller// 获取对应的本地数据
var goods = appData.goods
var ratings = appData.ratings
var apiRoutes = express.Router()
app.use('/api', apiRoutes)// 通过路由请求数据
var server = require('http').createServer(app)

app.get('/api/seller', function (req, res) {
  res.json({
    errno: 0,
    data: seller
  })
})
app.get('/api/goods', function (req, res) {
  res.json({
    errno: 0,
    data: goods
  })
})
app.get('/api/ratings', function (req, res) {
  res.json({
    errno: 0,
    data: ratings
  })
})

server.listen(3001)
console.log('success listen at port:3001......')
