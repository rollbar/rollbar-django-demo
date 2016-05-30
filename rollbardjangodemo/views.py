def broken(request):
    data = None
    return data['result']


def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    return is_valid_login(email, password)
