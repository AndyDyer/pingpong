<template>
  <div class="game-clock">
    <p class="time">
      {{ time }}
    </p>
  </div>
</template>

<script>
export default {
  name: 'GameClock',
  data: () => ({
    time: '',
  }),
  beforeMount() {
    setInterval(() => {
      this.time = this.getTime();
    }, 1000);
  },
  methods: {
    getMinutes() {
      return `0${this.getDate().getMinutes()}`.slice(-2);
    },
    getHours() {
      return this.getDate().getHours();
    },
    getDate() {
      return new Date();
    },
    getSeconds() {
      return this.getDate().getSeconds();
    },
    getTime() {
      return `${this.getHours()}:${this.getMinutes()}`;
    },
  },
};
</script>

<style scoped>
.time {
  font-size: 4em
}
</style>
