from django.forms import ModelForm

from core.forms.input import SelectWithModal
from core.models import Cohort


class CohortForm(ModelForm):
    class Meta:
        model = Cohort
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owners'].widget = SelectWithModal(url_name='contact_add', entity_name='contact',
                                                          choices=self.fields['owners'].widget.choices,
                                                          allow_multiple_selected=True)

    field_order = [
        'title',
        'owners',
        'institutes',
        'comments'
    ]


class CohortFormEdit(CohortForm):
    pass
