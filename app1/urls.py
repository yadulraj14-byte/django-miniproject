from django.urls import path
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('register/',views.register,name='register'),
  path('login/',views.login_view,name='login_view'),
  path('home/',views.home,name='home'),
  path('admin1/',views.admin,name='admin'),
  path('candidate/',views.candidate,name='candidate'),
  path('recruiter/',views.recruiter,name='recruiter'),  
  path('add/',views.Add,name='add'),
  path('job_details/<int:id>/',views.Job_details,name='job_details'),
  path('apply/<int:id>/',views.Apply_job,name='apply_job'),
  path("applications/",views.view_applications,name="view_applications"),
  path("update/<int:id>/",views.update_status,name="update_status"),
  path("myapplications/",views.my_applications,name="my_applications"),
  path("view_recruiters/", views.view_recruiters, name="view_recruiters"),
  path("view_candidates/", views.view_candidates, name="view_candidates"),
  path("view_jobs/", views.view_jobs, name="view_jobs"),
  path("view_all_applications/", views.view_all_applications, name="view_all_applications"),
  path("add_recruiter/",views.add_recruiter,name="add_recruiter"),
  path("edit_recruiter/<int:id>/",views.edit_recruiter,name="edit_recruiter"),
  path("delete_recruiter/<int:id>/",views.delete_recruiter,name="delete_recruiter"),
  path("add_candidate/",views.add_candidate,name="add_candidate"),
  path("edit_candidate/<int:id>/",views.edit_candidate,name="edit_candidate"),
  path("delete_candidate/<int:id>/",views.delete_candidate,name="delete_candidate"),
  path("profile/", views.profile, name="profile"),
  path("edit_profile/",views.edit_profile,name="edit_profile"),
  path("save_job/<int:id>/",views.save_job,name="save_job"),
  path("saved_job/",views.saved_jobs,name="saved_jobs"),
  path("remove_saved_job/<int:id>/",views.remove_saved_job,name="remove_saved_job")
]