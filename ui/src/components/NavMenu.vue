<template>
  <li :class="[isActive ? 'active' : '', `nav-item`]">
    <a class="nav-link" :href="url">
        <span class="nav-link-icon d-md-none d-lg-inline-block">
          <svg-icon class-name="icon icon-tabler icon-tabler-layout-dashboard" :name="icon"/>
        </span>
      <span class="nav-link-title">{{ name }}</span>
    </a>
  </li>
</template>

<script lang="ts">
import {defineComponent} from "vue"
import SvgIcon from '@/components/SvgIcon.vue'

export default defineComponent({
  name: "NavMenu",
  props: {
    name: {
      type: String,
      required: true
    },
    url: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    }
  },
  components: {
    SvgIcon
  },
  computed: {
    isActive() {
      return location.pathname.endsWith(this.url)
    }
  }
})
</script>