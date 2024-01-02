<template>
  <div class="home">
    <h1 class="text-5xl font-extrabold mb-2">Recent Posts</h1>
    <p class="text-gray-500 text-lg mb-5">
      A blog created with Django, Vue.js and TailwindCSS
    </p>

    <post-list :posts="this.allPosts"></post-list>
    
    <pages-footer :hasNextPage="this.hasNextPage" @nextPosts="next_posts('Next')" :hasPrevPage="this.hasPrevPage"></pages-footer>


  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import PagesFooter from "@/components/PagFooter.vue";
import { ALL_POSTS_PAG } from "@/queries";


export default {
  components: { PostList, PagesFooter },
  name: "HomeView",

  methods: {
    //say: function (message) {
    next_posts(message) {      
      //alert(message + "->" +
      //      this.allPosts_pag_pageinfo.endCursor +
      //      " hasNextPage=" + this.allPosts_pag_pageinfo.hasNextPage)      
      if (this.allPosts_pag_pageinfo.hasNextPage) { 
        this.endCursor = this.allPosts_pag_pageinfo.endCursor      
        this.$apollo.query({
          variables: {
            defaultNumberOfPosts: this.defaultNumberOfPosts,
            startCursor: this.endCursor
          },
          query: ALL_POSTS_PAG,
        }).then(next_posts_pag => {          
          this.next_posts_pag = next_posts_pag.data.allPostsPaginated.edges        
          this.allPosts_pag_pageinfo = next_posts_pag.data.allPostsPaginated.pageInfo
            
          this.next_posts_pag.forEach(node => {      
            this.allPosts.push(node.node)
          });  

          this.hasNextPage = this.allPosts_pag_pageinfo.hasNextPage
        });   
      }   
      // https://vue-apollo.netlify.app/guide/apollo/queries.html#simple-query
      
      
    },

    prev_posts(message) {
      console.log("prev_posts()-start:"+ message)   
      console.log("prev_posts()-end")
    }
  },

  data() {
    return {
      allPosts: [], // return an empty array to please the prop definition
      defaultNumberOfPosts: 5, // returns by default number of posts
      startCursor: "", // returns from a specific cursor for paging 
      hasNextPage: false,
      hasPrevPage: false,
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
      this.allPosts.push(node.node)
    });       
    
    this.hasNextPage = this.allPosts_pag_pageinfo.hasNextPage
  },
};
</script>