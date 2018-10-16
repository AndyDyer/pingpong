<template>
  <div id="app">
    <GameClock/>
    <GameSettings
    v-if="!settingsSet"
    @done="startGame"/>
    <ScoreBoard
    v-if="gameReady"
    @game-over="gameOver"/>
  </div>
</template>

<script>
/* eslint-disable no-return-assign */
import ScoreBoard from './components/ScoreBoard.vue';
import GameClock from './components/GameClock.vue';
import GameSettings from './components/GameSettings.vue';

export default {
  name: 'app',
  data: () => ({
    settings: {},
    gameReady: true, // TODO change to false to start
    settingsSet: true, // TODO change to false to start
  }),
  components: {
    GameClock,
    ScoreBoard,
    GameSettings,
  },
  methods: {
    startGame() {
      this.settingsSet = true;
      this.gameReady = true;
    },
    gameOver(score1, score2) {
      this.gameReady = false;
      console.log(score1, score2);
      this.$nextTick()
        .then(() => this.gameReady = true);
      // TODO do some sort of summary screen
      // decide new game or not and
      // and then 5 seconds later start new game or save and reset
    },
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
