# -*- encoding: utf-8 -*-

from django.forms import ModelForm

from apps.publications.models import Tag, Publication


TAGS = [x.tag for x in Tag.objects.all()]


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ['body','tags']

    # def clean_somedata(self):
    #     return sometransformation(self.cleaned_data['somedata'])

# class PublicationForm(forms.Form):
#     name = forms.CharField()
#     body = forms.CharField(widget=forms.Textarea)
#     tag = forms.MultipleChoiceField(initial=TAGS)
#
