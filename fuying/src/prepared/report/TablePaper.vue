<!--前端生成报告所用的组件，备用-->

<template>
  <div id="table-div">
    <table width="570" border="0" cellspacing="0" cellpadding="0">
      <tr>
        <td class="content-blue" colspan="4" style="text-align: center;">
          <slot name="title"></slot>
        </td>
      </tr>
      <tr style="font-weight: bold;">
        <td>序号</td>
        <td>项目名称</td>
        <td>您的预测评分</td>
        <td>健康状态</td>
      </tr>
      <tr>
        <td id="t1-num">1.1</td>
        <td id="t1-title">生理年龄评价</td>
        <td id="t1-score">-3</td>
        <td id="t1-status">?</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: "TablePaper"
};
</script>

<style scoped>
#table-div table td {
  border: .0625rem /* 1/16 */ solid #000;
  height: 1.875rem /* 30/16 */;
  width: 6.25rem /* 100/16 */;
  padding-left: .625rem /* 10/16 */;
}

#table-div table {
  margin-left: .625rem /* 10/16 */;
  margin-top: 1.25rem /* 20/16 */;
}
</style>
