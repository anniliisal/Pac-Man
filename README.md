# Pac-Man

Sovelluksella pelataan Pac-Man tyylistä peliä. Pac-manilla liikutaan sokkeloita pitkin ja syödään pisteitä.
Kentällä liikkuu myös haamuja joita pitää varoa. 

## Python-versio

Sovellusta on testattu Python versiolla 3.6

## Dokumentaatio

[vaativuusmäärittely.md](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmäärittely.md)

[työaikakirjanpito.md](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[arkkitehtuuri.md](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennoilla:

* *poetry install*
* *poetry add cowsay*
* *poetry add invoke*
* *poetry add coverage --dev*
* *poetry add pygame*
* *poetry add pylint --dev*


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















