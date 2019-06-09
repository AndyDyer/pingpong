<template>
  <div class="game-settings">
    <h1> GAME SETTINGS </h1>
    <input
    type="tel"
    autofocus
    v-model="player1Number"
    v-show="currentStep === 'player1Number'"
    ref="player1Number"
    />
    <input
    type="tel"
    autofocus
    v-model="player2Number"
    v-show="currentStep === 'player2Number'"
    ref="player2Number"
    />

  </div>
</template>

<script>
export default {
  name: 'GameSettings',
  data: () => ({
    player1Number: '',
    player2Number: '',
    currentStepIndex: 0,
    steps: ['player1Number', 'player2Number', 'done'],
  }),
  computed: {
    currentStep() {
      return this.steps[this.currentStepIndex];
    },
  },
  watch: {
    currentStep(val) {
      if (val === 'done') {
        this.callServer()
      }
    },
  },
  beforeMount() {
    document.addEventListener('keydown', this.cycleStep);
  },
  beforeDestroy() {
    document.removeEventListener('keydown', this.cycleStep);
  },
  methods: {
    callServer() { 
      // TODO put in call to flask server and emit
      this.$emit('done')
    },
    cycleStep(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        this.currentStepIndex = this.currentStepIndex + 1;
      } else if (e.key === 'Tab') {
         e.preventDefault();
        this.currentStepIndex = this.currentStepIndex - 1;
      }
    },
  },
};
</script>

<style scoped>

</style>
