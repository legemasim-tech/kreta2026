from content_helpers import maps_link


TITLE = "Elafonisi – Der rosafarbene Traumstrand"

IMAGE = "Kreta_Westkueste_12_Elafonisi_Strand.jpeg"

PHOTO_STYLE = "vertical"

EXTRA_IMAGES = [
    {
        "file": "elafonissi 2.webp",
        "caption": "Elafonisi – rosa Sand und türkisfarbenes Meer"
    },
    {
        "file": "Elafonisi 3.jpeg",
        "caption": "Kristallklares Wasser und endlose Sandbänke"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)

ELAFONISI = maps_link(
    "Elafonisi",
    "Elafonisi Beach, Crete, Greece",
)

ELAFONISI_PARKPLATZ = maps_link(
    "Parkplatz bei Elafonisi",
    "Elafonisi Beach Parking, Crete, Greece",
)

ELAFONISI_INSEL = maps_link(
    "Insel Elafonisi",
    "Elafonisi Island, Crete, Greece",
    travelmode="walking",
)

AGIA_SOFIA_HOEHLE = maps_link(
    "Agia-Sofia-Höhle",
    "Agia Sofia Cave, Topolia, Crete, Greece",
)

TOPOLIA_SCHLUCHT = maps_link(
    "Topolia-Schlucht",
    "Topolia Gorge, Crete, Greece",
)

THE_CELLAR = maps_link(
    "The Cellar",
    "The Cellar Tavern, Kissamos, Crete, Greece",
)

CAPTAIN_FIDIAS = maps_link(
    "Captain Fidias",
    "Captain Fidias, Sfinari, Kissamos, Crete, Greece",
)


TEXT = f"""
<h2>Ein Tag am berühmtesten Strand Kretas</h2>

<p>{ELAFONISI} gehört zu den bekanntesten Stränden Europas. Berühmt ist der
feine Sand, der an manchen Stellen durch winzige Muschel- und Korallenreste
leicht rosa schimmert. Zusammen mit dem glasklaren Wasser entsteht eine
Landschaft, die fast karibisch wirkt.</p>

<p>Trotz seiner Bekanntheit findet jeder ein ruhiges Plätzchen – besonders
dann, wenn ihr ein paar Minuten vom Hauptbereich weggeht. Das Wasser ist
flach, angenehm warm und eignet sich hervorragend zum Baden, Schnorcheln
und Entspannen.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li>
<strong>Fahrzeit ab {VILLA_PERICLES}:</strong>
ca. 1 Stunde
</li>

<li>
<strong>Parken:</strong>
großer kostenpflichtiger {ELAFONISI_PARKPLATZ} direkt vor dem Strand
</li>

<li>
<strong>Fußweg:</strong>
vom Parkplatz nur wenige Minuten bis zum Wasser
</li>

<li>
<strong>Beste Zeit:</strong>
möglichst früh am Vormittag oder ab ca. 16 Uhr
</li>

<li>
<strong>Mitnehmen:</strong>
Sonnenschutz, Wasser, Badeschuhe und Schnorchel
</li>

</ul>

</div>

<h2>Was euch erwartet</h2>

<ul>

<li>Feiner heller Sand mit den berühmten rosafarbenen Bereichen.</li>

<li>Kristallklares Wasser in vielen Blau- und Türkistönen.</li>

<li>Flache Lagunen – ideal zum Baden und Waten.</li>

<li>Geschützte Dünenlandschaft mit seltenen Pflanzen.</li>

<li>Viele Fotomotive und traumhafte Sonnenuntergänge.</li>

</ul>

<h2>Unser Vorschlag</h2>

<p>Fahrt möglichst früh los und verbringt den Vormittag am Strand.
Geht anschließend zu Fuß über die flachen Lagunen bis auf die kleine
{ELAFONISI_INSEL}. Dort wird es meist ruhiger und ihr erlebt die Landschaft
noch ursprünglicher.</p>

<p>Am Nachmittag lohnt sich auf dem Rückweg ein Halt an der
{AGIA_SOFIA_HOEHLE} oberhalb der {TOPOLIA_SCHLUCHT}.</p>

<h2>Essen unterwegs</h2>

<ul>

<li>
<strong>Mittag:</strong>
Picknick am Strand oder eine der einfachen Tavernen direkt bei Elafonisi.
</li>

<li>
<strong>Abend:</strong>
{THE_CELLAR} in Kissamos oder {CAPTAIN_FIDIAS} in Sfinari,
wenn ihr den Tag gemütlich am Meer ausklingen lassen möchtet.
</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Geht nicht nur zum Hauptstrand. Schon nach wenigen Minuten erreicht ihr
deutlich ruhigere Abschnitte mit kleinen Sandbänken und flachen Lagunen.
Gerade dort zeigt sich Elafonisi von seiner schönsten Seite.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>

<strong>Παραλία</strong><br>

<em>Paralía</em><br>

Strand

</p>

</div>

<blockquote>

„Manchmal genügt ein Tag am Meer, um noch lange davon zu träumen.“

</blockquote>
"""