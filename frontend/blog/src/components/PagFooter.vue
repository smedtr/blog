<template>
  <div class="space-y-2 pt-6 pb-8 md:space-y-5">
      <nav class="flex justify-between">       
        <button rel="previous" :disabled="!hasPrevPage" @click="$emit('prevPosts')">Previous</button>
        <span>1 of 2</span>       
        <button rel="next" :disabled="!hasNextPage" @click="$emit('nextPosts')">Next</button>
        
      </nav>    
  </div>
</template>

<script>
export default {
  name: "PostListComponent",  
  props: {
    hasNextPage: {
      type: Boolean,
      required: true,    
    },
    hasPrevPage: {
      type: Boolean,
      required: true,  
    },
  },
  computed: {
    publishedPosts() {      
      //return this.posts.filter((post) => post.isPublished);
      return true;
    },
  },
  methods: {
    stripHTML(string) {
      return string.replace(/<\/?[^>]+>/gi, " ");
    },
   
  },
};
</script>