<!--首页可交互饼图-->

<template>
  <div id="home-pie">
    <div ref="chart" style="width:700px;height:700px"></div>
  </div>
</template>

<script>
export default {
  name: "HomePie",
  mounted() {
    this.getEchartData();
  },
  methods: {
    getEchartData() {
      const chart = this.$refs.chart;
      if (chart) {
        const myChart = this.$echarts.init(chart);
        const option = {
          title: {
            // text: '身体组成占比',//主标题
            x: "center" //x轴方向对齐方式
          },
          tooltip: {
            trigger: "item",
            formatter: "{b} : {d}%"
          },
          legend: {
            orient: "vertical",
            bottom: "bottom",
            data: [
              "DNA-RNA",
              this.$t("public.protein"),
              this.$t("public.virus"),
              this.$t("public.molecule"),
              this.$t("public.metallic")
            ]
          },
          series: [
            {
              name: "身体占比",
              type: "pie",
              radius: "55%",
              center: ["50%", "60%"],
              data: [
                { value: 3, name: "DNA-RNA" },
                { value: 50, name: this.$t("public.protein") },
                { value: 15, name: this.$t("public.virus") },
                { value: 31, name: this.$t("public.molecule") },
                { value: 1, name: this.$t("public.metallic") }
              ],
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: "rgba(0, 0, 0, 0.5)"
                }
              }
            }
          ]
        };
        myChart.setOption(option);
      }
    }
  }
};
</script>

<style scoped></style>
