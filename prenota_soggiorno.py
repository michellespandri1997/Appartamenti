from __future__ import annotations

from datetime import date, timedelta
from uuid import uuid4

import streamlit as st


st.set_page_config(
    page_title="Prenota Milano",
    page_icon=":material/apartment:",
    layout="centered",
)

TODAY = date.today()
PROPERTIES = {
    "Brera Loft": {
        "zona": "Brera · Milano centro",
        "ospiti": 4,
        "tariffa": 178,
        "image": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1100&q=85",
        "descrizione": "Un punto di partenza nel cuore creativo di Milano.",
    },
    "Navigli Studio": {
        "zona": "Navigli · Darsena",
        "ospiti": 2,
        "tariffa": 132,
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1100&q=85",
        "descrizione": "La città da vivere tra i canali e le vie dei Navigli.",
    },
}
SAMPLE_RESERVATIONS = {
    "Brera Loft": {
        "check_in": TODAY + timedelta(days=20),
        "check_out": TODAY + timedelta(days=23),
    },
    "Navigli Studio": {
        "check_in": TODAY + timedelta(days=27),
        "check_out": TODAY + timedelta(days=31),
    },
}


def format_date(value: date, language: str) -> str:
    return value.strftime("%d/%m/%Y" if language == "it" else "%b %d, %Y")


def euro(value: int) -> str:
    return f"€ {value:,.0f}".replace(",", ".")


COPY = {
    "it": {
        "language": "Lingua",
        "eyebrow": "SOGGIORNI SELEZIONATI · MILANO, ITALIA",
        "headline": "La tua Milano, da abitare.",
        "intro": "Due appartamenti, due quartieri da vivere. Trova il tuo spazio in città.",
        "up_to": "fino a {count} ospiti",
        "starting_at": "Da",
        "per_night": "a notte",
        "search_title": "Trova il tuo soggiorno",
        "search_caption": "Esempio: il calendario mostra un periodo occupato per ogni appartamento. Le altre date sono libere nella demo.",
        "property": "Appartamento",
        "availability_title": "Disponibilità di esempio",
        "available": "Disponibile",
        "available_until": "Check-out entro il {date}",
        "available_from": "Dal {date}",
        "unavailable": "Occupato",
        "unavailable_period": "Dal {start} al {end}",
        "check_in": "Check-in",
        "check_out": "Check-out",
        "guests": "Ospiti",
        "guest_one": "1 ospite",
        "guest_many": "{count} ospiti",
        "search_button": "Calcola il preventivo",
        "checkout_error": "Il check-out deve essere successivo al check-in.",
        "unavailable_error": "Date non disponibili per {property}: l'appartamento è occupato dal {start} al {end}. Scegli altre date.",
        "guest_limit": "{property} può ospitare al massimo {count} persone.",
        "quote_title": "Il tuo soggiorno",
        "nights_one": "1 notte",
        "nights_many": "{count} notti",
        "total": "Totale indicativo",
        "quote_note": "Disponibilità simulata a scopo dimostrativo, non collegata a prenotazioni reali. Imposte ed eventuali extra non sono inclusi.",
        "request_title": "Invia una richiesta",
        "guest_name": "Nome e cognome",
        "email": "Email",
        "email_placeholder": "nome@esempio.it",
        "note": "Nota per il proprietario",
        "note_placeholder": "Orario di arrivo o altre informazioni utili",
        "request_button": "Invia richiesta demo",
        "name_error": "Inserisci nome e cognome.",
        "email_error": "Inserisci un indirizzo email valido.",
        "confirmation": "Richiesta demo registrata · codice {code}",
        "not_sent": "La richiesta non è stata inviata al proprietario né salvata. Per ricevere prenotazioni reali occorre collegare un servizio di invio e gestione.",
        "new_search": "Inizia una nuova ricerca",
        "footer": "Demo indipendente da Booking.com. Disponibilità, prezzi e richieste non sono collegati a servizi esterni.",
    },
    "en": {
        "language": "Language",
        "eyebrow": "A CURATED STAY · MILAN, ITALY",
        "headline": "Make yourself at home in Milan.",
        "intro": "Two apartments, two neighbourhoods to explore. Find your place in the city.",
        "up_to": "up to {count} guests",
        "starting_at": "From",
        "per_night": "per night",
        "search_title": "Find your stay",
        "search_caption": "Example: the calendar shows one booked period for each apartment. Other dates are free in this demo.",
        "property": "Apartment",
        "availability_title": "Sample availability",
        "available": "Available",
        "available_until": "Check-out by {date}",
        "available_from": "From {date}",
        "unavailable": "Booked",
        "unavailable_period": "{start} to {end}",
        "check_in": "Check-in",
        "check_out": "Check-out",
        "guests": "Guests",
        "guest_one": "1 guest",
        "guest_many": "{count} guests",
        "search_button": "Get an estimate",
        "checkout_error": "Check-out must be after check-in.",
        "unavailable_error": "Dates unavailable for {property}: the apartment is booked from {start} to {end}. Choose different dates.",
        "guest_limit": "{property} accommodates up to {count} guests.",
        "quote_title": "Your stay",
        "nights_one": "1 night",
        "nights_many": "{count} nights",
        "total": "Estimated total",
        "quote_note": "Availability is simulated for demonstration and is not connected to real bookings. Taxes and any extras are not included.",
        "request_title": "Send an enquiry",
        "guest_name": "Full name",
        "email": "Email address",
        "email_placeholder": "name@example.com",
        "note": "Note to the owner",
        "note_placeholder": "Arrival time or anything else we should know",
        "request_button": "Send demo request",
        "name_error": "Enter your full name.",
        "email_error": "Enter a valid email address.",
        "confirmation": "Demo request recorded · reference {code}",
        "not_sent": "This request was not sent to the owner or saved. A booking and messaging service must be connected to accept real reservations.",
        "new_search": "Start a new search",
        "footer": "Independent demo, not connected to Booking.com. Availability, prices and requests are not synced with external services.",
    },
}

