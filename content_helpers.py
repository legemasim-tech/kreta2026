from html import escape
from urllib.parse import urlencode


VALID_TRAVEL_MODES = {
    "driving",
    "walking",
    "bicycling",
    "transit",
}


def maps_url(
    destination: str,
    *,
    place_id: str | None = None,
    travelmode: str = "driving",
) -> str:
    """
    Erzeugt einen Google-Maps-Link zur Navigation.

    destination:
        Exakter Ortsname mit Adresse oder geprüfte Koordinaten,
        zum Beispiel:
        "Tamam Restaurant, Zampeliou 49, Chania, Crete"
        oder:
        "35.123456,23.123456"

    place_id:
        Optional. Eine Google Place ID macht den Zielort eindeutiger.

    travelmode:
        driving, walking, bicycling oder transit
    """

    if not destination.strip():
        raise ValueError("Für den Maps-Link fehlt das Ziel.")

    if travelmode not in VALID_TRAVEL_MODES:
        raise ValueError(
            f"Ungültige Fortbewegungsart: {travelmode}"
        )

    parameters = {
        "api": "1",
        "destination": destination,
        "travelmode": travelmode,
        "dir_action": "navigate",
    }

    if place_id:
        parameters["destination_place_id"] = place_id

    return (
        "https://www.google.com/maps/dir/?"
        + urlencode(parameters)
    )


def maps_link(
    label: str,
    destination: str,
    *,
    place_id: str | None = None,
    travelmode: str = "driving",
) -> str:
    """
    Erzeugt einen direkt in TEXT verwendbaren HTML-Link.
    """

    url = maps_url(
        destination,
        place_id=place_id,
        travelmode=travelmode,
    )

    safe_label = escape(label)
    safe_url = escape(url, quote=True)

    return (
        f'<a class="maps-link" '
        f'href="{safe_url}" '
        f'target="_blank" '
        f'rel="noopener noreferrer">'
        f'{safe_label}'
        f'<span class="maps-link-icon" aria-hidden="true">↗</span>'
        f'</a>'
    )