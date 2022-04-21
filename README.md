# Opintojen seurantasovellus
TKT20002 Harjoitustyö

Tässä sovelluksessa opiskelija voi pitää kirjaa työajasta, jota hän on käyttänyt käymiinsä kursseihin. Sovellukseen luodaan käyttäjätunnus, joten sitä voi käyttää myös useampi käyttäjä samalta laitteelta.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/arkkitehtuuri.md)

## Asennus
Voit asentaa tarvittavat riippuvuudet komentoriviltä komennolla:
~~~ poetry install ~~~

## Sovelluksen käynnistäminen
Voit käynnistää sovelluksen komentoriviltä komennolla:
''' poetry run invoke start '''

## Muut komennot
Voit suorittaa koodin laadun tarkistuksen Pylint -työkalulla komennolla:
''' poetry run invoke lint '''

Voit suorittaa koodin testikattavuusraportin Coverage - työkalulla komennolla:
''' 
poetry run invoke coverage
'''
