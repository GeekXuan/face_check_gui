import requests,datetime, time

#str_length = 0

def main(name = 'wangzhixuan'):
    global str_length
    timenow = datetime.date.today()
    timetor = datetime.date.today() + datetime.timedelta(days=1)
    starttime = '%d-%d-%d' % ((timenow.year,timenow.month,timenow.day))
    endtime = '%d-%d-%d' % ((timetor.year,timetor.month,timetor.day))
    #print(starttime,endtime)
    #starttime = '2017-12-10'
    #endtime = '2017-12-11'
    url = 'https://crawl.jiyunhudong.net/ops/ajax/get_merge_data/?db_name=ops_mergedata&collection_name=tcs_verifier_merge_hourly&match=%7B%22merge_id.verifier%22:%22{name}%22%7D&merge=[]&aggregate=%7B%22$group%22:%7B%22verify_count%22:%7B%22$sum%22:%22$verify_count%22%7D,%22product_type%22:%7B%22$first%22:%22$merge_id.product_type%22%7D,%22blind_same_count%22:%7B%22$sum%22:%22$blind_same_count%22%7D,%22lapse_task_ids%22:%7B%22$push%22:%22$lapse_task_ids%22%7D,%22blind_not_same_task_ids%22:%7B%22$push%22:%22$blind_not_same_task_ids%22%7D,%22verify_duration_sum%22:%7B%22$sum%22:%22$verify_duration_sum%22%7D,%22verify_delay_sum%22:%7B%22$sum%22:%22$verify_delay_sum%22%7D,%22first_verified_count%22:%7B%22$sum%22:%22$first_verified_count%22%7D,%22first_audit_count%22:%7B%22$sum%22:%22$first_audit_count%22%7D,%22closed_count%22:%7B%22$sum%22:%22$closed_count%22%7D,%22_id%22:%22$merge_id.project_title%22,%22blind_not_same_count%22:%7B%22$sum%22:%22$blind_not_same_count%22%7D,%22blind_count%22:%7B%22$sum%22:%22$blind_count%22%7D,%22lapse_count%22:%7B%22$sum%22:%22$lapse_count%22%7D%7D%7D&start_time={starttime}+00:00:00&end_time={endtime}+00:00:00'.format(name = name,starttime=starttime,endtime = endtime)
    headers = {'Accept':'application/json, text/plain, */*', \
            'Cookie':'sessionid=rgnfz7in1jxcx5vhf170t6eahkojcbu3', \
            'Host':'crawl.jiyunhudong.net', \
            'Referer':'https://crawl.jiyunhudong.net/ops/dashboard/%E4%B8%AA%E4%BA%BA%E4%BB%BB%E5%8A%A1%E7%BB%9F%E8%AE%A1/?verifier={name}'.format(name = name), \
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', \
              }

    r = requests.get(url=url, headers = headers)
    #r.encoding = 'unicode'
    data = r.json()['data']
    #print(data)
    #print(str_length)
    #print('\b' * str_length,end='', flush=True)
    str_length = 0
    for each in data:
        #str_length += len(each['_id'].replace(' ','') + ':' + str(each['verify_count'])) + 1
        print(each['_id'].replace(' ','') + ':' + str(each['closed_count']))


if __name__ == '__main__':
    name = input('请输入要查询的名字：')
    try:
        while True:
            main() if name == '' else main(name)
            time.sleep(60 * 1)
    except KeyboardInterrupt:
        print('\nDone.')