PROPERTY_COPY = {
    "Brera Loft": {
        "en_zone": "Brera · central Milan",
        "en_description": "A base in the heart of Milan's creative quarter.",
    },
    "Navigli Studio": {
        "en_zone": "Navigli · Darsena",
        "en_description": "Settle in by the canals and lively Navigli streets.",
    },
}

with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"):
    st.markdown("**MILANO / STAY**")
    selected_language = st.segmented_control(
        "Language",
        ["Italiano", "English"],
        default="Italiano",
        key="site_language",
        label_visibility="collapsed",
        width="content",
    )

language = "en" if selected_language == "English" else "it"
text = COPY[language]
st.caption(text["eyebrow"])
st.title(text["headline"], icon=":material/apartment:")
st.write(text["intro"])

property_columns = st.columns(2)
for column, (property_name, details) in zip(property_columns, PROPERTIES.items()):
    with column:
        with st.container(border=True):
            st.image(details["image"], width="stretch")
            st.subheader(property_name)
            zone = details["zona"] if language == "it" else PROPERTY_COPY[property_name]["en_zone"]
            description = details["descrizione"] if language == "it" else PROPERTY_COPY[property_name]["en_description"]
            st.caption(zone)
            st.write(description)
            st.badge(text["up_to"].format(count=details["ospiti"]), icon=":material/person:", color="green")
            st.caption(f"{text['starting_at']} {euro(details['tariffa'])} {text['per_night']}")

st.header(text["search_title"], icon=":material/calendar_month:")
st.caption(text["search_caption"])

property_name = st.selectbox(text["property"], list(PROPERTIES), key="search_property")
reservation = SAMPLE_RESERVATIONS[property_name]
st.caption(text["availability_title"])
availability_columns = st.columns(3)
with availability_columns[0]:
    st.badge(text["available"], icon=":material/check_circle:", color="green")
    st.caption(text["available_until"].format(date=format_date(reservation["check_in"], language)))
with availability_columns[1]:
    st.badge(text["unavailable"], icon=":material/event_busy:", color="red")
    st.caption(text["unavailable_period"].format(
        start=format_date(reservation["check_in"], language),
        end=format_date(reservation["check_out"], language),
    ))
with availability_columns[2]:
    st.badge(text["available"], icon=":material/check_circle:", color="green")
    st.caption(text["available_from"].format(date=format_date(reservation["check_out"], language)))

