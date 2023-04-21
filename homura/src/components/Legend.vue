<template>
    <div class="g6-x" id="containerG6" ref="containerG6"></div>
</template>

<script>
import { defineComponent } from 'vue'
import G6 from '@antv/g6'
export default defineComponent({
  name: 'Legend',
  data () {
    return {
      graphdata: {
        nodes: [{
          id: 'node1',
          type: 'ellipse',
          x: 100,
          y: 100
        }, {
          id: 'node2',
          type: 'circle',
          x: 100,
          y: 200
        }, {
          id: 'node3',
          type: 'rect',
          x: 100,
          y: 300
        }, {
          id: 'node4',
          type: 'circle',
          x: 100,
          y: 400
        }]
      }
    }
  },
  mounted () {
    const nodes = this.graphdata.nodes
    nodes.forEach(node => {
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
      if (node.id === 'node4') {
        node.style.stroke = '#ffd400'
        node.style.lineWidth = 3
      }
    })
    const graph = new G6.Graph({
      container: 'containerG6',
      width: 500,
      height: 500,
      defaultNode: {
        type: 'circle',
        size: 50,
        style: {
        //   fill: '#C6E5FF',
          stroke: '#5B8FF9'
        }
      }
    })
    graph.data(this.graphdata)
    graph.render()
  }
})
</script>
