from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm
from .models import Review
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
# Create your views here.

#class based view
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()

#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(request, "reviews/review.html", {
#             "form": form
#         })



# form view: the class based view to work with form 
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"
#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)

#createview = It automatically saves data
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    

#template view
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context

# This is template view
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

# this is list view
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    def get_querryset(self):
    
      base_querry = super().get_querryset()
      data = base_querry.filter(rating_gt = 4)
      return data



# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context

# DetailView

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    # this method defines the context that will be set for the template
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get('favorite_review')
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context
    


#adding a view to make the session work
class AddFavorite(View):
    def post(self, request):
        review_id = request.POST.get('review_id')  # Use get() method instead of ()
        request.session['favorite_review'] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

