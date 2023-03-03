<template>
  <div class="scroll-bar">
    <div id="myDIV">In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
    <br><br>
    'Whenever you feel like criticizing anyone,' he told me, just remember that all the people in this world haven't had the advantages that you've had.'</div>

    <p id="demo">output</p>
  </div>
</template>

<script>
  export default {
    data: () => ({
      offsetTop: 0,
    }),

    methods: {
      onScroll (e) {
        this.offsetTop = e.target.scrollHeight
        console.log(e.target.scrollTop);
        console.log(e.target.offsetHeight);
        console.log(e.target.scrollHeight);
      },
    },
    mounted() {
      document.getElementById("myDIV").addEventListener("scroll", myFunction);

      function myFunction() {
        document.getElementById("demo").innerHTML = "You scrolled in div.";
      }
      console.log('mounted')
    },
    updated() {
      console.log('updated');
    }
  }
</script>

<style>
#myDIV {
  border: 1px solid black;
  width: 200px;
  height: 100px;
  overflow: scroll;
}
</style>