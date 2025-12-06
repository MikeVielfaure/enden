
export default {
    data() {
      return {
        user: {
          email: "",
          mdp: ""
        }
      };
    },
    methods: {
      async handleLogin() {
        console.log('Connexion avec', this.user);
        console.log(JSON.stringify(this.user));
        // Appeler une API backend pour la connexion classique

        await fetch(`${this.$apiUrl}/login/`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.user),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Réponse:', data);
            // Gérer la réponse
        })
        .catch(error => console.error('Erreur:', error));
      },
      loginWithGoogle() {
        console.log('Connexion avec Google');
        // Redirection vers Google OAuth
        window.location.href = "https://accounts.google.com/o/oauth2/auth?...";
      }
    }
  };