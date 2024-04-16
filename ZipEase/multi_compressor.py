import os
import zipfile

def zip_file(input_dir, output_zip):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zfile:
        for iter_dir_path, dirs, files in os.walk(input_dir):
            for file in files:
                fpath = os.path.join(iter_dir_path, file)
                zfile.write(fpath)

def unzip_file(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, "r") as zfile:
        zfile.extractall(target_dir)

def handle_duplicate_filename(file_path):
    base, ext = os.path.splitext(file_path)
    num = 1
    while os.path.exists(file_path):
        file_path = f"{base}({num}){ext}"
        num += 1
    return file_path

def main():
    while True:
        print("请选择模式:压缩(1)，解压(2)")
        choice = input("请输入数字选择模式: ")

        if choice == '1':
            mode = '压缩'
        elif choice == '2':
            mode = '解压'
        else:
            print("选择错误，请重新输入。")
            continue

        file_path = input("请输入文件路径: ")
        if not os.path.exists(file_path):
            print("文件路径不存在，请重新输入。")
            continue

        if mode == '压缩':
            output_zip = os.path.splitext(file_path)[0] + ".zip"
            output_zip = handle_duplicate_filename(output_zip)  # 处理重复文件名
            zip_file(file_path, output_zip)
            print("压缩完成！压缩文件保存在:", output_zip)
        elif mode == '解压':
            target_dir = os.path.splitext(file_path)[0] + "_comp"
            target_dir = handle_duplicate_filename(target_dir)  # 处理重复文件夹名
            unzip_file(file_path, target_dir)
            print("解压完成！解压文件保存在:", target_dir)

        choice = input("是否继续  是(1)/否(2): ").lower()
        while choice not in ['是', '否', '1', '2']:
            print("请选择是(1)或否(2)")
            choice = input("是否继续  是(1)/否(2): ").lower()
        if choice == '否' or choice == '2':
            break

if __name__ == "__main__":
    main()