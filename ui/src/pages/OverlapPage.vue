<template>
  <div class="page">
    <header class="navbar navbar-expand-md navbar-dark d-print-none">
      <div class="container-xl">
        <h1 class="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3">
          <a href="/">
            <img src="@/assets/logo_w.png" class="navbar-brand-image" style="height: 1.5em;">
          </a>
        </h1>
        <div class="navbar-nav flex-row order-md-last">
          <div class="nav-item">
            <a href="#" class="nav-link d-flex lh-1 text-reset p-0">
              <div class="col-auto">
                <span class="avatar avatar-sm avatar-rounded">王</span>
              </div>
              <div class="d-none d-xl-block ps-2">
                <div>王小二</div>
                <div class="mt-1 small text-muted">数据分析师</div>
              </div>
            </a>
          </div>
        </div>
        <div class="collapse navbar-collapse" id="navbar-menu">
          <div class="d-flex flex-column flex-md-row flex-fill align-items-stretch align-items-md-center">
            <ul class="navbar-nav">
              <nav-menu icon="home" url="/index.html" name="首页"/>
              <nav-menu icon="dashboard" url="/dashboard.html" name="数据面板"/>
              <nav-menu icon="search" url="/search.html" name="搜索"/>
              <nav-menu icon="database" url="/datasource.html" name="数据源"/>
              <nav-menu icon="settings" url="/settings.html" name="系统"/>
            </ul>
          </div>
        </div>
      </div>
    </header>
    <div class="page-wrapper">
      <div class="page-body">
        <slot name="page-body"></slot>
      </div>
    </div>
  </div>
</template>

<script>
import NavMenu from "@/components/NavMenu.vue";

export default {
  name: "OverlapPage",
  props: {
    title: {
      type: String,
      required: true
    }
  },
  components: {
    NavMenu
  }
}
</script>