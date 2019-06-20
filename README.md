# astar_zenji_bachr2
A* (A Star) für Zenji

Zenji ist ein Zustandsraumproblem, auch bekannt aus dem C64-Game Zenji.
Dies ist ein kleines Python-Projekt gemacht in PyCharme für das Wahlfach AI an der BFH.
Es implementiert einen A*-Algorithmus mit Heuristik für Zenji.

Erstellt von Rico Bachmann (bachr2)

## Aufgabenstellung

Zenji ist ein Zustandsraumproblem, es besteht aus einer Reihe von quadratischen Feldern mit Röhren, die in einem (rechtwinkligen) Gitter angeordnet sind. Das linke obere Feld enthält eine Wasserquelle, daslinke untere Feld ist ein Hahn. Die Röhren-Felderdürfen gedreht werden, jedoch nicht ersetzt oder verändert werden. Aufgabe ist es diese Röhrenquadrateso zu drehen, dass ein durchgängiger Wasserfluss von der Quelle (links oben) zum Hahn (rechts unten) möglich wird.Die Röhren habenzudem eineEingangs-oderAusgangsrichtung. Diese istbeim Wasserfluss zu beachten.In der Basisaufgabe wollen wir annehmen, dass das Wasser (aufgrund der Steigung) nur von links nach rechts und von oben nach unten fliessen kann.Die Basisaufgabe besteht nun darin ein Programm in Python oder Java zu schreiben, dasdieses Puzzle löst. Dieses Programm muss die Codierung der Problemdomäne enthaltenundeinen Suchalgorithmus. Die Ausgabemuss nicht grafisch sein, sondernkann als Text auf das Protokollfenster oder in ein File erfolgen.

## Karte und Weg

| n x m  | 0 | 1  | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0  | 0, 0  | 0, 1  | 0, 2  | 0, 3  |
| 1  | 1, 0  | 1, 1  | 1, 2  | 1, 3  |
| 2  | 2, 0  | 2, 1  | 2, 2  | 2, 3  |
| 3  | 3, 0  | 3, 1  | 3, 2  | 3, 3  |
Beispiel des Koordinatensystems der Karte

Eine Karte besteht aus einem, auf n mal m Feldern (n x m == Reihen x Kollonen) ausgelegten, Röhrensystem. Jedes der Felder (ausser Start und Endpunkt) können im Uhrzeigersinn gedreht werden.

TODO Bild "echte" Karte
Die Beispielmap aus dem Projekt

### Feld

| |  |   |
| --- | --- | --- |
|   | 0 |   |
| 1 |   | 0 |
|   | 2 |   |
Beispiel eines Feldes welches in Position 0 im Norden und im Osten eine Blockade hat, im Süden einen Ausgang und im Westen einen Eingang

Ein Feld besteht aus einem Teil des Röhrensystem, jedes Seite des Feldes ist entweder ein Eingang (1), Ausgang (2) oder eine Blockade (0).
Im Spiel sind Zusätzlich noch der Wassereinlass (3)

## A *

TODO Schnellbeschreibung A *

### Speziell für Zenji

#### Generierung Kinderknoten

#### Heuristik und zurückgelegte Strecke

## Quellen

[easy-a-star-pathfinding](https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2), Beispiel für A* an einem einfachen Irrgartenspiel
