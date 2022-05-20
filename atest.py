"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

mytext = """Digitale Tabellenextraktion bewerkstelligen – mit der richtigen Software
Tabellen beherbergen häufig die wertvollsten Daten eines Dokumentes. Umso wichtiger ist es, für die Digitalisierung solcher Dokumente eine Software zu nutzen, die den besonderen Anforderungen der Datenauslese von Tabellen genügt. Erfahre in diesem Beitrag, warum Polydocs genau auf diesem Einsatzgebiet brilliert und den Bearbeitungsaufwand für die Tabellenextraktion in deinem Betrieb massiv reduzieren kann.
Tabellenextraktion – der Schlüssel für mehr Effizienz in deinem Unternehmen
In unserer heutigen Welt sind Tabellen in all ihren Formen und Eigenarten nicht mehr aus dem Alltag von Behörden, Unternehmen und auch Privatpersonen wegzudenken. Wie kaum ein anderes Mittel erleichtern sie es, Übersichtlichkeit in Datenmengen und organisatorische Informationen zu bringen.
Tabellen dienen im jeweiligen Dokument dazu, Werte bzw. Posten übersichtlich darzustellen. Dem Leser soll also der Umstand genommen werden, sich mühsam durch einen Fließtext zu lesen, um an die benötigten Informationen zu kommen – egal, ob es sich um die Auflistung der einzelnen Waren in einer Bestellung handelt, um Lieferscheine oder um verwaltungstechnische Informationen wie Abschlusskonten oder Mitarbeiterdetails.
So weit, so gut. Doch als Daten im reinen Druckformat nutzen dir solche Tabellen in der heutigen Zeit nur wenig in Anbetracht der Möglichkeiten, die eine digitalisierte Datenverarbeitung deinem Unternehmen bietet. Wenn du zum Beispiel Statistiken, Auswertungen oder Prognosen für bestimmte Sektoren deines Unternehmens aus den in den Tabellen aufgelisteten Daten berechnen lassen möchtest, um
"""

