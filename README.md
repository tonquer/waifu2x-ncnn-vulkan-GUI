# waifu2x-ncnn-vulkan-GUI
这是使用[waifu2x-ncnn-vulkan-python](https://github.com/tonquer/waifu2x-ncnn-vulkan-python)和qt实现的demo，支持png和jpg图片转换
支持放大倍数，去噪等级，模型选择
# 界面
![image](https://user-images.githubusercontent.com/22116659/116770684-0add3a00-aa78-11eb-90b7-c34547adfb51.png)
# Windows
  1. 下载最新的版本 https://github.com/tonquer/waifu2x-ncnn-vulkan-GUI/releases
  2. 解压zip
  3. 打开start.exe
  4.请安装[Vs运行库](https://download.visualstudio.microsoft.com/download/pr/366c0fb9-fe05-4b58-949a-5bc36e50e370/015EDD4E5D36E053B23A01ADB77A2B12444D3FB6ECCEFE23E3A8CD6388616A16/VC_redist.x64.exe)
# Linux
  1. 下载安装qt依赖， http://ftp.br.debian.org/debian/pool/main/x/xcb-util/libxcb-util1_0.4.0-1+b1_amd64.deb
  2. 安装依赖，sudo dpkg -i ./libxcb-util1_0.4.0-1+b1_amd64.deb
  3. 安装vulkan驱动，sudo apt install mesa-vulkan-drivers
  4. 下载最新的版本 https://github.com/tonquer/waifu2x-ncnn-vulkan-GUI/releases
  5. 解压tar -zxvf start.tar.gz 
  6. cd start && chmod +x start
  7. ./start
