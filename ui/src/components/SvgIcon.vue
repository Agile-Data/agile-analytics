<template>
  <svg :class="className">
    <use :href="'#icon-' + name"></use>
  </svg>
</template>
<script>
export default {
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
    const requireAll = (requireContext) => {
      return requireContext.keys().map(requireContext);
    }
    requireAll(req)
  }
}
</script>