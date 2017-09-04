from django.conf.urls import url
from todoapp import views


urlpatterns=[
    url(r'printlist/',views.printlist),
    url(r'printtodohome/(?P<id>[0-9]+)/$',views.printlistlinks),
    url(r'printtodohome/$',views.printtodohome,name="todohome"),
    url(r'todoinsertitem/$',views.createtodoitem.as_view()),
    url(r'todoupdateitem/(?P<pk>[0-9]+)/$',views.updatetodoitem.as_view()),
    url(r'tododeleteitem/(?P<pk>[0-9]+)/$',views.deletetodoitem.as_view()),
    url(r'todoinsertlist/$',views.createtodolist.as_view()),
    url(r'todoupdatelist/(?P<pk>[0-9]+)/$',views.updatetodolist.as_view()),
    url(r'tododeletelist/(?P<pk>[0-9]+)/$',views.deletetodolist.as_view()),
    url(r'printtodolist_using_serializers/$',views.print_todolist_using_serializers.as_view()),
    url(r'printtodolist_using_id_serializers/(?P<pk>[0-9]+)/$',views.print_todolist_using_id_serializers.as_view()),
    url(r'printtodoitem_using_serializers/$',views.print_todoitem_using_serializers.as_view()),
    url(r'printtodoitem_using_id_serializers/(?P<pk>[0-9]+)/$',views.print_todoitem_using_id_serializers.as_view()),
    url(r'printlist_css/$',views.temporary),
]