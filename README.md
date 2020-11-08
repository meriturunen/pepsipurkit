# pepsipurkit
pepsipurkkien junction 2020

API contains the very simple Flask API that uses pandas to read csv:s and returns them as json objects.

The frontend is contained in src/shcool-client folder and is made with react.

Parsing the data from opetushallitus json is done in the root of the repository. It consists of multiple python scripts that modify and further enrich the data. The data analysis parts that utilize Google Cloud Platofrm have been moved to GCP folder and all the tokens have been invalidated.
