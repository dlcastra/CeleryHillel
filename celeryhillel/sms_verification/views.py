from django.shortcuts import render, redirect
from sms_verification.forms import SmsVerificationForm
from sms_verification.tasks import send_sms


def send_sms_view(request):
    if request.method == "POST":
        form = SmsVerificationForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            message = form.cleaned_data["verification_message"]
            send_sms.delay(phone_number, message)
            return redirect("success")
    else:
        form = SmsVerificationForm()

    return render(request, "send_sms_page.html", {"page": form})


def success(request):
    return render(request, "success_page.html")
