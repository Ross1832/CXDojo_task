from django import forms
from .models import User
import csv
from datetime import datetime
import xmltodict
import re
import urllib.request



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'date_joined',
        ]

        widgets = {
            'date_joined': forms.DateInput(),
        }


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'date_joined',
        ]

        widgets = {
            'date_joined': forms.DateInput(),
        }


class UploadFileForm(forms.Form):
    file = forms.FileField()
    widgets = {
        'file': forms.ClearableFileInput(attrs={
            'multiple': True,
        }),
    }

    def clean_file(self):
        file = self.cleaned_data['file']
        if str(file).endswith('.csv'):
            decoded_file = file.read().decode('utf-8').splitlines()
            csv_file = csv.DictReader(decoded_file)
            for row in csv_file:
                username = re.sub(r'\(.*\)', '', str(row['username']))
                if username and row['password'] and row['date_joined']:
                    try:
                        user = User.objects.create_user(
                            username=username,
                            password=row['password'],
                            date_joined=datetime.fromtimestamp(int(row['date_joined']))
                        )
                        user.save()
                    except:
                        print('User already created')

        elif str(file).endswith('.xml'):
            xml_file = xmltodict.parse(file, process_namespaces=True)['user_list']['user']['users']['user']
            for row in xml_file:
                first_name = re.sub(r"\(.*\)", '', str(row['first_name']))
                last_name = re.sub(r"\(.*\)", '', str(row['last_name']))
                if first_name is not '' and last_name is not '':
                    User.objects.filter(username__icontains=last_name).update(
                        last_name=last_name, first_name=first_name)

