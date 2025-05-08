import requests
import os
import urllib3

urllib3.disable_warnings()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 获取必应图片 URL
def get_bing_image_info():
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1" #国内版https://s.cn.bing.net/HPImageArchive.aspx?format=js&idx=0&n=1
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    return "https://www.bing.com" + data["images"][0]["url"],data["images"][0]["copyright"],data["images"][0]["startdate"]

# 下载并保存图片
def download_image():
    image_url, title,date = get_bing_image_info()
    response = requests.get(image_url,verify=False,headers=headers)
    if response.status_code == 200:
        # 生成文件名（日期格式）
        filename = f"images/{date}"

        # 创建 images 目录（如果不存在）
        os.makedirs("images", exist_ok=True)

        # 保存图片
        with open(filename+".jpg", "wb") as f:
            f.write(response.content)
        with open(filename + "-title.txt", "w",encoding="utf-8") as f:
            f.write(title)
        print(f"Downloaded: {filename}")
    else:
        print("Failed to download image")

if __name__ == "__main__":
    download_image()
