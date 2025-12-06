// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite";
export default defineNuxtConfig({
  compatibilityDate: '2025-03-22',
  devtools: { enabled: true },
  
  plugins: [
    '~/plugins/api.js', // Indiquer le chemin vers le fichier api.js
  ],
  components: [
    '~/components',          // Inclut tout le répertoire components
    '~/components/EventForm', // Inclut le sous-répertoire EventForm
  ],
  css: ['~/assets/css/main.css'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },

  // Si tu veux ajouter d'autres options globales à Axios, tu peux le faire ici.
  // Mais comme tu utilises un plugin pour la configuration, ce n'est pas nécessaire dans ce cas.
});