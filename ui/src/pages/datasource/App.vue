<template>
  <overlap-page title="数据源">
    <template v-slot:page-body>
      <div class="container-xl">
        <div class="row row-deck row-cards">
          <div class="col-xl-12">
            <div class="card">
              <div class="card-body">
                <div class="d-flex align-items-center">
                  <split-panel style="height: 400px">
                    <panel min-size="20">1</panel>
                    <panel>test</panel>
                  </split-panel>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </overlap-page>
</template>

<script>
import "./main.scss"
import "@/session"
import {SplitPanel, Panel} from "@/components/splitpanel"
import OverlapPage from "@/pages/OverlapPage";

export default {
  components: {
    OverlapPage, SplitPanel, Panel
  }
}
</script>
