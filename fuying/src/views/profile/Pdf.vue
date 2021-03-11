<!--查看pdf-->

<template>
  <div id="pdf">
    <div class="tools">
      <el-button
        :theme="'default'"
        type="submit"
        :title="'基础按钮'"
        @click.stop="prePage"
        class="mr10"
      >
        上一页</el-button
      >
      <div class="page">{{ pageNum }}/{{ pageTotalNum }}</div>
      <el-button
        :theme="'default'"
        type="submit"
        :title="'基础按钮'"
        @click.stop="nextPage"
        class="mr10"
      >
        下一页</el-button
      >
      <el-button
        :theme="'default'"
        type="submit"
        :title="'基础按钮'"
        @click.stop="printAll"
        class="mr10"
      >
        打印</el-button
      >
    </div>
    <div class="tips">其中数据请参考，建议下载后本地查看</div>
    <div class="pdf-div">
      <pdf
        ref="pdf"
        :src="url"
        :page="pageNum"
        :rotate="pageRotate"
        @progress="loadedRatio = $event"
        @page-loaded="pageLoaded($event)"
        @num-pages="pageTotalNum = $event"
        @error="pdfError($event)"
        @link-clicked="page = $event"
      >
      </pdf>
    </div>
  </div>
</template>

<script>
import pdf from "vue-pdf";
import report from "../../assets/img/report/report_res.pdf";

export default {
  name: "Pdf",
  components: {
    pdf
  },
  data() {
    return {
      url: report,
      pageNum: 1,
      pageTotalNum: 1,
      pageRotate: 0,
      // 加载进度
      loadedRatio: 0,
      curPageNum: 0
    };
  },
  mounted() {},
  methods: {
    // 上一页函数，
    prePage() {
      var page = this.pageNum;
      page = page > 1 ? page - 1 : this.pageTotalNum;
      this.pageNum = page;
    },
    // 下一页函数
    nextPage() {
      var page = this.pageNum;
      page = page < this.pageTotalNum ? page + 1 : 1;
      this.pageNum = page;
    },
    // 页面顺时针翻转90度。
    clock() {
      this.pageRotate += 90;
    },
    // 页面逆时针翻转90度。
    counterClock() {
      this.pageRotate -= 90;
    },
    // 页面加载回调函数，其中e为当前页数
    pageLoaded(e) {
      this.curPageNum = e;
    },
    // 其他的一些回调函数。
    pdfError(error) {
      console.error(error);
    },
    // 打印函数
    printAll() {
      this.$refs.pdf.print();
    }
  }
};
</script>

<style scoped>
.pdf-div {
  width: 62.5rem /* 1000/16 */;
  /* height: var(--screen-height); */
  overflow: hidden;
  border: .0625rem /* 1/16 */ solid #000;
  margin-left: auto;
  margin-right: auto;
}

.tools {
  width: 12.5rem /* 200/16 */;
  margin-left: auto;
  margin-right: auto;
  display: flex;
  margin-bottom: 1.25rem /* 20/16 */;
}

.page {
  margin-top: .625rem /* 10/16 */;
  margin-left: .625rem /* 10/16 */;
  margin-right: .625rem /* 10/16 */;
  display: flex;
}
.page input {
  margin-top: -.625rem /* 10/16 */;
  width: 1.875rem /* 30/16 */;
  float: left;
}
.tips {
  width: 40%;
  margin-left: 31%;
  text-align: center;
  margin-bottom: 1.25rem /* 20/16 */;
  font-size: .875rem /* 14/16 */;
  color: gray;
}
</style>
