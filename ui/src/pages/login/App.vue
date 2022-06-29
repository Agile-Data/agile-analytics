<template>
  <border-top-wide-page>
      <div class="container-tight py-4">
        <div class="text-center mb-2">
          <a href="." class="navbar-brand navbar-brand-autodark">
            <img src="@/assets/logo.png" height="48" alt="">
          </a>
        </div>
        <form class="card card-md" autocomplete="off">
          <div class="card-body">
            <h2 class="card-title text-center mb-4">登 录</h2>
            <div class="mb-3">
              <label class="form-label">帐号：</label>
              <input type="input" class="form-control" autocomplete="off">
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
    </border-top-wide-page>
</template>

<script>
import "@/session"
import BorderTopWidePage from "@/components/BorderTopWidePage";

export default {
  components: {
    BorderTopWidePage
  }
}
</script>
