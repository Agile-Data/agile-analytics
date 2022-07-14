<template>
  <page>
    <template>
      <div class="container-xl full-page">
        <split-pane class="default-theme">
          <pane size="25" min-size="25">
            <left-pane/>
          </pane>
          <pane>
            <div class="card-tabs ">
                  <!-- Cards navigation -->
                  <ul class="nav nav-tabs" role="tablist">
                    <li class="nav-item" role="presentation"><a href="#tab-top-1" class="nav-link" data-bs-toggle="tab" aria-selected="false" role="tab" tabindex="-1">字段</a></li>
                    <li class="nav-item" role="presentation"><a href="#tab-top-2" class="nav-link" data-bs-toggle="tab" aria-selected="false" role="tab" tabindex="-1">表</a></li>
                    <li class="nav-item" role="presentation"><a href="#tab-top-3" class="nav-link" data-bs-toggle="tab" aria-selected="false" role="tab" tabindex="-1">表关系</a></li>
                    <li class="nav-item" role="presentation"><a href="#tab-top-4" class="nav-link active" data-bs-toggle="tab" aria-selected="true" role="tab">Tab 4</a></li>
                  </ul>
                  <div class="tab-content">
                    <!-- Content of card #1 -->
                    <div id="tab-top-1" class="card tab-pane show" role="tabpanel">
                      <div class="card-body">
                        <div class="card-title">Content of tab #1</div>
                        <p class="text-muted">
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, alias aliquid distinctio dolorem expedita, fugiat hic magni molestiae molestias odit.
                        </p>
                      </div>
                    </div>
                    <!-- Content of card #2 -->
                    <div id="tab-top-2" class="card tab-pane" role="tabpanel">
                      <div class="card-body">
                        <div class="card-title">Content of tab #2</div>
                        <p class="text-muted">
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, alias aliquid distinctio dolorem expedita, fugiat hic magni molestiae molestias odit.
                        </p>
                      </div>
                    </div>
                    <!-- Content of card #3 -->
                    <div id="tab-top-3" class="card tab-pane" role="tabpanel">
                      <div class="card-body">
                        <div class="card-title">Content of tab #3</div>
                        <p class="text-muted">
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, alias aliquid distinctio dolorem expedita, fugiat hic magni molestiae molestias odit.
                        </p>
                      </div>
                    </div>
                    <!-- Content of card #4 -->
                    <div id="tab-top-4" class="card tab-pane active" role="tabpanel">
                      <div class="card-body">
                        <div class="card-title">Content of tab #4</div>
                        <p class="text-muted">
                          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci, alias aliquid distinctio dolorem expedita, fugiat hic magni molestiae molestias odit.
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
          </pane>
        </split-pane>
      </div>
    </template>
  </page>
</template>

<script>
import "./main.scss"
import "@/session"
import {SplitPane, Pane} from "@/components/split-pane"
import Page from "@/pages/Page";
// import {Tabs, Tab} from 'vue3-tabs-component';


export default {
  components: {
    Page, SplitPane, Pane
  }
}
</script>