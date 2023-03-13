<template>
  <div class="container">
    <div class="footer-top">
      <div class="navbar">
        <a href="#" class="nav">Trang chủ</a>
        <a href="#" class="nav">Liên hệ</a>
      </div>
    </div>
    <div class="footer-copyright pt-5">
      <p class="white--text pl-15">&#169; Viện Toán ứng dụng và Tin học, ĐHBK Hà Nội.  1 Đại Cồ Việt, Hai Bà Trưng, Hà Nội</p>
    </div>
  </div>
</template>
<script>
export default {
  
}
</script>
<style scoped>
.container {
  height: auto;
}
.footer-top {
  background-color: #f2f1eb;
  height: 40px;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  display: flex;
}
.navbar .nav:not(:first-child) {
  border-left: 2px solid #333;
}
.nav {
  padding: 0 12px;
  text-decoration: none;
  font-weight: 400;
}
.footer-copyright {
  background-color: #015a8f;
  height: 60px;
}
</style>