var sliderWidth = 96; // 需要设置slider的宽度，用于计算中间位置

Page({
  data: {
    tabs: ["未使用", "可兑换", "已失效"],
    activeIndex: 0,
    sliderOffset: 0,
    sliderLeft: 0,
    coupon1:[
      { price: "20", title: '优惠券名称', time:'2020-10-1至2020-12-1'},
      { price: "30", title: '优惠券名称', time: '2020-10-2至2020-12-2' }
    ],
    coupon2: [
      { price: "20", title: '优惠券名称（需要积分200）', time: '2020-10-1至2020-12-1' },
      { price: "30", title: '优惠券名称（需要积分300）', time: '2020-10-2至2020-12-2' }
    ],
    coupon3:[
      { price: "20", title: '优惠券名称', time: '2020-3-1至2020-5-1' },
      { price: "20", title: '优惠券名称', time: '2020-2-1至2020-4-1' }
    ]
  },
  onLoad: function () {
    var that = this;
    wx.getSystemInfo({
      success: function (res) {
        that.setData({
          sliderLeft: (res.windowWidth / that.data.tabs.length - sliderWidth) / 2+10,
          sliderOffset: res.windowWidth / that.data.tabs.length * that.data.activeIndex
        });
      }
    });
  },
  tabClick: function (e) {
    this.setData({
      sliderOffset: e.currentTarget.offsetLeft,
      activeIndex: e.currentTarget.id
    });
  }
});