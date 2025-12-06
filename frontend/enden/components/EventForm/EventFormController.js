import EventValidator from "./EventValidator";
export default {
    props: {
      // Le modèle de données de l'événement (peut être vide pour la création)
      eventData: {
        type: Object,
        default: () => ({
          title: '',
          date: '',
          description: '',
        }),
      },
    },
    data() {
      return {
        event: { ...this.eventData }, // On initialise l'événement avec les props
        isEdit: !!this.eventData.id,  // Si l'ID est présent, on est en mode édition
      };
    },
    methods: {
      // Cette méthode sera appelée lors de la soumission du formulaire
      async handleSubmit() {
        try {
          if (this.isEdit) {
            // Si c'est un événement existant, on fait une requête PUT pour mettre à jour
            await this.updateEvent();
          } else {
            // Si c'est un nouvel événement, on fait une requête POST pour créer
            await this.createEvent();
          }
        } catch (error) {
          console.error('Erreur:', error);
        }
      },
      // Méthode pour créer un événement
      async createEvent() {
          console.log('CRRRRRRRRRRRR')
          // Appel API pour créer un événement (à adapter à ton API)

          fetch(`${this.$apiUrl}/events/`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.event),
            mode: 'no-cors',  // Envoi des données de l'événement
          })
            .then(response => response.json())  // Parse la réponse en JSON
            .then(data => {
              console.log('Réponse:', data);  // Affiche les données renvoyées par l'API
            })
            .catch(error => {
              console.error('Erreur:', error);  // Gère les erreurs
            });
        //   console.log('LLLLLLLLLLLLLLLL')
        //   console.log('Événement créé', response);
        //   this.$router.push('/events/'); // Rediriger après la création
        // } catch (error) {
        //   console.error('Erreur lors de la création', error);
        // }
      },
      // Méthode pour mettre à jour un événement
      async updateEvent() {
        try {
          // Appel API pour mettre à jour un événement existant
          const response = await this.$axios.put(`/events/${this.event.id}`, this.event);
          console.log('Événement mis à jour', response);
          this.$router.push('/events'); // Rediriger après la mise à jour
        } catch (error) {
          console.error('Erreur lors de la mise à jour', error);
        }
      },
      // Méthode pour supprimer un événement
      async handleDelete() {
        try {
          if (confirm('Êtes-vous sûr de vouloir supprimer cet événement ?')) {
            // Appel API pour supprimer l'événement
            await this.$axios.delete(`/events/${this.event.id}`);
            console.log('Événement supprimé');
            this.$router.push('/events'); // Rediriger après la suppression
          }
        } catch (error) {
          console.error('Erreur lors de la suppression', error);
        }
      },
    },
  };
  