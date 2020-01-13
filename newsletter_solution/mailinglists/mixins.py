from django.views.generic.base import ContextMixin


class MailingListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        if 'menu' not in kwargs:
            kwargs['menu'] = 'lists'
        return super().get_context_data(**kwargs)
