<template>
<div>
    <b-tabs content-class="mt-3" v-model="tabIndex" vertical pills justified lazy card>
        <b-tab title="Guerrier" active>
            <div v-on:click="select_class">
                <b-card title="Guerrier" :img-src="img_guerrier" img-alt="Image" img-left max-height="10cm">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Magicien">
            <div v-on:click="select_class">
                <b-card title="Mage" :img-src="img_mage" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Voleur">
            <div v-on:click="select_class">
                <b-card title="Voleur" :img-src="img_voleur" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Pretre">
            <div v-on:click="select_class">
                <b-card title="Pretre" :img-src="img_pretre" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Illusionniste">
            <div v-on:click="select_class">
                <b-card title="Illusionniste" :img-src="img_illusionniste" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Druide">
            <div v-on:click="select_class">
                <b-card title="Druide" :img-src="img_druide" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Ranger">
            <div v-on:click="select_class">
                <b-card title="Ranger" :img-src="img_ranger" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Paladin">
            <div v-on:click="select_class">
                <b-card title="Paladin" :img-src="img_paladin" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Assassin">
            <div v-on:click="select_class">
                <b-card title="Assassin" :img-src="img_assassin" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
        <b-tab title="Barde">
            <div v-on:click="select_class">
                <b-card title="Barde" :img-src="img_barde" img-alt="Image" img-left max-height="35rem">
                <b-card-text>
                    Ceci est le descriptif...
                </b-card-text>
                </b-card>
            </div>
        </b-tab>
    </b-tabs>
    <div class="container-center">
        <b-button size="lg" variant="outline-success" class="text-center" v-on:click="emit_class">Valider</b-button>
    </div>
    <div v-if="classes_choisies.items.length" class="container-center">
        <span>Classe(s) actuelle(s): </span><span v-for="(c,i) in classes_choisies.items" :key="c.id"> {{ c }} <span v-if="i+1 < classes_choisies.items.length">,</span></span>
    </div>
</div>
</template>


<script>
import img_guerrier from '@/assets/img/Guerrier1.jpg'
import img_mage from '@/assets/img/Mage1.jpg'
import img_voleur from '@/assets/img/Voleur1.png'
import img_pretre from '@/assets/img/Pretre1.jpg'
import img_illusionniste from '@/assets/img/Illusionniste1.jpg'
import img_ranger from '@/assets/img/Ranger1.jpg'
import img_druide from '@/assets/img/Druide1.jpg'
import img_paladin from '@/assets/img/Paladin1.jpg'
import img_assassin from '@/assets/img/Assassin1.jpg'
import img_barde from '@/assets/img/Barde1.jpg'



  export default {

  methods: {
      select_class: function () {
          let currentClass = this.classes[this.tabIndex]
          let already_chosen = false
          for (let i = 0; i < this.classes_choisies.items.length; i++) {
              if (currentClass === this.classes_choisies.items[i]) {
                  already_chosen = true
              }
          }
          if (already_chosen) {
            let ind = this.classes_choisies.items.indexOf(currentClass)
            let new_classes = this.classes_choisies.items
            if (ind > -1) {
                new_classes.splice(ind,1)
            }
            this.$set(this.classes_choisies,"items",new_classes)
            alert("Attention, vous avez déjà choisi cette classe, elle vient d'être supprimer de votre liste de choix")
          }
          else if (this.classes_choisies.items.length == 2) {
                alert("Vous ne pouvez choisir que 2 classes maximum.")
            } else {
                let new_classes = this.classes_choisies.items
                new_classes.push(currentClass)
                this.$set(this.classes_choisies,"items",new_classes)
            }
            console.log("Vous avez choisi la classe: " + currentClass +"    "+ this.classes_choisies.items)
            return null
      },
    emit_class: function () {
        this.$emit("submitClass",this.classes_choisies.items)
    }
  },
        data: function () {
            return {
                tabIndex: 1,
                classe: null,
                classe_limitation_table: [

                ]
            }
        }
    }

</script>

<style>
.container-center {
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card{
    border-radius: 4px;
    background: #fff;
    box-shadow: 0 6px 10px rgba(0,0,0,.08), 0 0 6px rgba(0,0,0,.05);
      transition: .3s transform cubic-bezier(.155,1.105,.295,1.12),.3s box-shadow,.3s -webkit-transform cubic-bezier(.155,1.105,.295,1.12);
  padding: 14px 80px 18px 36px;
  cursor: pointer;
}

.card:hover{
     transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0,0,0,.12), 0 4px 8px rgba(0,0,0,.06);
}
</style>
