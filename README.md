# Opintojen seurantasovellus
TKT20002 Harjoitustyö

Tässä sovelluksessa opiskelija voi pitää kirjaa työajasta, jota hän on käyttänyt käymiinsä kursseihin. Sovellukseen luodaan käyttäjätunnus, joten sitä voi käyttää myös useampi käyttäjä samalta laitteelta.

## Dokumentaatio
- [Ensimmäinen release](https://github.com/hhuuskon/ohte-harjoitustyo/releases/tag/viikko5)
- [Toinen release](https://github.com/hhuuskon/ohte-harjoitustyo/releases/tag/viikko6)
- [Vaatimusmäärittely](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/arkkitehtuurikuvaus.md)
- [Käyttöohje](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kayttoohje.md)

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

## Muut komennot
Voit suorittaa koodin laadun tarkistuksen Pylint -työkalulla komennolla:
```
poetry run invoke lint
```

Voit suorittaa koodin testikattavuusraportin Coverage - työkalulla komennolla:
```
poetry run invoke coverage
```

Voit luoda visuaalisen testikattavuusraportin komennolla:
```
poetry run invoke coverage-report
```

