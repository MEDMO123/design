from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import *
from . import forms

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,permission_required

from django.conf import settings
from django.shortcuts import get_object_or_404


# Create your views here.
#Vue pour le login
def loginView(request):
    form = forms.loginForm()    
    if request.method == 'POST':
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)                
                if user.is_staff:
                    return redirect('modele')
                return redirect('modele')
                          
    return render(
        request, 'design/login.html', context={'form': form})

#Vue pour la creation de compte
def signupView(request):
    form = forms.signupForm()
    if request.method == 'POST':
        form = forms.signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('modele')
    return render(request, 'design/signup.html', {'form': form})

#Vue de la page d'accueil des modeles
def ModeleView(request):
    model=Modele.objects.all()   
    return render(request,'design/modele.html',{'models':model})

#Vue de la page d'accueil des accessoires
def AccessoireView(request):   
    model=Accessoire.objects.all() 
    return render(request,'design/accessoire.html',{'models':model})

#Vue detaillée  pour les modeles
def DetailModeleView(request,pk):
    model=get_object_or_404(Modele,pk=pk)
    return render(request,'design/detail_modele.html',{'model':model})

#Vue  pour les modeles Hommes only
def ModeleHommeView(request):
    model=Modele.objects.filter(genre='Homme')
    return render(request,'design/modele_homme.html',{'models':model})

#Vue  pour les modeles Femmes only
def ModeleFemmeView(request):
    model=Modele.objects.filter(genre='Femme')
    return render(request,'design/modele_femme.html',{'models':model})

#Vue  pour les accessoires Hommes only
def AccessoireHommeView(request):
    model=Accessoire.objects.filter(genre='Homme')
    return render (request,'design/accessoire_homme.html',{'models':model})

#Vue  pour les accessoires Femmes only
def AccessoireFemmeView(request):
    model=Accessoire.objects.filter(genre='Femme')
    return render (request,'design/accessoire_femme.html',{'models':model})

#Vue pour ajouter un nouveau modele
def ModelePostView(request):
    form=forms.modeleForm()
    if request.method=='POST':
        form=forms.modeleForm(request.POST,request.FILES)
        if form.is_valid():            
            form.save()
            return redirect('modele')
        form=forms.modeleForm()
        
    return render(request,'design/admin/modele_post.html',{'form':form})
#Vue pour modifier un  modele
def ModeleUpdateView(request,pk):
    modele=get_object_or_404(Modele, pk=pk)
    form=forms.modeleForm(instance=modele)
    if request.method=='POST':
        form=forms.modeleForm(request.POST,request.FILES,instance=modele)
        if form.is_valid():
            form.save()
            return redirect ('modele')
        form=forms.modeleForm(instance=modele)
    return render (request,'design/admin/modele_update.html',{'form':form})

#Vue pour supprimer un  modele
def ModeleDeleteView(request,pk):
    modele=Modele.objects.get(pk=pk)
    if request.method=='POST':
        modele.delete()
        return redirect('modele')
    return render (request, 'design/admin/modele_delete.html',{'modele':modele})

#Vue pour ajouter un nouvel accesssoire
def AccessoirePostView(request):
    form=forms.accessoireForm()
    if request.method=='POST':
        form=forms.accessoireForm(request.POST,request.FILES)
        if form.is_valid():            
            form.save()
            return redirect('accessoire')
        form=forms.accessoireForm()
    return render(request,'design/admin/accessoire_post.html',{'form':form})

#Vue pour modifier un  accesssoire
def AccessoireUpdateView(request,pk):
    accessoire=get_object_or_404(Accessoire, pk=pk)
    form=forms.accessoireForm(instance=accessoire)
    if request.method=='POST':
        form=forms.accessoireForm(request.POST,request.FILES,instance=accessoire)
        if form.is_valid():
            form.save()
            return redirect ('accessoire')
        form=forms.accessoireForm( instance=accessoire) 
    return render (request,'design/admin/accessoire_update.html',{'form':form})

#Vue pour supprimer un  accesssoire
def AccessoireDeleteView(request,pk):
    accessoire=Accessoire.objects.get(pk=pk)
    if request.method=='POST':
        accessoire.delete()
        return redirect('accessoire')
    return render (request, 'design/admin/accessoire_delete.html',{'accessoire':accessoire})


#Vue pour effectuer une demande de rdv
@login_required
def RdvView(request):
    form=forms.rdv_clientForm()
    if request.method=='POST':
        form=forms.rdv_clientForm(request.POST)
        if form.is_valid():
            client=request.user
            date_rdv=form.cleaned_data.get('date_rdv')
            objet=form.cleaned_data.get('objet')
            Rdv.objects.create(client=client,date_rdv=date_rdv,objet=objet).save()
            return redirect('profile')
    return render (request,'design/rdv.html',{'form':form})

#Vue pour afficher la liste des rdv
@login_required
def RdvListView(request):
    model=Rdv.objects.all()
    return render(request,'design/admin/rdv_liste.html',{'models':model})

#Vue pour modifier un rdv
@login_required
def RdvUpdateView(request,pk):
    rdv=get_object_or_404(Rdv,pk=pk)
    form=forms.rdv_adminForm(instance=rdv)
    if request.method=='POST':
       form=forms.rdv_adminForm(request.POST,instance=rdv) 
       form.save()
       return redirect('rdvlist')
    form=forms.rdv_adminForm(instance=rdv)
    return render (request,'design/admin/rdv_update.html',{'form':form})

