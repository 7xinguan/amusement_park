// pages/orderConfirm/orderConfirm.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    listItem: [
      { id: '1', title: '。。。', img: '../../assets/imgs/listImg2.png', num: '3', price: '50', attr: '属性1;属性2' },
      { id: '2', title: '。。。', img: '../../assets/imgs/listImg2.png', num: '3', price: '50', attr: '属性1;属性2' }
    ],
    addr:{}
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
 
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
 
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log(this.data.addr)
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  toPay() {
    wx.navigateTo({
      url: '../orderPay/orderPay'
    })
  },
  toAddr() {
    wx.navigateTo({
      url: '../addrMan/addrMan'
    })
  }
})