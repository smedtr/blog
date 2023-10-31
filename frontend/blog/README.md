# blog

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Pending Issues

Uilezen van de isAuthenticated vanuit de store ipc local storage.

New post kunnen maken

Refresh gaan doen van de JWT : Zie ook https://jasonwatmore.com/vue-3-pinia-jwt-authentication-with-refresh-tokens-example-tutorial

Bij logout/login neemt de router de history -1 nu als dan het vorige scherm niet OK (vb login scherm) dan krijg je een verkeerd scherm.
Beter zou zijn om een vast of een conditioneel re-routing te gaan doen.

Bij het selecteren van All Categories en Tags -> pagineren. Dit is nu een dummy pagina

Ongoing : user/Account.vue mag verwijderd worden. Geen idee waar dit scherm voor dient is vervangen door Signup, Profile.

Done :Logout/Login : Signout Signin komt niet goed bv. signout keert hem terug naar het basis scherm waar de logout is gegeven. 
Done : New comment plaatsen bij een post
