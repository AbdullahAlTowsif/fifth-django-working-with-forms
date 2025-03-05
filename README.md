# Django Built-in Forms

Django provides a powerful `forms` module that simplifies form handling in web applications. It helps in creating, validating, and processing forms efficiently with minimal code.

## Features of Django Forms
- **Automatic form generation** from Django models
- **Built-in validation** for common fields
- **Reusable form classes**
- **Error handling**
- **CSRF protection**
- **Integration with Django templates**

## Creating a Form
Django provides two main ways to create forms:
1. **Using `forms.Form`** (Manually defining fields)
2. **Using `forms.ModelForm`** (Creating forms based on Django models)

### Example: Using `forms.Form`
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

### Example: Using `forms.ModelForm`
```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
```

## Rendering Forms in Templates
Django provides multiple ways to render forms in templates:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
Other rendering options:
- `{{ form.as_table }}` - Renders fields in a table
- `{{ form.as_ul }}` - Renders fields as an unordered list

## Handling Forms in Views
Example of processing a form submission in a Django view:
```python
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            print(form.cleaned_data)
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```

## Form Validation
Django automatically validates fields based on their type, but custom validation can be added using `clean_<fieldname>()` methods.
```python
class ContactForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "example.com" not in email:
            raise forms.ValidationError("Email must be from example.com")
        return email
```

## Conclusion
Django's built-in forms provide an easy way to handle form processing, validation, and rendering in web applications. Whether using `forms.Form` or `forms.ModelForm`, Django simplifies form handling, making it a powerful tool for developers.

