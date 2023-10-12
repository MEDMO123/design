from django.urls import path
from . import views
from django.contrib.auth.views import (
     LogoutView, PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    #Chemin pour l'authentification
    path('login/',views.loginView,name='login'),   
    path('signup/',views.signupView,name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='design/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='design/password_change_done.html'),
         name='password_change_done'     
         ),

    #Chemin pour l'affichage des produits et filtres
     #Modeles
    path('',views.ModeleView,name='modele'),
    path('modelehomme/',views.ModeleHommeView,name='modelehomme'),
    path('modelefemme/',views.ModeleFemmeView,name='modelefemme'),
    path('detailmodele/<int:pk>/',views.DetailModeleView,name='detailmodele'),
     #Accessoires
    path('accessoire/',views.AccessoireView,name='accessoire'),    
    path('accessoirehomme/',views.AccessoireHommeView,name='accessoirehomme'),
    path('accessoirefemme/',views.AccessoireFemmeView,name='accessoirefemme'),    
    

    #Admin
    #Modeles
    path('modelepost/',views.ModelePostView,name='modelepost'),
    path('modeleupdate/<int:pk>/update',views.ModeleUpdateView,name='modeleupdate'),
    path('modeledelete/<int:pk>/delete',views.ModeleDeleteView,name='modeledelete'),
    #Accessoires
    path('accessoirepost/',views.AccessoirePostView,name='accessoirepost'),
    path('accessoireupdate/<int:pk>/update',views.AccessoireUpdateView,name='accessoireupdate'),
    path('accessoiredelete/<int:pk>/delete',views.AccessoireDeleteView,name='accessoiredelete'),

    
    #Chemins relatifs aux rdv
    path('rdv/',views.RdvView,name='rdv'),
    #Admin
    path('rdvlist/',views.RdvListView,name='rdvlist'),
    path('rdvupdate/<int:pk>/update',views.RdvUpdateView,name='rdvupdate'),
    path('rdvdelete/<int:pk>/delete',views.RdvDeleteView,name='rdvdelete'),
    
    # Chemins relatifs au Commandes
    #User
    path('cmdmodele/',views.CmdModeleView,name='cmdmodele'),
    path('cmdaccessoire/',views.CmdAccessoireView,name='cmdaccessoire'),

    # Admin
    #Modeles
    path('cmdmodelelist/',views.CmdModelelistView,name='cmdmodelelist'),
    path('cmdmodeleupdate/<int:pk>/update',views.CmdModeleUpdateView,name='cmdmodeleupdate'),
    path('cmdmodeledelete/<int:pk>/delete',views.CmdModeleDeleteView,name='cmdmodeledelete'),
    #Accessoires
    path('cmdaccessoirelist/',views.CmdAccessoirelistView,name='cmdaccessoirelist'),
    path('cmdaccessoireupdate/<int:pk>/update',views.CmdAccessoireUpdateView,name='cmdaccessoireupdate'),
    path('cmdaccessoiredelete/<int:pk>/delete',views.CmdAccessoireDeleteView,name='cmdaccessoiredelete'),

    path('adminkl/',views.AdminView,name='adminkl'),
    path('profile/',views.UserProfileView,name='profile'),
    #Users
    path('userlist/',views.UserListView,name='userlist'),
    path('userupdate/<int:pk>/update',views.UserUpdateView,name='userupdate'),
    path('userlist/<int:pk>/delete',views.UserDeleteView,name='userdelete'),

]