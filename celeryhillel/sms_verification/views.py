from django.shortcuts import render, redirect

from sms_verification.forms import SmsVerificationForm
from sms_verification.tasks import send_sms


def send_sms_view(request):
    if request.method == "GET":
        form = SmsVerificationForm()
        return render(request, "send_sms_page.html", {"page": form})
    form = SmsVerificationForm(request.POST)
    if form.is_valid():
        send_sms.delay(
            form.cleaned_data["phone_number"], form.cleaned_data["verification_message"]
        )
        return redirect("success")
    return render(request, "send_sms_page.html")


def success(request):
    return render(request, "success_page.html")


def test_send(request):
    send_sms.delay("+48733375448", "Try it")
    return render(request, "main.html")
