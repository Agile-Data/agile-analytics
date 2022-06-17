<template>
  <div id="login-box" class="h-screen flex justify-center items-center">
    <div class="bg-white shadow sm:rounded-md w-2/6 min-w-min h-96">
      <div class="flex justify-center" style="margin-top: -44px;">
        <img id="logo" src="@/assets/logo.png" class="shadow-sm rounded-full bg-white p-1">
      </div>
      <p class="flex justify-center mt-4 text-3xl text-gray-600	">
        Agile Analytics
      </p>
      <div class="px-16 mt-10">
        <form class="relative">
          <input
              class="focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-300 rounded-md px-5 py-2"
              type="text" aria-label="帐号" placeholder="帐号"/>
          <input
              class="mt-5 focus:border-green-500 focus:ring-1 focus:ring-green-500 focus:outline-none w-full text-sm text-black placeholder-gray-500 border border-gray-300 rounded-md px-5 py-2"
              type="password" aria-label="密码" placeholder="密码"/>
          <button
              class="mt-10 w-full inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
              type="submit">登 入
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import "@/index.css"
import "@/session"

export default {
  components: {}
}
</script>

<style>

#login-box #logo {
  width: 84px;
  height: 84px;
}

</style>
