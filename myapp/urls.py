from django.conf.urls import patterns, include, url
from login.views import *
from dash.views import *
from django.views.static import *

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^create/$', create),
    url(r'^createPapers/(?P<profile_id>\d+)/$', createPapers),
    url(r'^all/',profiles),
    url(r'^get/(?P<profile_id>\d+)/$', profile),
    url(r'^report/$', report),
    url(r'^makePdf/$', makePdf),
    url(r'^filters/$', filters),
    url(r'^reportProf/(?P<profile_id>\d+)/$', reportProf),
    url(r'^generatedReport/$', generatedReport),
    url(r'^job/(?P<profile_id>\d+)/$', job),
    url(r'^acads/(?P<profile_id>\d+)/$', acads),
    url(r'^BooksCount/(?P<profile_id>\d+)/$', books_count),
    url(r'^books/(?P<profile_id>\d+)/$', books),
    url(r'^CourseCount/(?P<profile_id>\d+)/$',course_count),
    url(r'^courses/(?P<profile_id>\d+)/$', courses),
    url(r'^ResearchAgencyCount/(?P<profile_id>\d+)/$',researchAgency_count),
    url(r'^ResearchAgency/(?P<profile_id>\d+)/$', researchAgency),
    url(r'', include('social_auth.urls')),	
)
