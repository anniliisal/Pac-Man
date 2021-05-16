# Pac-Man

Sovelluksella pelataan Pac-Man tyylistä peliä. Pac-manilla liikutaan sokkeloita pitkin ja syödään pisteitä.
Kentällä liikkuu myös haamuja joita pitää varoa. 

## Release 

[Pac-Man](https://github.com/anniliisal/Pac-Man/releases/tag/%23loppupalautus)

## Python-versio

Sovellusta on testattu Python versiolla 3.6

## Dokumentaatio

[Käyttöohje](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/käyttöohje.md)

[Vaativuusmäärittely](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmäärittely.md)

[Työaikakirjanpito](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennolla:

*poetry install*

## Komentorivitoiminnot

**Ohjelman suoritus**

Suorita ohjelma komennolla:

*poetry run invoke start*
 
**Testaus**

Suorita ohjelman testit komennolla:

*poetry run invoke test*

**Testikattavuus**

Generoi ohjelman testikattavuus komennolla:

*poetry run invoke coverage-report*

Raportti generoituu htmlcov-hakemistoon.

**Laatutarkistus**

Laatuvaatimukset voi tarkistaa komennolla:

*poetry run invoke lint*












