# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä asenna riippuvuudet komennolla:

*poetry install*

Ohjelman voi käynnistää komennolla:

*poetry run invoke start*

### Pelaaminen

- Pelin avautuessa avautuu aloitusnäkymä:

![kuva](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Näyttökuva%202021-5-16%20kello%2015.45.26.png)

- Pac-manin liikuttaminen eri suuntiin tapahtuu nuolinäppäimillä 
- Pelin voi aloittaa painamalla enter-näppäintä
- Pac-man syö pisteitä niiden osuessa kohdalle. Pelin voittaa, kun saa syötyä kaikki 87 pistettä.
- Jos Pac-man törmää haamuun, peli päättyy. Näytölle avautuu ikkuna, jossa näkyy edellisen pelin pisteet. 
  Pelin voi aloittaa alusta painamalla enter-näppäintä.

