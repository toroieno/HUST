<template>
  <v-app id="inspire">
     <v-main>
        <v-container fluid fill-height>
           <v-layout align-center justify-center>
              <v-flex xs12 sm8 md4>
                 <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                       <v-toolbar-title>Đăng ký tài khoản</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                       <v-form @submit.prevent="handleSubmit">
                          <v-text-field
                             prepend-icon="mdi-account"
                             name="username"
                             label="Tên tài khoản"
                             type="text"
                             v-model="username"
                          ></v-text-field>
                          <v-text-field
                             prepend-icon="mdi-email"
                             name="username"
                             label="Email"
                             type="text"
                             v-model="email"
                          ></v-text-field>
                          <v-text-field
                             id="password"
                             prepend-icon="mdi-lock"
                             name="password"
                             label="Mật khẩu"
                             v-model="password"
                             :append-icon="icon_eye"
                             :type="type_password"
                             @click:append="viewPass"
                          ></v-text-field>
                          <v-text-field
                             id="password"
                             prepend-icon="mdi-lock"
                             name="password"
                             label="Nhập lại mật khẩu"
                             v-model="re_password"
                             :append-icon="icon_eye"
                             :type="type_password"
                             @click:append="viewPass"
                          ></v-text-field>
                       </v-form>
                    </v-card-text>
                    <!-- <v-card-text>
                      <v-spacer></v-spacer>
                      Quên mật khẩu?
                    </v-card-text> -->
                    <v-card-actions>
                       <v-spacer></v-spacer>
                       <v-btn color="primary"  @click="handleSubmit" to="/">Đăng ký</v-btn>
                    </v-card-actions>
                    <v-card-text>
                      Bạn đã có tài khoản? <v-btn class="btn-register" to="/login">Đăng nhập</v-btn>
                    </v-card-text>
                 </v-card>
              </v-flex>
           </v-layout>
        </v-container>
     </v-main>
  </v-app>
</template>

<script>
import api from '@/api';

export default {
  data() {
    return {
      username: '',
      password: '',
      type_password: 'password',
      icon_eye: 'mdi-eye-off-outline',
    }
  },
  name: 'LoginPage',

  methods: {
    handleSubmit() {
      const params = {
        username: this.username,
        password: this.password
      }
      console.log(params);
      api.login(params)
        .then((res) => {
          console.log('from login', res);
        })
    },

    viewPass() {
      this.type_password = this.type_password === 'password' ? 'text' : 'password'
      this.icon_eye = this.icon_eye === 'mdi-eye-outline' ? 'mdi-eye-off-outline' : 'mdi-eye-outline'
    }
  },
};
</script>

<style scoped>
.btn-register {
  background-color: transparent;
}
</style>
