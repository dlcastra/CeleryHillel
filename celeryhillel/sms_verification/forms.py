from django import forms
import phonenumbers
from sms_verification.models import SmsVerification


class SmsVerificationForm(forms.ModelForm):
    class Meta:
        model = SmsVerification
        fields = ["phone_number", "verification_message"]
        labels = {
            "phone_number": "Номер телефону:",
            "verification_message": "Повідомлення",
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number:
            raise forms.ValidationError(
                "Phone cannot be empty/Поле телефон не може бути пустим"
            )

        if len(phone_number) < 12:
            raise forms.ValidationError(
                "The number provided is too short/Наданий номер занадто короткий"
            )

        if any(char.isalpha() for char in phone_number):
            raise forms.ValidationError(
                "The phone number must not have a letter/Номер телефону не повинен містити літер"
            )

        try:
            parsed = phonenumbers.parse(phone_number, None)
        except phonenumbers.NumberParseException as error:
            raise forms.ValidationError(
                f"{error.args[0]}/Наданий рядок, схоже, не був номером телефону "
            )

        formatted_phone = phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )
        return formatted_phone

    # def clean_verification_message(self):
    #     verification_message = self.cleaned_data["verification_message"]
    #     if len(verification_message) > 50:
    #         raise forms.ValidationError(
    #             "The message is too long, the maximum length is 50 characters/"
    #             "Повідомлення занадто довге, максимальна довжина - 50 символів"
    #         )
