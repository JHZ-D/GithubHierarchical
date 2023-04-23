<template>
  <div id="SectionWhole">
  <n-layout style="background-color: rgba(255, 255, 255, 0);">
    <n-layout-header bordered id="header">
      <n-space id="head-space" size="huge" align="baseline">
        <n-h1>Github层次化学习系统</n-h1>
        <n-tooltip trigger="hover">
          <template #trigger>
            <n-button ghost circle size="small" @click="showModal = true"><n-icon
                size="20"><help-icon /></n-icon></n-button>
          </template>
          帮助
        </n-tooltip>
      </n-space>
    </n-layout-header>
    <n-grid :cols="4" :rows="1" :col-gap="32" :row-gap="16" class="grid">
      <n-grid-item span="3">
          <div class="g6-x" id="containerG6" ref="containerG6"><img id="image" src="../assets/legendnew.gif" width="200" /></div>
      </n-grid-item>
      <n-grid-item span="1">
        <n-grid :cols="1" :rows="2" :row-gap="16" class="mygrid">
          <n-grid-item span="1">
            <n-card title="jQuery" size="huge" class="mycard">
              jQuery is a JavaScript framework designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. It is free, open-source software using the permissive MIT License. As of Aug 2022, jQuery is used by 77% of the 10 million most popular websites. Web analysis indicates that it is the most widely deployed JavaScript library by a large margin, having at least 3 to 4 times more usage than any other JavaScript library.
              <br><br><br>
              Wikipedia Link: <a href="https://en.wikipedia.org/wiki/JQuery">https://en.wikipedia.org/wiki/JQuery</a>
              <br><br>
              Github Topic Link: <a href="https://github.com/topics/jquery">https://github.com/topics/jquery</a>
            </n-card>
          </n-grid-item>
          <n-grid-item span="1">
        </n-grid-item>
        </n-grid>
      </n-grid-item>
    </n-grid>
    <!-- <Legend></Legend> -->
    <!-- <n-layout style="height: 93vh;"> -->
      <!-- <div class="waterfall-container" @scroll="handleScroll"> -->
        <n-modal v-model:show="showModal">
          <n-card style="width: 600px;" title="如何使用" :bordered="false"
            size="huge">
            <p>下图是本系统提供的基于Wikipedia和Github的软件开发领域知识图的一部分。通过之前的搜索或点击，您来到了黄圈所代表的知识点所在位置。</p>
            <p>图中的每个椭圆代表一个Wikipedia软件开发领域的知识，每个圆代表一个Github Topic所代表的知识。本系统将它们联系起来，体现在一张图中。</p>
            <p>您可以在下图中选择与本知识点相关的其他知识点跳转到相应页面进行学习。</p>
            <p>知识图右方的卡片提供了本知识点的简要介绍，并提供了相应的Wikipedia或Github链接，您也可以通过链接跳转到对应网站进行详细学习。</p>
            <!-- <n-gradient-text :size="18">注意事项</n-gradient-text> -->
            <br/><p style="font-size: medium;">注意事项</p>
            <p>如果您对这些概念都掌握得比较好，您可以尝试我们提供的<router-link class="link" to="/search"><n-gradient-text
                  type="info">搜索功能</n-gradient-text></router-link>来寻找与自己感兴趣主题相关的Github仓库。</p>
          </n-card>
        </n-modal>
        <!-- <div class="waterfall-content">
          <div class="piping" ref="piping0">
          </div>
          <div class="piping" ref="piping1">
          </div>
          <div class="piping" ref="piping2">
          </div>
          <div class="piping" ref="piping3">
          </div>
        </div> -->
      <!-- </div> -->
    <!-- </n-layout> -->
  </n-layout>
</div>
</template>

<script>
import { defineComponent, h } from 'vue'
// import SectionCard from './SectionCard'
// import store from '../store'
// import router from '../router'
import { useNotification, NAvatar } from 'naive-ui'
import { Help as HelpIcon } from '@vicons/ionicons5'
import { mapState } from 'vuex'
import G6 from '@antv/g6'
import graphdata from '@/assets/graph.json'
import repographdata from '@/assets/repograph.json'
// import Legend from '@/components/Legend.vue'

// const loadLimit = 20
// let WFmaxContentHeight = 0
// let loadingMessage = null
let showed = false

