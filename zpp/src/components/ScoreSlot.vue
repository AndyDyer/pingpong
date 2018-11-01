<template>
  <div class="score-slot">
    
    <div class="score">
      {{score}}
    </div>
    <span class="serve" v-show="service"> Serving </span>
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
  font-size: 20em;
  flex-grow: 2
}
.user-stats {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
}
.name {
  font-size: 5em;
  flex-grow: 2
}
.serve {
  font-size: 2em;
  font-weight: 600;
}
</style>