#Vue pour supprimer un rdv
@login_required
def RdvDeleteView(request,pk):
    rdv=get_object_or_404(Rdv,pk=pk)    
    if request.method=='POST':
        rdv.delete()
        return redirect('rdvlist')
    return render (request,'design/admin/rdv_delete.html',{'rdv':rdv})

#Vue pour effectuer une commande de modele
@login_required
def CmdModeleView(request):
    form=forms.cmdmodel_clientForm()
    if request.method=='POST':
        form=forms.cmdmodel_clientForm(request.POST)
        if form.is_valid():
            client=request.user
            modele=form.cleaned_data.get('modele')
            taille=form.cleaned_data.get('taille')
            reception=form.cleaned_data.get('reception')            
            Commandemodele.objects.create(client=client,modele=modele,taille=taille,reception=reception).save()
            return redirect('profile')
    return render(request,'design/cmd_modele.html',{'form':form}) 
 
#Vue pour afficher lla liste des cmd de modele et d'
@login_required
def CmdModelelistView(request):
    model=Commandemodele.objects.all()   
    return render(request,'design/admin/cmdmodele_liste.html',{'models':model})


#Vue pour modifier une commande de modele
@login_required
def CmdModeleUpdateView(request,pk):
    commandemodele=get_object_or_404(Commandemodele,pk=pk)
    form=forms.cmdmodele_adminform(instance=commandemodele)
    if request.method=='POST':
       form=forms.cmdmodele_adminform(request.POST,instance=commandemodele) 
       form.save()
       return redirect('cmdmodelelist')
    form=forms.cmdmodele_adminform(instance=commandemodele)
    return render (request,'design/admin/cmd_modele_update.html',{'form':form})

#Vue pour supprimer une commande de modele
@login_required
def CmdModeleDeleteView(request,pk):
    commandemodele=get_object_or_404(Commandemodele,pk=pk)
    if request.method=='POST':
        commandemodele.delete()
        return redirect('cmdmodelelist')
    return render (request,'design/admin/cmd_modele_delete.html',{'commandemodele':commandemodele})
  

#Vue pour effectuer une commande d'accessoire
@login_required
def CmdAccessoireView(request):
    form=forms.cmdaccessoire_clientForm()
    if request.method=='POST':
        form=forms.cmdaccessoire_clientForm(request.POST)
        if form.is_valid():
            client=request.user
            accessoire=form.cleaned_data.get('accessoire')
            reception=form.cleaned_data.get('reception')
            Commandeaccessoire.objects.create(client=client,accessoire=accessoire,reception=reception).save()
            return redirect('profile')
    return render(request,'design/cmd_accessoire.html',{'form':form})    


#Vue pour afficher la liste des commandes d'accesssoire
@login_required
def CmdAccessoirelistView(request):
    model=Commandeaccessoire.objects.all()   
    return render(request,'design/admin/cmdaccessoire_liste.html',{'models':model})

#Vue pour modifier une commande d'accesssoire
@login_required
def CmdAccessoireUpdateView(request,pk):
    commandeaccessoire=get_object_or_404(Commandeaccessoire,pk=pk)
    form=forms.cmdaccessoire_adminform(instance=commandeaccessoire)
    if request.method=='POST':
       form=forms.cmdaccessoire_adminform(request.POST,instance=commandeaccessoire) 
       form.save()
       return redirect('cmdaccessoirelist')
    form=forms.cmdaccessoire_adminform(instance=commandeaccessoire)
    return render (request,'design/admin/cmd_accessoire_update.html',{'form':form})

#Vue pour supprimer une commande d'accesssoire
@login_required
def CmdAccessoireDeleteView(request,pk):
    commandeaccessoire=get_object_or_404(Commandeaccessoire,pk=pk)
    if request.method=='POST':
        commandeaccessoire.delete()
        return redirect('cmdaccessoirelist')
    return render (request,'design/admin/cmd_modele_delete.html',{'commandeaccessoire':commandeaccessoire})
  

@login_required(login_url='/login/')
def UserProfileView(request):
    user=request.user
    rdv=Rdv.objects.all()
    cmdmodele=Commandemodele.objects.all()  
    cmdaccessoire=Commandeaccessoire.objects.all()    
    return render (request, 'design/profile.html',{'rdvs':rdv, 'cmdmodeles':cmdmodele,'cmdaccessoires':cmdaccessoire})

def AdminView(request):
    return render(request,'design/admin/admin.html')

def UserListView(request):
    model=User.objects.all()
    return render(request,'design/admin/user.html',{'models':model})

def UserUpdateView(request,pk):
    user=get_object_or_404(User,pk=pk)
    form=forms.userUpdateForm(instance=user)
    if request.method=='POST':
       form=forms.userUpdateForm(request.POST,instance=user) 
       form.save()
       return redirect('userlist')
    form=forms.userUpdateForm(instance=user)
    return render (request,'design/admin/user_update.html',{'form':form})

def UserDeleteView(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        user.delete()
        return redirect('userlist')
    return render (request,'design/admin/user_delete.html',{'user':user})
  
