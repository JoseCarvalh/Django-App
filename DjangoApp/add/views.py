from add.UserForm import UserForm
from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email

from list.models import Users


def is_email_valid(email):
    try:
        validate_email(email)
        return True
    finally:
        return False


def index(request):

    if request.method == "POST":

        user_form = UserForm(request.POST)

        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            email = user_form.cleaned_data['email']

            if len(name) > 2:
                if is_email_valid(email):
                    user = Users(
                        name=name,
                        email=email
                    )
                    user.save()
                    messages.info(request, 'User added successfully!')

                    return render(request, 'menu/index.html')

                else:
                    messages.info(request, 'Please insert a valid email')
            else:
                messages.info(request, 'Name needs at least 3 characters')
        else:
            messages.info(request, 'Please fill all the text fields!')

    return render(request, 'add/index.html')
