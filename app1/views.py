from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,LoginForm,Jobform,ApplicationForm,UserProfileForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .models import Job,Application,User,UserProfile,SavedJob
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
  return render(request,'index.html')

def register(request):
  msg = None
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      msg = 'user created'
      return redirect('login_view')
    else:
      msg = 'form is not valid'
  else:
    form = SignUpForm()
  return render(request,'register.html',{'form':form,'msg':msg})

def login_view(request):
  form = LoginForm(request.POST or None)
  msg = None
  if request.method == 'POST':
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user = authenticate(username=username,password=password)
      if user is not None and user.is_admin:
        login(request,user)
        return redirect('admin')
      elif user is not None and user.is_candidate:
        login(request,user)
        return redirect('candidate')
      elif user is not None and user.is_recruiter:
        login(request,user)
        return redirect('recruiter')
      else:
        msg='invalid credentials'

    else:
      msg = 'error validating form'
  return render(request, 'login.html', {'form': form, 'msg': msg})
def home (request):
  return render(request,'homepage.html')
def admin(request):

    recruiters = User.objects.filter(is_recruiter=True).count()

    candidates = User.objects.filter(is_candidate=True).count()

    jobs = Job.objects.count()

    applications = Application.objects.count()

    context = {
        "recruiters": recruiters,
        "candidates": candidates,
        "jobs": jobs,
        "applications": applications,
    }

    return render(request, "admin.html", context)
def candidate (request):
  jobs= Job.objects.all()
  
  return render(request,'candidate.html',{"jobs":jobs})
def recruiter (request):
  return render(request,'recruiter.html')




from django.db.models import Q

def candidate(request):

    search = request.GET.get("search")
    company = request.GET.get("company")
    position = request.GET.get("position")

    jobs = Job.objects.all()

    if search:
        jobs = jobs.filter(
            Q(position__icontains=search) |
            Q(company_name__icontains=search)
        )

    if company:
        jobs = jobs.filter(company_name=company)

    if position:
        jobs = jobs.filter(position=position)

    companies = Job.objects.values_list(
        "company_name",
        flat=True
    ).distinct()

    positions = Job.objects.values_list(
        "position",
        flat=True
    ).distinct()

    return render(
        request,
        "candidate.html",
        {
            "jobs": jobs,
            "search": search,
            "companies": companies,
            "positions": positions,
            "selected_company": company,
            "selected_position": position,
        },
    )

def Add(request):
  form = Jobform(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('index')
  return render(request,'forms.html',{'form':form}) 

def Job_details(request,id):
  job = get_object_or_404(Job,id=id)
  return render(request,'job_details.html',{'job':job})

def Apply_job(request , id):
  job = get_object_or_404(Job,id=id)
  if request.method == "POST":
    form = ApplicationForm(
      request.POST,
      request.FILES
    )
    if form.is_valid():
      application = form.save(commit=False)
      application.candidate = request.user
      application.job = job
      application.save()
      return redirect("candidate")
  else:
    form = ApplicationForm()
  return render(request,'apply_job.html',{"form":form,"job":job})
  

def view_applications(request):
  applications = Application.objects.all()

  return render(request,"view_applications.html",{"applications":applications})

def update_status(request,id):

    application=get_object_or_404(
        Application,
        id=id
    )

    if request.method=="POST":

        application.status=request.POST["status"]

        application.save()

        return redirect(
            "view_applications"
        )

    return render(
        request,
        "update_status.html",
        {
            "application":application
        }
    )

def my_applications(request):
  applications = Application.objects.filter(candidate = request.user)
  return render(request,"my_applications.html",{"applications":applications})


def view_recruiters(request):
  recruiters = User.objects.filter(is_recruiter = True)
  return render(request,"view_recruiters.html",{"recruiters":recruiters})

def view_candidates(request):

    candidates = User.objects.filter(is_candidate=True)

    return render(request,"view_candidates.html",{"candidates": candidates})

def view_all_applications(request):

    applications = Application.objects.all()

    return render(request,"view_all_applications.html",{"applications": applications})

def view_jobs(request):

    jobs = Job.objects.all()

    return render(request,"view_jobs.html",{"jobs": jobs})


def add_recruiter(request):
  form = SignUpForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      user = form.save(commit=False)
      user.is_recruiter = True
      user.is_candidate = False
      user.is_admin = False

      user.save()
      return redirect("view_recruiters")
    
  return render(request,"register.html",{"form":form})


def edit_recruiter(request,id):
  recruiter=get_object_or_404(User,id=id)
  form = SignUpForm(request.POST or None, instance = recruiter)
  if form.is_valid():
    form.save()
    return redirect("view_recruiters")
  return render(request,"register.html",{"form":form})

def delete_recruiter(request,id):
  recruiter=get_object_or_404(User,id=id)
  recruiter.delete()
  return redirect("view_recruiters")


def add_candidate(request):
  form = SignUpForm(request.POST or None)
  if request.method == "POST":
    if form.is_valid():
      user = form.save(commit=False)
      user.is_candidate = True
      user.is_recruiter = False
      user.is_admin = False

      user.save()

      return redirect("view_candidates")
    
  return render(request,"register.html",{"form":form})

def edit_candidate(request,id):
  candidate = get_object_or_404(User,id=id)
  form = SignUpForm(request.POST or None,instance = candidate)
  if form.is_valid():
    form.save()
    return redirect("view_candidates")
  return render(request,"register.html",{"form":form})

def delete_candidate(request,id):
  candidate = get_object_or_404 (User,id=id)
  candidate.delete()
  return redirect("view_candidates")


@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    is_profile_complete = any([
        profile.phone,
        profile.qualification,
        profile.skills,
        profile.address,
        profile.profile_picture
    ])

    return render(
        request,
        "profile.html",
        {
            "profile": profile,
            "is_profile_complete": is_profile_complete
        }
    )

@login_required
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

   
    form = UserProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=profile
    )

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "edit_profile.html", {"form": form})


@login_required
def save_job(request,id):
   job = get_object_or_404(Job, id=id)

   SavedJob.objects.get_or_create(candidate = request.user,job=job)
   return redirect("candidate")


@login_required
def saved_jobs(request):
   jobs = SavedJob.objects.filter(candidate=request.user)
   return render(request,"saved_jobs.html",{"jobs":jobs})


@login_required
def remove_saved_job(request,id):
   saved = get_object_or_404(SavedJob,id=id,candidate=request.user)
   saved.delete()
   return redirect("saved_jobs")