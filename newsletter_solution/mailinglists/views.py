from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from newsletter_solution.mailinglists.mixins import MailingListMixin
from newsletter_solution.mailinglists.models import MailingList


class MailingListListView(MailingListMixin, ListView):
    model = MailingList
    context_object_name = 'mailing_lists'
    ordering = ('name', )
    paginate_by = 10


class MailingListCreateView(MailingListMixin, CreateView):
    model = MailingList
    fields = ('name', 'slug', 'campaign_default_from_name', 'campaign_default_from_email', 'campaign_default_subject')


class MailingListDetailView(MailingListMixin, DetailView):
    model = MailingList
    context_object_name = 'mailing_list'

