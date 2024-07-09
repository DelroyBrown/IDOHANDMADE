# idohandmade_markets/views.py
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import VendorApplicationForm
from .models import VendorApplication, MarketEvent, EventDate


def apply_to_market_event(request, market_event_id):
    market_event = get_object_or_404(MarketEvent, id=market_event_id)
    event_dates = market_event.event_dates.all()

    if request.method == "POST":
        form = VendorApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.market_event = market_event

            # Retrieve event_date_id from the form data and get the EventDate object
            event_date_id = request.POST.get("event_date_id")
            event_date = get_object_or_404(EventDate, id=event_date_id)

            application.event_date = event_date  # Assign selected EventDate
            application.save()

            # Email functionality
            subject = f"New Vendor Application for {market_event.title}"
            message = f"Vendor Name: {application.vendor_name}\n"
            message += f"Company Name: {application.company_name}\n"
            message += f"Products: {application.products}\n"
            message += f"Social Media Link: {application.social_media_links}\n"
            message += f"Website Link: {application.website_link}\n"
            message += f"Email: {application.email}\n"
            message += f"Contact Number: {application.contact_number}\n"
            message += f"Date Applied: {application.event_date.date}\n"
            message += f"Price Applied: £{application.event_date.price}\n"

            from_email = os.getenv("EMAIL_HOST_USER")
            to_email = os.getenv("EMAIL_HOST_USER")
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            messages.success(request, "Application submitted successfully!")
            return redirect("idohandmade_markets:market_event_list")
    else:
        form = VendorApplicationForm()

    return render(
        request,
        "markets/apply_to_market_event.html",
        {"form": form, "market_event": market_event, "event_dates": event_dates},
    )


def market_event_list(request):
    market_events = (
        MarketEvent.objects.prefetch_related("event_dates")
        .all()
        .order_by("-created_at")
    )
    # Adding the count of event dates to each market event
    for event in market_events:
        event.date_count = event.event_dates.count()
    return render(
        request, "markets/market_event_list.html", {"market_events": market_events}
    )
