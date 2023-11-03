<template>
  <div class="home">
    <h1 class="text-5xl font-extrabold mb-2">Recent Posts</h1>
    <p class="text-gray-500 text-lg mb-5">
      A blog created with Django, Vue.js and TailwindCSS
    </p>

    <post-list :posts="this.allPosts"></post-list>

    <div class="space-y-2 pt-6 pb-8 md:space-y-5">
      <nav class="flex justify-between">
        <button rel="previous">Previous</button>
        <span>1 of 2</span>
        <button rel="next">Next</button>
      </nav>
    </div>
  

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
      defaultNumberOfPosts: 5, // returns by default number of posts
      startCursor: "" // returns from a specific cursor for paging 
    };
  },

  async created() {    
    const posts_pag = await this.$apollo.query({
      variables: {
        defaultNumberOfPosts: this.defaultNumberOfPosts,
        startCursor: this.startCursor
      },
      query: ALL_POSTS_PAG,
    });
    this.allPosts_pag = posts_pag.data.allPostsPaginated.edges        
    this.allPosts_pag_pageinfo = posts_pag.data.allPostsPaginated.pageInfo
    
    console.log(this.allPosts_pag_pageinfo)     
    console.log(`defaultNumberOfPosts= ` + this.defaultNumberOfPosts)
    console.log(`startCursor= ` + this.startCursor)
    console.log(`lastCursor= ` + this.allPosts_pag_pageinfo.endCursor)
      
    this.allPosts_pag.forEach(node => {                
      //this.post = {        
      //  "cursor": node.cursor, 
      //  "data": node.node,
      //} 
      //this.allPostsPag.push(this.post)     
      this.allPosts.push(node.node)
    });       
    
  },
};
</script>