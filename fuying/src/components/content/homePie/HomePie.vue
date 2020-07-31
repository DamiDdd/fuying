<template>
  <div id="home-pie">
    <div ref="chart" style="width:700px;height:700px"></div>
  </div>
</template>

<script>
export default {
  name: "HomePie",
  mounted(){
    this.getEchartData()
  },
  methods:{
    getEchartData(){
      const chart = this.$refs.chart;
      if(chart){
        const myChart = this.$echarts.init(chart);
        const option = {
          title : {
              // text: '身体组成占比',//主标题
              x:'center',//x轴方向对齐方式
          },
          tooltip : {
              trigger: 'item',
              formatter: "{b} : {d}%"
          },
          legend: {
              orient: 'vertical',
              bottom: 'bottom',
              data: ['DNA-RNA','蛋白质 多态','微生物 病毒','小分子 脂类','金属等元素类']
          },
          series : [
              {
                  name: '身体占比',
                  type: 'pie',
                  radius : '55%',
                  center: ['50%', '60%'],
                  data:[
                      {value:3, name:'DNA-RNA'},
                      {value:50, name:'蛋白质 多态'},
                      {value:15, name:'微生物 病毒'},
                      {value:31, name:'小分子 脂类'},
                      {value:1, name:'金属等元素类'},
                  ],
                  itemStyle: {
                      emphasis: {
                          shadowBlur: 10,
                          shadowOffsetX: 0,
                          shadowColor: 'rgba(0, 0, 0, 0.5)'
                      }
                  }
              }
          ]
        };
        myChart.setOption(option);
    }
    }
  }
}
</script>

<style scoped>

</style>