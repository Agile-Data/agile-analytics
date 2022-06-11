<template>
  <div id="login-box" class="h-screen flex justify-center items-center">
    <div class="bg-white border border-gray-300 w-2/6 min-w-min h-96 rounded-md">
      <div class="flex justify-center" style="margin-top: -44px;">
        <img src="@/assets/logo.png" class="shadow-sm rounded-full bg-white" style="width:84px;height:84px;">
      </div>
      <div class="flex justify-center mt-4 text-xl">
        登录
      </div>
      <div class="px-16 mt-10">
        <form class="relative">
          <input
              class="focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-200 rounded-md px-5 py-2"
              type="text" aria-label="邮箱" placeholder="邮箱"/>
          <input
              class="mt-5 focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-200 rounded-md px-5 py-2"
              type="text" aria-label="验证码" placeholder="验证码"/>
          <button class="mt-10 transition duration-150 ease-in-out w-full rounded-md hover:bg-green-400 bg-green-500 text-white px-5 py-2" type="submit">确 定</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import "@/index.css"
import "./auth"

export default {
  components: {}
}
</script>

<style>
html, body, #app {
  height: 100%;
}
</style>
