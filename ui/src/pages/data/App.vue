<template>
  <page>
    <template v-slot:body>
      <div class="container-xl full-page">
        <div class="card full-page">
          <div class="card-header">
            <ul class="nav nav-pills card-header-pills">
              <li class="nav-item">
                <router-link class="nav-link active" to="dataset"> 数据集 </router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="datasource"> 数据源 </router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#" tabindex="-1">
                  Disabled
                </a>
              </li>
            </ul>
          </div>
          <div class="card-body">
            <router-view/>
          </div>
        </div>
      </div>
    </template>
  </page>
</template>

<script>
import "./main.scss"
import "@/session"
// import {SplitPane, Pane} from "@/components/split-pane"
import Page from "@/pages/Page";


export default {
  components: {
    Page
  }
}
</script>