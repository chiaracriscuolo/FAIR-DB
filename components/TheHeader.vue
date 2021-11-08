<template>
  <header class="header">
    <div class="header-content">
      <div class="title">
        <h1>
          <a href="/" aria-current="page" class="nuxt-link-exact-active nuxt-link-active light-hover">
            FAIR-DB
          </a>
        </h1>
      </div>
      <!--<nav class="right">
        <div
          v-for="(item, itemIndex) of menuOptions"
          :key="'menu-item-' + itemIndex"
          class="menu-item"
        >
          <nuxt-link :to="item.path">
            {{ item.name }}
          </nuxt-link>
        </div>
      </nav>-->
    </div>
  </header>
</template>

<script>
export default {
  /* data() {
    return {
      /* menuOptions: [
        {
          name: 'Home',
          path: '/',
        },
        {
          name: 'Blog',
          path: '/blog',
        },
        {
          name: 'About',
          path: '/about',
        },
      ],
    }
  },
  */
}
</script>

<style>
.header {
  height: 90px;
  background: #9627ba;
  color: white;
  display: flex;
  justify-content: space-between;
  text-align: center;
}
.header-content {
  width: 100%;
  max-width: 800px;
  margin: auto;
  align-items: center;
}
.right {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin: auto;
  max-width: 50%;
}
.title {
  font-size: 1.3rem;
  margin-bottom: 5px;
}
.light-hover.nuxt-link-exact-active.nuxt-link-active:hover{
  background-color:#9627ba;
  color: lightgrey;
  border-radius: 1rem;
}
</style>
