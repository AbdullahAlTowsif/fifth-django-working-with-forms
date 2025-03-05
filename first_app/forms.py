from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Username')
    file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # PIZZA = [('P', 'Pepperoni'), ('M', 'Mushroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=PIZZA)
    