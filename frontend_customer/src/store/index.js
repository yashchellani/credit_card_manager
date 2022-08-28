import Vue from 'vue'
import Vuex from 'vuex'

// import example from './module-example'
import HighchartsVue from 'highcharts-vue'
import Stock from "highcharts/modules/stock";
import Highcharts from "highcharts";
// import example from './module-example'

Stock(Highcharts);
Vue.use(Vuex)
Vue.use(HighchartsVue)
// Highcharts.Pointer.prototype.reset = function () {
//   return undefined;
// };

Highcharts.setOptions({
  time: {
      useUTC: false
  }
});



/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      // example
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEBUGGING
  })

  return Store
}
