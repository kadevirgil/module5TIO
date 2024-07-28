from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/confirmation'

class ConfirmationView(TemplateView):
    template_name = 'reviews/confirmation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This is our message'
        return context
    
class ReviewListView(ListView): 
    template_name = 'reviews/review_list.html'
    model = Review 
    context_object_name = 'reviews'
    
class ReviewDetailsView(DetailView):
    template_name = 'reviews/review_details.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        context['is_favorite'] = True
        
        
    
class AddFavorite(View):
    def post(self, request):
        review_id = request.POST['review_id']
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect('/reviews/' + review_id)
    