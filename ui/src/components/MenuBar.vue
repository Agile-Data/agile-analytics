<template>
  <div class="collapse navbar-collapse" id="navbar-menu">
    <div class="d-flex flex-column flex-md-row flex-fill align-items-stretch align-items-md-center">
      <ul class="navbar-nav">
        <Menu icon="home" url="/index.html" name="首页"/>
        <Menu icon="dashboard" url="/index.html" name="数据面板"/>
        <Menu icon="search" url="/index.html" name="搜索"/>
        <Menu icon="database" url="/index.html" name="数据源"/>
        <Menu icon="setting" url="/index.html" name="系统"/>
      </ul>
    </div>
  </div>
</template>

<script>

import Menu from "@/components/Menu"

export default {
  name: "MainMenu",
  components: {
    Menu
  }
}
</script>