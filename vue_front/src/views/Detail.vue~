<template>
  <div class="Detail_Home">
    <div v-if='list'>
      <h1>{{ list.title }}</h1>
      <p>{{ list.body }}</p>
      <p>{{ list.created_at }}</p> 
    </div>
    <div v-else>
      <h1 class='Error_Text'>404 - Error</h1>
    </div>
  </div> 
</template>

<script>
import { apiService } from '@/common/api.service.js';

export default {
  name: 'Detail',
  props: {
    tag: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      list: {}
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getListData() {
      let endpoint = `/api/detail/${this.tag}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.list = data;
            this.setPageTitle(data.tag)
          } else {
            this.list = null;
            this.setPageTitle("404 - Page Not Found")
          }
      })    
    }
  },
  created() {
    this.getListData()
  }
}
</script>

