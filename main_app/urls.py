from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('applications/', views.ApplicationList.as_view(), name='application-index'),
    path('applications/<int:pk>/', views.ApplicationDetail.as_view(), name='application-detail'),
    path('applications/create/', views.ApplicationCreate.as_view(), name='application-create'),
    path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='application-update'),
    path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application-delete'),
    path('applications/<int:pk>/add-interaction/', views.add_interaction, name='add-interaction'),
    path('tags/create/', views.TagCreate.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('tags/', views.TagList.as_view(), name='tag-index'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tag-delete'),
    path('applications/<int:app_id>/associate-tag/<int:tag_id>/',views.associate_tag,name='associate-tag'),
    path('applications/<int:app_id>/remove-tag/<int:tag_id>/', views.remove_tag, name='remove-tag'),
    path('accounts/signup/', views.signup, name='signup'),
]

