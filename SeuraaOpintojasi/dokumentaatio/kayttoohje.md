### Käyttöohje

## Asennus
Voit asentaa tarvittavat riippuvuudet komentoriviltä komennolla:
```
poetry install
```

## Sovelluksen käynnistäminen

Voit käynnistää sovelluksen komentoriviltä komennolla:
```
poetry run invoke start
```

## Sisäänkirjautuminen

Sovellus käynnistyy näkymään johon käyttäjä voi syöttää jo olemassa olevan tunnuksen ja salasanan ja painamalla "Kirjaudu sisään" -painiketta.

![Kirjaudu sisään](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/kirjaudusisaan.png)

## Uuden tunnuksen luominen

Sovellukseen voi luoda uuden tunnuksen painamalla sisäänkirjautumisen näkymästä "Luo uusi tunnus" -painiketta.

![Luo uusi tunnus](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/luotunnus.png)

Käyttäjä voi nyt syöttää valitsemansa käyttäjätunnuksen ja salasanan ja painaa "Luo tunnus" -painiketta.

![Luo tunnus](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/luouusitunnus.png)

Jos tunnuksen luominen onnistuu niin ohjelma kirjaa käyttäjän sisään automaattisesti.
Jos käyttäjätunnus on jo varattu, ohjelma ilmoittaa siitä virheviestillä.

![Virhe](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/tunnusonjoolemassa.png)

Jos käyttäjä muistaakin, että hänellä oli jo tunnus sovellukseen voi hän palata kirjautumisnäkymään painamalla "Minulla on jo tunnus" -painiketta.

![Tunnus jo olemassa](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/minullaonjotunnus.png)

## Tietojen lisääminen

Sovellukseen voi lisätä päänäkymässä tietoa kuinka monta tuntia opiskelija on käyttänyt tiettynä päivänä aikaa jonkin kurssin tekemiseen.
Käyttäjä syöttää kurssin tunnisteen (esim. TKT20002), käytetyt tunnit numerona (esim. 4) sekä päivämäärän muodossa PP.KK.VVVV.
Painamalla "Lisää tietokantaan" -painiketta, tiedot tallentuvat.

![Lisää kurssin tiedot](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/lisaatietokantaan.png)

## Koosteen luominen

Käyttäjä voi luoda koosteen painamalla "Näytä kooste" -painiketta *Ominaisuus vasta tulossa*

## Uloskirjautuminen

Jos käyttäjä on kirjautunut sisään sovellukseen, hän näkee myös jokaisessa näkymässä "Logout" -painikkeen jota painamalla käyttäjä kirjataan ulos ja palautetaan kirjatumisnäkymään.

![Kirjaudu ulos](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/logout.png)






