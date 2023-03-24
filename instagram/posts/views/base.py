from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView


class IndexView(View):
    def get(self, request):
        query = request.GET.get('search')
        context = {}
        if query:
            users = get_user_model().objects.filter(Q(username__icontains=query) | Q(email__icontains=query) | Q(
                first_name__icontains=query))
            context = {
                'user_obj': users
            }
        else:
            users = get_user_model().objects.filter(Q(subscriptions=request.user.pk))
            context = {
                'user_obj': users
            }
        return render(request, 'index.html', context=context)
