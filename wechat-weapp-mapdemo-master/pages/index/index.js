Page( {// 拍摄按钮按下, 执行record 触发拍摄
  record(){
    this.data.cameraContext = wx.createCameraContext()
    this.data.cameraContext.takePhoto({
      quality:"high", //高质量的图片
      success: res => {
        //res.tempImagePath照片文件在手机内的的临时路径
        let tempImagePath = res.tempImagePath
        wx.saveFile({
          tempFilePath: tempImagePath,
          success: function (res) {
            //返回保存时的临时路径 res.savedFilePath
            const savedFilePath = res.savedFilePath
            // 保存到本地相册
            wx.saveImageToPhotosAlbum({
              filePath: savedFilePath,
            })
          },
          //保存失败回调（比如内存不足）
          fail: console.log
        })
      }
    })
  }
})