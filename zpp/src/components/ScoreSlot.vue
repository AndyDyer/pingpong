<template>
  <div class="score-slot">
    <div
      class="score"
      :class="{ underline: service, winner: winner }"
      > {{score}}
    </div>
    <div class="user-stats">
      <span class="name"> {{user.name}} </span>
      ELO: {{user.elo}}
      <span>
        {{user.wins}}W - {{user.losses}}L
      </span>
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
    winner: false,
  },
};
</script>

<style>
.score-slot {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.score {
  font-size: 12em;
  flex-grow: 2
}
.user-stats {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.winner {
  color: green;
}
.underline {
  text-decoration: underline;
}
.name {
  font-size: 5em;
  flex-grow: 2
}
</style>
