from django import forms

# widgets = field to html input

class contactForm(forms.Form):
    name = forms.CharField(label='Username', help_text="Text must be within 70 characters", required=False, disabled=False, widget=forms.Textarea(attrs={'placeholder' : 'Enter your Name'}))
    # file = forms.FileField()
    email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    PIZZA = [('Pepperoni', 'Pepperoni'), ('Mushroom', 'Mushroom'), ('Beef', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=PIZZA, widget=forms.CheckboxSelectMultiple)
    