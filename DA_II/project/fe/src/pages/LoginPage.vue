<template>
  <v-app id="inspire">
    <MessageNoti />
     <v-main>
        <v-container fluid fill-height>
           <v-layout align-center justify-center>
              <v-flex xs12 sm8 md4>
                 <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                       <v-toolbar-title>Đăng nhập</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                       <v-form
                        onSubmit="return false;"
                        ref="formLogin"
                        v-model="valid"
                       >
                          <v-text-field
                             prepend-icon="mdi-account"
                             name="username"
                             label="Tên tài khoản"
                             type="text"
                             v-model="username"
                          ></v-text-field>
                          <v-text-field
                             id="password"
                             prepend-icon="mdi-lock"
                             name="password"
                             label="Mật khẩu"
                             type="password"
                             v-model="password"
                          ></v-text-field>
                          <v-card-actions>
                            <p>Quên mật khẩu?</p>
                          </v-card-actions>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn 
                              :loading="loading"
                              type="submit"
                              color="primary"  
                              @click="login"
                            >
                              Đăng nhập
                            </v-btn>
                            <v-btn @click="handleSubmit">Test</v-btn>
                         </v-card-actions>
                       </v-form>
                    </v-card-text>
                    <v-card-text>
                      Bạn chưa có tài khoản? <v-btn class="btn-register" to="/register">Đăng ký</v-btn>
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
import { authLogin } from '@/api/backend';
import MessageNoti from '@/components/MessageNotification';
import { HOST_POINT } from '@/config';

export default {
  data: (vm) => ({
    rules: {
      requireName: (value) => (!!value && !!value.trim()) || vm.$t("Rule_Name"),
      // requireName_Amount: (value) =>
      //   value.length > 4 || vm.$t("Rule_Name_Amount"),
      // requiredUserName: (value) =>
      //   (!!value && !!value.trim()) || vm.$t("Rule_User"),
      // requiredUserName_Amount: (value) =>
      //   value.length > 4 || vm.$t("Rule_User_Amount"),
      // requiredEmail: (value) =>
      //   (!!value && !!value.trim()) || vm.$t("Rule_Email"),
      // requiredEmail_Forrmat: (value) =>
      //   /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
      //   vm.$t("Rule_Email_Forrmat"),

      // requiredPhone: (value) =>
      //   (!!value && !!value.trim()) || vm.$t("Rule_Phone"),

      // requiredPhone_Amount_10: (value) =>
      //   (!!value && value.length) > 9 || vm.$t("Rule_Phone_Amount_10"),
      // requiredPhone_Amount_12: (value) =>
      //   (!!value && value.length < 13) || vm.$t("Rule_Phone_Amount_12"),

      // requiredPassword: (value) =>
      //   (!!value && !!value.trim()) || vm.$t("Rule_Password"),
      // requiredPassword_format: (value) => {
      //   const pattern =
      //     /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/;
      //   return pattern.test(value) || vm.$t("Rule_Forrmat_Password");
      // },

      // requiredConfirmPassword: (value) =>
      //   (!!value && !!value.trim()) || vm.$t("Rule_Confirm_Password"),
      // requiredConfirmPasswordCompare: (value) =>
      //   value === vm.dataRegister.password ||
      //   vm.$t("Rule_Compare_Confirm_Password"),
    },
    loading: false,
    username: '',
    password: '',
    valid: false,
  }),
  name: 'LoginPage',
  components: {
    MessageNoti,
  },

  methods: {
    async login() {
      console.log('click');
      this.$refs.formLogin.validate();
      console.log('valid', this.valid);
      if (!this.valid) {
        console.log('fail');
        return;
      }
      try {
        console.log('try');
        this.loading = true;
        const result = await authLogin({
          username: this.username,
          password: this.password,
        });
        console.log('result', result);
        location.href = `${location.origin}`;
        // this.$store.commit("message/SHOW_SUCCESS", vm.$t("Login_Successfully"));
        this.$store.commit("message/SHOW_SUCCESS", "Login_Successfully");
      } catch (e) {
        if (e.code === 402) {
          this.$refs.notifi.openDialog({
            code: 402,
            email: this.email_login,
          });
        }
      } finally {
        this.loading = false;
      }
    },

    handleSubmit() {
      const params = {
        username: this.username,
        password: this.password
      }
      console.log(params);
      api.post( `${HOST_POINT}/webauthenticate`, params)
        .then((res) => {
          console.log('from login', res);
        })
    }
  },
};
</script>

<style scoped>
.btn-register {
  background-color: transparent;
}
</style>
