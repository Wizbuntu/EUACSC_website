from django.shortcuts import render
from .models import Ebooks, Contact
from .forms import EbookSearchForm, ContactForm
from search_views.search import SearchListView
from search_views.filters import BaseFilter


# Create your views here.


def index(request):
    return render(request, 'csc/index.html', {})


# contact
def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # save contact form
            contact_form.save()
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form
    }
    return render(request, 'csc/contact.html', context)


# Admission requirements
def admission(request):
    return render(request, 'csc/admission_requirements.html', {})


# Course Module
def course_module(request):
    return render(request, 'csc/course_modules.html', {})


# Staff Profile
def staff_profile(request):
    return render(request, 'csc/staff_profile.html', {})


# Ebooks View
class EbookFilter(BaseFilter):
    search_fields = {
        'search_text': ['title', 'author'],


    }


class EbookSearchList(SearchListView):
    model = Ebooks
    paginate_by = 10
    template_name = "csc/ebooks.html"
    form_class = EbookSearchForm
    filter_class = EbookFilter

# def ebooks(request):
#     return render(request, 'csc/ebooks.html')
