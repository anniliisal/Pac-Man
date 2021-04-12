# Pac-Man

Sovelluksella pelataan Pac-Man tyylistä peliä. Pac-manilla liikutaan sokkeloita pitkin ja syödään pisteitä.
Kentällä liikkuu myös haamuja joita pitää varoa. 

## Python-versio

Sovellusta on testattu Python versiolla 3.9.4

## Dokumentaatio

[vaativuusmäärittely.md](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/vaativuusmäärittely.md)

[työaikakirjanpito.md](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)


## Komentorivitoiminnot

**Ohjelman suoritus**

Suorita ohjelma komennolla:

*poetry run invoke start*
 
tai:

*poetry run python3 src/game.py*

**Testaus**

Suorita ohjelman testit komennolla:

*poetry run invoke test*

tai:

*poetry run python3 src/tests/Game_test.py*


**Testikattavuus**

Generoi ohjelman testikattavuus komennolla:

*poetry run invoke coverage-report*

Raportti generoituu htmlcov-hakemistoon.















