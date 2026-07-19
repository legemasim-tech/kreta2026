from content_helpers import maps_link

TITLE = "Chania – Altstadt, Hafen und venezianisches Flair"

IMAGE = "Kreta_Westkueste_10_Chania_Venezianischer_Hafen.webp"

PHOTO_STYLE = "grid-large"

EXTRA_IMAGES = [
    {
        "file": "chania 3.jpg",
        "caption": "Der venezianische Hafen"
    },
    {
        "file": "chania 2.jpg",
        "caption": "Das moderne Chania"
    },
    {
        "file": "chania 4.jpg",
        "caption": "Abendstimmung am Hafen"
    },
    {
        "file": "chania 5.jpg",
        "caption": "Mediterranes Flair"
    }
]

QUOTE_AFTER_IMAGES = True

TALOS_PARKING = maps_link(
    "Talos Parking",
    "Talos Parking, Chania, Crete, Greece",
)

MUNICIPAL_PARKING = maps_link(
    "Municipal Parking",
    "Municipal Parking Regina, Kiprou 4, Chania 731 32, Crete, Greece",
)

TAMAM = maps_link(
    "Tamam",
    "Tamam Restaurant Chania, 49 Zampeliou str Old Harbour, Chania 731 00, Crete, Greece",
)

TO_MARIDAKI = maps_link(
    "To Maridaki",
    "To Maridaki, Daskalogianni 33, Chania, Crete, Greece",
)

PALLAS = maps_link(
    "Pallas",
    "Pallas, Venetian Harbour, Chania, Crete, Greece",
)

TEXT = f"""
<h2>Der schönste Stadtbesuch Westkretas</h2>

<p>Chania ist wahrscheinlich der stimmungsvollste Stadtbesuch eurer Reise.
Die Altstadt mit ihren engen Gassen, kleinen Geschäften, venezianischen Häusern
und dem berühmten Hafen gehört zu den schönsten Orten auf Kreta.</p>

<p>Am besten besucht ihr Chania nicht in Eile. Lasst euch treiben, schaut in
kleine Seitengassen, trinkt einen Kaffee, esst ein Eis und geht später zum
venezianischen Hafen. Besonders schön wird die Stadt am späten Nachmittag,
wenn das Licht weicher wird.</p>

<div class="info">
<h2>Praktische Infos</h2>
<ul>
<li><strong>Fahrzeit ab Villa Pericles:</strong> ca. 1 Stunde 15 Minuten</li>
<li><strong>Zeitbedarf:</strong> 5–7 Stunden</li>
<li>
    <strong>Parkmöglichkeiten:</strong><br>
    {TALOS_PARKING} – bewacht, am westlichen Rand der Altstadt, Samstags bis 16 Uhr geöffnet,
    Sonntags geschlossen<br>
    {MUNICIPAL_PARKING} – zusätzliche zentrale Parkmöglichkeit
</li>
<li><strong>Fußweg:</strong> ca. 5–10 Minuten bis zum venezianischen Hafen</li>
<li><strong>Beste Zeit:</strong> später Nachmittag bis Abend</li>
<li><strong>Ideal für:</strong> Altstadt, Hafen, Restaurants, Fotos und Eis</li>
</ul>
</div>

<h2>Unser Rundgang</h2>

<ul>
<li>Vom Parkplatz Talos Richtung Altstadt und Hafen spazieren.</li>
<li>Altstadtgassen erkunden.</li>
<li>Venezianischen Hafen besuchen.</li>
<li>Zum Leuchtturm oder zumindest entlang der Hafenmauer spazieren.</li>
<li>Kleine Geschäfte und Cafés entdecken.</li>
<li>Abendessen oder Drink am Hafen.</li>
</ul>

<h2>Fotospots</h2>

<ul>
<li>Der Blick auf den Leuchtturm und die Sonnenuntergangsstimmung am Hafenbecken.</li>
<li>Die kleinen Seitengassen hinter dem Hafen und die venezianischen Häuser am Wasser.</li>
</ul>

<h2>Restaurant-Empfehlungen</h2>

<ul>

<li>
    <strong>{TAMAM}</strong><br>
    Zampeliou 49, mitten in der Altstadt nahe dem
    venezianischen Hafen. Sehr beliebt, kretische Küche
    in historischem Ambiente.
</li>

<li>
    <strong>{TO_MARIDAKI}</strong><br>
    Daskalogianni 33 im Viertel Splantzia.
    Gute Wahl für Fisch, Meeresfrüchte und einfache
    griechische Küche.
</li>

<li>
    <strong>{PALLAS}</strong><br>
    Direkt am venezianischen Hafen. Schön für Drinks,
    Dessert oder Abendessen mit Blick auf Hafen und
    Leuchtturm.
</li>

</ul>

<div class="tip">
<h2>Tipp</h2>
<p>Fahrt nicht zu früh nach Chania. Am Nachmittag ist es angenehmer,
das Licht wird schöner und ihr könnt den Hafen in der Abendstimmung erleben.</p>
</div>

<div class="greek">
<h2>Griechisch des Tages</h2>
<p><strong>Λιμάνι</strong><br>
<em>Limáni</em><br>
Hafen</p>
</div>

<blockquote>„Chania ist keine Stadt zum Abhaken. Chania ist eine Stadt zum Schlendern.“</blockquote>
"""