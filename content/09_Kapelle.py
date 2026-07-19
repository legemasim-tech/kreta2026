from content_helpers import maps_link


TITLE = "Varsamakia – Wanderung zum Turm des Heiligen Demetrius"

IMAGE = "Kreta_Westkueste_01_Turm_Agios_Dimitrios_Varsamakia_Kissamos.jpg"

PHOTO_STYLE = "single"

EXTRA_IMAGES = [
    {
        "file": "Varsamakia 1.jpg",
        "caption": "Varsamakia und der Turm des Heiligen Demetrius",
        "style": "portrait"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
    travelmode="walking",
)

SFINARI = maps_link(
    "Sfinari",
    "Sfinari, Kissamos, Crete, Greece",
    travelmode="walking",
)

VARSAMAKIA = maps_link(
    "Varsamakia",
    "Βαρσαμακια Ιερός ναός Αγίου Δημητρίου, Crete, Greece",
    travelmode="walking",
)

TURM_AGIOS_DIMITRIOS = maps_link(
    "Turm des Heiligen Demetrius",
    "Βαρσαμακια Ιερός ναός Αγίου Δημητρίου, Crete, Greece",
    travelmode="walking",
)


TEXT = f"""
<h2>Ein Vormittag zu Fuß ab der Villa</h2>

<p>Diese Wanderung beginnt direkt bei der {VILLA_PERICLES} und führt euch über
{SFINARI} hinauf Richtung {VARSAMAKIA}. Sie ist kein kurzer Spaziergang, sondern
eine richtige kleine Bergwanderung: Der Aufstieg dauert etwa zwei Stunden
und überwindet knapp 500 Höhenmeter.</p>

<p>Der Lohn dafür sind weite Ausblicke über die Westküste, das Meer und die
Berge rund um Sfinari. Gerade weil ihr dafür nicht ins Auto steigen müsst,
ist diese Tour ein besonders schöner Vormittagsausflug direkt vor eurer Haustür.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li>
<strong>Start:</strong>
direkt bei der {VILLA_PERICLES}
</li>

<li>
<strong>Route:</strong>
Villa – {SFINARI} – {VARSAMAKIA} – zurück auf gleichem Weg
</li>

<li>
<strong>Aufstieg:</strong>
ca. 2 Stunden
</li>

<li>
<strong>Höhenmeter:</strong>
knapp 500 m
</li>

<li>
<strong>Rückweg:</strong>
entsprechend wieder bergab, etwa 1½–2 Stunden
</li>

<li>
<strong>Parken:</strong>
nicht nötig – ihr startet direkt am Haus
</li>

<li>
<strong>Mitnehmen:</strong>
Wasser, feste Schuhe, Kopfbedeckung und Kamera
</li>

</ul>

</div>

<h2>Der Turm des Heiligen Demetrius</h2>

<p>Bei {VARSAMAKIA}, westlich von Kissamos und nahe Sfinari, befindet sich der
{TURM_AGIOS_DIMITRIOS}. Er steht nahe dem ehemaligen Kloster Agios
Dimitrios und vermutlich an der Stelle des alten, heute unbekannten Dorfes
Monoplatanos.</p>

<p>Um den Turm rankt sich eine Legende: Angeblich soll dort ein verborgener
Schatz liegen. Manche erzählen, dass italienische Schatzsucher in den
1960er- oder 1970er-Jahren mit alten Karten danach gesucht haben.
Ob sie etwas gefunden haben, weiß niemand genau.</p>

<h2>Unterwegs</h2>

<p>Der Weg führt euch aus dem ruhigen Küstenbereich hinauf in die trockenere,
steinige Landschaft oberhalb von Sfinari. Je höher ihr kommt, desto weiter
öffnet sich der Blick auf das Meer und die Westküste.</p>

<h2>Zum Abschluss</h2>

<ul>

<li>Früh starten, bevor es zu heiß wird.</li>

<li>Oben genügend Zeit für Aussicht und Fotos einplanen.</li>

<li>Nach der Rückkehr: Pool, Meer oder Mittagessen in {SFINARI}.</li>

<li>Perfekt für einen aktiven Vormittag ohne Autofahrt.</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Diese Wanderung nur machen, wenn ihr wirklich Lust auf Bewegung habt.
500 Höhenmeter sind bei kretischer Sonne nicht zu unterschätzen. Früh losgehen
und lieber zu viel Wasser mitnehmen.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>
<strong>Πύργος</strong><br>
<em>Pýrgos</em><br>
Turm
</p>

</div>

<blockquote>
„Manchmal beginnt das Abenteuer nicht auf der Straße, sondern direkt vor der Haustür.“
</blockquote>
"""