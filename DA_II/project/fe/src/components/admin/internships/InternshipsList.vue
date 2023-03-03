<template>
  <div class="container">
    <div class="filter-form container">
      <v-row>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Tìm kiếm theo tên giảng viên"
            single-line
            hide-details
          ></v-text-field> 
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
        <v-select
          :items="items"
          label="Phân loại theo học kì"
        ></v-select>
        </v-col>
        <v-col
          cols="12"
          sm="6"
          md="4"
        >
        <v-select
          :items="items"
          label="Phân loại theo trạng thái duyệt"
        ></v-select>
        </v-col>
      </v-row>
    </div>
    <v-data-table
      :headers="headers"
      :items="projects"
      sort-by="time_register"
      sort-desc=false
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Danh sách thông tin thực tập</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <!-- <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
              >
                Thêm sinh viên mới
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
  
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="12"
                      md="12"
                    >
                      <v-text-field
                        v-model="editedItem.full_name"
                        label="Tên sinh viên"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                      cols="12"
                      sm="12"
                      md="12"
                    >
                      <v-text-field
                        v-model="editedItem.gender"
                        label="Giới tính"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
  
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="close"
                >
                  Huỷ bỏ
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="save"
                >
                  Lưu
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog> -->
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Bạn muốn xoá thông tin này?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Huỷ bỏ</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">Đồng ý</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:[`item.status_check`]="{ item }">
        <p>{{ item.status_check == 0 ? 'chưa duyệt' : 'đã duyệt' }}</p>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <!-- <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon> -->
        <v-icon
          class="ml-4"
          @click="deleteItem(item)"
        >
          mdi-information-outline
        </v-icon>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="initialize"
        >
          Reset
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
// import api from '@/api/Api';
import axios from 'axios';
import { HOST_POINT } from '@/config';

  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'Mã',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'Học kì', value: 'semester' },
        { text: 'Họ và tên sinh viên', value: 'student.full_name' },
        { text: 'Họ và tên giảng viên', value: 'lecturer.full_name' },
        { text: 'Thời gian đăng ký', value: 'time_register' },
        { text: 'Trạng thái duyệt', value: 'status_check' },
        { text: 'Xem chi tiết', value: 'actions', sortable: false },
      ],
      projects: [],
      editedIndex: -1,
      editedItem: {
        id: '',
        name: '',
        gender: '',
      },
      defaultItem: {
        id: '',
        name: '',
        gender: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Thêm sinh viên mới' : 'Chỉnh sửa thông tin sinh viên'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        axios.get(`${HOST_POINT}/internships`)
          .then((res) => {
            console.log(res);
            this.projects = res.data
          })
        // console.log(this.projects);
      },

      editItem (item) {
        this.editedIndex = this.projects.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.projects.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.projects.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.projects[this.editedIndex], this.editedItem)
        } else {
          this.projects.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>