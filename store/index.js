import Vuex from 'vuex'

const createStore = () => {
  return new Vuex.Store({
    state: {
      file: null
    },
    mutations: {
      updateFile (state, file) {
        state.file = file
      }
    },
    getters: {
      getFile (state) {
        return state.file
      }
    }
  })
}

export default createStore
