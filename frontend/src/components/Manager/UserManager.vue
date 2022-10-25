<template>
  <div class="UserManager">
    <el-container>
      <el-container>
        <el-aside id="left_aside">
          <el-table :data="birefTableData" border style="width: 100px">
            <el-table-column prop="username" label="ID"></el-table-column>
            <el-table-column prop="username" label="名称"></el-table-column>
          </el-table>
        </el-aside>
        <el-main id="center_main">Main</el-main>
      </el-container>
    </el-container>
    <router-view></router-view>
  </div>
</template>

<script>
import {ApiGetBriefUserList} from '../../api/query'

export default {
  name: 'UserManager',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      birefTableData: [],
      birefPageCount: 0
    }
  },
  methods: {
    getBriefUser (event = null) {
      ApiGetBriefUserList({'page_num': 1, 'page_size': 10}).then(
        resp => {
          console.log('请求了一下')
          this.birefPageCount = resp['page_count']
          this.birefTableData = resp['data']
        }
      )
    }
  },
  mounted: function () {
    this.getBriefUser()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#left_aside {
  width: 30%;
  line-height: 60px;
  background-color: #B3C0D1;
}

#center_main {
  background-color: #E9EEF3;
  line-height: 160px;
}
</style>
