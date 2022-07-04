<template>
  <overlap-page>
    <template v-slot:page-body>
      <div class="container-xl full-page">
        <split-pane class="default-theme">
          <pane size="25" min-size="25">
            <left-pane/>
          </pane>
          <pane>
            <tabs>
              <tab name="显示字段">
                First tab content
              </tab>
              <tab name="数据表">
                Second tab content
              </tab>
              <tab name="数据表关系">
                Third tab content
              </tab>
            </tabs>
          </pane>
        </split-pane>
      </div>
    </template>
  </overlap-page>
</template>

<script>
import "./main.scss"
import "@/session"
import {SplitPane, Pane} from "@/components/split-pane"
import OverlapPage from "@/pages/OverlapPage";
import LeftPane from "./left-pane"
import {Tabs, Tab} from 'vue3-tabs-component';


export default {
  components: {
    OverlapPage, SplitPane, Pane, LeftPane, Tabs, Tab
  }
}
</script>