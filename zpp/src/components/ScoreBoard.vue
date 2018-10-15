<template>
  <div class="score-board">
    <h1> ZPP Is Modern </h1>
    <div class="score-slots-container">
      <ScoreSlot
      :score='leftPlayer.score'
      :user='leftPlayer.user'
      :service="service === 'leftPlayer'"
      ></ScoreSlot>
      <ScoreSlot
      :score='rightPlayer.score'
      :user='rightPlayer.user'
      :service="service === 'rightPlayer'"
      ></ScoreSlot>
    </div>
  </div>
</template>

<script>
import ScoreSlot from './ScoreSlot.vue';

export default {
  name: 'ScoreBoard',
  data: () => ({
    leftPlayer: {},
    rightPlayer: {},
    divisor: 5,
    service: '',
  }),
  components: {
    ScoreSlot,
  },
  computed: {
    totalScore() {
      return this.leftPlayer.score + this.rightPlayer.score;
    },
  },
  watch: {
    totalScore(newTotalScore, oldTotalScore) {
      if (newTotalScore > oldTotalScore) {
        if (newTotalScore !== 0 && newTotalScore % this.divisor === 0) {
          this.flipService();
        }
      } else if (oldTotalScore % this.divisor === 0) {
        this.flipService();
      }
    },
  },
  beforeMount() {
    this.service = Math.round(Math.random()) === 1 ? 'leftPlayer' : 'rightPlayer';
    // stubbed data below
    this.leftPlayer = {
      score: 0,
      user: {
        name: 'Andy',
        elo: 2000,
        wins: 15,
        losses: 5,
      },
    };
    this.rightPlayer = {
      score: 0,
      user: {
        name: 'Shando',
        elo: 1505,
        wins: 10,
        losses: 5,
      },
    };
    // stubbed data above
    document.addEventListener('keydown', (event) => {
      event.preventDefault();
      event.stopPropagation();
      this.onClick(event);
    });
  },
  methods: {
    flipService() {
      if (this.service === 'leftPlayer') {
        this.service = 'rightPlayer';
      } else {
        this.service = 'leftPlayer';
      }
    },
    onClick(event) {
      switch (event.which) {
        case 38: // up arrow
          this.leftPlayer.score = this.leftPlayer.score - 1;
          break;

        case 37: // left arrow
          this.leftPlayer.score = this.leftPlayer.score + 1;
          break;

        case 40: // down arrow
          this.rightPlayer.score = this.rightPlayer.score - 1;
          break;

        case 39: // right arrow
          this.rightPlayer.score = this.rightPlayer.score + 1;
          break;

        default:
          break;
      }
    },
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
