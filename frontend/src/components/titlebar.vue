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
      console.log(key, keypath)
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
