from django.urls import path
from . import views


urlpatterns = [
    path('', views.logandreg),
    path('register', views.register),
    path('login', views.login),
    path('process_quote', views.process_quote),
    path('quotes', views.quotes),
    path('logout', views.logout),
    path('user_profile/<int:id>',views.profile),
    path('my_profile/<int:id>', views.edituser),
    path('updateaccount/<int:id>', views.updateaccount),
    path('delete/<int:id>', views.destroy),
    path('like/<int:id>', views.add_like),

]
