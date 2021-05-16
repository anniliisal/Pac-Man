# Arkkitehtuurikuvaus

## Käyttöliittymä

Peli sisältää yhden pelinäkymän. Itse pelinäkymän lisäksi näytölle ilmestyy aloitusikkunoita, jotka sisältävät ohjeita pelaajalle. 
* Ensimmäisen pelin alkaessa näytölle ilmestyy ikkuna, jossa on ohjeet liikkumiseen ja pelin aloittamiseen.
Pelin voi aloittaa painamalla enter-näppäintä, jonka jälkeen ikkuna poistuu ja Pac-mania pystyy liikuttamaan. 
* Jos peli päättyy haamuun osuttaessa, näytölle piirtyy uusi game over-ikkuna, jossa näkyy edellisen pelin pisteet. Uuden pelin voi aloittaa taas enteriä painamalla. 
* Jos pelin voittaa keräämällä kaikki pisteet, näytölle ilmestyy ikkuna, joka ilmoittaa pelin päättymisestä. Myös voittamisen jälkeen uuden pelin voi aloittaa enteriä painamalla.

## Sovelluslogiikka

Main-luokka toimii pelin tapahtumankäsittelijänä. Uuden pelin alkaessa Main-luokka kutsuu Game-luokkaa pelin alustusta varten. 
Pelin ollessa käynnissä Main-luokan play-metodi kutsuu Game-luokan metodeita draw_screen, update_place ja game.move, 
sekä päivittää pelin tilan metodilla pygame.display.flip(). 

![game](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Game().png)

* Main-luokka kutsuu luokan Game konstruktoria pelinäkymän alustamista varten. Game-luokan konstruktori luo oman luokan atribuutit, 
kutsuen muiden luokkien konstruktoreita ja rakennusmetodeita. 

Pelissä näytölle piirretyt objektit ovat:

* Pac-Man, jota pelaaja voi liikuttaa nuolinäppäimillä.
* Kolme haamua, jotka liikkuvat näytöllä ja Pac-maniin osuessa 
  aiheuttavat pelin päättymisen. 
* Seinät, jotka rajaavat Pac-manin ja haamujen liikkumista.
* Pisteet, joita Pac-man voi kerätä niihin osuessa.

Kaikki näytölle piirretyt objektit, poislukien pistelaskuri, ovat Sprite-olioita. 

![play](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/play().png)

* Main-luokan play-metodi kutsuu Game-luokan draw_screen-metodia, joka piirtää pygame-ikkunaan seinät (self.walls), 
pisteet (self.points), pistetilanteen (self.point_count), haamut (self.ghosts_list), sekä pacmanin (self.pacman_group). Metodi kutsuu
oman luokan get_points-metodia, joka tarkistaa Point-luokan collect_points-metodia käyttäen törmääkö pacman näytöllä olevaan pisteeseen,
ja kasvattaa self.point_count-atribuuttia jos törmäys tapahtuu. 

* Main-luokan play-metodi kutsuu Game-luokan update_place-metodia. Jos peliä ei ole vielä aloitettu, pacman_start_screen-metodi lisää näytölle aloitusikkunan. Jos peli on aloitettu enter-näppäintä painamalla, pacmania pystyy liikuttamaan. Pacman_move-metodi määrittää pacmanille uudet koordinaatit riippuen pacmanin suunnasta. Pacman_move-metodi tarkistaa Wall-luokan collision-metodia käyttäen, törmääkö pacman johonkin seinistä, ja pysäyttää pacmanin liikkeen törmäyksen tapahtuessa. 
Update_place-metodi kutsuu Ghosts-luokan ghost_collision-metodia, jossa tarkistetaan, törmääkö pacman haamujen kanssa. Update-place-metodi tallentaa myös erikseen jokaisen haamun liikkumissuunnan kutsumalla Ghosts-luokan ghost_move-metodia. Ghost_move-metodi määrittää haamulle uudet koordinaatit ja tarkistaa haamun törmäämisen seinään Wall-luokan collision-metodilla. Jos haamu osuu seinään, Ghosts-luokan new_direction-metodi arpoo haamulle uuden suunnan.

* Main-luokan play-metodi kutsuu Game-luokan move-metodia. Move-metodi ohjaa pacmanin liikkumista ohjaamalla suunnanvaihtometodiin, joka määrittyy siitä, mitä näppäintä on painettu alas. Luokkakaavion esimerkkitilanteessa pelaaja on painanut oikeaa nuolinäppäintä, joka ohjaa metodiin pacman_set_direction_right. Pacman_set_direction_right 
muuttaa pacmanin suunta- ja koordinaatti atribuutit oikeaa suuntaa vastaavaksi. 


## Alustava luokkakaavio
![luokkakaavio](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pac-Man.png)

## Alustava sekvenssikaavio
![sekvenssikaavio](https://github.com/anniliisal/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/sekvenssikaavio4.png)
