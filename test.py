import os
import shutil

base_dir = "json_internation"

for filename in os.listdir(base_dir):
    # 只处理8位数字开头，后缀 .json 的文件
    if not filename.endswith(".json") or len(filename) < 12:
        continue
    date_str = filename[:8]
    if not date_str.isdigit():
        continue

    year = date_str[:4]
    target_folder = os.path.join(base_dir, year)
    os.makedirs(target_folder, exist_ok=True)

    src_path = os.path.join(base_dir, filename)
    dst_path = os.path.join(target_folder, filename)

    # 如果目标已经存在，跳过避免覆盖
    if os.path.exists(dst_path):
        print(f"跳过（已存在）：{filename}")
        continue

    shutil.move(src_path, dst_path)
    print(f"移动 {filename} → {target_folder}")

print("✅ 文件整理完成！")
