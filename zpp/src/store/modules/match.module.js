/* eslint-disable no-param-reassign */
import axios from 'axios';
import helpers from '../../helpers';


const state = {
  instance: {
    player1: {},
    player2: {},
    games: [],
    player1Wins: 0,
    player2Wins: 0,
  },
};


const mutations = {
  // eslint-disable-next-line no-shadow
  setMatch(state, { match }) {
    state.instance = helpers.deepCopy(match);
  },
  // eslint-disable-next-line no-shadow
  addGame(state, game) {
    state.instance.games.push(game);
  },
};

const actions = {
  recordGame({ commit }, game) {
    // check if match is over
    commit('addGame', game);
  },
  async queryUser({ commit }, { player1ID, player2ID }) {
    const response = await axios.get('http://127.0.0.1:5000/start-game', {
      params: {
        player1ID,
        player2ID,
      },
    });
    commit('setMatch', { match: response.data });
  },
};

export default {
  namespaced: true,
  state,
  // getters,
  actions,
  mutations,
};
