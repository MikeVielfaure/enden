import axios from 'axios';

export default defineNuxtPlugin(nuxtApp => {
  // Configuration d'axios
  const axiosInstance = axios.create({
    baseURL: 'http://localhost:8080',// Remplace par l'URL de ton API
    proxyHeaders: false,
    credentials: false 
  });

//   const axiosInstance = axios.create({
//     baseURL: 'http://localhost:8080', // Remplace par l'URL de ton API
//     timeout: 10000, // Délai d'attente de 10 secondes
//     headers: {
//       'Content-Type': 'application/json',
//       'Accept': 'application/json',
//     },
//   });

  // Si tu veux ajouter des en-têtes par défaut ou un token, tu peux le faire ici
  // axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${yourToken}`;
  const apiUrl = 'http://localhost:8080';
  // Utilisation d'Axios dans toute l'application via `nuxtApp.provide`
  nuxtApp.provide('axios', axiosInstance);
  nuxtApp.provide('apiUrl', apiUrl);
});




