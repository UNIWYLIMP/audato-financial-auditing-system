from . import audit_engine
import random as ran
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import django.core.mail as mailer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import *
import random
from django.db.models import Q
from pathlib import Path
import os


# Create your views here.
def index(request):
    if request.method == 'POST':
        identity = request.POST['email']
        password = request.POST['password']
        message = ""
        print(identity)
        print(password)
        valid = False
        if CustomUser.objects.filter(email=identity).exists():
            if CustomUser.objects.filter(email=identity)[0].codex == password:
                valid = True
            else:
                pass

        if valid:
            user_con = CustomUser.objects.filter(email=identity)[0]
            auth.login(request, user_con)
            email_id = identity
            request.session['userId'] = email_id
            message = "success"
            return redirect("/home")

        else:
            message = "Invalid Details"
            messages.info(request, 'Credentials Invalid')
    return render(request, "login.html")


def signup(request):
    if request.method == 'POST':
        fullname = request.POST['name']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        username = str(fullname).split(" ")[0] + str(random.randint(35345,23345433))

        if password == password2:
            if CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In Use')
                return redirect("/signup")
            elif fullname == "":
                messages.info(request, 'Full name can not be empty')
                return redirect("/signup")

            elif email == "":
                messages.info(request, 'Email can not be empty')
                return redirect("/signup")

            elif len(password) < 8:
                messages.info(request, 'password is too short. Try again')
                return redirect("/signup")

            else:
                # create profile
                user = CustomUser.objects.create_user(username=username, email=email, password=password, codex=password, first_name=fullname, last_name="_____")
                user.save()

                auth.login(request, user)
                request.session['userId'] = email

                return redirect('/home')

        else:
            messages.info(request, 'passwords does not match')
            return redirect('/signup')

    return render(request, "signup.html")


def home(request):
    if not request.user.is_authenticated:
        return redirect("/")

    if not request.session.get('userId', None):
        auth.logout(request)
        return redirect('/')

    profile = CustomUser.objects.get(email=request.session.get('userId'))
    if request.method == "POST":
        bank_record = request.FILES.get("file1")
        manual_record = request.FILES.get("file2")

        new_instance = BinSaver()
        new_instance.file_one = bank_record
        new_instance.file_two = manual_record
        new_instance.save()

        BASE_DIR = os.getcwd()

        print(BASE_DIR)
        url1 = f"./{new_instance.file_one.url}"
        url2 = f"./{new_instance.file_two.url}"

        print(url1)
        print(url2)

        response_audit = str(audit_engine.Audit().run_engine_address(url1, url2)).replace("\n", ".................................")
        new_audit = AuditFile()
        new_audit.file_one = bank_record
        new_audit.file_two = manual_record
        new_audit.response = response_audit
        new_audit.profile = profile
        new_audit.save()
        print(response_audit)
        return redirect(f"/view_result/{new_audit.id}")
    stack_list = AuditFile.objects.filter(profile=profile)
    length_of_stack = len(list(stack_list))
    return render(request, "index.html", {"stack_list": stack_list, "length_of_stack": length_of_stack})


def view_result(request, audit_id):
    if not request.user.is_authenticated:
        return redirect("/")

    if not request.session.get('userId', None):
        auth.logout(request)
        return redirect('/')

    instance = AuditFile.objects.get(id=audit_id)
    file_one = instance.file_one.url
    file_two = instance.file_two.url
    result = instance.response

    profile = CustomUser.objects.get(email=request.session.get('userId'))

    if profile.id == instance.profile.id:
        pass
    else:
        auth.logout(request)
        return redirect("/")
    return render(request, "view_result.html", {"result": result, "file_one": file_one, "file_two": file_two})


def logout(request):
    auth.logout(request)
    return redirect('/')
