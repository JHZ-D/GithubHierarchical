<template>
  <div class="search-page">
    <n-space vertical size="large" class="space-back">
      <div style="background-color: rgba(255, 255, 255, 0.1);">
        <n-layout>
          <n-layout-header bordered id="header" style="background-color: rgba(118, 190, 204,0.9);">
            <n-space id="head-space" size="huge" align="baseline">
              <n-h1>Github层次化检索系统</n-h1>
                <n-tooltip trigger="hover">
                  <template #trigger>
                    <n-button ghost circle size="small" @click="showModal = true"><n-icon
                    size="20"><help-icon /></n-icon></n-button>
                  </template>
                  帮助
                </n-tooltip>
            </n-space>
          </n-layout-header>
        </n-layout>
          <!-- <n-layout-content class="headerasearch" style="background-color: rgba(144, 215, 236,0.7);"> -->
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
          <!-- </n-layout-content> -->
      </div>
      <!-- <div class="card">
        <n-card title="搜索结果" size="huge" style="background-color:rgba(255, 255, 255,0.2);">
          <n-grid :x-gap="12" :y-gap="8" :cols="4">
            <n-grid-item v-for="num in repodata.length" :key="num">
              <a :href="'https://github.com/'+repodata[num - 1]" target="_blank">
                <div :class="num % 2 === 0 ? 'light-green' : 'green'">{{ repodata[num - 1] }}</div>
              </a>
            </n-grid-item>
          </n-grid>
        </n-card>
      </div> -->
      <!-- <n-table :single-line="false">
    <thead>
      <tr>
        <th>Repository</th>
        <th>Description</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="num in ">
        <td>放弃</td>
        <td>反常的</td>
        <td>彻底废除</td>
        <td>...</td>
        <td>干！我刚才背的是啥</td>
      </tr>
      <tr>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
        <td>...</td>
      </tr>
    </tbody>
  </n-table> -->
  <n-data-table style="height: 500px; width: 1500px; margin: 50px auto; --td-padding: 15px; --th-padding: 17px" :columns="columns" :data="repodata" :pagination="pagination" flex-height />
    </n-space>
  </div>
</template>

<script>
import { defineComponent, reactive } from 'vue'
import { Search, TrashOutline, Help as HelpIcon } from '@vicons/ionicons5'
import { mapState, mapMutations } from 'vuex'
import MultiSearchBread from '../components/MultiSearchBread.vue'
import repodata from '@/assets/exrepos.json'

// const tableData = Array.from(repodata).map((item, index) => ({
//   key: index,
//   reponame: item
// }))
const columns = [
  {
    title: 'Repository',
    width: 400,
    key: 'reponame'
  },
  {
    title: 'Description',
    width: 1000,
    key: 'description'
  }
]

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
  setup () {
    const paginationReactive = reactive({
      page: 1,
      pageSize: 10,
      // showSizePicker: true,
      // pageSizes: [3, 5, 7],
      onChange: (page) => {
        paginationReactive.page = page
      },
      onUpdatePageSize: (pageSize) => {
        paginationReactive.pageSize = pageSize
        paginationReactive.page = 1
      }
    })
    return {
      columns,
      pagination: paginationReactive
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
    margin-top: 20px;
    margin-bottom: 5px;
    /* width: 50%; */
}

#head-space{
  height:50px !important;
  margin-top: 0 !important;
}
.card {
  padding: 10px;
  word-break: break-all;
  width: 80%;
  height: 80%;
  border-radius: 5px;
  box-shadow: 0px 0px 5px #888888;
  margin-bottom: 20px;
  margin-left: 10%;
  margin-right: 10%;
  margin-top: 2%;
  /* background-color: blueviolet;
  color: aquamarine; */
}

.light-green {
  height: 90px;
  background-color: rgba(0, 128, 0, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
}
.green {
  height: 90px;
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

.search-page {
  background: url("../assets/backgd.jpg");
  width: 100%;
  height: 100%;
  background-size: cover;
  background-attachment:fixed;
}

.space-back {
  background: url("../assets/backgd.jpg");
  background-size: cover;
  background-attachment:fixed;
  margin-bottom: 0;
}

.headerasearch {
  background-color:rgba(220,38,38,0.2);
  /* margin-top: -10px; */
}
</style>
