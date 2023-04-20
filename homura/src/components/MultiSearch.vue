<template>
  <div id="selector">
   <div v-for="num in chooseArray.length" :key="num">
     <h1>{{num}}级分类</h1>
     <n-select :value="objArr[num-1]" placeholder="请选择" :options="chooseArray[num-1]" @update:value="updateObjArr(num-1, $event)">
     <!-- <n-select v-model="objArr[num-1]" placeholder="请选择" :options="chooseArray[num-1]" @update:value="chooseChildrenArr"> -->
       <!-- 单纯为el-option绑定单击事件是不生效的，需要为其添加.native 修饰符 -->
      <!-- <el-option
      v-for="item in chooseArray[num-1]"
        @click.native="chooseChildrenArr(item)"
        :key="item.id"
        :value="item.name">
        {{item.name}}
      </el-option> -->
    </n-select>
   </div>
  </div>
</template>

  <!-- 引入vue.js文件 -->
  <!-- <script src="./vue.js"></script> -->
  <!-- 引入样式element-ui样式 -->
<!-- <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css"> -->
<!-- 引入element-ui组件库 -->
<!-- <script src="https://unpkg.com/element-ui/lib/index.js"></script> -->
<script>
import { defineComponent } from 'vue'
// import { SelectOption } from 'naive-ui'

export default defineComponent({
  name: 'MultiSearch',
  data () {
    return {
      // 所有下拉框数据
      array: [
        {
          name: 'A',
          level: 1,
          parent_id: null,
          id: 1,
          value: 1,
          label: 'A',
          children: [
            {
              name: 'A-A',
              level: 2,
              parent_id: 1,
              id: 4,
              value: 4,
              label: 'A-A',
              children: [
                {
                  name: 'A-A-A',
                  level: 3,
                  parent_id: 4,
                  id: 10,
                  value: 10,
                  label: 'A-A-A',
                  children: []
                },
                {
                  name: 'A-A-B',
                  level: 3,
                  parent_id: 4,
                  id: 11,
                  value: 11,
                  label: 'A-A-B',
                  children: []
                }
              ]
            },
            {
              name: 'A-B',
              level: 2,
              parent_id: 1,
              id: 5,
              value: 5,
              label: 'A-B',
              children: []
            }
          ]
        },
        {
          name: 'B',
          level: 1,
          parent_id: null,
          id: 3,
          value: 3,
          label: 'B',
          children: [
            {
              name: 'B-A',
              level: 2,
              parent_id: 3,
              id: 8,
              value: 8,
              label: 'B-A',
              children: []
            },
            {
              name: 'B-B',
              level: 2,
              parent_id: 3,
              id: 9,
              value: 9,
              label: 'B-B',
              children: []
            }
          ]
        },
        {
          name: 'C',
          level: 1,
          parent_id: null,
          id: 99,
          value: 99,
          label: 'C',
          children: []
        }
      ],
      // 选中的下拉框数据
      chooseArray: [],
      // el-select选中的数据
      objArr: [],
      //  选中的数据详情
      detailMsg: ''
    }
  },
  methods: {
    chooseChildrenArr (val) {
      // 每次重新点击下拉框都要清楚，后续下拉框的值，重新为其赋值
      if (val.children.length > 0) { // 如果选中的元素，其有子元素，那么保留下一级的下拉框
        // this.obj = {}
        this.chooseArray[val.level] = val.children
        this.chooseArray.splice(val.level + 1)
        this.objArr.splice(val.level)
      } else { // 如果选中的元素，没有子元素，那么只保留切换的下拉框，清楚其以下的所有下拉框
        this.chooseArray.splice(val.level)
        this.objArr.splice(val.level)
      }
      // 每次重新选择，都将上一次detailMsh清空，防止下一次的选择干扰它
      this.detailMsg = ''
      for (const key in this.objArr) {
        this.detailMsg += (key * 1 + 1) + '级分类:' + this.objArr[key] + ' '
      }
    },
    updateObjArr (index, value) {
      const vm = this
      // use Vue.set to update the array element and trigger reactivity
      vm.$set(vm.objArr, index, value)
      // call the chooseChildrenArr method with the value
      this.chooseChildrenArr(value)
    }
  },
  created () {
    const arr = []
    this.array.forEach(ele => {
      if (ele.level === 1)arr.push(ele)
    })
    /*
    初始化页面，将数据中一级分类保留放入到要便利的数组中
    其核心思路是
    [[一级下拉框数据],[二级下拉框数据],[三级下拉框]....[n级下拉框]  ]
    */
    this.chooseArray[this.chooseArray.length] = arr
  }
})
// const app = new Vue({
// el:"#app",

// })
</script>
