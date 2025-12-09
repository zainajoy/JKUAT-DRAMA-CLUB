from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import member , event , gallery
from .forms import memberForm ,eventForm  ,galleryForm,SignUpForm
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {}
    return render(request,'dramaapp/homepage.html', context)
def home(request):
    context = {}
    return render(request,'dramaapp/home.html', context)
def contacts(request):
    context = {}
    return render(request,'dramaapp/contacts.html', context)
def productions(request):
    context = {}
    return render(request,'dramaapp/productions.html', context)
def events(request):
    context = {}
    return render(request,'dramaapp/events.html', context)  
def gallery(request):
    context = {}
    return render(request,'dramaapp/gallery.html', context)
def dashboard(request):
    context = {}
    return render(request,'dramaapp/dashboard.html', context)   


def login(request):
    context = {}
    return render(request,'dramaapp/login.html', context)       
def home(request):
    context = {}
    return render(request,'dramaapp/home.html', context)
def productions(request):
    context = {}
    return render(request,'dramaapp/productions.html', context)
def gallery(request):
    context = {}
    return render(request,'dramaapp/gallery.html', context)
def createmember(request):
    form = memberForm()
    context = {"form":form}

    if request.method == "POST":
        form = memberForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("home")            

    return render(request, "dramaapp/form.html", context )

def createevent(request):
    form = eventForm()
    context = {"form":form}

    if request.method == "POST":
        form = eventForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("home")            

    return render(request, "dramaapp/form.html", context )
def creategallery(request):
    form = galleryForm()
    context = {"form":form}

    if request.method == "POST":
        form = galleryForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("home")            

    return render(request, "dramaapp/form.html", context )
    
def read_ALL_member(request):
    members = member.objects.all()
    context={"members":members}
    return render(request,"dramaapp/home.html",context)
def update_member(request, pk):
    members_obj = member.objects.get(id=pk)
    form = memberForm(instance=members_obj)
    if request.method == "POST":
        form = memberForm(request.POST,request.FILES, instance=members_obj)
        if form.is_valid(): 
            form.save()
            return redirect("read_ALL_member")            
    context ={"form":form}
    return render(request, "dramaapp/form.html", context)
def delete_member(request, pk):
    members_obj = member.objects.get(id=pk)
    if request.method == "POST":        
        members_obj.delete()
        return redirect("home")
    context={"member":members_obj}
    return render(request, "dramaapp/delete.html",context=context)


def read_event(request):
    events = event.objects.all()
    context={"events":events}
    return render(request,"dramaapp/events.html",context)
def update_event(request, pk):
    events_obj = event.objects.get(id=pk)
    form = eventForm(instance=events_obj)
    if request.method == "POST":
        form = eventForm(request.POST,request.FILES, instance=events_obj)
        if form.is_valid(): 
            form.save()
            return redirect("read_event")            
    context ={"form":form}
    return render(request, "dramaapp/form.html", context)
def delete_event(request, pk):
    events_obj = event.objects.get(id=pk)
    if request.method == "POST":        
        events_obj.delete()
        return redirect("read_event")
    context={"event":events_obj}
    return render(request, "dramaapp/delete.html",context=context)

def read_gallery(request):
    galleries = gallery.objects.all()
    context={"galleries":galleries}
    return render(request,"dramaapp/gallery.html",context)
def update_gallery(request, pk):
    galleries_obj = gallery.objects.get(id=pk)
    form = galleryForm(instance=galleries_obj)
    if request.method == "POST":
        form = galleryForm(request.POST,request.FILES, instance=galleries_obj)
        if form.is_valid(): 
            form.save()
            return redirect("read_gallery")            
    context ={"form":form}
    return render(request, "dramaapp/form.html", context)
def delete_gallery(request, pk):
    galleries_obj = gallery .objects.get(id=pk)
    if request.method == "POST":        
        galleries_obj.delete()
        return redirect("read_gallery")
    context={"gallery":galleries_obj}
    return render(request, "dramaapp/delete.html",context=context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # By default, form.save() creates a user with is_staff=False
            # 1. Add a success message to show on the login page
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in.')
            
            # 2. Redirect specifically to the 'login' URL name
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'dramaapp/signny.html', {'form': form})