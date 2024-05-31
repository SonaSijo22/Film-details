from django import forms
from myapp.models import Movie

class MovieForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields ="__all__"
        widgets={#style chayyan vendi
            "title":forms.TextInput(attrs={"class":"form-control"}),#form control kodukkan kaaranam title ennu kofuthitttu athinte adiyil ezhuthan paattunna rethiyilchayyan vendi ahnu
            "director":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.TextInput(attrs={"class":"form-control"}),
            "geners":forms.TextInput(attrs={"class":"form-control"}),
            "poster":forms.FileInput(attrs={"class":"form-control"}),
            "actors":forms.TextInput(attrs={"class":"form-control"}),
            "run_time":forms.NumberInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "writers":forms.TextInput(attrs={"class":"form-control"}),
            "languages":forms.TextInput(attrs={"class":"form-control"})
            
        }

# errors
# ---------
# matching query doesn't exist
# template deoen't exist
# context must be dictionary rather than set

