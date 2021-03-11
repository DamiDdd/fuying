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
  min-width: 1200px;
  height: 200px;
}

.bg {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

.main-window {
  width: 80%;
  min-width: 800px;
  min-height: 1200px;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid gray;
  background: white;
}

.top-window {
  height: 100px;
  width: 68%;
  float: left;
  border: 1px solid gray;
}

.text-window {
  height: 800px;
  width: 68%;
  float: left;
  border: 1px solid gray;
}

.side-window {
  height: 800px;
  width: 30%;
  float: right;
  border: 1px solid gray;
}

.title-div {
  height: 65px;
  font-weight: bold;
  font-size: 32px;
  text-align: center;
  margin-top: 10px;
}

.author {
  color: gray;
  float: right;
}
</style>
