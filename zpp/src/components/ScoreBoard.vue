<template>
  <div class="score-board">
    <h1> ZPP Is Modern </h1>
    <ScoreSlot
    :score='game.player1.score'
    :user='game.player1.user'
    ></ScoreSlot>
    <ScoreSlot
    :score='game.player2.score'
    :user='game.player2.user'
    ></ScoreSlot>
  </div>
</template>

<script>
import ScoreSlot from './ScoreSlot.vue';

export default {
  name: 'ScoreBoard',
  data: () => ({
    game: {},
  }),
  components: {
    ScoreSlot,
  },
  beforeMount() {
    
    this.game = {
      player1: {
        score: 0,
        user: {
          name: 'Andy',
          elo: 2000,
          wins: 15,
          losses: 5,
        },
      },
      player2: {
        score: 5,
        user: {
          name: 'Shando',
          elo: 1505,
          wins: 10,
          losses: 5,
        },
      },
    };
    document.addEventListener('click', (event) => {
      event.preventDefault();
      event.stopPropagation();
      this.game.player1.score++
    });
    document.addEventListener('contextmenu', (event) => {
      event.preventDefault();
      event.stopPropagation();
      this.game.player2.score++
    });
  },
};
</script>

<style>
</style>
