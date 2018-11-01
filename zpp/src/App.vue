<template>
  <div id="app">
    <GameClock/>
    <!-- Matchover === true -->
    <h1 v-show="matchOver"> Match is over!</h1>
    <h1 v-show="matchOver"> {{ winner }} has won the match by a score of 
    {{ matchData.player1Wins}}-{{ matchData.player2Wins}}!</h1>
    <h2 v-show="matchOver"> To start a rematch, press Y. </h2>
    <h2 v-show="matchOver"> Game will reset in {{ time }} seconds. </h2>
    <!-- Intermission === true -->
    <h2 v-show="intermission"> {{ winner }} has won Game {{ gameData.gameNumber }}! </h2>
    <h2 v-show="intermission"> Final score: </h2>
    <div v-show="intermission" class="score"> {{ currentP1Score }}-{{ currentP2Score }} </div>
    <h2 v-show="intermission"> Next game starts in: {{ intermissionTime }} </h2>
    <!-- GameReady === true -->
    <GameSettings
    v-if="!settingsSet"
    @done="startGame"/>
    <ScoreBoard
    v-if="gameReady"
    :game-data="gameData"
    :match-data="matchData"
    :match-over="matchOver"
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
    matchOver: false,
    gameReady: true, // TODO change to false to start
    settingsSet: true, // TODO change to false to start
    gameData: {},
    matchData: {
      player1Wins: 0,
      player2Wins: 0,
      gamesList: [],
    },
    currentP1Score: 0,
    currentP2Score: 0,
    winner: '',
    intermissionTime: 5,
    time: 5,
    intermission: false,
  }),
  components: {
    GameClock,
    ScoreBoard,
    GameSettings,
  },
  watch:{
    matchOver(val) {
      if (val) {
        this.intermission = false;
        if (this.matchData.player1Wins > this.matchData.player2Wins) {
          this.winner = this.gameData.player1.name
        }else {
           this.winner = this.gameData.player2.name
        }
        document.addEventListener('keydown', (event) => {
          this.rematch(event);
        });
        setTimeout(this.countDownTime, 1000);
        setTimeout(this.hardReset, 5000);
        
       // still send data to server
      }
    },
  },
  // stubbed data below
  beforeMount(){
    this.gameData = {
      gameNumber: 1,
      player1: {
        name: 'P1',
        elo: 2000,
        wins: 15,
        losses: 5,
      },
      player2: {
        name: 'P2',
        elo: 1505,
        wins: 10,
        losses: 5,
      },
    };
    // stubbed data above
  },
  methods: {
    startGame() {
      this.settingsSet = true;
      this.gameReady = true;
    },
    gameOver(leftPlayerScore, rightPlayerScore) {
      setTimeout(this.countDownIntermission, 1000);
      this.gameReady = false;
      this.intermission = true;
      this.currentP1Score = leftPlayerScore;
      this.currentP2Score = rightPlayerScore;
      this.matchData.gamesList.push({
        player1: this.gameData.player1.name,
        player1Score: leftPlayerScore, 
        player2: this.gameData.player2.name,
        player2Score: rightPlayerScore, 
      });
      leftPlayerScore > rightPlayerScore ? this.winner = this.gameData.player1.name : this.winner = this.gameData.player2.name ;
      leftPlayerScore > rightPlayerScore ? this.matchData.player1Wins++ : this.matchData.player2Wins ++;
      if (this.matchData.player1Wins === 3 || this.matchData.player2Wins === 3) {
         this.$nextTick()
          .then(() => this.matchOver = true);
       
      }else {
        this.$nextTick()
          .then(() => setTimeout(this.nextGame, 5000));
      }
    },
    nextGame() {
      this.gameData.gameNumber++;
      this.gameReady = true;
      this.intermission = false;
      this.intermissionTime = 5;
    },
    matchRematch() {
      this.matchData.player1Wins = 0;
      this.matchData.player2Wins = 0;
      this.matchData.gamesList = [];
      this.matchOver = false;
      this.gameReady = true;
      this.time = 5;
      this.intermissionTime = 5;
      this.winner = '';
      this.gameData.gameNumber = 1;
    },
    hardReset() {
      if (this.gameReady === false) {
        this.matchOver = false;
        this.settingsSet = false;
        this.matchData.player1Wins = 0;
        this.matchData.player2Wins = 0;
        this.matchData.gamesList = [];
        this.time = 5;
        this.intermissionTime = 5;
        this.winner = '';
        this.gameData.gameNumber = 1;
      }
    },
     countDownIntermission() {
      if (this.gameReady === false) {
        this.intermissionTime--;
        if (this.intermissionTime > 1) {
          setTimeout(this.countDownIntermission, 1000);
        }
      }
    },
    countDownTime() {
      if (this.gameReady === false) {
        this.time--;
        if (this.time > 1) {
          setTimeout(this.countDownTime, 1000);
        }
      }
    },
    rematch(event) {
      switch (event.which) {
        case 89: // y
          this.matchRematch();
          break;

        default:
          break;
      }
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
