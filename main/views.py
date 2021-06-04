'''
from django.shortcuts import render

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()

def home(request):
    return render(request, 'index.html')'''
from django.shortcuts import redirect, render
from .models import Document
from django.http import HttpResponse
from .forms import DocumentForm
from django.http import JsonResponse
#import prediction
import multipred
import color_classification_image
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser,logout
def validate_ajax(request):
    #pixy_img = request.FILES.get('file', None)
    newdoc = Document(docfile=request.FILES['file'])

    # print(newdoc.docfile.name)
    newdoc.save()
    print("hi")


    data = {
        'status': "I've reached"
    }
    return JsonResponse(data)

def ho(request):
    f = "cat"

    print(request.GET[0])
    if request.method=='GET':
        print("hi")
        #return HttpResponse("success")
        return render(request, 'pre.html', {'ans': f})
    else:



        return render(request,'pre.html',{'ans':f})
    #return render(request, 'index.html')
def home(request):

    print(request.GET)
    print(request.POST)
    print(request.method)
    print("hi")
    print(request.GET.get('id'))
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():

            newdoc = Document(docfile=request.FILES['docfile'])
            #print(newdoc.docfile.name)
            #print(newdoc.flag)


            newdoc.save()
            # Redirect to the document list after POST
            #context = {'d':"higgggggggggggggggggggggggggggggggggggggggggggggg"}
            #return render(request, 'index.html', context)
            if "go" in request.POST:
                f=color_classification_image.cool(newdoc.docfile.name)
            else:

                f=multipred.cool(newdoc.docfile.name)
            print("hi")
            print(request.POST.get('id'))
            print(newdoc)
            print(type(f))
            print(f)

            return render(request, 'pre.html',{'ans':f[0],'pro':f[1]})
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form,'d':'mess'}
    return render(request, 'index.html',context)






def login(request):
    if request.method == 'POST':
        print("hi")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("done",user)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('login')