from django.urls import path

from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.AllPostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailsView.as_view(), name='post-details'),
    path('read-later', views.ReadLaterView.as_view(), name='read-later')
]
