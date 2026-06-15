import json

import requests
import os
import urllib3

urllib3.disable_warnings()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}

# 获取必应图片 URL
def get_bing_image_info():
#https://bing.xinac.net/?page=1
    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN&setmkt=zh-CN" #国际版https://www.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    return "https://www.bing.com" + data["images"][0]["url"],data["images"][0]["copyright"],data["images"][0]["enddate"],data["images"][0]["copyrightlink"]

# 下载并保存图片
def download_image():
    image_url, title,date,copyrightlink= get_bing_image_info()
    response = requests.get(image_url,verify=False,headers=headers)
    if response.status_code == 200:
        # 生成文件名（日期格式）
        # filename = f"images/{date}"
        # 创建 images 目录（如果不存在）
        # os.makedirs("images", exist_ok=True)

        # 保存图片
        # with open(filename+".jpg", "wb") as f:
        #     f.write(response.content)
        # with open(filename + "-title.txt", "w",encoding="utf-8") as f:
        #     f.write(title)

        os.makedirs("json", exist_ok=True)
        data = {
            "copyright": title,
            "copyrightlink":copyrightlink,
            "url": image_url
        }
        with open(f"json/{date}.json", "w",encoding="utf-8") as f:
            f.write(json.dumps(data,ensure_ascii=False,indent=2))
        print(f"Downloaded and write json to json explorer: {date}.json successs\n标题：{title}\n链接：{image_url}")
    else:
        print("Failed to download json")

if __name__ == "__main__":
    download_image()
