<template>
  <div>
    <el-form ref="form" :model="form" label-width="10%">
      <el-form-item label="用户ID">
        <el-input v-model="form.id" :disabled="true" v-show="form.id!==-1"></el-input>
      </el-form-item>
      <el-form-item label="姓">
        <el-input v-model="form.first_name"></el-input>
      </el-form-item>
      <el-form-item label="名">
        <el-input v-model="form.last_name"></el-input>
      </el-form-item>
      <el-form-item label="昵称">
        <el-input v-model="form.username"></el-input>
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item label="是否超级用户">
        <el-checkbox v-model="form.is_staff"></el-checkbox>
      </el-form-item>
      <el-form-item label="是否激活">
        <el-checkbox v-model="form.is_active"></el-checkbox>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">确认修改</el-button>
        <el-button type="primary" @click="onDel">删除数据</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {ApiGetUiserDetil} from '../../api/query'

export default {
  name: 'UserDetil',
  data () {
    return {
      form: {
        'id': -1,
        'is_superuser': true,
        'username': '',
        'first_name': null,
        'last_name': null,
        'email': '',
        'is_staff': false,
        'is_active': false,
        'group': [],
        'user_permissions': []
      },
      query_id: null
    }
  },
  methods: {
    onSubmit () {
      console.log('提交数据')
    },
    onDel () {
      console.log('删除数据')
    },
    setUserID (userid) {
      this.query_id = userid
      console.log('初始化一次', this.query_id)
    }
  },
  watch: {
    query_id () {
      console.log('内部初始化')
      ApiGetUiserDetil({'userid': this.query_id}).then(
        resp => {
          console.log(resp.data)
          this.form.id = resp.data.id
          this.form.is_superuser = resp.data.is_superuser
          this.form.username = resp.data.username
          this.form.first_name = resp.data.first_name
          this.form.last_name = resp.data.last_name
          this.form.email = resp.data.email
          this.form.is_staff = resp.data.is_staff
          this.form.is_active = resp.data.is_active
          this.form.group = resp.data.group
          this.form.user_permissions = resp.data.user_permissions
        }
      )
    }
  }
}
</script>

<style scoped>

</style>
