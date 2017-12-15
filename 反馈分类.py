#coding:utf-8
import os,shutil

folders = [x for x in os.listdir() if x.endswith(('.doc','.docx'))]
for each in folders:
    folder_name = each.split('-')[0]
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    shutil.move(each, os.path.join(os.getcwd(), folder_name, each))
print('完成。')
