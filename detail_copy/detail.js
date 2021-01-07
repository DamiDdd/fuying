var app = getApp();
var goodsData = require("../../../utils/goodsData.js");
Page({
  data: {
    assessSelected: true,
    riskPrediction: "",
    prognosisPrediction: "",
    datas: [],
    num: 1,
    totalNum: 0,
    hasCarts: true,
    loaded: false,
    curIndex: 0,
    show: false,
    scaleCart: false,
    idx_risk: -1,
    idx_pro: -1,
    multiIndex: [-1, -1, -1],
    totalPrice: 0,
    p1: 0,
    p2: 0,
    p3: 0,
    riskItem: "",
    progItem: "",
  },

  onLoad: function (options) {
    console.log("项目", options);
    console.log("app", app.globalData);
    this.setData({
      content: app.globalData.content.customer_detail,
    });
    var that = this;
    var obj = goodsData.data[options.item];
    for (var i in goodsData.data) {
      console.log("goodsData", i);
    }
    this.initGoods(obj);
    var InitialPrice = this.data.InitialPrice;
    that.setData({ loaded: true, totalPrice: InitialPrice });
  },
  getTotalPrice: function () {
    this.setData({
      totalPrice:
        this.data.p1 + this.data.p2 + this.data.p3 + this.data.InitialPrice,
    });
  },
  bindAssessmentChange: function () {
    var that = this;
    var selected = this.data.assessSelected;
    selected = !selected;
    that.setData({
      assessSelected: selected,
    });
    if (this.data.assessSelected) {
      that.setData({
        p1: 500,
      });
    } else {
      that.setData({
        p1: 0,
      });
    }
    that.getTotalPrice();
  },
  bindriskChange: function (e) {
    var that = this;
    var id = e.currentTarget.dataset.id;
    that.setData({
      idx_risk: id,
      p2: this.data.content.riskArr[id].price,
      riskPrediction: this.data.content.riskArr[id].name,
    });
    that.getTotalPrice();
  },
  bindprognosisChange: function (e) {
    var that = this;
    var id = e.currentTarget.dataset.id;
    that.setData({
      idx_pro: id,
      p3: this.data.content.prognosisArr[id].price,
      prognosisPrediction: this.data.content.prognosisArr[id].name,
    });
    that.getTotalPrice();
  },
  bindPrognosisChange: function (e) {
    console.log(e);
    var selected = this.data.progSelected;
    selected = !selected;
    this.setData({
      idx_pro: e.detail.value,
      progSelected: selected,
    });
  },

  initGoods: function (d) {
    console.log("初始化商品函数d");
    console.log(d);
    var that = this;
    wx.setNavigationBarTitle({ title: d.name });
    this.setData({
      imgMinList: (function () {
        var _list = [];
        _list.push();
        return _list;
      })(),
      img: d.img,
      name: d.name,
      num: 1,
      des: d.detail,
      InitialPrice: d.price,
      parameter: d.parameter,
      stock: d.stock,
      Type: d.type,
      ServiceType: {
        healthAssess: d.ServiceType.healthAssess,
        riskPrediction: d.ServiceType.riskPrediction,
        prognosisPrediction: d.ServiceType.prognosisPrediction,
      },
      supplyno: d.supplyno,
    });
  },
  addCount() {
    let num = this.data.num;
    num++;
    this.setData({
      num: num,
    });
  },
  deleteCount() {
    let num = this.data.num;
    if(num > 1){
      num--;
    }
    this.setData({
      num: num,
    });
  },
  addToCart() {
    console.log("addcart");
    console.log(this.data);
    const that = this;
    const num = this.data.num;
    let total = this.data.totalNum;
    console.log("total"+total);
    if (this.data.stock) {
      if (
        this.data.assessSelected ||
        this.data.riskPrediction ||
        this.data.prognosisPrediction
      ) {
        that.setData({
          show: true,
        });
        setTimeout(function () {
          that.setData({
            show: false,
            scaleCart: true,
          });
          setTimeout(function () {
            that.setData({
              scaleCart: false,
              hasCarts: true,
              totalNum: num + total,
            });
          }, 200);
        }, 300);
        app.cart.add({
          supplyno: this.data.supplyno,
          name: this.data.name,
          price: this.data.totalPrice,
          num: this.data.num,
          img: this.data.img,
          selected: true,
          healthAssess: this.data.assessSelected,
          riskPrediction: this.data.riskPrediction,
          prognosisPrediction: this.data.prognosisPrediction,
        });
        console.log(wx.getStorageSync("carts"));
        console.log(app.globalData.openID);

        var obj = wx.getStorageSync("carts");
        var arr = Object.values(obj);
        console.log("arr");
        console.log(arr);
        // wx.request({
        //   url: "https://phenomics.fudan.edu.cn/firmiana/healthprogram/updatecart/",
        //   method: "POST",
        //   header: {
        //     "content-type": "application/json",
        //   },
        //   data: {
        //     user: app.globalData.openID,
        //     items: JSON.stringify(arr),
        //   },
        //   success(res) {
        //     console.log("res", res);
        //   },
        // });
        wx.request({
          url: "https://phenomics.fudan.edu.cn/firmiana/healthprogram/updatecart/",
          method: "POST",
          header: {
            "content-type": "application/json",
          },
          data: {
            user: app.globalData.openID,
            items: JSON.stringify(arr),
          },
          success(res) {
            console.log("res", res);
          },
        });
      } else {
        wx.showModal({
          title: "提示",
          content: "请至少为你的产品选择一项服务！",
        });
      }
    } else {
      wx.showModal({
        title: "抱歉",
        content: "此产品当前暂无货，请耐心等待！",
      });
    }
  },
  bindTap(e) {
    const index = parseInt(e.currentTarget.dataset.index);
    this.setData({
      curIndex: index,
    });
  },
});
