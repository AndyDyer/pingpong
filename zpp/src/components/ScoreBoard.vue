<template>
  <div class="score-board">
    <h1 v-if="gameOver == false"> Game {{gameData.gameNumber}} </h1>
    <h2 v-show="gameOver"> Game {{gameData.gameNumber}} is over! </h2>
    <h2> {{ matchData.player1Wins}} - {{ matchData.player2Wins }} </h2>
    <div class="score-slots-container">
      <ScoreSlot
      :score='leftPlayerScore'
      :user='gameData.player1'
      :service="service === 'leftPlayer'"
      ></ScoreSlot>
      <ScoreSlot
      :score='rightPlayerScore'
      :user='gameData.player2'
      :service="service === 'rightPlayer'"
      ></ScoreSlot>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-plusplus */
/* eslint-disable no-mixed-operators */
/* eslint-disable consistent-return */
import ScoreSlot from './ScoreSlot.vue';

export default {
  name: 'ScoreBoard',
  data: () => ({
    leftPlayerScore: 0,
    rightPlayerScore: 0,
    service: '',
  }),
  props: {
    gameData: {},
    matchData: {
      player1Wins: 0,
      player2Wins: 0,
      gamesList: [],
    },
  },
  components: {
    ScoreSlot,
  },
  computed: {
    totalScore() {
      return this.leftPlayerScore + this.rightPlayerScore;
    },
    inDeuce() {
      return this.leftPlayerScore >= 10 && this.rightPlayerScore >= 10;
    },
    gameOver() {
      if (this.inDeuce) {
        return Math.abs(this.leftPlayerScore - this.rightPlayerScore) === 2;
      }
      return this.leftPlayerScore > 10 || this.rightPlayerScore > 10;
    },
  },
  watch: {
    totalScore(newTotalScore, oldTotalScore) {
      if (this.inDeuce) {
        return this.flipService();
      }
      if (newTotalScore > oldTotalScore) {
        if (newTotalScore !== 0 && newTotalScore % this.divisor === 0) {
          return this.flipService();
        }
      } else if (oldTotalScore % this.divisor === 0) {
        return this.flipService();
      }
    },
    gameOver(val) {
      if (val) {
        this.$emit('game-over', this.leftPlayerScore, this.rightPlayerScore)
      }
    },
  },
  beforeMount() {
    this.service = Math.round(Math.random()) === 1 ? 'leftPlayer' : 'rightPlayer';
  
    document.addEventListener('keydown', (event) => {
      // event.preventDefault();
      // event.stopPropagation();
      this.onClick(event);
    });
  },
  created() {
    this.scoreMax = 11;
    this.divisor = 2;
  },
  methods: {
    scoreWithin(n) {
      return Math.abs(this.leftPlayerScore - this.rightPlayerScore) <= n;
    },
    flipService() {
      if (this.service === 'leftPlayer') {
        this.service = 'rightPlayer';
      } else {
        this.service = 'leftPlayer';
      }
    },
    onClick(event) {
      switch (event.which) {
        case 39: // right arrow
          this.rightPlayerScore++;
          break;

        case 37: // left arrow
          this.leftPlayerScore++;
          break;

        case 40: // down arrow
          this.rightPlayerScore--;
          break;

        case 38: // up arrow
          this.leftPlayerScore--;
          break;

        default:
          break;
      }
    },
  }
}

</script>

<style>
  .score-slots-container {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
  }
</style>