export default defineComponent({
  data () {
    return {
      loadEnabled: true,
      currentPage: 0,
      loadOver: false,
      messageBox: undefined,
      showModal: false,
      jsonGraphData: graphdata,
      graph: null,
      repographdata: repographdata
    }
  },
  components: {
    HelpIcon
    // Legend
  },
  // async created () {
  //   const message = useMessage()
  //   this.messageBox = message
  //   loadingMessage = message.loading('loading learning entry data', { duration: 5000 })
  //   await this.fetchSections()
  // },
  mounted () {
    const notification = useNotification()
    if (!showed) {
      showed = true
      notification.create({
        title: '提示',
        description: '关于Github层次化学习系统的说明',
        content: `Github层次化学习系统以Wikipedia软件开发领域的层级知识图谱为基础，根据Wikipedia与Github仓库的连接，将该知识图谱延展到Github Topic所代表的知识，并结合实际的Github仓库帮助软件开发初学者进行系统性的软件开发技能学习。
您可以点击左侧的"?"按钮以查看详细说明
        `,
        avatar: () =>
          h(NAvatar, {
            size: 'small',
            round: true,
            src: 'https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg'
          })
      })
    }
    this.initG6()
    const rnodes = this.repographdata.nodes
    const redges = this.repographdata.edges
    rnodes.forEach(node => {
      if (!node.style) {
        node.style = {}
      }
      switch (node.type) {
        case 'rect': {
          node.size = [130, 40]
          node.style.fill = '#008792'
          break
        }
        case 'circle': {
          node.size = 80
          node.style.fill = '#C6E5FF'
          break
        }
      }
    })
    redges.forEach(edge => {
      if (!edge.style) {
        edge.style = {}
      }
      if (parseInt(edge.target) > 5) {
        edge.style.lineDash = [2, 2]
        edge.style.endArrow = false
      } else {
        edge.style.endArrow = { path: G6.Arrow.vee(5, 20, 15), d: 15 }
      }
    })
    this.graph.on('node:click', (e) => {
    // 先将所有当前有 click 状态的节点的 click 状态置为 false
      const clickNodes = this.graph.findAllByState('node', 'click')
      clickNodes.forEach((cn) => {
        this.graph.setItemState(cn, 'click', false)
      })
      const nodeItem = e.item
      // 设置目标节点的 click 状态 为 true
      this.graph.setItemState(nodeItem, 'click', true)
      // this.graph.layout.nodesep(10)
      // this.graph.layout.ranksep(10)
      this.graph.data(this.repographdata)
      this.graph.render()
    })
  },
  methods: {
    initG6 () {
      // const graphData = this.jsonGraphData
      const containerG6 = this.$refs.containerG6
      const nodes = this.jsonGraphData.nodes
      // const edges = this.jsonGraphData.edges
      nodes.forEach(node => {
        node.label = node.id
        if (!node.style) {
          node.style = {}
        }
        switch (node.type) {
          case 'ellipse': {
            node.size = [120, 40]
            node.style.fill = '#afb4db'
            break
          }
          case 'rect': {
            node.size = [130, 40]
            node.style.fill = '#008792'
            break
          }
          case 'circle': {
            node.size = 80
            node.style.fill = '#C6E5FF'
            break
          }
        }
        if (node.id === 'jquery') {
          node.style.stroke = '#ffd400'
          node.style.lineWidth = 3
        }
      })

      this.graph = new G6.Graph({
        container: containerG6,
        // width: 800,
        height: 650,
        fitView: true,
        modes: {
          default: ['drag-canvas', 'zoom-canvas']
        },
        defaultNode: {
          // size: [100, 40],
          style: {
            // fill: '#C6E5FF',
            stroke: '#5B8FF9'
          },
          labelCfg: {
            style: {
              fill: '#00287E',
              fontSize: 12
            }
          }
        },
        defaultEdge: {
          // type: 'cubic-vertical',
          type: 'line',
          style: {
            stroke: '#A3B1BF',
            // endArrow: true
            endArrow: {
              path: G6.Arrow.vee(5, 20, 15), // 使用内置箭头路径函数，参数为箭头的 宽度、长度、偏移量（默认为 0，与 d 对应）
              d: 15
            }
          }
        },
        layout: {
          type: 'dagre',
          rankdir: 'TB',
          nodesep: 25,
          ranksep: 25
        }
      })
      this.graph.data(this.jsonGraphData)
      this.graph.render()
    }
  },
  computed: {
    loadUrl () {
      return '/getLearnSections/' + this.docName
    },
    ...mapState({
      docName: 'doc_name',
      en: 'en'
    })
  }
})
</script>

<style>
.waterfall-container {
  height: 100%;
  /* overflow: auto; */
  display: flex;
  justify-content: center;
}

.waterfall-content {
  margin: auto;
  width: 1240px;
  display: flex;
  align-items: flex-start;
}

.waterfall-content .piping {
  width: 25%;
  padding: 10px;
  padding-bottom: 0px;
}

.mycard {
  padding: 10px;
  word-break: break-all;
  width: 290px;
  border-radius: 5px;
  box-shadow: 0px 0px 5px #888888;
  margin-bottom: 20px;
  /* margin-right: 20px; */
  margin-left: 0;
  height: 100%;
}

.section-id {
  text-align: center;
}

.g6-x {
  /* width: 800px; */
  position: relative;
  width: 80%;
  /* height: 800px; */
  box-sizing: border-box;
  border: 1px solid #ccc;
  margin-right: 1px;
  background-color: rgba(255, 255, 255, 0.7);
}

.grid {
    margin-top: 50px;
    margin-left: 100px;
    margin-right: 30px;
    width: 90%;
    background-color: rgba(255, 255, 255, 0);
}

.mygrid {
    /* margin-top: 50px; */
    /* margin-left: 100px; */
    margin-right: 30px;
    width: 90%;
    background-color: rgba(255, 255, 255, 0);
}

#gridright {
  display: flex;
  flex-direction: column;
}

#image {
  /* margin-left: 80px; */
  position: absolute;
  top: 0;
  right: 0;
  /* opacity: 0.5; */
  /* transform: translate(0, -100%); */
}

#SectionWhole {
  background-image: url('../assets/backgd.jpg');
  background-size: cover;
  background-attachment:fixed;
  width: 100%;
  height: 100%;
  background-color:#cccccc;
}

#header {
  height: 8vh;
  justify-content: center;
  display: flex;
  flex-direction: column;
  align-items: left;
  padding-top: 20px;
  padding-left: 55px;
  padding-bottom: 20px;
  background-color:rgba(242, 234, 218,0.7);
  color: #afdfe4;
}</style>
