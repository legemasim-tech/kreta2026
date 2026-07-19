from content_helpers import maps_link


TITLE = "Kissamos – Das Tor zum Westen Kretas"

IMAGE = "Kissamos_Kreta_Griechenland.webp"

IMAGE_STYLE = "cover"

PHOTO_STYLE = "vertical"

TOP_IMAGES = []

BOTTOM_IMAGES = [
    {
        "file": "Mavro Molos Kissamos.jpg",
        "caption": "Der Strand von Mavros Molos"
    },
    {
        "file": "The cellar Kissamos.png",
        "caption": "Westkreta: Meer, Einkaufen und Entspannen"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)

KISSAMOS = maps_link(
    "Kissamos",
    "Kissamos, Crete, Greece",
)

SYNKA_KISSAMOS = maps_link(
    "SYN.KA Supermarkt",
    "SYN.KA Supermarket, Kissamos, Crete, Greece",
)

LIDL_KISSAMOS = maps_link(
    "Lidl Kissamos",
    "Lidl, Kissamos, Crete, Greece",
)

MAVROS_MOLOS = maps_link(
    "Mavros Molos",
    "Paralia Mavros Μolos, Kissamos 734 00, Crete, Greece",
)

KISSAMOS_PORT = maps_link(
    "Hafen von Kissamos",
    "Port of Kissamos, Kavonisi, Crete, Greece",
)

THE_CELLAR = maps_link(
    "The Cellar",
    "The Cellar Tavern, Kissamos, Crete, Greece",
)

PIXIDA = maps_link(
    "Pixida Restaurant",
    "Pixida Restaurant, Kissamos, Crete, Greece",
)

MARIA_BEACH = maps_link(
    "Maria Beach Restaurant",
    "Maria Beach Restaurant, Kissamos, Crete, Greece",
)


TEXT = f"""
<h2>Die wichtigste Stadt eurer Reise</h2>

<p>{KISSAMOS} ist keine klassische Sehenswürdigkeit, sondern die kleine Stadt,
die ihr während eures Urlaubs vermutlich am häufigsten besuchen werdet.
Hier erledigt ihr eure Einkäufe, startet zu einigen Ausflügen und findet
zahlreiche Tavernen, Cafés und den {KISSAMOS_PORT}.</p>

<p>Im Vergleich zu Chania geht es hier deutlich ruhiger zu. Gerade deshalb
lohnt es sich, nicht nur zum Einkaufen hierherzukommen, sondern auch einmal
durch die Straßen zu bummeln oder am Strand von {MAVROS_MOLOS} einen Kaffee
zu genießen.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li>
<strong>Fahrzeit ab {VILLA_PERICLES}:</strong>
ca. 20 Minuten bis Kissamos
</li>

<li>
<strong>{SYNKA_KISSAMOS}:</strong>
ca. 30 Minuten Fahrzeit, große Auswahl an Lebensmitteln
und regionalen Produkten.
</li>

<li>
<strong>{LIDL_KISSAMOS}:</strong>
ca. 55 Minuten Fahrzeit, ideal für den ersten Großeinkauf.
</li>

<li><strong>Tankstellen:</strong> mehrere an der Ortseinfahrt.</li>

<li><strong>Apotheken:</strong> mehrere im Stadtzentrum.</li>

<li><strong>Bankomat:</strong> mehrfach im Zentrum vorhanden.</li>

</ul>

</div>

<h2>Was ihr hier erledigen könnt</h2>

<ul>

<li>Großeinkauf für die Villa.</li>

<li>Getränke, Grillgut und Vorräte besorgen.</li>

<li>Frischen Fisch oder regionale Spezialitäten einkaufen.</li>

<li>Am {KISSAMOS_PORT} oder am Strand von {MAVROS_MOLOS} spazieren gehen.</li>

<li>Gemütlich einen Kaffee trinken oder ein Eis genießen.</li>

</ul>

<h2>Restaurant-Empfehlungen</h2>

<ul>

<li>
<strong>{THE_CELLAR}</strong><br>
Direkt an der Uferpromenade von Kissamos.<br>
Gemütliche Atmosphäre mit schöner Terrasse und Blick aufs Meer.
Bekannt für traditionelle kretische Küche, frischen Fisch und
hervorragende Fleischgerichte.
</li>

<li>
<strong>{PIXIDA}</strong><br>
Nahe dem Hafen von Kissamos.<br>
Eine der besten Adressen für Fisch und Meeresfrüchte.
Modernes Ambiente mit mediterraner Küche und freundlichem Service.
</li>

<li>
<strong>{MARIA_BEACH}</strong><br>
Direkt am Strand von Mavros Molos.<br>
Ideal für ein entspanntes Mittag- oder Abendessen mit Blick aufs Meer.
Besonders beliebt sind Fischgerichte, Salate und kretische Spezialitäten.
</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Verbindet den Einkauf gleich mit einem Spaziergang am Strand von
{MAVROS_MOLOS} oder einem Essen am Meer. So wird aus einer
Besorgungsfahrt ein kleiner Urlaubsausflug.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>

<strong>Αγορά</strong><br>

<em>Agorá</em><br>

Markt

</p>

</div>

<blockquote>

„Manche Orte besucht man nicht wegen einer Sehenswürdigkeit,
sondern weil sie zum Alltag des Urlaubs gehören.“

</blockquote>
"""