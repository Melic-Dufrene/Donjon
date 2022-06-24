<template>
  <div>
    <div class="Searchbox">
      <b-form-input v-model="search_string" v-on:input="intuitive_search" id="searchbar" aria-placeholder="Search"></b-form-input>
      <div v-for="spell in propositions.items" :key="spell.name">
        <div class="suggest" v-on:click="select_spell($event,spell.name)">{{ spell.name }} ({{ spell.classe }})</div>
      </div>
    </div>
    <div v-if="spell_chosen">
      <Spellcard :spell="spell"/>
    </div>
  </div>
</template>

<script>
import Spellcard from './Spellcard.vue'
import spells from '../assets/output.json'

export default {
  components: { Spellcard },
  methods: {
    intuitive_search: function() {
      let propos = this.search_string === "" ? [] : spells.filter( item => item.name.toLocaleLowerCase().includes(this.search_string.toLocaleLowerCase()))
      console.log(propos)
      let props = []
      for (let i =0; i < Math.min(5,propos.length); i++) {
        props.push(propos[i])
      }
      this.$set(this.propositions,"items",props)
      return null
    },

    select_spell: function(event, spell_name) {
      this.$set(this, "search_string", "")
      this.$set(this.propositions,"items", [])
      this.$set(this,"spell_chosen",true)
      this.$set(this,"spell",spells.find(el => el.name === spell_name))
    },

  },
  data () {
    return {
      spell_chosen: false,
      spell :  {},
      search_string: "",
      propositions: {items: []}
    }
  },
  name: 'HelloWorld'
}
</script>

<style>
#searchbar {
  margin: 40px 40px 40px;
}

#Searchbox {
  margin: 40px;
}

.suggest {
  font-size: 22px;
}

.suggest:hover {
  background-color: gray;
  color:white;
}
</style>
