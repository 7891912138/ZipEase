import os
import shutil
import subprocess

def get_ghostscript_path():
    gs_names = ['gs', 'gswin32', 'gswin64']
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(f'No GhostScript executable was found on path ({"/".join(gs_names)})')

def compress(input_file_path, power=3):
    """Function to compress PDF via Ghostscript command line interface"""
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
        # 压缩程度实际上是从小到大排列
    }

    # 确定输出文件路径
    parent_path = os.path.dirname(input_file_path)
    file_name, file_ext = os.path.splitext(os.path.basename(input_file_path))
    output_file_path = os.path.join(parent_path, file_name + '_comp' + file_ext)

    # 确定输出文件路径不重复
    index = 1
    while os.path.exists(output_file_path):
        output_file_path = os.path.join(parent_path, file_name + '_comp' + f'({index})' + file_ext)
        index += 1

    # 获取 Ghostscript 路径
    gs = get_ghostscript_path()
    print("Compress PDF...", input_file_path)
    initial_size = os.path.getsize(input_file_path)

    # 执行 Ghostscript 命令进行压缩
    subprocess.call([gs, '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[power]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
                    )

    # 输出压缩结果
    final_size = os.path.getsize(output_file_path)
    ratio = (initial_size - final_size) / initial_size  # 修正了压缩比例的计算方法
    print("压缩比例: {0:.0%}".format(ratio))
    show_size = final_size / 1024
    if show_size < 1024:
        print("最终文件大小: {0:.1f}KB".format(show_size))
    else:
        show_size = show_size / 1024
        print("最终文件大小: {0:.1f}MB".format(show_size))
    print("----" * 5)
    print()

# 输入文件路径和压缩值
input_file_path = input("请输入pdf文件的路径: ")
compression_level = int(input("请输入压缩程度(0-4):"))

# 执行压缩
compress(input_file_path, power=compression_level)
