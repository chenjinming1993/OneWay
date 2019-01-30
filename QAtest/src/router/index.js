import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import architecture from '../components/architecture/architecture'
import testCase from '../components/testCase/testCase'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: 'architecture'
    },
    {
      path: '/architecture',
      name: 'architecture',
      component: architecture
    },
    {
      path: '/testCase',
      name: '/testCase',
      component: testCase
    }
  ]
})
