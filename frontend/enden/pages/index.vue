<template>
    <div>
        <div>
            Test Composant
        </div>
      <!-- Appel du composant EventForm -->
      <LoginForm  />
    </div>
  </template>
  
  <script>
  // 1. Importer le composant EventForm
  import EventForm from '~/components/EventForm/EventForm.vue';
  
  export default {
    // 2. Déclarer le composant dans la section 'components'
    components: {
      EventForm,
    },
    data() {
      return {
        // 3. Passer des données au composant via la prop eventData
        eventData: {
          title: 'Nouvel Événement',
          date: '2025-03-23',
          description: 'Description de l\'événement.',
          id: null, // Null pour un nouvel événement
        },
      };
    },
  };
  </script>
  
  <style scoped>
  /* Ton style spécifique pour index.vue ici */
  </style>
  