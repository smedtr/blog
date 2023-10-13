import { defineStore } from "pinia";


//export const useUserStore = defineStore({
export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    token: localStorage.getItem("token") || null,
    user: localStorage.getItem("user") || null,
    loggedIn: localStorage.getItem("loggedIn") || null,
  }),
  getters: {
    getToken:  (state) => state.token,
    getUser: (state) => JSON.parse(state.user),
    getIsLoggedIn : (state) => state.loggedIn,
  },
  actions: {
    setToken(token) {
      this.token = token;
      this.loggedIn = true;

      // Save token to local storage
      localStorage.setItem("token", this.token);
      localStorage.setItem("loggedIn", this.loggedIn);
    },
    removeToken() {
      this.token = null;
      this.loggedIn = null;

      // Delete token from local storage
      localStorage.removeItem("token");
      localStorage.removeItem("loggedIn");
    },
    setUser(user) {
      this.user = JSON.stringify(user);

      // Save user to local storage
      localStorage.setItem("user", this.user);
    },
    removeUser() {
      this.user = null;
      this.loggedIn = null;

      // Delete user from local storage
      localStorage.removeItem("user");
      localStorage.removeItem("loggedIn");
    },
  },
});