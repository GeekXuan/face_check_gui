#coding:utf-8
import requests,json
url = 'https://oapi.dingtalk.com/robot/send?access_token=be93cac782d279b4e8c614a761199449b63cd3f6ddcf0ed9c69d8520a2d9c077'
headers = {'Content-Type' : 'application/json','charset' : 'utf-8'}

#文本
def fun1(text,atall='false'):
    data = {
        'msgtype': 'text',
        'text': {
            'content': text,
        },
        'at': {
            'atMobiles': [
                #'17611103411',
            ],
            'isAtAll': atall,
        }
    }
    return data

#link
def fun2(text,title,link,piclink):
    data = {
        'msgtype': 'link',
        'link': {
            'text': text,
            'title': title,
            'picUrl': piclink,
            'messageUrl': link
        }
    }
    return data
'''
#feedback
data = {
    'feedCard': {
        'links': [
            {
                'title': '时代的火车向前开', 
                'messageURL': 'https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI', 
                'picURL': 'https://www.dingtalk.com/'
            },
            {
                'title': '时代的火车向前开2', 
                'messageURL': 'https://mp.weixin.qq.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI', 
                'picURL': 'https://www.dingtalk.com/'
            }
        ]
    }, 
    'msgtype': 'feedCard'
}
#独立跳转
data = {
    'actionCard': {
        'title': '乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身', 
        'text': '![screenshot](@lADOpwk3K80C0M0FoA) \
 ### 乔布斯 20 年前想打造的苹果咖啡厅 \
 Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划', 
        'hideAvatar': '0', #1-隐藏头像
        'btnOrientation': '0', #1-横向按钮
        'btns': [
            {
                'title': '内容不错', 
                'actionURL': 'https://www.dingtalk.com/'
            }, 
            {
                'title': '不感兴趣', 
                'actionURL': 'https://www.dingtalk.com/'
            }
        ]
    }, 
    'msgtype': 'actionCard'
}
#整体跳转
data = {
    'actionCard': {
        'title': '乔布斯 20 年前想打造一间苹果咖啡厅，而它正是 Apple Store 的前身', 
        'text': '![screenshot](@lADOpwk3K80C0M0FoA) 
 ### 乔布斯 20 年前想打造的苹果咖啡厅 
 Apple Store 的设计正从原来满满的科技感走向生活化，而其生活化的走向其实可以追溯到 20 年前苹果一个建立咖啡馆的计划', 
        'hideAvatar': '0', 
        'btnOrientation': '0', 
        'singleTitle' : '阅读全文',
        'singleURL' : 'https://www.dingtalk.com/'
    }, 
    'msgtype': 'actionCard'
}
'''



def main():
    choice = input('选项：\n1.文本样式；\n2.文本样式（@所有人）；\n3.链接样式。\n请选择：\n')
    if choice == '1' or choice == '2':
        text = input('请输入文本：\n')
        atall = 'true' if choice == '2' else 'false'
        data = fun1(text,atall)
    elif choice == '3':
        title = input('请输入标题：\n')
        text = input('请输入简介：\n')
        link = input('请输入链接：\n')
        piclink = input('请输入图片链接：\n')
        data = fun2(text, title, link, piclink)

    data = json.dumps(data)
    r = requests.post(url, headers=headers, data=data)
    print(r.status_code)
    print(r.text)
if __name__ == '__main__':
    main()