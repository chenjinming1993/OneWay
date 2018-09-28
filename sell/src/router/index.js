import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
// import HelloWorld from '@/components/HelloWorld'
// import Sellheader from '../components/header/Sellheader'
import goods from '../components/table/goods'
import ratings from '../components/table/ratings'
import seller from '../components/table/seller'

import '../common/stylus/index.styl'

Vue.use(Router)
Vue.use(VueResource)

export default new Router({
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: 'goods'
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
