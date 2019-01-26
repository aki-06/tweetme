from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    """ログインしないとtweetできないようにするMixin"""
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
            return self.form_invalid(form)


class FormOwnerMixin(object):
    """他ユーザーのtweetをupdateできないようにするMixin"""
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(FormOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['This user is not allowed to change this data'])
            return self.form_invalid(form)