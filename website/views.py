from django.shortcuts import render
from django.http import JsonResponse
import json
from SHHLog.MLog import mlog as VLog
from SHHDatabase.MGengine import MongoEngine as Mongo
from index.models import SecondHouse



def mainpage_views(request):
    if request.method == 'GET':
        # 根据页码来返回数据
        page = request.GET.get('p')
        if page:
            houseMesLength = 20
            skipLength = (int(page)-1) * houseMesLength
            defaultHouses = SecondHouse.objects.filter(house_region__city='gz').skip(skipLength).limit(houseMesLength)
            return render(request, 'mainpage.html', {'default': defaultHouses, 'city': '广州'})
        else:
            defaultHouses = SecondHouse.objects.filter(house_region__city='gz').limit(20)
            return render(request, 'mainpage.html', {'default': defaultHouses, 'city': '广州'})

    else:
        selectWebsit = request.POST.get('website', '')
        selectCity = request.POST.get('city', '')
        selectDistrict = request.POST.get('district', '')
        if selectWebsit == '自如网站':
            if selectCity == '广州':
                _city = 'gz'
            else:
                _city = ''
            houses = SecondHouse.objects.filter(house_region__city=_city, house_region__district=selectDistrict).limit(20)
            return render(request, 'mainpage.html', {'content': houses, 'city': '广州'})

        else:
            return render(request, 'mainpage.html')

