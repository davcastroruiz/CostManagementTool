from django import forms


class UpdateDetailsForm(forms.Form):
    excel_file = forms.FileField(label='Excel File', required=False, validators=['xls', 'xlsx'])
