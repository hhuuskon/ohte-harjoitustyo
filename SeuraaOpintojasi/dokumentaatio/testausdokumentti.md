## Testausdokumentti

- Ohjelmaan on tehty automatisoituja testejä käyttäen siihen tarkoitukseen suunniteltua unittest moduulia.
- Testien koodi löytyy [täältä](https://github.com/hhuuskon/ohte-harjoitustyo/tree/master/SeuraaOpintojasi/src/tests)

### Testaaminen
#### Sovelluslogiikka
- Sovelluslogiikasta vastaavat ```CourseServices``` ja ```UsersServices``` -luokat testataan erillisillä ```TestUsersServices``` ja ```TestCourseServices``` -luokilla. Molemmissa luokissa alustetaan ensin testitietokanta. 
- ```TestCourseServices``` testeissä syötetään ensin tietokantaan tietoja. Tämä tehdään sen takia, jotta saisimme testattua laskeeko ohjelma sen tuottamat koosteet oikein, kun syötteitä on useampia. Näin saamme monta eri skenaariota testattua.
- ```TestUsersServices``` testeissä teemme ensin muutaman testikäyttäjän jonka sisäänkirjautumista voimme testata esimerkiksi oikeilla ja väärillä käyttäjätunnus ja salasana yhdistelmillä. Myös olemassa oleva käyttäjätunnus on helppo testata tällä tapaa.

#### Tietokantakyselyt
- Tietokantakyselyistä vastaavat ```CourseRepository``` ja ```UsersRepository``` -luokat testataan erillisillä ```TestCourseRepository``` ja ```TestUsersRepository``` -luokilla. Molemmissa alustamme ensin testitietokannan.
- ```TestCourseRepository``` alustamme ensin muutaman olion, joita voimme syöttää testeissä tietokantaan. Tämän jälkeen voimme testata tietokantaa antaako se oikeanlaiset koosteet meille oikeanlaiset syötteet ja koosteet.
-  ```TestUsersRepository``` testeissä teemme ensin muutaman testikäyttäjän jonka avulla pystymme ```TestUsersServices``` -testien tapaan testaamaan erilaisia yhdistelmiä käyttäjistä. Tällä tavoin saamme selville osaako tämä luokka ilmoittaa jo olemassa olevat käyttäjät ja väärät käyttäjätunnus ja salasana yhdistelmät.

### Testikattavuus

- Testikattavuus tässä lopullisessa versiossa on coverage-reportin mukaan 84%. Alla olevasta kuvasta selviää tarkempi prosentuaalinen jakauma. Testeihin ei ole sisällytetty käyttöliittymän testaamista.

![Coverage-Report](https://github.com/hhuuskon/ohte-harjoitustyo/blob/master/SeuraaOpintojasi/dokumentaatio/kuvat/coverage-final.png)

### Käyttöliittymän ja järjestelmän testaus

- Sovellusta ja sen käyttöliittymää on testattu paljon manuaalisesti. Tähän on sisältynyt erilaisten syötteiden antamista, tyhjäksi jättämistä ja sovelluksessa kulkemista edes takaisin valikkojen välillä.
- Sovellus on haettu GitHubista ja testattu toimivaksi laitoksen Linux "fuksi läppärillä" sekä toisella macOS tietokoneella.
- Käyttöohjeet ovat käyty läpi ja niitä on päivitetty ominaisuuksien lisäämisen myötä.

### Sovelluksen laatuongelmat

- Sovelluksen tietokanta alustetaan, kuin testit ajetaan läpi. Tämä johtuu siitä, koska sovelluksen toimintaperiaatetta muttettiin vastaamaan saatua palautetta, jotta tietokanta olisi myös pysyvä ohjelman sammutettua, eikä vain yhden käyttökerran aikana. Tämä on hyvä huomioida sovellusta testattaessa.

- Osa Pylint virheistä tulee yksinkertaisesti vain siitä, että tietokanta on nimetty koodiin eikä siinä voida käyttää Pylintin vaatimaa "snake case" formaattia.