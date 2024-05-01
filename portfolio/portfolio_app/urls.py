from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('content/', views.content, name='content'),
    path('contact/', views.contact, name='contact'),
    path("blog_page/<str:pk>/", views.blog_page, name="blog_page"),
    path("contact_form_submit/", views.contact_form_submit, name="contact_form_submit"),
    path('Projects/',views.projects, name = 'Projects'),
    path('download-resume/', views.download_resume, name='download_resume'),
    path("resume_contact/", views.resume_contact, name="resume_contact"),
    path('download_resume_adv/', views.download_resume_adv, name='download_resume_adv'),
    path('image/', views.work, name='work'),
    path('bosch/', views.bosch, name='bosch')
    ] 