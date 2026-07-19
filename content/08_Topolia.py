from content_helpers import maps_link


TITLE = "Topolia-Schlucht & Agia-Sofia-Höhle"

IMAGE = "topolia 2.webp"

PHOTO_STYLE = "vertical"

EXTRA_IMAGES = [
    {
        "file": "topolia 4.png",
        "caption": "Die beeindruckende Topolia-Schlucht"
    },
    {
        "file": "topolia 3.jpg",
        "caption": "Die Agia-Sofia-Höhle mit ihrer kleinen Kapelle"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)

TOPOLIA_SCHLUCHT = maps_link(
    "Topolia-Schlucht",
    "Topolia Gorge, Crete, Greece",
)

AGIA_SOFIA_HOEHLE = maps_link(
    "Agia-Sofia-Höhle",
    "Agia Sofia Cave, Topolia, Crete, Greece",
)

AGIA_SOFIA_PARKPLATZ = maps_link(
    "Parkplatz bei der Agia-Sofia-Höhle",
    "Agia Sofia Cave, Topolia, Crete, Greece",
)

ELAFONISI = maps_link(
    "Elafonisi",
    "Elafonisi Beach, Crete, Greece",
)

KISSAMOS = maps_link(
    "Kissamos",
    "Kissamos, Crete, Greece",
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
<h2>Ein lohnender Zwischenstopp in den Bergen</h2>

<p>Die {TOPOLIA_SCHLUCHT} gehört zu den eindrucksvollsten Landschaften
Westkretas. Die Straße schlängelt sich zwischen hohen Felswänden hindurch
und bietet immer wieder schöne Ausblicke. Schon die Fahrt durch die Schlucht
ist ein Erlebnis.</p>

<p>Oberhalb der Straße liegt die {AGIA_SOFIA_HOEHLE}. Von der Terrasse
vor der Höhle habt ihr einen herrlichen Blick über die Schlucht.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li>
<strong>Fahrzeit ab {VILLA_PERICLES}:</strong>
ca. 50 Minuten
</li>

<li>
<strong>Zeitbedarf:</strong>
1½–2 Stunden
</li>

<li>
<strong>Parken:</strong>
kostenlos am {AGIA_SOFIA_PARKPLATZ} direkt gegenüber der Höhle
an der Hauptstraße
</li>

<li>
<strong>Fußweg:</strong>
ca. 10 Minuten über rund 250 Steinstufen
</li>

<li>
<strong>Schwierigkeit:</strong>
leicht bis mittel wegen der Stufen
</li>

<li>
<strong>Empfehlung:</strong>
als Nachmittagsprogramm nach {ELAFONISI}
</li>

</ul>

</div>

<h2>Unser Vorschlag für den Tag</h2>

<p>Startet morgens nach {ELAFONISI} und verbringt dort einige Stunden
am Strand. Mittags könnt ihr entweder etwas mitnehmen oder eine einfache
Strandtaverne nutzen.</p>

<p>Am Nachmittag fahrt ihr weiter zur {AGIA_SOFIA_HOEHLE} und anschließend
über {KISSAMOS} zurück zur Villa.</p>

<h2>Die Topolia-Schlucht</h2>

<p>Die {TOPOLIA_SCHLUCHT} wurde tief in den Kalkstein geschnitten und zeigt
Kreta von seiner raueren, ursprünglichen Seite. Besonders schön ist der
Kontrast zwischen den steilen Felsen, den Olivenbäumen und der kurvigen
Straße, die sich durch die Berge zieht.</p>

<h2>Die Agia-Sofia-Höhle</h2>

<p>Der Aufstieg zur {AGIA_SOFIA_HOEHLE} ist kurz, aber bei sommerlichen
Temperaturen spürt man die rund 250 Stufen durchaus. Oben angekommen
erwartet euch eine beeindruckend große Höhle mit einer kleinen Kapelle
sowie ein wunderschöner Aussichtspunkt über die Topolia-Schlucht.</p>

<p>Die Höhle war bereits in der Antike bekannt. Die Mischung aus Natur,
Geschichte und Aussicht macht diesen kurzen Abstecher zu einem der
schönsten Stopps im Westen Kretas.</p>

<p>Mit etwas Glück entdeckt ihr unterwegs Greifvögel, wilde Ziegen oder
die für Kreta typische mediterrane Vegetation. Hier zeigt sich die
ursprüngliche Schönheit der Insel.</p>

<h2>Zum Abschluss des Tages</h2>

<ul>

<li>
<strong>Mittag:</strong>
Picknick am Strand oder eine einfache Taverne bei {ELAFONISI}.
</li>

<li>
<strong>Abendessen:</strong>
{THE_CELLAR} in Kissamos auf dem Rückweg.
</li>

<li>
<strong>Alternative:</strong>
{CAPTAIN_FIDIAS} in Sfinari, wenn ihr den Tag lieber direkt am Meer
ausklingen lasst.
</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Nehmt für die Höhle Wasser und feste Schuhe mit. Nach dem Strandtag ist
dieser kurze Abstecher eine schöne Mischung aus Natur, Aussicht und Kultur.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>
<strong>Σπήλαιο</strong><br>
<em>Spíleo</em><br>
Höhle
</p>

</div>

<blockquote>
„Zwischen den Felsen der Topolia-Schlucht zeigt Kreta seine wilde Seite.“
</blockquote>
"""