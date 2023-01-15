# ff_transfer 将Media_Folder中选定的媒体转换成已选择的媒体格式 yuki sui


import os
import time
import logging
import subprocess
import shutil

input_dir = '.\\Media_Folder\\'
cur_dir = '.\\ff-logs\\'
datetime_dir = str(time.strftime('%Y%m%d', time.localtime())) + '\\'
true_dir = cur_dir + datetime_dir

if os.path.exists(cur_dir):
    pass
else:
    os.mkdir(cur_dir)
if os.path.exists(true_dir):
    pass
else:
    os.mkdir(true_dir)

log_path = os.path.join(true_dir, "ff_transfer.log")
if os.path.exists(log_path):
    logging.basicConfig(filename=log_path, level=logging.DEBUG,
                        filemode='a', format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
else:
    file = open(log_path, 'w', encoding='utf-8', newline='')
    file.close()
    logging.basicConfig(filename=log_path, level=logging.DEBUG,
                        filemode='w', format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def get_all_abs_path(source_dir):
    path_list = []
    for fpathe, dirs, fs in os.walk(source_dir):
        for f in fs:
            p = os.path.join(fpathe, f)
            path_list.append(p)
    return path_list


def main():
    if not os.path.exists('.\\libs\\ffmpeg.exe'):
        print('ff_transfer.py: \r\n!!!!!!Not detect ffmpeg.exe in .\libs, please download it from https://github.com/BtbN/FFmpeg-Builds\r\n')
    else:
        filenum = len(get_all_abs_path(input_dir))
        print('===================\n现在是 ' + str(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())) + '\n===================\n')
        print('一共有 ' + str(filenum) + ' 个待处理文件')
        logging.debug('total ' + str(filenum) + ' files')
        for i in get_all_abs_path(input_dir):
            print('文件 ' + i + ' 格式为 ' + str(i.rsplit(".", 1)[1]))
            logging.debug('file ' + i + ' format is ' + str(i.rsplit(".", 1)[1]))
        while 1 == 1:
            new_format = input('\n你想转换成什么格式呢？输完后按回车 ')
            new_format_confirm = input('转换成 ' + new_format + ' 格式，确认吗？ 无误请直接按回车 ')
            if new_format_confirm == '':
                break
            else:
                pass
        print('\n开始转换~')
        logging.debug('finally format is ' + new_format)
        done_file = 0
        for i in get_all_abs_path(input_dir):
            command = '.\\libs\\ffmpeg.exe  -y -i "' + i + '"  ".\\OUTPUT_TEMP_TRANSFER.' + new_format + '" -loglevel error'
            print(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read())
            logging.debug(command)
            os.remove(str(i.rsplit(".", 1)[0]) + '.' + str(i.rsplit(".", 1)[1]))
            shutil.move(('.\\OUTPUT_TEMP_TRANSFER.' + new_format), str(i.rsplit(".", 1)[0]) + '.' + new_format)
            done_file += 1
            info_msg = i + ' transfer to ' + new_format + ' done ( ' + str(done_file) + ' / total ' + str(filenum) + ' )'
            print(info_msg)
            logging.info(info_msg)
        os.system("echo.")
        logging.debug('file transfer done')
        os.system("echo all file transfer DONE! please press any key to continue~ \n")
    os.system("pause")
    os.system("echo.")


main()
