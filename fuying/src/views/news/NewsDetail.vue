<template>
  <div>
    <img class="nav-bg" src="~assets/img/bg/item-bg.jpg" alt="/" />
    <div class="bg">
      <div class="main-window">
        <div class="top-window">
          <div class="title-div">title</div>
          <div class="author">author</div>
        </div>
        <div class="text-window">
          text
        </div>
        <div class="side-window">side</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewsDetail"
};
</script>

<style scoped>
.nav-bg {
  width: 100%;
  min-width: 75rem /* 1200/16 */;
  height: 12.5rem /* 200/16 */;
}

.bg {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

.main-window {
  width: 80%;
  min-width: 50rem /* 800/16 */;
  min-height: 75rem /* 1200/16 */;
  margin-left: auto;
  margin-right: auto;
  border: .0625rem /* 1/16 */ solid gray;
  background: white;
}

.top-window {
  height: 6.25rem /* 100/16 */;
  width: 68%;
  float: left;
  border: .0625rem /* 1/16 */ solid gray;
}

.text-window {
  height: 50rem /* 800/16 */;
  width: 68%;
  float: left;
  border: .0625rem /* 1/16 */ solid gray;
}

.side-window {
  height: 50rem /* 800/16 */;
  width: 30%;
  float: right;
  border: .0625rem /* 1/16 */ solid gray;
}

.title-div {
  height: 4.0625rem /* 65/16 */;
  font-weight: bold;
  font-size: 2rem /* 32/16 */;
  text-align: center;
  margin-top: .625rem /* 10/16 */;
}

.author {
  color: gray;
  float: right;
}
</style>
