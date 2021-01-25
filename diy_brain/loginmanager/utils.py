from signupmanager.models import UserData
from django.http import HttpResponseRedirect
from .models import SessionData
from hashlib import sha1
import base64
import ipaddress


def verify_credentials(email_address, password):
    rows = UserData.objects.filter(email_address=email_address)
    for row in rows:
        encoded_plain = base64.b64encode(bytes(password, 'utf-8'))
        encoded_password = sha1(encoded_plain).hexdigest()
        if encoded_password == row.password:
            return True
        else:
            return False


def add_session(request, email_address):
    request.session.set_expiry(7200)
    if ipaddress.ip_address(request.META['REMOTE_ADDR']).is_private:
        ip_address = request.META['REMOTE_ADDR']
    else:
        ip_address = request.META['HTTP_X_FORWARDED_FOR']
    rows = SessionData.objects.filter(email_address=email_address, ip_address=ip_address)
    if len(rows) == 0:
        row = SessionData(email_address=email_address, ip_address=ip_address)
        row.save()
    request.session['email_address'] = email_address


def remove_session(request):
    email_address = request.session['email_address']
    if ipaddress.ip_address(request.META['REMOTE_ADDR']).is_private:
        ip_address = request.META['REMOTE_ADDR']
    else:
        ip_address = request.META['HTTP_X_FORWARDED_FOR']
    rows = SessionData.objects.filter(email_address=email_address, ip_address=ip_address)
    for row in rows:
        row.delete()
    request.session['email_address'] = ''
    return HttpResponseRedirect("/login")
