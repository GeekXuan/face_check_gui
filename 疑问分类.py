#coding:utf-8
import os,shutil

people = ['吴美欣','申冰','王智轩','张欢']
folders = [x for x in os.listdir() if x.endswith(('.doc','.docx'))]
for each in people:
    if not os.path.exists(each):
        os.mkdir(each)
for each in folders:
    folder_name = each.split('-')[1].split('.')[0]
    if folder_name in people:
        shutil.move(each, os.path.join(os.getcwd(), folder_name, each))
print('完成。')
