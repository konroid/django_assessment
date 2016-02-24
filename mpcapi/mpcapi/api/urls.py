from django.conf.urls import url
from . import views as api_views
#from views import post_detail, post_list

urlpatterns = [
    #'app.views',
    url(r'^posts/$', api_views.post_list, name='post_list'),
    url(r'^posts$', api_views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)$', api_views.post_detail, name='post_detail'),
    url(r'^posts/(?P<pk>[0-9]+)/$', api_views.post_detail, name='post_detail'),
    url(r'^comments/$', api_views.comment_list, name='comment_list'),
    url(r'^comments$', api_views.comment_list, name='comment_list'),
    url(r'^comments/(?P<pk>[0-9]+)$', api_views.comment_detail, name='comment_detail'),
    url(r'^comments/(?P<pk>[0-9]+)/$', api_views.comment_detail, name='comment_detail'),
    url(r'^comments_from_post/(?P<pk>[0-9]+)$', api_views.comments_post, name='comments_post'),
    url(r'^comments_from_post/(?P<pk>[0-9]+)/$', api_views.comments_post, name='comments_post')
]

