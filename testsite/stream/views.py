from django.shortcuts import render
from django.views.generic import ListView
from stream.models import Stream

class Index(ListView):
    model = Stream

    def get_queryset(self):
        return super(Index, self).get_queryset().exclude(
            photo__deleted=True, tweet__deleted=True)
