import {
    ApolloClient,
    createHttpLink,
    InMemoryCache,
} from "@apollo/client/core";

// HTTP Connection to the API
const httpLink = createHttpLink({
    uri: "http://127.0.0.1:8000/graphql"
})

// Cache implementation
const cache = new InMemoryCache();

// Create the apollo client
const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
})

