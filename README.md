# PJATK_ZUM_projekt

(English below)  
**Projekt zaliczeniowy z Zastosowań Uczenia Maszynowego PJATK 2022-23**    
 
Projekt dotyczył tworzenia modeli NLP w Pythonie, wymagane było przygotowanie, procesowanie i otagowanie zbioru danych (Twitter/Reddit), wytrenowanie klasycznych modeli, sieci neuronowej oraz modelu językowego.  
  
Zawartość repozytorium:
- folder *01_data_scraping* zawiera kod do pobrania danych (oraz dane) z subreddit popularnego brytyjskiego programu komediowego "Taskmaster" - skupiamy się na dyskusjach dotyczących odcinków, celem było zebranie próby ok. 10000 komentarzy
- folder *02_data_preprocessing_tagging* zawiera notebooki do wstępnej analizy zescrapowanych danych, czyszenia, lematyzacji, tokenizacji, oraz szybkiego stworzenia klastrów przy pomocy K-Means (nie jest to rozwiązanie idealne, ale w dużym uproszczeniu można uznać, że mamy 2 kategorie - komentarze pozytywne oraz komentarze neutralne/negatywne)
- folder *00_DATA_preprocessed* zawiera plik z oczyszczonymi, otagowanymi danymi przygotowanymi do dalszych zadań (plik z tokenizacją jest za duży dla githuba, ale jego generowanie jest też w kodzie w notebooku w folderze 02)
- folder *03_classic_ml* zawiera notebooki z próbami dopasowania i ewaluacji modeli z pakietu sklearn: LinearSVM, LinearSVM z dodanymi wagami (odpowiadającymi udziałowi poszczególnych klas w całym zbiorze danych), NaiveBayes
- folder *04_neural_networks* zawiera notebooki z próbami wytrenowania sieci neuronowych

Wyniki i wnioski:

- scraper dość dobrze poradził sobie ze zbieraniem komentarzy, chociaż na przyszłość należy zadbać o nieuwzględnianie usuniętych komentarzy już na etapie pobierania danych, warto też zabezpieczyć się na wypadek nieprzewidzianych sytuacji (np. niestabilne łącze) 
- klasyfikatory z pakietu sklearn osiągały dość dobre wyniki, accuracy na poziomie 85-97%
- na przyszłość dobrze byłoby sprawdzić co się stanie jesli z naszych danych usuniemy np. słowa kluczowe związane z programem, pojawiające się bardzo często a niekoniecznie wnoszące wiele znaczenia w kontekście wykonywanej klasyfikacji (np. nazwiska uczestników, tytuły, bezpośrenie cytaty z programu)

**Final project for Applications of Machine Learning PJAIT 2022-23**
