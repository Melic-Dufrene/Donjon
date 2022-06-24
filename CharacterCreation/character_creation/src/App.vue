<template>
  <div>
    <b-tabs content-class="mt-3" v-model="tabIndex" card justified>
        <b-tab title="Création de personnage" disabled></b-tab>
        <b-tab title="Nom et histoire" active><Nom @submitNom="initNom"/></b-tab>
        <b-tab title="Classe"><Classes @submitClass="initClass"/></b-tab>
        <b-tab title="Race"><Race /></b-tab>
        <b-tab title="Caractéristiques"></b-tab>
        <b-tab title="Inventaire"></b-tab>
    </b-tabs>
  </div>
    
</template>

<script>
import Nom from './components/Nom.vue'
import Classes from './components/Classes.vue'
import Race from './components/Race.vue'

export default {
  data () {
    return {
       tabIndex: 1,
       classe: [],
       name: '',
       history: ''
    }
  },
  methods: {
    initNom: function (name, history) {
      console.log(name + history)
    },
    initClass: function(classeList) {
      this.classe = classeList
      console.log(this.classe)
    }
  },
  name: 'App',
  components: {
    Nom,
    Classes,
    Race
  },

  
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
