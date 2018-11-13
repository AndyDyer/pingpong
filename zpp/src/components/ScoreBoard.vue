<template>
  <div class="score-board">
    <h2> Game {{matchData.gamesList.length + 1}}</h2>
    <div class="score-slots-container">
      <ScoreSlot
      :score='leftPlayerScore'
      :user='userData.player1'
      :service="service === 'leftPlayer'"
      ></ScoreSlot>
      <ScoreSlot
      :score='rightPlayerScore'
      :user='userData.player2'
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
import { mapActions } from 'vuex';

export default {
  name: 'ScoreBoard',
  data: () => ({
    service: '',
  }),
  props: {
    matchData: {},
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
        this.$emit('game-over', this.leftPlayerScore, this.rightPlayerScore);
      }
    },
  },
  beforeMount() {
    this.service = Math.round(Math.random()) === 1 ? 'leftPlayer' : 'rightPlayer';
    document.addEventListener('keydown', this.incrementPlayerOneScore); // temporary
  },
  created() { // settings
    this.scoreMax = 11;
    this.divisor = 2;
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.incrementPlayerOneScore);
  },
  methods: {
    flipService() {
      if (this.service === 'leftPlayer') {
        this.service = 'rightPlayer';
      } else {
        this.service = 'leftPlayer';
      }
    },
    onDoubleClick(event) {
      if (event.button === 0) {
        if (this.leftPlayerScore !== 0) {
          this.decrementPlayerOneScore();
        }
      } else if (this.rightPlayerScore !== 0) {
        this.decrementPlayerTwoScore();
      }
    },
    onClick(event) {
      if (event.button === 0) {
        this.incrementPlayerOneScore();
      } else {
        this.incrementPlayerTwoScore();
      }
    },
    ...mapActions(['incrementPlayerOneScore',
      'incrementPlayerTwoScore',
      'decrementPlayerOneScore',
      'decrementPlayerTwoScore',
    ]),
  },
};
</script>

<style>
  .score-slots-container {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
  }
</style>
