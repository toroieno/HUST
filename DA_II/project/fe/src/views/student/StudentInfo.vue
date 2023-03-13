<template>
  <div class="container">
    <v-row>
      <v-col 
        class="text-h5"
        cols="12"
        md="6"
        sm="4"
      >
        Thông tin sinh viên
      </v-col>
      <v-col 
        class="text-h5"
        cols="12"
        md="6"
        sm="4"
      >
        <v-btn color="primary">
          Cập nhật thông tin
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
        sm="4"
      >
        <p><b>Họ và tên:</b> {{ student.full_name }}</p>
        <p><b>Giới tính:</b> {{ student.gender == 0 ? 'nữ' : 'nam' }}</p>
        <p><b>Mã số sinh viên:</b> {{ student.student_code }}</p>
        <p><b>Lớp học:</b> {{ student.class_id }}</p>
      </v-col>
      <v-col
        cols="12"
        md="6"
        sm="4"
      >
        <p><b>Email trường:</b> {{ student.user.email }}</p>
        <p><b>Email cá nhân:</b> {{ student.user.email_other }}</p>
        <p><b>Facebook:</b> {{ student.facebook_link }}</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col class="text-h5">Thông tin học tập</v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
        sm="4"
      >
        <p><b>Điểm trung bình tích luỹ:</b> {{ student.cpa }}</p>
        <p><b>Số tín chỉ nợ:</b> {{ student.school_credit_debt }}</p>
        <p><b>Số tín chỉ đã qua:</b> {{ student.school_credit_complete }}</p>
      </v-col>
    </v-row>

  </div>
</template>
<script>
import axios from 'axios';
import { HOST_POINT } from '@/config';

export default {
  data: () => ({
    student: '',
  }),
  created() {
    axios.get(`${HOST_POINT}/students/20216059`)
      .then((res) => {
        this.student = res.data[0]
      })
    console.log(this.student);
  }
}
</script>
<style>
  
</style>