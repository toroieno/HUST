<template>
  <v-navigation-drawer
    app
    clipped
    v-model="DRAWER_STATE"
    :mini-variant="!DRAWER_STATE"
    :width="sidebarWidth"
    :permanent="$vuetify.breakpoint.mdAndUp"
    :temporary="$vuetify.breakpoint.smAndDown"
    :mini-variant-width="sidebarMinWidth"
    :class="{'drawer-mini': !DRAWER_STATE}">

    <div class="v-list">
      <a class="v-list-item v-list-item--link grey--text text-sm-h6 justify-center" target="_blank" href="https://flatlogic.com/generator">SAMI</a>
    </div>

    <v-list>
      <template v-for="(item, i) in items">
        <v-row
          v-if="item.heading"
          :key="item.heading"
          align="center">
          <v-col cols="6" class="py-5">
            <span
              style="padding-left: 32px"
              class="text-body-1 subheader"
              :class="(item.heading && DRAWER_STATE) ? 'show ' : 'hide'">
              {{ item.heading }}
              </span>
          </v-col>
          <v-col
            cols="6"
            class="text-center">
          </v-col>
        </v-row>
        <v-divider
          v-else-if="item.divider"
          :key="i"
          dark
          class="my-4"
        ></v-divider>
        <v-list-group
          color="primary"
          v-else-if="item.children && DRAWER_STATE"
          :key="item.title"
          v-model="item.model"
          append-icon="mdi-triangle-small-down">
            <template v-slot:prependIcon>
              <v-icon size="28">{{item.icon}}</v-icon>
            </template>
            <template v-slot:activator >
              <v-list-item-content >
                <v-list-item-title
                  class="grey--text">
                    {{ item.title }}
                </v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item
              v-for="(child, i) in item.children"
              :key="i"
              :to="child.link"
              link>
                <!-- <v-list-item-action v-if="child.icon">
                  <v-icon size="">{{ child.icon }}</v-icon>
                </v-list-item-action> -->
                <v-list-item-content>
                  <v-list-item-title class="grey--text">
                    {{ child.title }}
                  </v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </v-list-group>
        <v-list-item
          color="primary"
          v-else
          :key="item.text"
          :href="item.href ? item.href : null"
          :to="item.link === '#' ? null : item.link"
          link>
          <v-list-item-action>
            <v-icon
              size="28"
              :color="item.color ? item.color : ''"
            >{{ item.icon }}</v-icon>
          </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title
                class="grey--text"
                link>
                {{ item.title }}
              </v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
    </v-navigation-drawer>
</template>

<script>
import {mapActions, mapState} from 'vuex'

  export default {
    props: {
        source: String,
    },
    data(){
      return {
        items: [
          { title: 'Thống kê', icon: 'mdi-chart-line', link: '/admin/dashboard' },
          // { title: 'Typography', icon: 'mdi-format-size', link: '/typography' },
          // { title: 'Tables', icon: 'mdi-grid-large', link: '/tables' },
          // { title: 'Notifications', icon: 'mdi-bell-outline', link: '/notifications' },
          {
            title: 'Sinh viên',
            icon: 'mdi-account-multiple',
            link: '/admin/students',
            model: false,
            children: [
              { title: 'Danh sách sinh viên', icon: 'mdi-circle-small', link: '/admin/students'},
              { title: 'Quản lý học tập', icon: 'mdi-circle-small', link: '/charts'},
            ],
          },
          {
            title: 'Giảng viên',
            icon: 'mdi-account-school',
            link: '/admin/lecturers',
            model: false,
            children: [
              { title: 'Danh sách giảng viên', icon: 'mdi-circle-small', link: '/admin/lecturers'},
              { title: 'Danh sách đồ án', icon: 'mdi-circle-small', link: '/charts'},
              { title: 'Danh sách thực tập', icon: 'mdi-circle-small', link: '/maps'},
            ],
          },
          {
            title: 'Đồ án',
            icon: 'mdi-book',
            link: '/admin/projects',
            model: false,
            children: [
              { title: 'Danh sách đăng ký', icon: 'mdi-circle-small', link: '/admin/projects'},
              { title: 'Charts', icon: 'mdi-circle-small', link: '/charts'},
            ],
          },
          {
            title: 'Thực tập',
            icon: 'mdi-account-hard-hat',
            link: '/admin/internships',
            model: false,
            children: [
              { title: 'Danh sách đăng ký', icon: 'mdi-circle-small', link: '/admin/internships'},
              { title: 'Charts', icon: 'mdi-circle-small', link: '/charts'},
            ],
          },
          { divider: true },
          { heading: 'HELP' },
          { title: 'Library', icon: 'mdi-book-variant-multiple', href: 'https://flatlogic.com/templates'},
          { title: 'Support', icon: 'mdi-forum', href: 'https://flatlogic.com/forum/'},
          { title: 'FAQ', icon: 'mdi-help-circle-outline', href:'https://flatlogic.com/templates/vue-material-template'},
          // { divider: true },
          // { heading: 'PROJECTS' },
          // { title: 'My recent', icon: 'mdi-circle-medium', color: 'warning'},
          // { title: 'Starred', icon: 'mdi-circle-medium', color: 'primary'},
          // { title: 'Background', icon: 'mdi-circle-medium', color: 'error'}

        ],
        sidebarWidth: 240,
        sidebarMinWidth: 96
      }
    },
    computed: {
      ...mapState('admin', ['drawer']),
      DRAWER_STATE: {
        get() {
          return this.drawer
        },
        set(newValue) {
          if (newValue === this.drawer) return;
          this.TOGGLE_DRAWER();
        }
      }
    },
    methods: {
      ...mapActions('admin', [ 'TOGGLE_DRAWER' ]),
    }
  }
</script>

<style src="./Sidebar.scss" lang="scss"/>
