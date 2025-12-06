
<template>
    <div class="flex min-h-screen items-center justify-center bg-gray-100 p-6">
      <div class="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
        <h1 class="text-center text-2xl font-bold text-gray-800 mb-6">Se connecter</h1>
  
        <form @submit.prevent="handleLogin" class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700">Email</label>
            <input v-model="user.email"
                   type="email"
                   required
                   class="w-full rounded-lg border border-gray-300 bg-gray-50 p-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"/>
          </div>
  
          <div>
            <label class="block text-sm font-medium text-gray-700">Mot de passe</label>
            <input v-model="user.mdp"
                   type="password"
                   required
                   class="w-full rounded-lg border border-gray-300 bg-gray-50 p-3 text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"/>
          </div>
  
          <div class="flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-4">
            <button type="submit"
                    class="w-full transform rounded-lg bg-blue-600 px-6 py-3 font-bold text-white shadow-md transition duration-300 hover:scale-105 hover:bg-blue-700">
              Connexion
            </button>
          </div>
  
          <div class="relative my-4">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-300"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="bg-white px-2 text-gray-500">OU</span>
            </div>
          </div>
  
          <button @click="loginWithGoogle"
                  type="button"
                  class="w-full flex items-center justify-center space-x-2 rounded-lg bg-red-500 px-6 py-3 font-bold text-white shadow-md transition duration-300 hover:scale-105 hover:bg-red-600">
            <svg class="w-5 h-5" viewBox="0 0 48 48">
              <path fill="#4285F4" d="M24 9.5c3.84 0 7.1 1.34 9.5 3.55l7.05-7.06C36.47 2.06 30.7 0 24 0 14.64 0 6.56 5.4 2.48 13.35l8.46 6.56C13.04 14.6 18.08 9.5 24 9.5z"/>
              <path fill="#34A853" d="M46.15 24.5c0-1.38-.12-2.7-.35-4H24v8.5h12.9c-.65 3.22-2.52 5.93-5.35 7.74l8.18 6.38c4.78-4.43 7.42-10.96 7.42-18.62z"/>
              <path fill="#FBBC05" d="M10.94 28.6a14.5 14.5 0 01-.94-5.1c0-1.77.33-3.47.94-5.1l-8.46-6.56A23.9 23.9 0 000 24c0 3.85.9 7.5 2.48 10.75l8.46-6.55z"/>
              <path fill="#EA4335" d="M24 48c6.48 0 11.9-2.15 15.88-5.8l-8.18-6.38a14.5 14.5 0 01-21.16-7.21l-8.46 6.56C6.56 42.6 14.64 48 24 48z"/>
            </svg>
            <span>Se connecter avec Google</span>
          </button>
        </form>
      </div>
    </div>
  </template>

<script src="~/components/LoginForm/LoginFormController.js"></script>