with st.form("stay_search"):
    date_columns = st.columns(2)
    with date_columns[0]:
        check_in = st.date_input(
            text["check_in"],
            value=TODAY + timedelta(days=14),
            min_value=TODAY + timedelta(days=1),
            format="DD/MM/YYYY",
            key="search_check_in",
        )
    with date_columns[1]:
        check_out = st.date_input(
            text["check_out"],
            value=TODAY + timedelta(days=17),
            min_value=TODAY + timedelta(days=2),
            format="DD/MM/YYYY",
            key="search_check_out",
        )
    guests = st.selectbox(
        text["guests"],
        range(1, 5),
        index=1,
        format_func=lambda count: text["guest_one"] if count == 1 else text["guest_many"].format(count=count),
    )
    search_submitted = st.form_submit_button(text["search_button"], type="primary", icon=":material/search:", width="stretch")

if search_submitted:
    st.session_state.pop("stay_quote", None)
    if check_out <= check_in:
        st.error(text["checkout_error"])
    elif guests > PROPERTIES[property_name]["ospiti"]:
        st.error(text["guest_limit"].format(property=property_name, count=PROPERTIES[property_name]["ospiti"]))
    elif check_in < reservation["check_out"] and check_out > reservation["check_in"]:
        st.error(text["unavailable_error"].format(
            property=property_name,
            start=format_date(reservation["check_in"], language),
            end=format_date(reservation["check_out"], language),
        ))
    else:
        nights = (check_out - check_in).days
        nightly_rate = PROPERTIES[property_name]["tariffa"]
        st.session_state.stay_quote = {
            "appartamento": property_name,
            "check_in": check_in,
            "check_out": check_out,
            "ospiti": guests,
            "notti": nights,
            "tariffa": nightly_rate,
            "totale": nightly_rate * nights,
        }

quote = st.session_state.get("stay_quote")
if quote:
    st.subheader(text["quote_title"], icon=":material/luggage:")
    with st.container(border=True):
        guest_label = text["guest_one"] if quote["ospiti"] == 1 else text["guest_many"].format(count=quote["ospiti"])
        night_label = text["nights_one"] if quote["notti"] == 1 else text["nights_many"].format(count=quote["notti"])
        if language == "it":
            arrival = quote["check_in"].strftime("%d/%m/%Y")
            departure = quote["check_out"].strftime("%d/%m/%Y")
        else:
            months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
            arrival = f"{months[quote['check_in'].month - 1]} {quote['check_in'].day}, {quote['check_in'].year}"
            departure = f"{months[quote['check_out'].month - 1]} {quote['check_out'].day}, {quote['check_out'].year}"
        st.write(f"**{quote['appartamento']}** · {guest_label}")
        st.write(f"{arrival} – {departure} · {night_label}")
        st.caption(f"{quote['notti']} × {euro(quote['tariffa'])}")
        st.write(f"**{text['total']}** · **{euro(quote['totale'])}**")
        st.caption(text["quote_note"])

    if st.session_state.get("stay_request_sent"):
        st.success(text["confirmation"].format(code=st.session_state.stay_request_code))
        st.info(text["not_sent"])
        if st.button(text["new_search"], icon=":material/search:"):
            st.session_state.pop("stay_quote", None)
            st.session_state.pop("stay_request_sent", None)
            st.session_state.pop("stay_request_code", None)
            st.rerun()
    else:
        st.subheader(text["request_title"], icon=":material/mark_email_read:")
        with st.form("stay_request"):
            guest_name = st.text_input(text["guest_name"])
            guest_email = st.text_input(text["email"], placeholder=text["email_placeholder"])
            st.text_area(text["note"], placeholder=text["note_placeholder"])
            request_submitted = st.form_submit_button(text["request_button"], type="primary", icon=":material/send:", width="stretch")

        if request_submitted:
            if not guest_name.strip():
                st.error(text["name_error"])
            elif "@" not in guest_email or "." not in guest_email.rsplit("@", 1)[-1]:
                st.error(text["email_error"])
            else:
                st.session_state.stay_request_sent = True
                st.session_state.stay_request_code = uuid4().hex[:8].upper()
                st.rerun()

st.caption(text["footer"])