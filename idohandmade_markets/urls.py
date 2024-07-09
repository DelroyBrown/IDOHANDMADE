# idohandmade_markets/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "idohandmade_markets"

urlpatterns = [
    path(
        "market-events/<int:market_event_id>/apply/",
        views.apply_to_market_event,
        name="apply_to_market_event",
    ),
    path("market-events/", views.market_event_list, name="market_event_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
