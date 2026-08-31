import json

import requests
import os
import urllib3

urllib3.disable_warnings()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 获取必应图片 URL
def get_bing_image_info():
#https://bing.xinac.net/?page=1
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1"
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    return "https://www.bing.com" + data["images"][0]["url"],data["images"][0]["copyright"],data["images"][0]["enddate"],data["images"][0]["copyrightlink"]

# 下载并保存图片
def download_image():
    image_url, title,date,copyrightlink= get_bing_image_info()
    response = requests.get(image_url,verify=False,headers=headers)
    if response.status_code == 200:
        # 截取年份 YYYY
        year = date[:4]
        # 拼接目录 json/2026
        save_dir = os.path.join("json_internation", year)
        # 存在则跳过创建
        os.makedirs(save_dir, exist_ok=True)
        # 完整文件路径 json_internation/2026/20260831.json
        json_path = os.path.join(save_dir, f"{date}.json")

        data = {
            "copyright": title,
            "copyrightlink": copyrightlink,
            "url": image_url
        }
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))
        print(f"Downloaded and write json to {json_path} success\n标题：{title}\n链接：{image_url}")
    else:
        print("Failed to download image")

if __name__ == "__main__":
    download_image()
