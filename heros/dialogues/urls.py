from django.urls import path
from dialogues import views
urlpatterns = ( 
    path('balayya/<int:pid>',views.bsearch),
    path('chiru/<int:pid>',views.csearch),
    path('venky/<int:pid>',views.vsearch)
)