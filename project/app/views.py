from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def hello(request):
    template=loader.get_template("index.html")
    return HttpResponse(template.render())

def about(request):
     template=loader.get_template("about.html")
     return HttpResponse(template.render())

def portfolio(request):
     template=loader.get_template("portfolio.html")
     return HttpResponse(template.render())

def contact(request):
     template=loader.get_template("contact.html")
     return HttpResponse(template.render())

def service(request):
     template=loader.get_template("service.html")
     return HttpResponse(template.render())


# Create your views here.
import mysql.connector as mysql
name=''
email=''
phone=''
message=''

# Create your views here.
def temp(request):
    global name,email,phone,message
    if request.method=="POST":
        mydb = mysql.connect(user="root", host="localhost", password="eliteabhi09", database="abb",
                                       auth_plugin="mysql_native_password")

        cursor=mydb.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="Name":
                name=value
            if key=="Email":
                email=value
            if key=="Phone":
                phone=value
            if key=="Message":
                message=value
            
        
        c="insert into client Values('{}','{}','{}','{}')".format(name,email,phone,message)
        cursor.execute(c)
        mydb.commit()
       