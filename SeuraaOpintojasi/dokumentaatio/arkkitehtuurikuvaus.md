### Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on kuvattu alla olevassa kuvassa ja sen pakkaukset sisältävät seuraavat toiminnallisuudet
- UI sisältää käyttöliittymän
- Services sisältää sovelluslogiikan
- Repositories sisältää tiedon tallennuksen tietokantoihin

![Pakkausrakenne](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/pakkauskaavio.png)

## Käyttöliittymä

Käyttöliittymä on rakennettu tkinter kirjastolla ja se sisältää neljä erilaista näkymää:

- Sisäänkirjautuminen

![Sisäänkirjautuminen](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/kirjaudusisaan.png)

- Uuden käyttäjätunnuksen luominen

![Tunnuksen luominen](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/luouusitunnus.png)

- Päätoiminnallisuus jossa tietoa voi lisätä

![Päänäkymä](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/lisaatietokantaan.png)

- Koostenäkymä

*Tulossa*

## Tiedon tallennus

Pakkausrakenteen repositories -luokassa toteutetaan tiedon tallennus SQLite tietokantaan. Tietokanta on laajennettavissa jos uusia ominaisuuksia halutaan lisätä ohjelmaan.

## Päätoiminnallisuudet

# Sisäänkirjautuminen

![Sekvenssikaavio](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/sekvenssikaavio.png)

# Uuden käyttäjän luominen

# Tietojen lisääminen

# Koosteen luominen