import Vue from 'vue';
import Vuex from 'vuex';

import match from './modules/match.module';

Vue.use(Vuex);
export default new Vuex.Store({
  modules: {
    match,
  },
});
