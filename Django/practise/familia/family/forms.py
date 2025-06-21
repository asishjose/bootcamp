from django.forms import ModelForm
from . models import FamilyMember

class FamForm(ModelForm):
    class Meta:
        model = FamilyMember
        fields='__all__'
        