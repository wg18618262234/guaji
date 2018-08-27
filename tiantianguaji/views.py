from django.shortcuts import render
from tiantianguaji import models
from django.http import JsonResponse
import json
# Create your views here.
def player(request):
    # 请求人IP地址输出
    print("IP : " + request.META['REMOTE_ADDR'])
    # if request.method == "POST":
    #     userid = request.POST.get("userid",None)
    #     name = request.POST.get("name",None)
    #     hp = request.POST.get("hp",None)
    #     power = request.POST.get("power",None)
    #
    #     print(userid,name,hp,power)
    #
    #     # 在数据库中添加数据
    #     models.player.objects.create(userid=userid,name=name,hp=hp,power=power)
    #     return JsonResponse({"isadd":"添加角色成功"})
    if request.method == "POST":
        userid = request.POST.get("userid",None)
        print(userid)
        if userid :
            #查询userid角色信息sql语句
            finduserid = "SELECT * FROM `tiantianguaji_player` WHERE userid = '%s'" % userid
            print(finduserid)
            playerdata = models.player.objects.raw(finduserid)
            print(list(playerdata))
        else:
            # 在数据库中查找数据
            playerdata = models.player.objects.values('userid','name','hp','power')
        return JsonResponse(list(playerdata),safe=False)

def clear(request):
    # 请求人IP地址输出
    print("IP : " + request.META['REMOTE_ADDR'])
    if request.method == "POST":
        userid = request.POST.get("userid",None)
        name = request.POST.get("name",None)
        hp = request.POST.get("hp",None)
        power = request.POST.get("power",None)

        print('userid:'+userid,'name:'+name,'hp:'+hp,'power:'+power)

        # 在数据库中添加数据
        models.clear.objects.create(userid=userid,name=name,hp=hp,power=power)
        return JsonResponse({"isadd":"添加怪物成功"})
    if request.method == "GET":
        # 在数据库中查找数据
        playerdata = models.clear.objects.values('userid','name','hp','power')
        return JsonResponse(list(playerdata),safe=False)