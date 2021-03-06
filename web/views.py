from django.shortcuts import render
from .models import Artwork
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.contrib.admin.widgets import FilteredSelectMultiple, RelatedFieldWidgetWrapper
from django.contrib.auth.decorators import login_required



# def userPrefs(request):
    # from bootstrap_themes import list_themes
    # theme = models.CharField(max_length=255, default='default', choices=list_themes())

# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated() and not request.user.is_anonymous():
        artwork = Artwork.objects.filter(user=request.user).all()
    else:
        artwork = {}
    return render(request, 'home/index.html', {'artworks': artwork})

class ArtworkUpdate(UpdateView):
    model = Artwork
    fields = ['name', 'inventory_id', 'media', 'finished', 'height', 'width', 'depth', 'mass']

    def get_object(self, queryset=None):
        obj = Artwork.objects.get(id=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'Saved')
        return '/artwork/%d/' % self.get_object().id

class ArtworkDelete(DeleteView):
    model = Artwork
    success_url = reverse_lazy('home')
