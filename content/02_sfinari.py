from content_helpers import maps_link


TITLE = "Unser Zuhause in Sfinari"

IMAGE = "Villa Perikles (26).avif"

IMAGE_STYLE = "cover"

PHOTO_STYLE = "double"

TOP_IMAGES = []

BOTTOM_IMAGES = [
    {
        "file": "Villa Perikles (4).avif",
        "caption": "Blick aufs Meer"
    },
    {
        "file": "Villa Perikles (6).webp",
        "caption": "Pool und Garten der Villa"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)

SFINARI = maps_link(
    "Sfinari",
    "Sfinari, Kissamos, Crete, Greece",
)

MINI_MARKET = maps_link(
    "Mini Market",
    "Grocery store, Sfinari 730 12, Crete, Greece",
    travelmode="walking",
)

LIDL_KISSAMOS = maps_link(
    "Lidl",
    "Lidl, Kissamos, Crete, Greece",
)

SYNKA_KISSAMOS = maps_link(
    "SYN.KA",
    "SYN.KA Supermarket, Platanos 734 00, Crete, Greece",
)

CAPTAIN_FIDIAS = maps_link(
    "Captain Fidias",
    "Captain Fidias, Sfinari, Kissamos, Crete, Greece",
    travelmode="walking",
)

ANTONIOS = maps_link(
    "Antonios",
    "Antonios Restaurant, Sfinari, Kissamos, Crete, Greece",
    travelmode="walking",
)


TEXT = f"""
<h2>Hier beginnt jeder Urlaubstag</h2>

<p>Es gibt Unterkünfte, in denen man nur schläft. Und es gibt Orte,
an denen man ankommt und sich sofort zuhause fühlt.
Die {VILLA_PERICLES} gehört eindeutig zur zweiten Kategorie.</p>

<p>Nur wenige Schritte trennen euch vom Meer. Morgens wacht ihr mit dem
Rauschen der Wellen auf, frühstückt auf der Terrasse und blickt hinaus auf
das Libysche Meer. Abends erlebt ihr von hier aus einige der schönsten
Sonnenuntergänge Westkretas.</p>

<p>Gerade deshalb lohnt es sich, nicht jeden Tag einen großen Ausflug zu
unternehmen. Manche der schönsten Urlaubsmomente entstehen genau hier:
am Pool, auf der Terrasse oder bei einem Glas Wein mit Blick aufs Meer.</p>

<h2>Die Villa Pericles</h2>

<ul>
<li>Direkte Strandlage (ca. 10 Meter zum Meer)</li>
<li>Privater Pool (9 × 5 Meter)</li>
<li>Große Terrasse mit Meerblick</li>
<li>Grillplatz für gemeinsame Abende</li>
<li>Jacuzzi im Hauptschlafzimmer</li>
<li>Volleyballnetz im Garten</li>
<li>Kostenloses WLAN und Klimaanlage</li>
<li>Privater Parkplatz direkt am Haus</li>
</ul>

<p>Das Haus wurde von Pericles, einem bekannten kretischen Musiker und
Geigenspieler, liebevoll renoviert. Viele seiner musikalischen Ideen sollen
genau hier – mit Blick aufs Meer – entstanden sein.</p>

<div class="info">

<h2>Praktische Infos</h2>

<ul>

<li><strong>Strand:</strong> direkt vor der Villa</li>

<li><strong>Mini Market:</strong> {MINI_MARKET}, ca. 12 Minuten zu Fuß</li>

<li><strong>Tavernen:</strong> ca. 12 Minuten zu Fuß nach {SFINARI}</li>

<li><strong>Große Einkäufe:</strong> {LIDL_KISSAMOS} oder {SYNKA_KISSAMOS} in Kissamos</li>

<li><strong>Parken:</strong> kostenlos an der Villa</li>

</ul>

</div>

<h2>Was ihr hier unbedingt machen solltet</h2>

<ul>

<li>Den ersten Sonnenuntergang auf der Terrasse genießen.</li>

<li>Vor dem Frühstück kurz ins Meer springen.</li>

<li>Einen gemeinsamen Grillabend veranstalten.</li>

<li>Schnorcheln direkt vor der Villa.</li>

<li>Einen ganzen Tag bewusst nichts unternehmen.</li>

</ul>

<h2>Sfinari</h2>

<p>Das kleine Fischerdorf {SFINARI} gehört zu den ruhigsten Orten an der
Westküste Kretas. Große Hotels sucht ihr hier vergeblich. Stattdessen erwarten
euch freundliche Tavernen, ein kleiner Mini Market und eine entspannte
Atmosphäre, wie man sie auf Kreta nur noch selten findet.</p>

<h2>Unsere Tavernen-Empfehlungen</h2>

<ul>

<li><strong>{CAPTAIN_FIDIAS}</strong><br>
Direkt an der Bucht von Sfinari, etwa 12 Minuten zu Fuß von der Villa entfernt.<br>
Frischer Fisch, Meeresfrüchte und traditionelle kretische Küche mit
herrlichem Blick aufs Meer.</li>

<li><strong>{ANTONIOS}</strong><br>
Im Ortszentrum von Sfinari, ebenfalls etwa 12 Minuten zu Fuß von der Villa
entfernt.<br>
Familiäre Atmosphäre, kretische Küche und regionale Spezialitäten.</li>

</ul>

<div class="tip">

<h2>Tipp</h2>

<p>Plant bewusst mindestens einen kompletten „Villa-Tag“ ein.
Nicht weil euch die Ausflugsziele ausgehen, sondern weil dieser Ort
selbst zu den schönsten Erinnerungen eurer Reise gehören wird.</p>

</div>

<div class="greek">

<h2>Griechisch des Tages</h2>

<p>

<strong>Θάλασσα</strong><br>

<em>Thálassa</em><br>

Meer

</p>

</div>

<blockquote>

„Manchmal muss man gar nicht weit fahren,
um den schönsten Platz des Urlaubs zu finden.“

</blockquote>
"""