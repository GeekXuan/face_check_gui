import os,shutil,random
if os.path.exists('抽取结果'):
    shutil.rmtree('抽取结果')
os.mkdir('抽取结果')
for each in [x for x in os.listdir() if os.path.isdir(x) and '错误率' in x]:
    name = each.split('(')[0]
    templist = [i for i in os.listdir(each) if i.endswith('.jpg')]
    number = int(len(templist)*0.15) + 1
    randomlist = random.sample(templist, number)
    folder = os.path.join('抽取结果', '%s(%d张)' % (name, number))
    os.mkdir(folder)
    for j in randomlist:
        old_path = os.path.join(each, j)
        new_path = os.path.join(folder, j)
        shutil.copy(old_path, new_path)
print('Done.')


