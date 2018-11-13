<template>
  <div id="app">
    <GameClock/>
    <GameSettings
      v-if="step === 'beforeMatch'"
      @done="startGame"/>
    <ScoreBoard
      v-if="step === 'inGame'"
      :user-data="userData"
      :match-data="matchData"
      @game-over="gameOver"
    />
    <GameSummary
      v-if="step === 'intermission'"
      player-1-score="player1Score"
      player-2-score="player2Score"
      @start-game="startGame"
      :user-data="userData"
    />
    <MatchSummary
      v-if="step === 'afterMatch'"
      :user-data="userData"
      :match-data="matchData"
    />
  </div>


</template>

<script>
/* eslint-disable no-return-assign */
import { mapActions } from 'vuex';

import ScoreBoard from './components/ScoreBoard.vue';
import GameClock from './components/GameClock.vue';
import GameSettings from './components/GameSettings.vue';
import GameSummary from './components/GameSummary.vue';
import MatchSummary from './components/MatchSummary.vue';

export default {
  name: 'app',
  data: () => ({
    step: 'inGame', // [beforeMatch, inGame, intermission, afterMatch] replace with vuex
    userData: {
      player1: {},
      player2: {},
    },
    player1Score: 0,
    player2Score: 0,
    matchData: {
      player1Wins: 0,
      player2Wins: 0,
      gamesList: [],
    },
  }),
  computed: {
    isMatchOver() {
      return this.matchData.player1Wins === 3 || this.matchData.player2Wins === 3;
    },
  },
  components: {
    GameClock,
    ScoreBoard,
    GameSettings,
    GameSummary,
    MatchSummary,
  },
  beforeMount() { // TODO delete
    this.userData = {
      player1: {
        name: 'Andy',
        elo: 2000,
        wins: 15,
        losses: 5,
      },
      player2: {
        name: 'Shando',
        elo: 1505,
        wins: 10,
        losses: 5,
      },
    };
  },
  methods: {
    startGame() {
      this.resetGame();
      this.step = 'inGame';
    },
    gameOver(score1, score2) {
      this.matchData.gamesList.push({
        player1Score: score1,
        player2Score: score2,
      });
      score1 > score2 ? this.matchData.player1Wins += 1 : this.matchData.player2Wins += 1; //eslint-disable-line
      if (this.isMatchOver) {
        this.step = 'afterMatch';
        return;
        // TODO send data to CRUD
      }
      this.step = 'intermission';
    },
    ...mapActions(['resetGame']),
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
