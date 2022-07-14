<template>
  <page>
    <template v-slot:body>
      <div class="container-xl">
        <ul class="nav nav-bordered mb-4">
          <li class="nav-item">
            <a class="nav-link active" href="#database">数据库</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#users">用户</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#system-info">系统信息</a>
          </li>
        </ul>
        <div class="row">
        </div>
      </div>
    </template>
  </page>
</template>

<script>
import "../common.scss"
import "./main.scss"
import "@/session"
import Page from "@/pages/Page";

export default {
  components: {
    Page
  },

  methods: {
    select(tabName) {
      console.info(tabName)
    },
  }
}
</script>
