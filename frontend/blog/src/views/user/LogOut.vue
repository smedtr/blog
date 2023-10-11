<template>
    <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
      <div class="flex flex-col justify-between h-screen">
        <header class="flex flex-row items-center justify-between py-10">
            <p class="text-gray-500 text-lg mb-5">
                You are logged out now. 
            </p>                    
        </header>
      </div>
    </div>
  </template>
  
  <script>  
  import { useUserStore } from "@/stores/user";
  
  export default {
    setup() {
      const userStore = useUserStore();    
      return { userStore };
    },
  
    data() {    
      return {
        menuOpen: false,
        mySite: null,
        user: {
          isAuthenticated: this.userStore.getIsLoggedIn || null,
          token: this.userStore.getToken || "",
          info: this.userStore.getUser || {},
        },
        dataLoaded: false,      
      };
      
    },
  
    async created() {      
        this.userStore.removeToken();
        this.userStore.removeUser();                
    },
  
    
  };
  </script>
  