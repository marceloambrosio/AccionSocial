from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index_expedientes"),
    path('persona_list/', views.persona_list, name="persona_list"),
    path('persona_new/', views.PersonaCreateViews.as_view(), name="persona_new"),
    path('persona_edit/<int:pk>/', views.PersonaUpdateViews.as_view(), name="persona_edit"),
    path('persona_delete/<int:pk>/', views.PersonaDeleteView.as_view(), name="persona_delete"),
    path('expediente_list/', views.persona_list, name="expediente_list"),
    path('expediente_new/', views.PersonaCreateViews.as_view(), name="expediente_new"),
    path('expediente_edit/<int:pk>/', views.PersonaUpdateViews.as_view(), name="expediente_edit"),
    path('expediente_delete/<int:pk>/', views.PersonaDeleteView.as_view(), name="expediente_delete"),
    path('barrio_list/', views.barrio_list, name="barrio_list"),
    path('barrio_new/', views.BarrioCreateViews.as_view(), name="barrio_new"),
    path('barrio_edit/<int:pk>/', views.BarrioUpdateViews.as_view(), name="barrio_edit"),
    path('barrio_delete/<int:pk>/', views.BarrioDeleteView.as_view(), name="barrio_delete"),
]