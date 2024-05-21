from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name ="home"),
    path("logout/", views.logout_user, name = "logout"),
    path("register/", views.register_user, name = "register"),
    path("record_all/",views.record_all, name = "record_all"),
    path("record/<int:pk>", views.customer_record, name = "record"),
    path("delete_record/<int:pk>", views.delete_record, name = "delete_record"),
    path("add_record/", views.add_record, name = "add_record"),
    path("update_record/<int:pk>", views.update_record, name = "update_record"),
    path("medical_report/", views.medical_report, name = "medical_report"),
    path("add_med_report/",views.add_med_report, name ="add_med_report"),
    path("list_patient/",views.list_patient, name ="list_patient"),
    path('all_patients/', views.all_patients, name='all_patients'),
    path('medication_usage_report/', views.medication_usage_report, name='medication_usage_report'),
    path('new_medication_entry/', views.new_medication_entry, name='new_medication_entry'),
    path('medication_stock_list/', views.medication_stock_list, name='medication_stock_list'),
]

