from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='user_login')
def index(request):
    events = Event.objects.all()
    return render ( request,'index.html', {'events':events})

@login_required(login_url='user_login')
def reservation(request):
    reservations = Reservation.objects.all()
    return render(request, 'events/reservations_list.html', {'reservations':reservations})

@login_required(login_url='user_login')
def restauration(request):
    restaurants= Fournisseurs.objects.all().order_by('name')
    return render(request, 'events/restaurations_list.html', {'restaurants':restaurants})


@login_required(login_url = 'user_login')
def profile(request):
    return render(request, "Client/profile.html")

@login_required(login_url='user_login')
def admin_profile(request):
    return render(request,"Admin/admin_profile.html")

@login_required(login_url='user_login')
def dashboard(request):
    events = Event.objects.all()
    total_event_count = Event.objects.count()    # Fetch all events from the database
    total_category_count = Category.objects.count()    
    context = {
        'events':events,
        'total_event_count' :total_event_count,
        'total_category_count' :total_category_count
    }
    return render(request, 'dashboard.html', context)


# @login_required(login_url='login')
# def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='user_login')
def reserve_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Create a reservation record
            reservation = form.save(commit=False)
            reservation.event = event
            reservation.user = request.user  # Assuming you have user authentication
            reservation.save()

            return redirect('/index')  # Redirect to a success page
    else:
        form = ReservationForm()

    return render(request, 'index.html', {'event': event})

# all about gestion des evenements 
@login_required(login_url='user_login')
def event_list(request):
    events = Event.objects.all()  # Fetch all events from the database
    return render(request, 'events/event_list.html', {'events': events})

@login_required(login_url='user_login')
def create_event(request):
    categories = Category.objects.all() 
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/')  # Redirect to the event catalog or a success page
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form, 'categories':categories})

@login_required(login_url='user_login')
def create_restauration(request):
    restaurations = Fournisseurs.objects.all()
    if request.method=='POST':
        form = RestaurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/restaurations')
    else:
        form = RestaurationForm()
    
    return render(request, 'events/create_restauration.html', {'form':form, 'restaurations':restaurations})

def delete_event(request, event_id):
    # Get the event object or return a 404 if it doesn't exist
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is authorized to delete the event (you can customize this)
    if request.user.is_authenticated:
        event.delete()
        return redirect('/events/')  # Redirect to the event catalog or a success page
    else:
        return redirect('/login')  # Redirect to the event catalog with a message or error

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'
    success_url = '/events/'  # Redirect to the event list page after editing


#all about categories 
@login_required(login_url='user_login')
def create_event_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events_category/')  # Redirect to the event catalog or a success page
    else:
        form = CategoryForm()

    return render(request, 'events/create_event_category.html', {'form': form})

def delete_event_category(request, category_id):
    # Get the event object or return a 404 if it doesn't exist
    category = get_object_or_404(Category, id=category_id)

    # Check if the user is authorized to delete the event (you can customize this)
    if request.user.is_authenticated:
        category.delete()
        return redirect('/events_category/')  # Redirect to the event catalog or a success page
    else:
        return redirect('/login')  # Redirect to the event catalog with a message or error

@login_required(login_url='user_login')
def event_list_category(request):
    categories = Category.objects.all()  # Fetch all categories from the database
    return render(request, 'events/event_list_category.html', {'categories': categories})

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'events/edit_event_category.html'
    success_url = '/events_category/'  # Redirect to the event list page after editing


#all about users list
def user_list(request):
    users = User.objects.all()
    return render(request, 'events/users_list.html', {'users': users})

def delete_user(request, user_id):
    # Get the event object or return a 404 if it doesn't exist
    user = get_object_or_404(User, id=user_id)

    # Check if the user is authorized to delete the event (you can customize this)
    if request.user.is_authenticated:
        user.delete()
        return redirect('/users_list/')  # Redirect to the event catalog or a success page
    else:
        return redirect('/login')  # Redirect to the event catalog with a message or error

@login_required(login_url='user_login')
def search_event_category(request):
    if request.method == 'POST':
        data = request.POST['search']
        event_category = Category.objects.filter(name__icontains=data)
        context = {
        'event_category': event_category
    }
        return render(request, 'events/event_category.html', context)
    return render(request, 'events/event_category.html')

#Auth Functions 
def user_register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "auth/register.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        userProfile = UserProfile.objects.create(user=user, user_type='client',image=image)
        userProfile.save()
        user.save()
        alert = True
        return render(request, "auth/register.html", {'alert':alert})
    return render(request, "auth/register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/dashboard")
            else:
                return redirect("/index")
        else:
            alert = True
            return render(request, "auth/login.html", {'alert':alert})
    return render(request, "auth/login.html")


def user_logout(request):
    logout(request)
    return redirect('/login')  # Redirect to login page after logout

#for edit profile info
def edit_profile(request):
    if request.method == 'POST':
        profile_form = CustomEditProfileForm(request.POST, instance=request.user)
        image_form = ImageUploadForm(request.POST, request.FILES)

        if profile_form.is_valid() and image_form.is_valid():
            # Handle profile data update
            new_email = profile_form.cleaned_data.get("new_email")
            new_first_name = profile_form.cleaned_data.get("new_first_name")
            new_last_name = profile_form.cleaned_data.get("new_last_name")

            # Update user profile data
            user = request.user
            user.email = new_email
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.save()

            # Handle image upload
            new_image = image_form.cleaned_data.get("image")
            if new_image:
                user.userprofile.image = new_image
                user.userprofile.save()

            return redirect('/profile')  # Redirect to the profile page or a success page
    else:
        profile_form = CustomEditProfileForm(instance=request.user)
        image_form = ImageUploadForm()

    return render(request, 'Client/edit_profile.html', {'profile_form': profile_form, 'image_form': image_form})


def edit_admin_profile(request):
    if request.method == 'POST':
        profile_form = CustomEditProfileForm(request.POST, instance=request.user)
        image_form = ImageUploadForm(request.POST, request.FILES)

        if profile_form.is_valid() and image_form.is_valid():
            # Handle profile data update
            new_email = profile_form.cleaned_data.get("new_email")
            new_first_name = profile_form.cleaned_data.get("new_first_name")
            new_last_name = profile_form.cleaned_data.get("new_last_name")

            # Update user profile data
            user = request.user
            user.email = new_email
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.save()

            # Handle image upload
            new_image = image_form.cleaned_data.get("image")
            if new_image:
                user.userprofile.image = new_image
                user.userprofile.save()

            return redirect('/admin_profile')  # Redirect to the profile page or a success page
    else:
        profile_form = CustomEditProfileForm(instance=request.user)
        image_form = ImageUploadForm()

    return render(request, 'admin/edit_profile.html', {'profile_form': profile_form, 'image_form': image_form})


#this is for edit password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update the session
            return redirect('/login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Client/change_password.html', {'form': form})