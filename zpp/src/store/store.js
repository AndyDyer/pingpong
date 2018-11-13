import Vuex from 'vuex';

const store = new Vuex.Store({
  state: {
    userData: null,
    player1Score: 0,
    player2Score: 0,
    matchData: null,
  },
});

export default store;
