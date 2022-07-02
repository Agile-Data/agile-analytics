<template>
  <svg :class="className">
    <use :href="'#icon-' + name"></use>
  </svg>
</template>
<script lang="ts">
import {defineComponent} from "vue";

export default defineComponent({
  name: 'SvgIcon',
  props: {
    name: {
      type: String,
      required: true
    },
    className: {
      type: String,
      required: true
    }
  },
  setup() {
    const req = require.context('@/assets/svg', true, /\.svg$/)
    // eslint-disable-next-line no-undef
    const requireAll = (requireContext: __WebpackModuleApi.RequireContext) => {
      return requireContext.keys().map(requireContext);
    }
    requireAll(req)
  }
})
</script>