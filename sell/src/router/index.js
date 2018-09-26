import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Sellheader from '../components/header/Sellheader'
import goods from '../components/table/goods'
import ratings from '../components/table/ratings'
import seller from '../components/table/seller'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Sellheader',
      name: 'Sellheader',
      component: Sellheader
    },
    {
      path: '/goods',
      name: 'goods',
      component: goods
    },
    {
      path: '/ratings',
      name: 'ratings',
      component: ratings
    },
    {
      path: '/seller',
      name: 'seller',
      component: seller
    }
  ]
})
