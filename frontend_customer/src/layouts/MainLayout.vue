<template>
  <q-layout view="lHh Lpr lFf">
    <q-header class="q-px-sm q-pt-sm" style="background-color:#000;color:white" elevated >
      <q-toolbar>
        <!-- <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          color="white"
          @click="leftDrawerOpen = !leftDrawerOpen"
        /> -->

        <q-toolbar-title class="font-600 font-size-24">
          Pomona Credit Card Dashboard - Greg G Tan
        </q-toolbar-title>

        
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      content-class="myGrey"
     
      :mini="miniState"
        @mouseover="miniState = false"
        @mouseout="miniState = true"
    >
      <q-list>
       
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Dashboard',
    caption: 'quasar.dev',
    icon: 'dashboard',
    link: '/'
  },
  {
    title: 'Help',
    caption: 'github.com/quasarframework',
    icon: 'help_outline',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Profile',
    caption: 'chat.quasar.dev',
    icon: 'account_circle',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Log Out',
    caption: 'forum.quasar.dev',
    icon: 'logout',
    link: 'https://forum.quasar.dev'
  },
  
]

export default {
  name: 'MainLayout',
  components: {
    EssentialLink
  },
  data () {
    return {
      miniState:true,
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  }
}
</script>
