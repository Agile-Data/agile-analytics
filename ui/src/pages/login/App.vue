<template>
  <div class="page page-center border-top-wide border-primary d-flex flex-column">
      <div class="container-tight py-4">
        <div class="text-center mb-2">
          <a href="." class="navbar-brand navbar-brand-autodark">
            <img src="@/assets/logo.png" height="48" alt="">
          </a>
        </div>
        <form class="card card-md" autocomplete="off">
          <div class="card-body">
            <h1 class="card-title text-center mb-4">登 录</h1>
            <div class="mb-3">
              <label class="form-label">帐号：</label>
              <input type="text" class="form-control" autocomplete="off">
            </div>
            <div class="mb-2">
              <label class="form-label">
                密码
              </label>
              <div class="input-group input-group-flat">
                <input type="password" class="form-control" autocomplete="off">
              </div>
            </div>
            <div class="form-footer">
              <button type="submit" class="btn btn-primary w-100">登 入</button>
            </div>
          </div>
        </form>
      </div>
    </div>
</template>

<script>
import "@/session"
import "@tabler/core/src/scss/tabler.scss"

export default {
}
</script>
