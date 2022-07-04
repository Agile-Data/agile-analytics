<template>
  <div class="card" style="flex: 1;">
    <div class="card-header">
      <div class="row d-lg-flex">
        <h3 class="card-title">数据源</h3>
      </div>
    </div>
    <div class="list-group card-list-group overflow-auto" style="max-height: 35rem">
      <div class="list-group-item active">
        <div class="row">
          <div class="col-auto">
            <a href="#">
              <span class="avatar" style="background-image: url(./static/avatars/023f.jpg)"></span>
            </a>
          </div>
          <div class="col text-truncate">
            <a href="#" class="text-body d-block">Clickhouse 数据源</a>
            <div class="text-muted text-truncate mt-n1">
              clickhouse://192.168.1.10@8123/nql
            </div>
          </div>
        </div>
      </div>
      <div class="list-group-item">
        <div class="row">
          <div class="col-auto">
            <a href="#">
              <span class="avatar" style="background-image: url(./static/avatars/023f.jpg)"></span>
            </a>
          </div>
          <div class="col text-truncate">
            <a href="#" class="text-body d-block">PostgreSQL 数据源</a>
            <div class="text-muted text-truncate mt-n1">
              clickhouse://192.168.1.10@8123/nql
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeftPane"
}
</script>
