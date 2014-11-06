from django.views.generic import View,TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from userprofiles.forms import UserProfileForm
from userprofiles.models import UserProfile
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
"""
class LoginView(TemplateView):
    template_name='login.html'

    def get_context_data(self,**kwargs):
        context=super (LoginView,self).get_context_data(**kwargs)
        auth=False
        user=None

        if self.request.user.is_authenticated():
            auth=True
            user=self.request.user.username

            data={
                'auth':auth,
                'user':user,
            }
            context.update(data)
            return context
"""
def listar(request):
    usuarios=UserProfile.objects.all()
    return render(request, 'userprofiles/lista.html',{'usuarios':usuarios})

class ListView(ListView):
    model=UserProfile

class DetailView(DetailView):
    model=UserProfile
    template_name='userprofiles/detail.html'
    @method_decorator(permission_required('userprofiles.view'))
    def dispatch(self,*args,**kwargs):
        return super(DetailView,self).dispatch(*args,**kwargs)

class CreateView(CreateView):
    template_name='userprofiles/create.html'
    model=UserProfile
    form_class=UserProfileForm

    @method_decorator(permission_required('userprofiles.create'))
    def dispatch(self,*args,**kwargs):
        return super(CreateView,self).dispatch(*args,**kwargs)

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return redirect(self.object)

class UpdateView(UpdateView):
    model=UserProfile
    template_name='userprofiles/update.html'
    form_class=UserProfileForm
    @method_decorator(permission_required('userprofiles.update'))
    def dispatch(self,*args,**kwargs):
        return super(UpdateView,self).dispatch(*args,**kwargs)

class DeleteView(DeleteView):
    model=UserProfile
    @method_decorator(permission_required('userprofiles.delete'))
    def dispatch(self,*args,**kwargs):
        return super(DeleteView,self).dispatch(*args,**kwargs)
    def get_succes_url(self):
        return reverse('list')


