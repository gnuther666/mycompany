<template>
  <div class="UserManager">
    <el-container>
      <el-aside id="left_aside">
        <el-table :data="birefTableData" border style="width: 100%">
          <el-table-column prop="id" label="ID"></el-table-column>
          <el-table-column prop="username" label="名称"></el-table-column>
        </el-table>
      </el-aside>
      <el-main id="center_main">
        <el-tabs v-model="ActivateTabName" @tab-click="handleRightTableSelect">
          <el-tab-pane label="用户详情" name="userdetil">用户详情</el-tab-pane>
          <el-tab-pane label="添加用户" name="adduser">添加用户</el-tab-pane>
          <el-tab-pane label="用户组管理" name="user_group_manage">用户组管理</el-tab-pane>
        </el-tabs>
      </el-main>
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
      birefPageCount: 0,
      ActivateTabName: 'userdetil'
    }
  },
  methods: {
    getBriefUser (event = null) {
      ApiGetBriefUserList({'page_num': 1, 'page_size': 10}).then(
        resp => {
          console.log('resp', resp)
          this.birefPageCount = resp.data.page_count
          this.birefTableData = resp.data.data
        }
      )
    },
    handleRightTableSelect (tab, event) {
      console.log(tab, event)
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
