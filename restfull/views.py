import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt


def getTrees(request):

    custom_data={
        "status":1,
        "error":False,
        "data":getTreeDefData()
    }
    return JsonResponse(custom_data)

@csrf_exempt
def getTreesPost(request):
    if(request.method == 'POST'):
        print('POST method')
        postbody = request.body
        print(postbody)
        json_s = json.loads(postbody)
        print('json data',json_s)
        ret = {
            "status":1,
            "data":getTreeDefData(),
            "msg":""
        }
        return JsonResponse(ret)
    else:
        return JsonResponse({"status":0,"msg":"error"})

def getTreeDefData():
    treeData=[
        {
            "ID":"0001",
            "name":"MA单",

        },
        {
            "ID":"0002",
            "name":"A单",
            
        },
        {
            "ID":"0003",
            "name":"BQCS",
            
        },
        {
            "ID":"0001001",
            "name":"总览",
            "categoryId":'0001'
        },
        {
            "ID":"0001002",
            "name":"细项",
            "categoryId":'0001'
        },
        {
            "ID":"0001003",
            "name":"报表",
            "categoryId":'0001'
        },
        {
            "ID":"0002001",
            "name":"总览",
            "categoryId":'0002'
        },
        {
            "ID":"0003001",
            "name":"总览",
            "categoryId":'0003'
        }
    ]
    return treeData
