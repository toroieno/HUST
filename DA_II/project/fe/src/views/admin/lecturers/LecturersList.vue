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
        <!-- <v-col
          cols="12"
          sm="6"
          md="4"
        >
        <v-select
          :items="items"
          label="Phân loại theo lớp"
        ></v-select>
        </v-col> -->
      </v-row>
    </div>
    <v-data-table
      :headers="headers"
      :items="lecturers"
      sort-by="full_name"
      class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
          flat
        >
          <v-toolbar-title>Danh sách giảng viên</v-toolbar-title>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
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
                Thêm giảng viên mới
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
                        label="Tên giảng viên"
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
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Bạn muốn xoá thông tin giảng viên này?</v-card-title>
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
      <template v-slot:[`item.gender`]="{ item }">
        <p>{{ item.gender == 0 ? 'nữ' : 'nam' }}</p>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
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
        { text: 'Họ và tên', value: 'full_name' },
        { text: 'Email', value: 'user.email' },
        { text: 'Giới tính', value: 'gender' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      lecturers: [],
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
        return this.editedIndex === -1 ? 'Thêm giảng viên mới' : 'Chỉnh sửa thông tin giảng viên'
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

    mounted () {
      // let data = api.getAllLecturers()
      // let data = axios.get(`${HOST_POINT}/lecturers`)
      // console.log(data);
    },

    methods: {
      initialize () {
        axios.get(`${HOST_POINT}/lecturers`)
          .then((res) => {
            console.log(res);
            this.lecturers = res.data
          })
        // console.log(this.lecturers);
      },

      editItem (item) {
        this.editedIndex = this.lecturers.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.lecturers.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        this.lecturers.splice(this.editedIndex, 1)
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
          Object.assign(this.lecturers[this.editedIndex], this.editedItem)
        } else {
          this.lecturers.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>