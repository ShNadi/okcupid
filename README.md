# OkCupid Stylometry Analysis Project

Version 0.1.0
# OkCupid classifier

This project aims to examine to what extent educational background can be inferred from the written text, based on the assumption that educational levels are associated with the style of writing. This includes people's signature fashion of using certain vocabulary of words which makes their literature unique and recognizable. Using a large public dataset of almost 60000 dating profiles, we aimed to model author style to be used as a predictor of educational background.

## Researcher & engineers

Researcher:

- Corten, R. (Rense)

Engineer:

- Shiva Nadi


## Installation

This project requires Python 3.5 or higher. Install the dependencies with the
code below.

```sh
pip install -r requirements.txt
```

## Project organization

```
.
├── .gitignore
├── CITATION.md
├── LICENSE.md
├── README.md
├── requirements.txt
├── bin                <- Compiled and external code, ignored by git (PG)
│   └── external       <- Any external source code, ignored by git (RO)
├── config             <- Configuration files (HW)
├── data               <- All project data, ignored by git
│   ├── processed      <- The final, canonical data sets for modeling. (PG)
│   ├── raw            <- The original, immutable data dump. (RO)
│   └── temp           <- Intermediate data that has been transformed. (PG)
├── docs               <- Documentation notebook for users (HW)
│   ├── manuscript     <- Manuscript source, e.g., LaTeX, Markdown, etc. (HW)
│   └── reports        <- Other project reports and notebooks (e.g. Jupyter, .Rmd) (HW)
├── results
│   ├── figures        <- Figures for the manuscript or reports (PG)
│   └── output         <- Other output for the manuscript or reports (PG)
└── src                <- Source code for this project (HW)

```


## License

This project is licensed under the terms of the [MIT License](/LICENSE.md)

## Citation

Please [cite this project as described here](/CITATION.md).
