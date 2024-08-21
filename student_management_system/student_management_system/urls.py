"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views,admin_views,employee_views,staffs_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    #login Path
    path('',views.LOGIN,name='login'),
    path('dologin',views.dologin,name='dologin'),
    path('dologout',views.doLogout,name='logout'),
    #Profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),
    #Admin pannel
    path('ADMIN/HOME',admin_views.HOME,name="home"),
    path('ADMIN/Employee/Add',admin_views.ADD_EMPLOYEE,name='add_employee'),
    path('ADMIN/Employee/View',admin_views.VIEW_EMPLOYEE,name='view_employee'),
    path('ADMIN/Employee/Edit/<str:id>',admin_views.EDIT_EMPLOYEE,name='edit_employee'),
    path('ADMIN/Employee/Update',admin_views.UPDATE_EMPLOYEE,name='update_employee'),
    
    path('Admin/Manager/Add',admin_views.ADD_MANAGER,name='add_manager'),
    path('Admin/Manager/view',admin_views.VIEW_MANAGER,name='view_manager'),
    path('ADMIN/Manager/Edit<str:id>',admin_views.EDIT_MANAGER,name='edit_manager'),
    path('ADMIN/Manager/Update',admin_views.UPDATE_MANAGER,name='update_manager'),
    
    path('ADMIN/Department/Add',admin_views.ADD_DEPARTMENT,name='add_department'),
    path('ADMIN/Department/View',admin_views.VIEW_DEPARTMENT,name='view_department'),
    path('ADMIN/Department/Edit/<str:id>',admin_views.EDIT_DEPARTMENT,name='edit_department'),
    path('ADMIN/Department/Update',admin_views.UPDATE_DEPARTMENT,name='update_department'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
