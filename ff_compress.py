# ff_compress, 自动压缩Media_Folder中媒体文件。  yuki sui


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

log_path = os.path.join(true_dir, "ff_compress.log")
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
    print('Starting compress.........')
    done_file = 0
    file_num = len(get_all_abs_path(input_dir))
    print('detect ' + str(file_num) + ' files~\n')
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
    for i in get_all_abs_path(input_dir):
        command = '.\\libs\\ffmpeg.exe  -y -i "' + i + '"  ".\\OUTPUT_TEMP_COMPRESS.' + str(
            i.rsplit(".", 1)[1]) + '" -loglevel error'
        print(subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read())
        logging.debug(command)
        os.remove(str(i.rsplit(".", 1)[0]) + '.' + str(i.rsplit(".", 1)[1]))
        shutil.move('.\\OUTPUT_TEMP_COMPRESS.' + str(i.rsplit(".", 1)[1]), i)
        done_file += 1
        try:
            os.remove('.\\OUTPUT_TEMP_COMPRESS.' + str(i.rsplit(".", 1)[1]))
        except FileNotFoundError:
            pass
        info_msg = i + ' compress done ( ' + str(done_file) + ' / total ' + str(file_num) + ' )'
        print(info_msg)

        logging.info(info_msg)
    os.system("echo.")
    logging.debug('file compress done')
    os.system("echo all file compress DONE! please press any key to continue~ \n")
    os.system("pause")
    os.system("echo.")


main()
