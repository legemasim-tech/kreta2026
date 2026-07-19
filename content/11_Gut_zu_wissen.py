from content_helpers import maps_link


TITLE = "Gut zu wissen – Praktische Tipps"

IMAGE = "Villa Perikles (10).avif"

PHOTO_STYLE = "single"

EXTRA_IMAGES = [
    {
        "file": "Villa Perikles (8).avif",
        "caption": "Entspannt einkaufen, grillen und den Tag auch Zuhause genießen"
    }
]

QUOTE_AFTER_IMAGES = True


VILLA_PERICLES = maps_link(
    "Villa Pericles",
    "Pericles Beach Villa, Sfinari, Kissamos, Crete, Greece",
)


MINI_MARKET_SFINARI = """
<a
    class="maps-link"
    href="https://maps.app.goo.gl/oGDaBX9DhvhrEfag9"
    target="_blank"
    rel="noopener noreferrer"
>
    Mini Market Sfinari
    <span class="maps-link-icon" aria-hidden="true">↗</span>
</a>
"""


SYNKA_KISSAMOS = """
<a
    class="maps-link"
    href="https://maps.app.goo.gl/AJJDsDM4mrXYHRQF7"
    target="_blank"
    rel="noopener noreferrer"
>
    SYN.KA
    <span class="maps-link-icon" aria-hidden="true">↗</span>
</a>
"""


LIDL_KISSAMOS = maps_link(
    "Lidl Kissamos",
    "Lidl, Kissamos, Crete, Greece",
)


CAPTAIN_FIDIAS = maps_link(
    "Captain Fidias – Sfinari",
    "Captain Fidias, Sfinari, Kissamos, Crete, Greece",
)


ANTONIOS = maps_link(
    "Antonios – Sfinari",
    "Antonios Restaurant, Sfinari, Kissamos, Crete, Greece",
)


THE_CELLAR = maps_link(
    "The Cellar – Kissamos",
    "The Cellar Tavern, Kissamos, Crete, Greece",
)


TAMAM = maps_link(
    "Tamam – Chania",
    "Tamam Restaurant, Zampeliou 49, Chania, Crete, Greece",
)


AVLI = maps_link(
    "Avli – Rethymno",
    "Avli Restaurant, Xanthoudidou 22, Rethymno, Crete, Greece",
)


TEXT = f"""
<h2>Die kleinen Dinge, die den Urlaub schöner machen</h2>

<p>Fast alles, was ihr für einen gelungenen Urlaub braucht, findet ihr in
der Umgebung der {VILLA_PERICLES}. Mit ein paar einfachen Tipps spart ihr euch
unnötige Wege und könnt die Zeit auf Kreta entspannter genießen.</p>

<div class="info">

<h2>Einkaufen</h2>

<ul>

<li>
<strong>{MINI_MARKET_SFINARI}:</strong>
Brot, Getränke, Eis und Kleinigkeiten – ca. 12 Minuten zu Fuß.
</li>

<li>
<strong>{SYNKA_KISSAMOS}:</strong>
griechischer Supermarkt mit Obst, Gemüse, Käse, Olivenöl,
Wein und regionalen Produkten.
</li>

<li>
<strong>{LIDL_KISSAMOS}:</strong>
ideal für Getränke, Wasser, Grillabende und den größeren Einkauf.
</li>

</ul>

</div>

<h2>Tanken</h2>

<p>Tankstellen gibt es rund um Kissamos genügend. Da viele Ausflüge durch
Berge und kleinere Orte führen, ist es entspannter, den Tank nie ganz leer
werden zu lassen.</p>

<h2>Unsere Lieblings-Tavernen</h2>

<ul>

<li>
<strong>{CAPTAIN_FIDIAS}:</strong>
Fisch und Meeresfrüchte direkt am Meer.
</li>

<li>
<strong>{ANTONIOS}:</strong>
familiäre Atmosphäre und traditionelle kretische Küche.
</li>

<li>
<strong>{THE_CELLAR}:</strong>
guter Abschluss nach einem Ausflug oder Einkauf.
</li>

<li>
<strong>{TAMAM}:</strong>
beliebte Adresse in der Altstadt mit besonderem Ambiente.
</li>

<li>
<strong>{AVLI}:</strong>
romantischer Innenhof und gehobene kretische Küche.
</li>

</ul>

<h2>Unsere kleinen Kreta-Tipps</h2>

<ul>
<li>☕ Probiert mindestens einmal einen griechischen Café Frappé oder einen Freddo Cappuccino.</li>
<li>🌅 Mindestens einen Sonnenuntergang direkt von der Terrasse der Villa genießen.</li>
<li>🐐 Auf Bergstraßen haben Ziegen fast immer Vorfahrt.</li>
<li>🍉 Obst vom Straßenstand schmeckt oft besser als aus dem Supermarkt.</li>
<li>🧊 Eine Kühltasche im Auto ist bei Strandtagen Gold wert.</li>
<li>📷 Die schönsten Fotos entstehen morgens oder kurz vor Sonnenuntergang.</li>
<li>💶 Etwas Bargeld dabeihaben – kleine Tavernen und Stände freuen sich darüber.</li>
<li>🇬🇷 Ein einfaches „Kaliméra“ öffnet auf Kreta fast immer Türen.</li>
</ul>

<h2>Am Strand</h2>

<ul>
<li>Immer genug Wasser mitnehmen.</li>
<li>Badeschuhe sind an felsigen Stellen angenehm.</li>
<li>Sonnenschutz nicht unterschätzen.</li>
<li>Die Natur respektieren und keinen Müll zurücklassen.</li>
</ul>

<h2>Ein paar griechische Wörter</h2>

<table class="greek-table">
    <thead>
        <tr>
            <th>Griechisch</th>
            <th>Aussprache</th>
            <th>Deutsch</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td lang="el">Καλημέρα</td>
            <td>Kaliméra</td>
            <td>Guten Morgen</td>
        </tr>
        <tr>
            <td lang="el">Καλησπέρα</td>
            <td>Kalispéra</td>
            <td>Guten Abend</td>
        </tr>
        <tr>
            <td lang="el">Ευχαριστώ</td>
            <td>Efcharistó</td>
            <td>Danke</td>
        </tr>
        <tr>
            <td lang="el">Παρακαλώ</td>
            <td>Parakaló</td>
            <td>Bitte</td>
        </tr>
        <tr>
            <td lang="el">Γεια σας</td>
            <td>Jássas</td>
            <td>Hallo</td>
        </tr>
    </tbody>
</table>

<div class="tip">

<h2>Unser persönlicher Tipp</h2>

<p>Plant nicht jeden Urlaubstag komplett durch. Oft entstehen die schönsten
Erinnerungen genau dann, wenn ihr spontan irgendwo stehen bleibt,
eine kleine Taverne entdeckt oder den Abend auf der Terrasse ausklingen lasst.</p>

</div>

<blockquote>
„Die schönsten Erinnerungen entstehen nicht nur an besonderen Orten,
sondern vor allem aus den Momenten, die man nicht geplant hat.“
</blockquote>
"""