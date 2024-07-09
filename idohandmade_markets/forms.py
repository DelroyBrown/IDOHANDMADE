# idohandmade_markets/forms.py
from django import forms
from .models import VendorApplication


class VendorApplicationForm(forms.ModelForm):
    class Meta:
        model = VendorApplication
        fields = (
            "vendor_name",
            "company_name",
            "products",
            "social_media_links",
            "website_link",
            "email",
            "contact_number",
        )
