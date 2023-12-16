from django import forms
from .models import Actors, ActorMovie
from django.forms import ModelForm


class ActorsForm(forms.ModelForm):
    class Meta:
        model = Actors
        fields = ['actor_id','FirstName', 'LastName', 'Age', 'BirthDate', 'BirthPlace', 'Height', 'Description','Status']

    def clean_roles(self):
        roles = self.cleaned_data['roles']
        return [role.strip() for role in roles.split(',') if role.strip()]

    def save(self, commit=True):
        # Save the actor instance
        actor = super().save(commit)

        # Associate the selected movies with the actor and set roles
        for movie, role in zip(self.cleaned_data['movies'], self.cleaned_data['roles']):
            ActorMovie.objects.create(actor=actor, movie=movie, role=role)

        return actor
