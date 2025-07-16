<script setup>
import { ref } from 'vue'
import { axios } from '@/common/api.service.js'
import { endpoints } from '@/common/endpoints'

const questions = ref([])
const isLoading = ref(false)
const error = ref('')

async function getQuestions() {
  error.value = ''
  isLoading.value = true
  
  try {
    const endpoint = endpoints.questionCRUD
    const response = await axios.get(endpoint)
    
    if (response.data && Array.isArray(response.data)) {
      questions.value = response.data
    } else {
      questions.value = []
      error.value = 'Formato dati non valido ricevuto dal server'
    }
    
    console.log('Domande caricate:', response.data)
    
  } catch (err) {
    console.error('Errore nel caricamento delle domande:', err)
    
    if (err.response) {
      error.value = `Errore ${err.response.status}: ${err.response.statusText}`
    } else if (err.request) {
      error.value = 'Errore di connessione. Controlla la tua connessione internet.'
    } else {
      error.value = err.message || 'Errore sconosciuto'
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <main>
    <button 
      @click="getQuestions" 
      :disabled="isLoading"
      class="btn btn-primary"
    >
      {{ isLoading ? 'Caricamento...' : 'Carica Domande' }}
    </button>
    
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
    
    <div v-if="questions.length > 0" class="questions-container">
      <h2>Domande caricate:</h2>
      <ul>
        <li v-for="question in questions" :key="question.id">
          {{ question.content }}
        </li>
      </ul>
    </div>
    
    <div v-else-if="!isLoading && !error" class="no-questions">
      Nessuna domanda disponibile.
    </div>
  </main>
</template>

<style scoped>
.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background-color: #0056b3;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
  padding: 10px;
  margin: 10px 0;
  border-radius: 4px;
}

.questions-container {
  margin-top: 20px;
}

.questions-container h2 {
  color: #333;
  margin-bottom: 15px;
}

.questions-container ul {
  list-style-type: none;
  padding: 0;
}

.questions-container li {
  background-color: #f8f9fa;
  padding: 10px;
  margin: 5px 0;
  border-radius: 4px;
  border-left: 4px solid #007bff;
}

.no-questions {
  color: #6c757d;
  font-style: italic;
  margin-top: 20px;
}
</style>