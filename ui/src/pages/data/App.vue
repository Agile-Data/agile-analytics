<template>
  <div id="login-box" class="h-screen flex justify-center items-center">
    <div class="bg-white shadow sm:rounded-md w-2/6 min-w-min h-96">
      <div class="flex justify-center" style="margin-top: -44px;">
        <img id="logo" src="@/assets/logo.png" class="shadow-sm rounded-full bg-white">
      </div>
      <div class="flex justify-center mt-4 text-xl">
        登 录
      </div>
      <div class="px-16 mt-10">
        <form class="relative">
          <input
              class="focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-300 rounded-md px-5 py-2"
              type="text" aria-label="邮箱" placeholder="邮箱"/>
          <input
              class="mt-5 focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-300 rounded-md px-5 py-2"
              type="text" aria-label="验证码" placeholder="验证码"/>
          <button
              class="mt-10 w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
              type="submit">确 定
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import "@/session"

export default {
  components: {}
}
</script>

<style>
html, body, #app {
  height: 100%;
}

#login-box #logo {
  width: 84px;
  height: 84px;
}
</style>
