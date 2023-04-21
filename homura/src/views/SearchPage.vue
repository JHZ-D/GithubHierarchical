<template>
  <n-space vertical size="large">
    <div>
  <n-layout>
    <n-layout-header bordered id="header">
      <n-space id="head-space" size="huge" align="baseline">
        <n-h1>Github层次化检索系统</n-h1>
        <n-tooltip trigger="hover">
          <template #trigger>
            <n-button ghost circle size="small" @click="showModal = true"><n-icon
                size="20"><help-icon /></n-icon></n-button>
          </template>
          {{ en ? "What is a learning entry?" : "什么是学习入口？" }}
        </n-tooltip>
      </n-space>
    </n-layout-header>
    <n-layout-content>
      <div id="search-container">
        <MultiSearchBread ></MultiSearchBread>
        <div id="search-space">
        <n-auto-complete
            id="search-input"
            :options="searchOptions"
            v-model:value="searchValue"
            size="large"
            placeholder="搜索仓库"
        />
        <n-button circle @click="onSearchClick">
            <template #icon>
            <n-icon><Search /></n-icon>
            </template>
        </n-button>
        </div>
      </div>
    </n-layout-content>
  </n-layout>
</div>
    <div class="card">
      <n-card title="搜索结果" size="huge">
        <!-- jQuery is a JavaScript framework designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. It is free, open-source software using the permissive MIT License. As of Aug 2022, jQuery is used by 77% of the 10 million most popular websites. Web analysis indicates that it is the most widely deployed JavaScript library by a large margin, having at least 3 to 4 times more usage than any other JavaScript library.
        <br><br><br>
        Wikipedia Link: <a href="https://en.wikipedia.org/wiki/JQuery">https://en.wikipedia.org/wiki/JQuery</a>
        <br><br>
        Github Topic Link: <a href="https://github.com/topics/jquery">https://github.com/topics/jquery</a> -->
        <n-grid :x-gap="12" :y-gap="8" :cols="4">
          <n-grid-item v-for="num in repodata.length" :key="num">
            <a :href="'https://github.com/'+repodata[num - 1]" target="_blank">
              <div :class="num % 2 === 0 ? 'light-green' : 'green'">{{ repodata[num - 1] }}</div>
            </a>
          </n-grid-item>
          <!-- <n-grid-item>
            <div class="green" />
          </n-grid-item>
          <n-grid-item>
            <div class="light-green" />
          </n-grid-item>
          <n-grid-item>
            <div class="green" />
          </n-grid-item>
          <n-grid-item>
            <div class="light-green" />
          </n-grid-item>
          <n-grid-item>
            <div class="green" />
          </n-grid-item>
          <n-grid-item>
            <div class="light-green" />
          </n-grid-item> -->
          <!-- <n-grid-item>
            <div class="green" />
          </n-grid-item> -->
        </n-grid>
      </n-card>
    </div>
</n-space>
</template>

<script>
import { defineComponent } from 'vue'
import { Search, TrashOutline, Help as HelpIcon } from '@vicons/ionicons5'
import { mapState, mapMutations } from 'vuex'
import MultiSearchBread from '../components/MultiSearchBread.vue'
import repodata from '@/assets/exrepos.json'

export default defineComponent({
  components: {
    Search,
    // MultilevelSelecter
    MultiSearchBread,
    HelpIcon
  },
  created () {
  },
  data () {
    return {
      searchValue: '',
      messageBox: undefined,
      literal_items: [],
      repodata: repodata
    }
  },
  methods: {
    async onSearchClick () {
      if (this.searchValue === '') {
        return
      }
      const paramObj = {
        query: this.searchValue
      }
      const literalRes = await this.$http.post(this.loadUrl, paramObj)
      const literalData = literalRes.data.data
      this.literal_items = literalData
      this.messageBox.success('thread info list loaded', { duration: 500 })
    },
    onViewClick (item) {
      this.set_id(item.id)
      this.set_section_id('')
      this.update_map(TrashOutline)
      this.set_show_map(false)
      this.$router.push('/roadmap')
    },
    ...mapMutations({
      set_id: 'set_current_center_node',
      set_section_id: 'set_current_section_id',
      set_show_map: 'set_map_show_mode',
      update_map: 'set_refresh_map'
    })
  },
  computed: {
    searchOptions () {
      return ['没做完', '是真的', '别想了'].map((suffix) => {
        const prefix = this.searchValue.split('@')[0]
        return {
          label: prefix + suffix,
          value: prefix + suffix
        }
      })
    },
    loadUrl () {
      return '/search/' + this.docName
    },
    loadConceptUrl () {
      return '/searchByConcept/' + this.docName
    },
    ...mapState({
      docName: 'doc_name',
      en: 'en'
    })
  }
})
</script>

<style>
#search-container {
    display: flex;
    justify-content: center;
    align-items: center;
    align-content: space-between;

    /* width: 50%; */
}

.card {
  padding: 10px;
  word-break: break-all;
  width: 80%;
  border-radius: 5px;
  box-shadow: 0px 0px 5px #888888;
  margin-bottom: 20px;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 3%;
}

.light-green {
  height: 108px;
  background-color: rgba(0, 128, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
}
.green {
  height: 108px;
  background-color: rgba(0, 128, 0, 0.24);
  display: flex;
  align-items: center;
  justify-content: center;
}

/* #search-space {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
    background-size: cover;
} */
</style>
