from django.urls import path

from blog.api_views import post_list, post_detail
from rest_framework.urlpatterns import format_suffix_patterns # .json in api

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>", post_detail, name="api_post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns) # sufix patten json