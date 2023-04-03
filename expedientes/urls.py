from django.urls import path
from . import views 
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name="index_expedientes"),
    path('persona_index/', login_required(views.PersonaIndexView.as_view()), name="persona_index"),
    path('persona_list/', login_required(views.PersonaListView.as_view()), name="persona_list"),
    path('persona_new/', login_required(views.PersonaCreateView.as_view()), name="persona_new"),
    path('persona_edit/<int:pk>/', login_required(views.PersonaUpdateView.as_view()), name="persona_edit"),
    path('persona_delete/<int:pk>/', login_required(views.PersonaDeleteView.as_view()), name="persona_delete"),
    path('expediente_list/', login_required(views.ExpedienteListView.as_view()), name="expediente_list"),
    path('expediente_new/', login_required(views.ExpedienteCreateView.as_view()), name="expediente_new"),
    path('expediente_edit/<int:pk>/', login_required(views.ExpedienteUpdateView.as_view()), name="expediente_edit"),
    path('expediente_delete/<int:pk>/', login_required(views.ExpedienteDeleteView.as_view()), name="expediente_delete"),
    path('barrio_list/', login_required(views.BarrioListView.as_view()), name="barrio_list"),
    path('barrio_new/', login_required(views.BarrioCreateView.as_view()), name="barrio_new"),
    path('barrio_edit/<int:pk>/', login_required(views.BarrioUpdateView.as_view()), name="barrio_edit"),
    path('barrio_delete/<int:pk>/', login_required(views.BarrioDeleteView.as_view()), name="barrio_delete"),
]