from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import signup, login_view, logout_view, add_member


urlpatterns = [
    path('', views.home, name='home'),
    path('plots/', views.plot_list, name='plot_list'),
    path('plots/add/', views.add_plot, name='add_plot'),
    path('plots/<int:plot_id>/', views.plot_detail, name='plot_detail'),
    path('plots/<int:plot_id>/edit', views.edit_plot, name='edit_plot'),
    path('plots/<int:plot_id>/delete', views.delete_plot, name='delete_plot'),
    path('add_member/', add_member, name='add_member'),
    path('members/', views.member_list, name='member_list'),
    path('members/<int:member_id>/', views.member_detail, name='member_detail'),
    path('transactions/', views.transactions, name='transactions'),
    path('events/', views.event_list, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('add_event/', views.add_event, name='add_event'),
    path('resources/', views.resources, name='resources'),
    path('add_resource/', views.add_resource, name='add_resource'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)