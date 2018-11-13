import Vue from 'vue';
import Vuex from 'vuex';
import App from './App.vue';


Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    userData: {
      player1: {},
      player2: {},
    },
    playerOneScore: 0,
    playerTwoScore: 0,
    matchData: {
      player1Wins: 0,
      player2Wins: 0,
      gamesList: [],
    },
  },
  mutations: {
    increment(state, key) {
      state[key] += 1; // eslint-disable-line
    },
    decrement(state, key) {
      state[key] -= 1; // eslint-disable-line
    },
    setFlags(state, flags) {
      Object.keys(flags).forEach((key) => {
        state[key] = flags[key];  // eslint-disable-line
      });
    },
  },
  actions: {
    resetGame({ commit }) {
      commit('setFlags', {
        playerOneScore: 0,
        playerTwoScore: 0,
      });
    },
    incrementPlayerOneScore({ commit }) {
      commit('increment', 'playerOneScore');
    },
    incrementPlayerTwoScore({ commit }) {
      commit('increment', 'playerTwoScore');
    },
    decrementPlayerOneScore({ commit, state }) {
      if (state.playerOneScore !== 0) {
        commit('decrement', 'playerOneScore');
      }
    },
    decrementPlayerTwoScore({ commit, state }) {
      if (state.playerTwoScore !== 0) {
        commit('decrement', 'playerTwoScore');
      }
    },
  },
  getters: {},
});
Vue.config.productionTip = false;

new Vue({
  store,
  render: h => h(App),
}).$mount('#app');
