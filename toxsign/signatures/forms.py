from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import FormActions

from toxsign.assays.models import Assay
from toxsign.signatures.models import Signature
from toxsign.ontologies.models import Disease


class SignatureCreateForm(forms.ModelForm):

    disease = forms.ModelChoiceField(
                queryset=Disease.objects.all(),
                widget=autocomplete.ModelSelect2(url='/ontologies/disease-autocomplete')
              )

    class Meta:
        model = Signature
        exclude = ("tsx_id", "created_at", "created_by", "updated_at", )

    def __init__(self, *args, **kwargs):
        assid = kwargs.pop('assid')
        super(SignatureCreateForm, self).__init__(*args, **kwargs)
        factors = Assay.objects.get(tsx_id=assid).factor_of.all()
        self.fields['factor'].queryset = factors
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('save', 'Save'))
