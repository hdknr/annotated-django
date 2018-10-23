# ファイルフィールド

## ModelForm じゃない場合はcleaned_data に入らない

~~~py
from django import forms
from django.utils.functional import cached_property

class ProfileForm(forms.Form):
    photo = forms.ImageField(label='写真', required=False)

    @cached_property
    def photo_data(self):
        return self.files.get('photo', None)
~~~

~~~py
def profile_update(request, id):
    form = forms.ProfileForm(request.POST, request.FILES)
    if form.is_valid(): 
        user = User.objects.get(id=id)
        user.photo_set.create(data=form.photo)
        user.save()
~~~