<template>
  <div class="home">
    <h1 class="text-5xl font-extrabold mb-2">Recent Posts</h1>
    <p class="text-gray-500 text-lg mb-5">
      A blog created with Django, Vue.js and TailwindCSS
    </p>

    <post-list :posts="this.allPosts"></post-list>
  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import { ALL_POSTS_PAG } from "@/queries";

export default {
  components: { PostList },
  name: "HomeView",

  data() {
    return {
      allPosts: [], // return an empty array to please the prop definition
    };
  },

  async created() {
    // Query vervangen door een paginated query nu met default 10 items
    //const posts = await this.$apollo.query({
    //  query: ALL_POSTS,
    //});
    //this.allPosts = posts.data.allPosts;
    
    const posts_pag = await this.$apollo.query({
      query: ALL_POSTS_PAG,
    });
    this.allPosts_pag = posts_pag.data.allPostsPaginated.edges        
    this.allPosts_pag_pageinfo = posts_pag.data.allPostsPaginated.pageInfo
    //console.log(this.allPosts_pag)
    //console.log(this.allPosts_pag_pageinfo) 
    this.allPosts = []   
    this.allPosts_pag.forEach(node => {                
      //this.post = {        
      //  "cursor": node.cursor, 
      //  "data": node.node,
      //} 
      //this.allPostsPag.push(this.post)     
      this.allPosts.push(node.node)
    });       
    //console.log(this.allPosts)
  },
};
</script>