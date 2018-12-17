const db = require('./db.js')

const mysql = require('mysql')

var conn = mysql.createConnection(db.mysql)
conn.connect()

const express = require('express')
const app = express()
app.use(express.static('../dist'))
var server = require('http').createServer(app)

// app.get('/api/name', function (req, res) {
//   conn.query('select name from architecture', function (error, results, fields) {
//     if (error) throw error
//     res.json(results)
//   })
// })

app.get('/api/list', function (req, res) {
  conn.query('select * from architecture', function (error, results, fields) {
    if (error) throw error
    res.json(results)
  })
})

server.listen(3000)
console.log('success listen at port:3000......')
