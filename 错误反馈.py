#coding:utf-8
import os,shutil
a = [x for x in os.listdir('all') if x.endswith('.jpg')]
b = [x for x in os.listdir('不合格') if x.endswith('.jpg')]
name_list1 = [x.split('_')[-1][:-4] for x in a]
name_list2 = [x.split('_')[-1][:-4] for x in b]
name_set = set(name_list1)
os.mkdir('统计')
os.chdir('统计')
dir_list = []
for each in name_set:
    dirname = each + '(错误率%d比%d=%.2f%%)'%(name_list2.count(each),name_list1.count(each),name_list2.count(each)/name_list1.count(each)*100)
    #print(dirname)
    os.mkdir(dirname)
    dir_list.append(dirname)
os.chdir('..')
for i in range(len(name_list2)):
    shutil.copy(os.path.join(os.getcwd(),'不合格',b[i]),os.path.join(os.getcwd(),'统计',dir_list[list(name_set).index(name_list2[i])],b[i]))
print('Done.')
