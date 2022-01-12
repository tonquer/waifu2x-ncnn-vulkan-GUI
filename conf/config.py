import sys

IsLoadingPicture = True

UpdateUrl = "https://github.com/tonquer/waifu2x-ncnn-vulkan-GUI/releases/latest"
UpdateUrl2 = "https://github.com/tonquer/waifu2x-ncnn-vulkan-GUI/releases"
UpdateVersion = "v1.0.2"
Language = 0

# waifu2x
CanWaifu2x = True
ErrorMsg = ""

Encode = 0
EncodeGpu = ""
UseCpuNum = 0
SelectEncodeGpu = ""

Waifu2xThread = 2
Format = "jpg"
Waifu2xPath = "waifu2x"
IsOpenWaifu = True

LookModel = 0       # 默认值
DownloadModel = 0   # 默认值
LogIndex = 0


Model0 = "cunet"     # 通用
Model1 = "cunet"     # 通用
Model2 = "photo"     # 写真
Model3 = "anime_style_art_rgb"  # 动漫

