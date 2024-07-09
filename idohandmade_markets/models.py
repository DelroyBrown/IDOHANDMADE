# idohandmade_markets/models.py
from django.db import models


class MarketEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2500)
    event_type = models.CharField(max_length=60, default='')
    location = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class EventDate(models.Model):
    market_event = models.ForeignKey(MarketEvent, related_name='event_dates', on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.market_event.title} on {self.date}"


class VendorApplication(models.Model):
    market_event = models.ForeignKey(MarketEvent, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    products = models.TextField()
    social_media_links = models.URLField(blank=True)
    website_link = models.URLField(blank=True)
    email = models.EmailField(max_length=200, default="")
    contact_number = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vendor_name} - {self.market_event}"
