from . import views
from django . urls import path

urlpatterns = [
    path('',views.index,name="index"),
    path('delete/<int:task_id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    # path('details/',views.details,name="details")
#     generic list view
    path('cbvhome/',views.tasklistview.as_view(),name="cbvhome"),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name="cbvdelete")
    ]
