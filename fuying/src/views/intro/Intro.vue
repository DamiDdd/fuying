<template>
  <div id="intro">
    <img class="nav-bg" src="~assets/img/bg/intro-bg.jpg" alt="/" />
    <div class="bg">
      <div class="main">
        <el-tabs tab-position="left" class="windows">
          <el-tab-pane label="公司简介"
            ><div class="article">
              <h1 class="title">公司简介</h1>
              iproteome健康（上海iproteome生物科技有限公司）是由海外高层次人才创建的基于数据驱动、生理预测的检测服务公司，旨在将生命科学、临床医学及数据挖掘等创新技术融为一体，推出全新的健康评估模式服务于人类健康。
              iproteome健康（上海iproteome生物科技有限公司）是生命健康领域的新兴企业，坚持自主创新和成果转化，立足新一代蛋白质组技术，基于数据驱动、健康评估的检测服务公司，旨在将生命科学、临床医学及数据挖掘等创新技术融为一体，推出全新的健康评估模式服务于人类健康。
              公司的现阶段主要产品为以指尖血为样本的蛋白质组-生理刻画，利用次时代蛋白质组技术，在指尖血中通过检测3000余项生理指标，完成15项蛋白质组学-生理刻画。后期将推出肿瘤预后/治疗判断、肿瘤患病风险判断、孕妇流产风险判断等全新产品。
            </div></el-tab-pane
          >
          <el-tab-pane label="产品亮点">
            <div class="article">
              <h1 class="title">产品亮点</h1>
              蛋白质组学生理刻画产品是利用次世代蛋白质组技术配合机器学习的大数据精准分型，以1滴指尖血为样本可获得2000+蛋白质检测指标，涵盖100+项生理功能，完成40+大类的生理刻画。与常规体检相比，样本采集更便捷；检测数据量提升近百倍；检测指标更为丰富；节省您宝贵时间的同时，提供更加完备的个人全景生理刻画。
            </div>
          </el-tab-pane>
          <el-tab-pane label="检测意义"
            ><div class="article">
              <h1 class="title">检测意义</h1>
              1、 评估生理年龄、基础生理指数，避免不良生活习惯 <br>
              2、评估免疫功能、代谢功能、神经递质功能、组织器官功能、消化功能等，掌握近期指标水平，提前调养改善机体情况<br>
              3、一次检测可获得当前完备的个人全景生理刻画，定期检测建立长期健康档案，有助于提早发现异常状态，预防疾病的发生
            </div>
          </el-tab-pane>
          <el-tab-pane label="联系我们"
            ><div class="article">
              <h1 class="title">联系我们</h1>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Intro"
};
</script>

<style scoped>
#intro {
  min-height: 31.25rem /* 500/16 */;
}

.nav-bg {
  width: 100%;
  min-width: 75rem /* 1200/16 */;
  height: 12.5rem /* 200/16 */;
}

.bg {
  background: -webkit-linear-gradient(top, white, lightblue, white);
}

.main {
  /* background: gray; */
  width: 70%;
  min-width: 75rem /* 1200/16 */;
  margin-left: auto;
  margin-right: auto;
  min-height: 50rem /* 800/16 */;
}

.windows {
  margin-top: 6.25rem /* 100/16 */;
  min-height: 12.5rem /* 200/16 */;
  width: 80%;
  margin-left: auto;
  margin-right: auto;
}

.article {
  margin-left: 6.25rem /* 100/16 */;
  line-height: 1.875rem /* 30/16 */;
}
</style>
