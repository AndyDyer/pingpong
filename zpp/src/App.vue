<template>
  <div id="app">
    <GameClock/>
    <ScoreBoard/>
  </div>
</template>

<script>
import ScoreBoard from './components/ScoreBoard.vue';
import GameClock from './components/GameClock.vue';

export default {
  name: 'app',
  components: {
    GameClock,
    ScoreBoard
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
