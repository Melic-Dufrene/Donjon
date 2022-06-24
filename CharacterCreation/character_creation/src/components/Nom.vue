<template>
  <b-container fluid class="text-center">
    <div id="Nom" role="group">
      <b-form-group>
        <label for="input-live">Entrez votre nom</label>
        <b-form-input
          id="input-live"
          v-model="name"
        ></b-form-input>
      </b-form-group>
      <b-form-group>
        <label for="input-txt">Entrez un bref résumé de votre histoire</label>
        <b-form-textarea
          id="input-txt"
          v-model="history"
          rows="4"
          max-rows="4"
        ></b-form-textarea>
      </b-form-group>
    </div>
  <b-button v-on:click="emit" variant="outline-success">Valider</b-button>
  </b-container>
</template>

<script>

export default {

  methods: {
    emit () {
      this.$emit("submitNom",this.name,this.history)
    },
    onReset () {
      console.log("reset")
    }
  },
  data () {
    return {
      name: '',
      history: ''
    }
  },
  mounted: function () {

  }
}
</script>

<style>
#Nom {
    text-align: center;
}
#input-live,#input-txt {
  margin-top: 0.5cm;
  margin-bottom: 0.5cm;
}
</style>