mytext2 = """- deinen Kunden noch bessere Dienste anbieten zu können,
- als Unternehmen innovativ zu bleiben,
- besser zu sein als die Konkurrenz,
ist es unerlässlich, sie effizient in ein maschinenlesbares Format umzuwandeln.
Maschinenlesbar bedeutet: nicht einfach nur das Dokument als PDF- oder Bilddatei einzuscannen, sondern auch den Text und somit die Werte im Dokument für intelligente Maschinen und Analyseanwendungen weiterverwertbar zu machen.
Dazu können gehören: Mengenangaben, Laufnummern, Prozentangaben, Artikelnummern, Artikelbezeichnungen, Farbangaben von Artikeln, Kundennummern, Währungsangaben, Datumsangaben, Postleitzahlen usw. Aus solcherlei Daten lässt sich beispielsweise berechnen, welche Artikel zu welchen Zeiten besonders häufig gekauft wurden, in welchen Postleitzahlengebieten dein Unternehmen vielleicht mehr Abnehmer hat als in anderen (und in welchen Gebieten entsprechend noch nicht geschöpftes Potenzial für Neukunden besteht), welche Artikel häufig zusammen gekauft werden und vieles andere mehr.
Die maschinenlesbare Digitalisierung von Dokumenten stellt also kein Endziel dar. Vielmehr bildet sie gewissermaßen das Eingangstor in die unbegrenzten Möglichkeiten, die die erweiterte Datenauswertung für die Erhöhung deines Unternehmenserfolges und die Optimierung deiner Unternehmensprozesse bietet.
Das technische Nadelöhr: Tabellen effizient digitalisieren
"""
mytext3 = """Gerade hier zeigt sich jedoch eine große technische Herausforderung. Denn so praktisch und hilfreich Tabellen für die Darstellung und Lesbarkeit jeweils sind, so schwierig sind gerade sie, wenn es darum geht, die betreffenden Dokumente so zu digitalisieren, dass Informationen auch automatisiert verarbeitet werden können. Die individuelle Formatierung macht Tabellen nämlich zu einer hartnäckigen Fehlerquelle für Texterkennungsprogramme, die sonst mit reinem Fließtext gut zurechtkommen.
Tabellen sind in Dokumenten stets auf eine bestimmte Weise optisch eingegliedert. Für den belesenen menschlichen Betrachter erschließt sich dabei meist auf den ersten Blick, wo der Fließtext aufhört und wo die Tabelle beginnt. Anders ist es bei Programmen: Für sie ist es oft nicht so einfach zu bewerkstelligen, die genauen Zonen der Tabelle zu erkennen und Abschnitte korrekt zuzuordnen.
So gibt es bislang noch keine einheitliche Formel, mittels derer man auch einem maschinellen System das Erkennen der Feldergrenzen einer Tabelle eindeutig vermitteln kann. In jedem Dokument haben Tabellen schließlich unterschiedliche Formate (Breite, Höhe, Leerraum, Zeilendichte usw.), die einem Auslese-Programm individuell vermittelt werden müssen. Dies trifft übrigens auch auf elektronische Dateien zu, bei denen eine Tabelle etwa im Bildformat gespeichert ist.
Somit kommt es häufig dazu, dass die Maschine eine Feldergrenze falsch platziert, sodass im digitalisierten Ausgabetext Wörter aus zwei Bereichen des Dokumentes zusammengewürfelt werden, die inhaltlich eigentlich nicht zusammengehören.
Geschieht dies nur bei einem einseitigen Einzeldokument, lässt sich der entstandene Wortsalat zwar nachträglich durch menschliche Bearbeiter wieder in Ordnung bringen. Wenn dein Unternehmen jedoch vor der Aufgabe steht, ganze Aktenschränke in ein maschinenlesbares Format umzuwandeln, können solche Ungenauigkeiten schnell zu einem enormen Frustfaktor werden.
Denn nicht nur sorgen sie dafür, dass viel Arbeitszeit, die für sinnvollere Dinge genutzt werden könnte, in die Fehlerbehebung fließt. Sondern mit jeder zusätzlichen händischen Korrektur, die anfällt, erhöht sich auch das Risiko, dass durch menschliche Unaufmerksamkeit Fehler übersehen werden.
Zu weiteren Problemen bei der automatischen Extraktion von Tabellen in Textdokumenten führt außerdem, dass manchmal Stellen aus dem Fließtext vom System mit einer Tabelle verwechselt und dann als solche eingelesen werden. Dass darüber hinaus Sonderzeichen oder Striche, die innerhalb der Tabelle eine ordnende Funktion einnehmen, bei der automatischen Texterkennung immer wieder falsch interpretiert werden, kommt noch hinzu. Ähnliches gilt übrigens auch für Logos oder andere Bereiche des Dokuments, die zwar als Bild „gemeint“ sind, aber von einer Maschine fälschlicherweise einem Tabellenformat zugewiesen werden können.
Die Folge ist, dass insbesondere das Auslesen von Tabellen zu einer besonderen Hürde wird, wenn es darum geht, Dokumente für die digitale Weiterverarbeitung aufzubereiten. Im Klartext bedeutet dies einen enormen zeitlichen Aufwand und hohe Personalkosten für dein Unternehmen, da die Mitarbeiter in deinem Betrieb die Werte aus der gedruckten Tabelle letztlich zum großen Teil von Hand übertragen und hinterher auch noch gründlich überprüfen und nachbessern müssen.
DOC² – unsere Lösung, spezialisiert auf Tabellenauslesung
Um deinem Unternehmen die effiziente Digitalisierung von Daten aus gedruckten Tabellendokumenten zu erleichtern, nutzen wir DOC². DOC² ist ein auf künstlicher Intelligenz basierendes Werkzeug, das Inhalte aus Dokumenten intelligent extrahiert.
Einer seiner großen Vorteile: Es benötigt deutlich weniger Betreuung durch Menschen als andere vergleichbare Systeme. Ein knapper Initialaufwand, in dem die Felder eines Tabellendokuments markiert werden, reicht aus, um die automatische Extraktion zum Laufen zu bringen.
Falls dann durch deinen zuständigen Mitarbeiter noch weiteres Feedback im Laufe des Digitalisierungsvorgangs eingegeben wird, lernt das System, diese Anweisungen in Folge umzusetzen.
"""
mytext4 = """Die großen Vorteile für dich:
- Zeitersparnis
- Entlastung deiner Mitarbeiter von mühsamem und monotonem Digitalisierungsprozedere
- verlässliche Datenqualität durch hochkarätige Auslesetechnologien
Der gesamte Prozess der Digitalisierung deiner Dokumente wird somit maßgeblich verschlankt und deine Mitarbeiter müssen nur geringfügige manuelle Prozesse durchführen, während der Hauptteil des Digitalisierungsvorgangs automatisch vom System übernommen wird.
Der Unterschied ist in etwa vergleichbar damit, ob die Bauarbeiter auf einer Baustelle die Ziegelsteine aus eigener Kraft in die Schubkarre hieven und die Karre hinterher selbst über das Gelände schieben müssen oder ob sie in der Steuerkabine eines Krans sitzen und dort mittels weniger Steuerbewegungen einer Hand große Mengen von Baumaterial durch den Kran umsetzen lassen.
In beiden Fällen kann auf menschlichen Einsatz nicht verzichtet werden. Während im erstgenannten Fall der Arbeitsvorgang allerdings extrem strapaziös und zeitaufwendig ist, gelingt im zweiten Fall ein Höchstmaß an Arbeitsleistung mit einem Mindestmaß an personellem Aufwand.
Ein Einblick in den Umgang mit unserer Tabellenextraktion
Praktisch sieht der Vorgang der Tabellenextraktion mit Polydocs für deine Mitarbeiter in etwa so aus:
Das Dokument wird zunächst einmal eingescannt und steht somit einer Bearbeitung mittels DOC² zur Verfügung. Im Bearbeitungsmodus für die Tabellenextraktion kann dein Mitarbeiter nur den Scan öffnen und mit wenigen Klicks und Mausbewegungen die genauen Felder und Bereiche festlegen, die ausgelesen werden sollen. Zudem kann dein Mitarbeiter genau bestimmen, in welche Ziel-Spalte die Werte jeweils einsortiert werden sollen. Eine besondere Erleichterung für den Arbeitsprozess bietet dabei die Besonderheit, Custom Columns (also zusätzliche Spalten, die völlig individuell formatiert und bearbeitet werden können) anzuweisen – und das ganz ohne Regex oder sonstige Programmierung. 
Umständliche zusätzliche Mausbewegungen oder Tastaturkürzel zum Kopieren und Einfügen der Werte fallen weg und erlauben es deinem Mitarbeiter, das Dokument flüssig und rasch durchzuarbeiten. Markierte Werte werden intelligent vom Programm erkannt und automatisch als maschinenlesbarer Wert in die gewünschten Felder übertragen.
Eine Auswahl von übersichtlich angeordneten Einstellungsmöglichkeiten und Zusatzfunktionen erlaubt es zudem, die Auslese der Tabelle mit nur wenigen Klicks so zu gestalten, wie es für das jeweilige Dokument nach Einschätzung deines Mitarbeiters nötig ist.
Somit ist Polydocs das ideale Werkzeug für das Digitalisieren selbst komplexer Tabellen mit nur wenigen Handgriffen und einem minimalisierten Betreuungsaufwand durch dein Personal.
Für die Übermittlung der ausgelesenen und aufbereiteten Daten benötigst du darüber hinaus keine besonderen, umständlichen Übertragungskanäle. Die Daten können unkompliziert per E-Mail oder durch automatisiertes Zuweisen in einen festgelegten Ordner übermittelt werden.
Du möchtest einen visuellen Eindruck davon erhalten, wie die Anwendung unseres Programmes konkret aussehen würde? Eine detaillierte Anleitung mit einer Demonstration in Echtzeit findest du hier im Video auf unserem YouTube-Kanal.
Bei etwaigen Fragen oder wenn du dich über eine maßgeschneiderte Lösung für deine Einsatzzwecke erkundigen möchtest, freuen wir uns auf deine Kontaktaufnahme.
Mache die Digitalisierung deiner Tabellendokumente zum Kinderspiel – mit Polydocs!

"""

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=mytext4)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="de-DE",name="de-DE-Wavenet-C", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("tab4.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
