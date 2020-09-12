from django.shortcuts import render
from django.shortcuts import HttpResponse #导入HttpResponse模块

list = [{'name':'bookname','wirter':'wang','bookid':'123','date':'1998-01-01'},{'name':'bookname1','wirter':'wang1','bookid':'1232','date':'1998-01-01'}]
list1=list[0:1]
list2=list[1:]
def index(request):#request是必须带的实例。类似class下方法必须带self一样
    return render(request, 'index.html',{'form':list1})#通过HttpResponse模块直接返回字符串到前端页面
# Create your views here.
def jump(request):
    return render(request,'destinations.html',{'form':list2})
