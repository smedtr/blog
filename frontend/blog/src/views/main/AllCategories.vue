<template>
  <div class="flex flex-col place-content-center place-items-center">
    <div class="py-8 border-b-2">
      <h1 class="text-5xl font-extrabold">All Categories</h1>
    </div>
    <div class="flex flex-wrap py-8">
      <router-link
        v-for="category in this.allCategories"
        :key="category.name"
        class=". . ."
        :to="`/category/${category.slug}`"
        >{{ category.name }}</router-link
      >
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PostList from "@/components/PostList.vue";
import { POSTS_BY_CATEGORY } from "@/queries";

export default {
  components: { PostList },
  name: "CategoryView",

  data() {
    return {
      postsByCategory: null,
    };
  },

  async created() {
    const posts = await this.$apollo.query({
      query: POSTS_BY_CATEGORY,
      variables: {
        category: this.$route.params.category,
      },
    });
    this.postsByCategory = posts.data.postsByCategory;
  },
};
</script>