<template>
  <div class="titlebar">
    <el-container>
      <el-header>
        <el-menu
          :default-active="defaultActiveIndex"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b">
          <el-menu-item index="1"><img class="weblogo" src="../assets/weblogo.png"></el-menu-item>
          <el-menu-item index="taskSquare">任务广场</el-menu-item>
          <el-submenu index="2">
            <template slot="title">系统管理</template>
            <el-menu-item index="usermanage">用户管理</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'titlebar',
  data () {
    return {
      defaultActiveIndex: 'taskSquare'
    }
  },
  methods: {
    handleSelect (key, keypath) {
      if (key === 'usermanage') {
        console.log('进入用户管理')
        this.$router.push({name: 'UserManager'})
      } else {
        console.log('key', key)
        console.log('keypath', keypath)
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img.weblogo {
  width: 110px;
  height: 45px;
}
</style>
