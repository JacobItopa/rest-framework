"""RF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name='home-view'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/post/', include('posts.urls')),
    #path('api/owner/<pk>/', OwnerDetailView.as_view(), name='owner-detail'),
    #path('api/comment/<pk>/', CommentDetailView.as_view(), name='comment-detail'),
    #path('api/post/', PostListView.as_view(), name='post-list'),
    #path('api/post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    #path('api/post/<apk>/delete', PostDestroyView.as_view(), name='post-destroy'),
    #path('api/post/', PostView.as_view(), name='post-list'),
    #path('api/post/<pk>/', PostView.as_view(), name='post-list'),
    #path('api/post-list/', post_list, name='post-list'),
    #path('api/post-details/<int:pk>/', post_detail, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)