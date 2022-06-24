<template>
    <div>
        <b-container fluid>
            <b-row class="row">
                <div id="spell_name">
                    {{ spell.name }}
                </div>
            </b-row>
            <b-row class="row">
                <b-col class="col" cols="5">
                    <div class="title">Niveaux:</div>
                    <div class="data">{{ spell.niveau }}</div>
                </b-col>
                <b-col class="col" cols="7">
                    <div class="title">Composantes:</div>
                    <div class="data" style="margin-right 10px">{{ spell.comps }}</div>
                    <div class="data">{{ (spell.comps_det) }}</div>
                </b-col>
            </b-row>
            <b-row class="row">
                <b-col class="col" cols="5">
                    <div class="title">Portée:</div>
                    <div class="data">{{ spell.portee }}</div>
                </b-col>
                <b-col class="col" cols="7">
                    <div class="title">Temps d'incantation:</div>
                    <div class="data">{{ spell.t_incant }}</div>
                </b-col>
            </b-row>
            
            <b-row class="row">
                <b-col class="col" cols="5">
                    <div class="title">Durée:</div>
                    <div class="data">{{ spell.duree }}</div>
                </b-col>
                <b-col class="col" cols="7">
                    <div class="title">Jet de protection:</div>
                    <div class="data">{{ spell.protection }}</div>
                </b-col>
            </b-row>

            <b-row class="row">
                <b-col class="col">
                    <div class="title">Zone d'effet:</div>
                    <div class="data">{{ spell.zone_effet }}</div>
                </b-col>

            </b-row>

        </b-container>
        <b-container fluid>
            <div class="col title" id="Description">Description:</div>
            <div class="col" id="desc_corpse">{{ spell.description }}</div>
        </b-container>
    </div>
</template>

<script>

export default {
    mounted: function () {

        this.display_lvl()
    },
  methods: {
      /*display_lvl: function() {
          let lvls = ""
          if (this.$props.spell.lvl_mage !== "") {
              lvls += " Mage: " + this.$props.spell.lvl_mage + " "
          }
          if (this.$props.spell.lvl_illu !== "") {
              lvls += " Illusionniste: " + this.$props.spell.lvl_illu + " "
          }
          if (this.$props.spell.lvl_clerc !== "") {
              lvls += " Clerc: " + this.$props.spell.lvl_clerc + " "
          }
          if (this.$props.spell.lvl_druide !== "") {
              lvls += " Druide: " + this.$props.spell.lvl_druide + " "
          }
          this.$set(this,"lvls",lvls)
      }*/
  },
  props: {
    spell:{
        type: Object,
        required: true
    }
  },
  data: function () {
      return {
          lvls : ""
      }
  },
    name: "Spellcard"
}
</script>


<style scoped>
.col {
    text-align: left;
}

.row {
    margin-top: 10px;
}

#Description {
    margin-top: 15px;
    font-size: 45;
}

#spell_name {
    text-align: center;
    font-size: 6ch;
    font-weight: bold;
}

.title {
    font-weight:bold;
    font-size: 4ch;
    display: inline;
    margin-right: 30px;
}

.data {
    display: inline;
    font-size: 2.8ch;
}

#desc_corpse {
    font-size: 2.2ch;
}
</style>