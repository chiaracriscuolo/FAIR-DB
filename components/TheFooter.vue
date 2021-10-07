<template>
  <header class="footer">
    <div class="footer-content">
      <h5>Chiara Criscuolo, Fabio Azzalini and Letizia Tanca, 2021</h5>
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
.footer {
  height: 60px;
  background: purple;
  color: black;
  display: flex;
  justify-content: space-between;
  text-align: center;
}
.footer-content {
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
</style>
