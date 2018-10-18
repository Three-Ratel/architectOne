from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def asset(request):
    '''

    获取客户端发送过来的资产信息
    :param request:
    :return:
    '''
    if request.method=='GET':
        #今日未采集服务器列表
        host_list=['c1.com','c2.com','c3.com']
        return HttpResponse(json.dumps(host_list))

    else:
        #print('POST内容:',request.POST)#获取请求体所有数据(经过转换)
        #print(request.body)#获取请求体中所有数据
        '''如果http请求中发送的请求体的格式:
            "hostname=c1 mem=5g"
        才能解析
        '''
        info=json.loads(request.body.decode('utf-8'))
        print(info)
        return HttpResponse('收到')