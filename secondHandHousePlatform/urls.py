"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


#主目录配置所有路由
# from index import views1 as  index_views1
# from index import views  as  index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index1/fun/',index_views1.fun_views),
    # path('index1/',index_views1.index_views),   #模拟首页地址匹配
    # path('index/login',index_views.login_views)

    # 路由分发
    path('index/', include('index.urls',)),
    path('users/', include('users.urls',)),
    path('website/', include('website.urls',)),
]
