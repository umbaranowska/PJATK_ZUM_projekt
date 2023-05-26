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
- proste sieci sekwencyjne były bardzo podatne na szybkie przetrenowanie, dodanie dropoutu nieco pomogło z tym problemem
- na przyszłość dobrze byłoby sprawdzić co się stanie jesli z naszych danych usuniemy np. słowa kluczowe związane z programem, pojawiające się bardzo często a niekoniecznie wnoszące wiele znaczenia w kontekście wykonywanej klasyfikacji (np. nazwiska uczestników, tytuły, bezpośrenie cytaty z programu)

**Final project for Applications of Machine Learning PJAIT 2022-23**

This project was about creating Natural Language Processing models in Python. We were required to prepare, preprocess, and tag a dataset (Twitter/Reddit), train classical ML models, neural networks and LLMs.

The repository contains:
- folder *01_data_scraping* contains the code used for scraping data from r/taskmaster dedicated to popular British comedy show "Taskmaster", and the collected data, the focus is on discussion threads about specific episodes and the goal was to collect a sample of approx. 10K comments
- folder *02_data_preprocessing_tagging* contains notebooks for EDA of collected data, cleaning, lemmatization, tokenization and quick creation of clusters using KMeans (not the ideal solution but the 2 clusters could be described as positive comments and neutral/negative comments)
- folder *00_DATA_preprocessed* contains the clean and preprocessed dataset (the tokenized version was too large to store on github, however the code used for generating it is available in folder 02)
- folder *03_classic_ml* contains notebooks dedicated to fitting models from scikit-learn: LinearSVM, LinearSVM with weights corresponding to proportions of comments tagged as belonging to each category in the entire dataset, NaiveBayes
- folder *04_neural_networks* contains notebooks with attempts to train neural networks

Results and conclusions:

- the scraper was quite efficient, but it is important to prevent errors that might arise from issues such as unstable internet connection 
- scikit-learn classifiers achieved quite good results, with accuracy at around 85-97%
- simple sequential neural networks were prone to overfitting after just a few epochs, adding dropout layers did help with this problem
- in the future it would be interesting to check what happens if we remove not only stopwords but also words that are very frequent in the comments but seemingly irrelevant in the context of the ML problem (such as hosts and contestants names)
