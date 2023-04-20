<template>
    <div class="c-selecter">
        <slot></slot>
        <Select v-for="(datas, i) in allData" :placeholder="placeholders[i] || '请选择'" :style="i>0?'margin-left: '+gap+'px;':''" v-model="model[i]" :key="i" @on-change="onSelectedChange(i)" :disabled="datas.length===0 && !placeholders[i]" >
            <Option v-for="item in datas" :value="JSON.stringify(item)" selected v-bind:key="item[idField]">{{ item[nameField] }}</Option>
        </Select>
    </div>
</template>
<script>

import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MultilevelSelecter',
  props: {
    /**
     * 显示级别数
     */
    levels: {
      type: Number,
      default: 3
    },
    /**
     * 数据加载器，必须是一个异步方法，返回的数据必须是对象数组
     */
    loader: {
      type: Function,
      default: () => {}
    },
    /**
     * 多个选框之间的间距
     */
    gap: {
      type: Number,
      default: 10
    },
    /**
     * 每个选择框的默认文字
     */
    placeholders: {
      type: Array,
      default: () => {
        return []
      }
    },
    idField: {
      type: String,
      default: 'id'
    },
    nameField: {
      type: String,
      default: 'name'
    }
  },
  data () {
    return {
      allData: [],
      model: []
    }
  },
  mounted () {
    this.dataMap = new Map()
    this.model = new Array(this.levels).fill(null)
    this.allData = new Array(this.levels).fill([])
    this.getLevelData(null)
  },
  methods: {
    async getLevelData (pid, level = 0) {
      if (level >= this.allData.length || pid === -1) {
        this.$emit('on-change', this.model.map(v => { return v ? JSON.parse(v) : null }))
        return
      }
      const cdata = this.dataMap.get(pid) || await this.loader(pid)
      this.allData[level] = cdata
      this.dataMap.set(pid, cdata)
      this.allData = [...this.allData]
      if (cdata.length) {
        this.model[level] = this.placeholders[level] ? null : JSON.stringify(cdata[0])
        this.getLevelData(cdata[0][this.idField], level + 1)
      } else {
        this.model[level] = null
        this.getLevelData(-1, level + 1)
      }
    },
    onSelectedChange (level) {
      this.getLevelData(this.model[level] ? JSON.parse(this.model[level])[this.idField] : -1, level + 1)
    }
  }
})
</script>
<style lang="less">
.c-selecter{
    display: inline-block;
    .ivu-select{
        width: auto;
        min-width: 100px;
    }
}
</style>
