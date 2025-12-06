<template>
    <div class="w-full max-w-xl bg-white p-8 rounded-lg shadow-lg">
      <h1 class="text-center text-3xl font-semibold text-gray-800 mb-8">
        {{ isEdit ? 'Modifier l\'événement' : 'Créer un nouvel événement' }}
      </h1>

      <form @submit.prevent="handleSubmit" class="space-y-6">
        
        <!-- Titre -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Titre</label>
          <input v-model="event.name"
                 type="text"
                 required
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Date de début -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Date de début</label>
          <input v-model="event.date_debut"
                 type="datetime-local"
                 required
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Date de fin -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Date de fin</label>
          <input v-model="event.date_fin"
                 type="datetime-local"
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Description -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Description</label>
          <textarea v-model="event.description"
                    required
                    class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"></textarea>
        </div>

        <!-- Ville -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Ville</label>
          <input v-model="event.ville"
                 type="text"
                 required
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Adresse -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Adresse</label>
          <input v-model="event.adresse"
                 type="text"
                 required
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Code Postal -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Code Postal</label>
          <input v-model="event.code_postal"
                 type="text"
                 required
                 class="w-full rounded-lg border border-gray-300 p-3 text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>

        <!-- Buttons -->
        <div class="flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-4">
          <button type="submit"
                  class="w-full rounded-lg bg-indigo-600 px-6 py-3 font-semibold text-white shadow-md transition duration-300 hover:bg-indigo-500">
            {{ isEdit ? 'Mettre à jour' : 'Créer' }}
          </button>

          <button v-if="isEdit"
                  type="button"
                  @click="handleDelete"
                  class="w-full rounded-lg bg-red-600 px-6 py-3 font-semibold text-white shadow-md transition duration-300 hover:bg-red-500">
            Supprimer l'événement
          </button>
        </div>
      </form>
    </div>
</template>

<script src="~/components/EventForm/EventFormController.js"></script>

<style scoped>
/* Styles modernisés */
.container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.event-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
  color: #444;
}

input, textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

textarea {
  resize: none;
}

.form-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.btn {
  padding: 10px 15px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.primary {
  background: #4CAF50;
  color: white;
}

.primary:hover {
  background: #45a049;
}

.danger {
  background: #e74c3c;
  color: white;
}

.danger:hover {
  background: #c0392b;
}

/* Responsive */
@media (max-width: 600px) {
  .container {
    width: 90%;
  }
  
  .form-buttons {
    flex-direction: column;
    gap: 10px;
  }
}
</style>
