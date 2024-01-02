<template>
  <div class="all-tags">
    <h1 class="text-5xl font-extrabold mb-2">Tag Name : {{ $route.params.tag }}</h1>
    <p class="text-gray-500 text-lg mb-5">
      A blog created with Django, Vue.js and TailwindCSS
    </p>

    <post-list :posts="postsByTag"></post-list>

    <pages-footer :hasNextPage="this.hasNextPage" @nextPosts="next_posts('Next')" :hasPrevPage="this.hasPrevPage"></pages-footer>
    
  </div>
</template>

<script>
import { computed } from 'vue'
import { useQuery } from '@vue/apollo-composable'
import gql from 'graphql-tag'
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import PagesFooter from "@/components/PagFooter.vue";
import { POSTS_BY_TAG_PAG } from "@/queries";
import { ALL_CATEGORIES } from "@/queries";

export default {
  components: { PostList,PagesFooter },
  name: "TagView",

  data() {
    return {
      postsByTag: [],
      allCategories: [],
      hasPrevPage: false,
      hasNextPage: true,
      defaultNumberOfPosts: 5,
    };
  },

  methods: {
    prev_posts(message) {
      console.log("Tag.vue->prev_posts()-start:"+ message)   
      // https://vueschool.io/articles/vuejs-tutorials/infinite-scrolling-in-vue-with-apollo/
      console.log("Tag.vue->prev_posts()-end")
    },
    next_posts(message) {
      console.log("Tag.vue->prev_posts()-start:"+ message)       
      console.log("Tag.vue->prev_posts()-end")
    }
  },

  setup() {    
    //
  },
  
  async created() {  
    this.$apollo.query({
      query: POSTS_BY_TAG_PAG,
      variables: {
        tag: this.$route.params.tag,
        defaultNumberOfPosts: this.defaultNumberOfPosts,
        startCursor: this.endCursor,
      },
    }).then(posts => {   
      this.postsByTag_pag = posts.data.allPostsByTagPaginated.edges  
      this.postsByTag_pageinfo_pag = posts.data.allPostsByTagPaginated.pageInfo    
      
      this.postsByTag_pag.forEach(node => {           
        this.postsByTag.push(node.node)
      }); 
      this.hasNextPage = this.postsByTag_pageinfo_pag.hasNextPage
      this.hasPrevPage = this.postsByTag_pageinfo_pag.hasPrevPage
    }).else(
      console.log("Tag.vue-> created() POSTS_BY_TAG_PAG Error = "+ this.postsByTag_pag) 
    )  
    
  },
  
};
</script>
