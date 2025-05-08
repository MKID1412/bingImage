import requests
import os

# 获取必应图片 URL
def get_bing_image_info():
    url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    response = requests.get(url)
    data = response.json()
    return "https://www.bing.com" + data["images"][0]["url"],data["images"][0]["startdate"]

# 下载并保存图片
def download_image():
    image_url,date = get_bing_image_url()
    response = requests.get(image_url)
    if response.status_code == 200:
        # 生成文件名（日期格式）
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"images/{date}.jpg"
        
        # 创建 images 目录（如果不存在）
        os.makedirs("images", exist_ok=True)
        
        # 保存图片
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print("Failed to download image")

if __name__ == "__main__":
    download_image()
