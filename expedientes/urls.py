from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name="index_expedientes"),
    path('persona_list/', login_required(views.PersonaListView.as_view()), name="persona_list"),
    path('persona_new/', views.PersonaCreateView.as_view(), name="persona_new"),
    path('persona_edit/<int:pk>/', views.PersonaUpdateView.as_view(), name="persona_edit"),
    path('persona_delete/<int:pk>/', views.PersonaDeleteView.as_view(), name="persona_delete"),
    path('expediente_list/', views.ExpedienteListView.as_view(), name="expediente_list"),
    path('expediente_new/', views.ExpedienteCreateView.as_view(), name="expediente_new"),
    path('expediente_edit/<int:pk>/', views.ExpedienteUpdateView.as_view(), name="expediente_edit"),
    path('expediente_delete/<int:pk>/', views.ExpedienteDeleteView.as_view(), name="expediente_delete"),
    path('barrio_list/', views.BarrioListView.as_view(), name="barrio_list"),
    path('barrio_new/', views.BarrioCreateView.as_view(), name="barrio_new"),
    path('barrio_edit/<int:pk>/', views.BarrioUpdateView.as_view(), name="barrio_edit"),
    path('barrio_delete/<int:pk>/', views.BarrioDeleteView.as_view(), name="barrio_delete"),
]