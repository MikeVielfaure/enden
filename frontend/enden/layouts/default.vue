<!-- layouts/default.vue -->
<template>
    <div>
      <!-- Header global -->
      <header>
        <h1>Bienvenue sur mon site</h1>
      </header>
  
      <!-- Le contenu de la page sera ici -->
      <main>
        <NuxtPage />
      </main>
  
      <!-- Footer global -->
      <footer>
        <p>© 2025 Mon Site</p>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    // Ce layout sera utilisé par défaut
  }
  </script>
  
  <style scoped>
  /* Ajoute ici ton style spécifique pour le layout */
  </style>