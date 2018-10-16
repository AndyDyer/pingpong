<template>
  <div class="score-slot">
    {{score}}
    {{user.name}}
    {{user.elo}}
    {{user.wins}}
    {{user.losses}}
    {{service}} Service
    <div class="user-stats">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ScoreSlot',
  props: {
    score: 0,
    user: {},
    service: false,
  },
  beforeMount() {
  },
};
</script>

<style>
</style>
