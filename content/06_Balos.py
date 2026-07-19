from content_helpers import maps_link


TITLE = "Balos – Die berühmteste Lagune Kretas"

IMAGE = "Kreta_Westkueste_13_Balos_Lagune.png"

PHOTO_STYLE = "vertical"

EXTRA_IMAGES = [
    {
        "file": "Balos 2.jpg",
        "caption": "Balos – türkisfarbenes Wasser, heller Sand und Lagunenblick"
    },
    {
        "file": "Balos 3.webp",
        "caption": "Sonnenuntergang"
    }
]

QUOTE_AFTER_IMAGES = True


BALOS_LAGUNE = maps_link(
    "Balos-Lagune",
    "Balos Beach, Kissamos, Crete, Greece",
)

KISSAMOS_HAFEN = maps_link(
    "Hafen von Kissamos",
    "Port of Kissamos, Kavonisi, Crete, Greece",
)

BALOS_PARKPLATZ = maps_link(
    "Parkplatz oberhalb der Lagune",
    "Balos Beach Parking, Kissamos, Crete, Greece",
)

BALOS_AUSSICHTSPUNKT = maps_link(
    "Aussichtspunkt oberhalb der Lagune",
    "Balos Viewpoint, Kissamos, Crete, Greece",
    travelmode="walking",
)

GRAMVOUSA = maps_link(
    "Insel Gramvousa",
    "Imeri Gramvousa, Kissamos, Crete, Greece",
)


BALOS_YACHTING = """
<a
    class="maps-link"
    href="https://www.balosyachting.com/"
    target="_blank"
    rel="noopener noreferrer"
>
    Balos Yachting
    <span class="maps-link-icon" aria-hidden="true">↗</span>
</a>
"""

BALOS_YACHTING_PREISE = """
<a
    class="maps-link"
    href="https://www.balosyachting.com/our-services/day-time-cruises"
    target="_blank"
    rel="noopener noreferrer"
>
    aktuelle Preise und Leistungen
    <span class="maps-link-icon" aria-hidden="true">↗</span>
</a>
"""


TEXT = f"""
<h2>Ein Ort wie aus einem Reisemagazin</h2>

<p>Die {BALOS_LAGUNE} gehört zu den bekanntesten Landschaften Griechenlands.
Türkisfarbenes Wasser, heller Sand und die flache Lagune machen diesen Ort
zu einem der meistfotografierten Plätze Kretas. Trotz der vielen Besucher
verliert Balos nichts von seiner Faszination.</p>

<p>Für euch gibt es zwei Möglichkeiten: mit dem Boot ab dem
{KISSAMOS_HAFEN} oder mit dem Mietwagen bis zum Parkplatz und
anschließend zu Fuß hinunter zur Lagune.</p>

<p>Da euer Vermieter eventuell ein Boot besitzt oder euch von Kissamos
nach Balos bringen kann, wäre dies die entspannteste Variante.
Ihr spart euch die holprige Schotterstraße und erlebt Balos vom Meer aus –
das ist wahrscheinlich die schönste Art anzukommen.</p>

<p>Eine weitere Möglichkeit ist eine private Tagestour mit
{BALOS_YACHTING}. Die angebotene Fahrt startet am Hafen von Kissamos
und führt zur Balos-Lagune sowie zur Insel Gramvousa.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li>
<strong>Fahrzeit bis Kissamos:</strong>
ca. 20 Minuten
</li>

<li>
<strong>Bootsfahrt:</strong>
ca. 1 Stunde bis Balos
</li>

<li>
<strong>Private Bootstour:</strong>
Laut Anbieter beginnt der Basispreis derzeit bei 700 €.
Das Boot bietet Platz für bis zu zehn Gäste.
Da sich Preise und Leistungen ändern können, findet ihr hier die
{BALOS_YACHTING_PREISE}.
</li>

<li>
<strong>Dauer der privaten Tagestour:</strong>
etwa 8 Stunden
</li>

<li>
<strong>Laut Anbieter inklusive:</strong>
Wasser, Softdrinks, Wein und eine Mahlzeit
</li>

<li>
<strong>Alternative:</strong>
Mietwagen und Wanderung
</li>

<li>
<strong>Parken:</strong>
{BALOS_PARKPLATZ}
</li>

<li>
<strong>Fußweg:</strong>
etwa 20 Minuten bergab, zurück entsprechend bergauf
</li>

<li>
<strong>Mitnehmen:</strong>
Wasser, Sonnenschutz, Badeschuhe und Kamera
</li>

</ul>

</div>

<h2>Mit dem Auto nach Balos</h2>

<p>Die Zufahrt erfolgt über eine rund acht Kilometer lange Schotterstraße.
Sie ist grundsätzlich gut befahrbar, allerdings langsam und je nach
Mietwagenanbieter nicht vollständig versichert. Informiert euch deshalb
vorher über die Bedingungen eures Vermieters.</p>

<p>Vom {BALOS_PARKPLATZ} führt ein gut ausgebauter Wanderweg hinunter
zur Lagune. Schon nach wenigen Minuten erreicht ihr den berühmten
{BALOS_AUSSICHTSPUNKT}, von dem aus die meisten bekannten Balos-Fotos
aufgenommen werden.</p>

<h2>Nicht verpassen</h2>

<ul>

<li>Den {BALOS_AUSSICHTSPUNKT} oberhalb der Lagune.</li>

<li>Ein Bad im flachen, türkisfarbenen Wasser der {BALOS_LAGUNE}.</li>

<li>Den Blick auf die {GRAMVOUSA} genießen.</li>

<li>Den weißen Muschelsand und die vielen Blautöne fotografieren.</li>

<li>Am späten Nachmittag wird das Licht besonders schön.</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Wenn ihr die Möglichkeit habt, Balos mit dem Boot zu besuchen,
nutzt sie. Die Anreise ist entspannter, das Auto bleibt geschont und
die Einfahrt in die Lagune vom Meer aus gehört zu den schönsten
Momenten des gesamten Ausflugs.</p>

<p>Prüft Preise, Leistungen, Wetter und Verfügbarkeit vor der Buchung
noch einmal direkt auf der Website von {BALOS_YACHTING}.
Die Fahrten sind wetterabhängig.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>

<strong>Λιμνοθάλασσα</strong><br>

<em>Limnothálassa</em><br>

Lagune

</p>

</div>

<blockquote>

„Manche Orte sehen auf Fotos wunderschön aus. Balos gehört zu den wenigen,
die in Wirklichkeit noch beeindruckender sind.“

</blockquote>
"""