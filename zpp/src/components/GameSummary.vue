<template>
  <div class="game-summary">
    <h1> Starting Next Game in </h1>
    <h2 >  {{time}} </h2>
    <div class='score-slots-container'>
      <ScoreSlot
      :score="leftPlayerScore"
      :user="userData.player1"
      :winner='leftPlayerScore > rightPlayerScore'
      ></ScoreSlot>
      <ScoreSlot
      :score="rightPlayerScore"
      :user="userData.player2"
      :winner="leftPlayerScore < rightPlayerScore"
      ></ScoreSlot>
    </div>
  </div>
</template>

<script>
import ScoreSlot from './ScoreSlot.vue';

export default {
  name: 'GameSummary',
  data: () => ({
    time: 8,
  }),
  props: {
    userData: {},
  },
  components: {
    ScoreSlot,
  },
  computed: {
    leftPlayerScore() {
      return this.$store.state.playerOneScore;
    },
    rightPlayerScore() {
      return this.$store.state.playerTwoScore;
    },
  },
  watch: {
    time(val) {
      if (val === 0) {
        this.$emit('start-game');
      }
    },
  },
  methods: {
    countDownTime() {
      this.time -= 1;
      if (this.time > 0) {
        setTimeout(this.countDownTime, 1000);
      }
    },
  },
  mounted() {
    this.countDownTime();
  },
};
</script>

<style>

.score-slots-container {
    height: 70%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
  }
</style>
