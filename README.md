# # Enriching Portuguese Word Embeddings with Visual Information
This repository contains all the code and data necessary to replicate the results of related dissertation. The custom test code and translated test set data are directly accessible through this GitHub page. The rest of the data is linked to below, including the trained multimodal models.

## Pre-Trained Multimodal Models
All multimodal models used for testing can be found in the following Google Drive folder: https://drive.google.com/drive/folders/14HsxuSsxQqEAi_5bBk46Fkst1TAnznfK?usp=sharing

This folder includes all tested combinations, at all tested Imagined Embedding Learning Epochs.

## Word Relatedness Tests
Both test corpora are available in the Word Relatedness folder, alongside the test code. 

The MEN translated corpus was originally obtained in the English language, and the original should also be cited in case you use the translation. The original English version is available [here](https://staff.fnwi.uva.nl/e.bruni/MEN), and should be cited as:
>**Multimodal Distributional Semantics** E. Bruni, N. K. Tran and M. Baroni. Journal of Artificial Intelligence Research 49: 1-47.

The GeoSim test corpus is also available [here](https://github.com/Petroles/Petrovec), in the original project's GitHub page, and should be cited as:
>**Portuguese Word Embeddings for the Oil and Gas Industry: development and evaluation** Diogo Gomes, Fabio Cordeiro, Bernardo Consoli, Nikolas Santos, Viviane Moreira, Renata Vieira, Silvia Moraes, Alexandre Evsukoff. "Portuguese Word Embeddings for the Oil and Gas Industry: Development and Evaluation". Computers in Industry, vol. 124, 2021, p. 103347. doi:10.1016/j.compind.2020.103347. [http://www.sciencedirect.com/science/article/pii/S0166361520305819](http://www.sciencedirect.com/science/article/pii/S0166361520305819)

## Analogy Prediction Tests
The Analogy Prediction test set was made available alongside NILC's Embedding repository, as a way to intrinsically test the embeddings. It can be found [here](https://github.com/nathanshartmann/portuguese_word_embeddings). The code to run the tests can be found alongside the test sets.

## Sentence Similarity Tests
The Semantic Similarity test set was also developed by NILC, and is available [here](http://www.nilc.icmc.usp.br/assin/). The code to evaluate this test set can be found [here](https://github.com/nathanshartmann/portuguese_word_embeddings). 

## Named Entity Recognition Tests
The Named Entity Recognition corpora are HAREM 1, MiniHarem and GeoCorpus 3.0. MiniHarem was used as the test set for a NER NN which was trained with HAREM 1, while GeoCorpus 3.0 was 10-Fold Cross-Validated.

Both HAREM 1 and MiniHarem can be found [here](https://www.linguateca.pt/primeiroHAREM/harem_encontroharem.html). GeoCorpus 3.0 can be found [here](https://github.com/Petroles/Petrovec).

The code used for running the NER test can be found [here](https://github.com/jneto04/ner-pt).

## Citing this work
TBD
