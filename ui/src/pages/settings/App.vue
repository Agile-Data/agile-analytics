<template>
  <page-body>
    <template v-slot:page-body>
      <div class="container-xl">
            <ul class="nav nav-bordered mb-4">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">View all</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Marketing</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Development</a>
              </li>
            </ul>
            <div class="row">
            </div>
          </div>
    </template>
  </page-body>
</template>

<script>
import "../common.scss"
import "./main.scss"
import "@/session"
import PageBody from "@/pages/PageBody";

export default {
  components: {
    PageBody
  }
}
</script>
