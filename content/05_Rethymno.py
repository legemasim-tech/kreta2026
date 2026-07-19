from content_helpers import maps_link


TITLE = "Rethymno – Altstadt, Fortezza und ein kurzer persönlicher Abstecher"

IMAGE = "Rethymno_4.jpg"

PHOTO_STYLE = "grid-small"

EXTRA_IMAGES = [
    {
        "file": "rethymno 2.jpg",
        "caption": "Venezianischer Hafen"
    },
    {
        "file": "rethymno 3.webp",
        "caption": "Rethymno und die Fortezza"
    },
    {
        "file": "rethymno 4.webp",
        "caption": "Altstadtgassen"
    },
    {
        "file": "Rethymno 5.jpg",
        "caption": "Venezianisches Flair"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)

RETHYMNO = maps_link(
    "Rethymno",
    "Rethymno, Crete, Greece",
)

FORTEZZA = maps_link(
    "Fortezza",
    "Fortezza of Rethymno, Crete, Greece",
)

FORTEZZA_PARKING = maps_link(
    "Parkplatz unterhalb der Fortezza",
    "35.373500,24.472111",
)

MARINA_PARKING = maps_link(
    "Marina-Parkplatz",
    "Rethymno Marina Parking, Rethymno, Crete, Greece",
)

VENETIAN_HARBOUR = maps_link(
    "venezianischen Hafen",
    "Venetian Harbour, Rethymno, Crete, Greece",
)

FERIENHAUS = maps_link(
    "Ferienhaus von Michi und Franzi",
    "35.324306,24.499250",
)

AVLI = maps_link(
    "Avli",
    "Avli Restaurant, Xanthoudidou 22, Rethymno, Crete, Greece",
)

CASTELO = maps_link(
    "Castelo",
    "Castelo Restaurant, Radamanthyos 19, Rethymno, Crete, Greece",
)

PRIMA_PLORA = maps_link(
    "Prima Plora",
    "Prima Plora, Akrotiriou 8, Rethymno, Crete, Greece",
)


TEXT = f"""
<h2>Warum sich Rethymno lohnt</h2>

<p>{RETHYMNO} ist kleiner und ruhiger als Chania, aber mindestens genauso charmant.
Die Stadt verbindet venezianische Häuser, enge Gassen, kleine Geschäfte,
osmanische Spuren und eine mächtige Festung über dem Meer.</p>

<p>Für euch ist Rethymno ein schöner Tagesausflug: Geschichte, Bummeln,
Essen und ein kurzer persönlicher Abstecher zum Ferienhaus von Gertis Schwester
lassen sich hier wunderbar verbinden.</p>

<h2>Die Fortezza</h2>

<p>Die {FORTEZZA} thront oberhalb der Altstadt und ist der wichtigste historische
Punkt in Rethymno. Von oben habt ihr einen weiten Blick über die Stadt,
den Hafen und das Meer.</p>

<div class="info">
<h2>Praktische Infos</h2>
<ul>

<li>
<strong>Fahrzeit ab {VILLA_PERICLES}:</strong>
ca. 1 Stunde 40 Minuten
</li>

<li>
<strong>Zeitbedarf:</strong>
6–8 Stunden inklusive Fortezza, Altstadt und Abstecher
</li>

<li>
<strong>Empfohlener Parkplatz:</strong>
{FORTEZZA_PARKING} / E. Kefalogianni Straße
</li>

<li>
<strong>Alternative:</strong>
{MARINA_PARKING} oder kostenpflichtiger Parkplatz nahe dem
{VENETIAN_HARBOUR}
</li>

<li>
<strong>Wichtig:</strong>
Nicht in die Altstadt hineinfahren – viele Gassen sind eng oder Fußgängerzone.
</li>

<li>
<strong>Beste Zeit:</strong>
Vormittag starten, später Altstadt und Hafen
</li>

</ul>
</div>

<h2>Kurzer Abstecher zu Michi´s & Franzi´s Ferienhaus</h2>

<p>Auf dem Weg nach oder von Rethymno bietet sich ein kurzer Halt beim
{FERIENHAUS} an. Niemand muss dort sein – es reicht, das Haus von außen
anzuschauen und die Umgebung kurz auf sich wirken zu lassen.</p>

<p>
<strong>Koordinaten:</strong>
35°19'27.5&quot;N · 24°29'57.3&quot;E
</p>

<h2>Rundgang durch Rethymno</h2>

<ul>
<li>{FORTEZZA} besuchen und Ausblick genießen.</li>
<li>Durch die Altstadtgassen schlendern.</li>
<li>Den {VENETIAN_HARBOUR} ansehen.</li>
<li>Kleine Läden und Cafés entdecken.</li>
<li>Zum Abschluss entspannt essen gehen.</li>
</ul>

<h2>Tavernen & Essen</h2>

<ul>

<li>
<strong>{AVLI}</strong><br>
Xanthoudidou 22, mitten in der Altstadt von Rethymno.<br>
Eines der bekanntesten Restaurants der Stadt. Wunderschöner Innenhof,
gehobene kretische Küche und besondere Atmosphäre.
Reservierung empfehlenswert.
</li>

<li>
<strong>{CASTELO}</strong><br>
Radamanthyos 19, in einer ruhigen Gasse der Altstadt.<br>
Gemütliches Restaurant mit mediterraner und kretischer Küche.
Ideal für ein entspanntes Abendessen nach dem Stadtbummel.
</li>

<li>
<strong>{PRIMA_PLORA}</strong><br>
Akrotiriou 8, direkt am Meer westlich der Altstadt.<br>
Wunderschöne Terrasse mit Blick aufs Wasser. Besonders bekannt für
frischen Fisch, Meeresfrüchte und mediterrane Küche.
</li>

</ul>

<div class="tip">
<h2>Tipp</h2>
<p>Beginnt bei der {FORTEZZA} und lasst euch anschließend durch die Altstadt treiben.</p>
</div>

<div class="greek">
<h2>Griechisch des Tages</h2>
<p><strong>Κάστρο</strong><br>
<em>Kástro</em><br>
Festung / Burg</p>
</div>

<blockquote>„Rethymno ist kein Ort zum Abarbeiten. Die Stadt wirkt am schönsten,
wenn man sich treiben lässt.“</blockquote>
"""