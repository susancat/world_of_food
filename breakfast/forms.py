from django import forms
from django.contrib.auth.models import User
from breakfast.models import Continent, Recipe, Review, Favourites, UserProfile


class ContinentForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the continent name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Continent
		fields = ('name',)


class RecipeForm(forms.ModelForm):
	recipe_name = forms.CharField(max_length=128, help_text="Please enter the name of the recipe.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	# short_description = forms.CharField(max_length=1280, help_text="Please enter the short description of the recipe.")
	# description = forms.CharField(max_length=1280, help_text="Please enter the description of the recipe.")
	# ingredients = forms.CharField(max_length=1280, help_text="Please enter the ingredients of the recipe.")
	# steps = forms.CharField(max_length=1280, help_text="Please enter the steps of the recipe.")
	# image = models.ImageField(upload_to='recipe_images', help_text="Please upload the picture of the recipe." )


	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')
		# If url is not empty and doesn't start with 'http://',
		# then prepend 'http://'.
		if url and not url.startswith('http://'):
			url = 'http://' + url
			cleaned_data['url'] = url

		return cleaned_data

	class Meta:
		model = Recipe
		exclude = ('continent',)


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(required=False)
	
	class Meta:
		model = UserProfile
		exclude = ('user',)
