from PIL import Image
import os

def compress_image(input_file_path, output_file_path=None):
    """Function to compress JPEG and PNG images"""

    # 如果未指定输出文件路径，则使用默认文件名后缀
    if output_file_path is None:
        output_file_path = input_file_path.split('.')[0] + '_comp.' + input_file_path.split('.')[1]

    # 检查输出文件路径是否已存在，若存在，则加后面加（num），num递增
    index = 1
    while os.path.exists(output_file_path):
        output_file_path = f"{input_file_path.split('.')[0]}_comp({index}).{input_file_path.split('.')[1]}"
        index += 1

    try:
        # 打开图像文件
        image = Image.open(input_file_path)

        # 输入压缩质量
        while True:
            try:
                quality = int(input("请输入压缩质量（0-100之间的整数，默认为85）: "))
                if 0 <= quality <= 100:
                    break
                else:
                    print("请输入0到100之间的整数！")
            except ValueError:
                print("请输入一个有效的整数！")

        # 压缩图像并保存
        image.save(output_file_path, quality=quality)

        # 输出压缩结果
        initial_size = os.path.getsize(input_file_path)
        final_size = os.path.getsize(output_file_path)
        ratio = (initial_size - final_size) / initial_size
        print("压缩比例: {0:.0%}".format(ratio))
        print("最终文件大小: {:.1f}KB".format(final_size / 1024))

    except Exception as e:
        print(f"压缩图片时出现错误: {e}")

# 输入文件路径
input_file_path = input("请输入图像文件的路径: ")

# 执行压缩
compress_image(input_file_path)
