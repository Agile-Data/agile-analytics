<template>
  <overlap-page>
    <template v-slot:page-body>
      <div class="container-xl full-page">
        <split-pane class="default-theme">
          <pane size="25" min-size="25">
            <left-pane/>
          </pane>
          <pane>
            <div class="card" style="flex: 1;">
              <div class="card-body">
                <div class="card-title">Basic info</div>
              </div>
            </div>
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
import LeftPane from "./LeftPane"


export default {
  components: {
    OverlapPage, SplitPane, Pane, LeftPane
  }
}
</script>
