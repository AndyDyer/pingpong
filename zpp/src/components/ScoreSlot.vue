<template>
  <div class="score-slot">
    {{score}}
    {{user.name}}
    {{user.elo}}
    {{user.wins}}
    {{user.losses}}
    <div class="user-stats">
     
    </div>
  </div>
</template>

<script>
  export default {
  name: 'ScoreSlot',
  props: {
    score: {
      default: 0
    },
    user: {},
  },
  beforeMount() {
    // this.user = {
    //   name: 'Andy',
    //   elo: 2000,
    //   wins: 22,
    //   losses: 1,
    // }
  },
};
</script>

<style>
  li {
    color: black
  }
</style>
