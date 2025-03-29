
# Data Product Canvas - Berlin LOR geodata

## Metadata

* owner: Open Data Product
* description: Data product providing Berlin geodata of LORs
* url: https://github.com/open-data-product/open-data-product-berlin-electoral-districts-geodata
* license: CC-BY 4.0
* updated: 2025-06-01

## Input Ports

### Bezirke

* owner: Geoportal Berlin
* url: https://daten.odis-berlin.de/de/dataset/bezirksgrenzen/
* updated: 2017-12-31

**Files**

* [bezirksgrenzen.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/bezirksgrenzen/bezirksgrenzen.geojson)

### Lebensweltlich orientierte Räume (LOR) - Prognoseräume (bis Ende 2020)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_prognoseraeume/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_prognoseraeume.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_prognoseraeume/lor_prognoseraeume.geojson)

### Lebensweltlich orientierte Räume (LOR) - Prognoseräume (ab 2021)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_prognoseraeume_2021/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_prognoseraeume_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_prognoseraeume_2021/lor_prognoseraeume_2021.geojson)

### Lebensweltlich orientierte Räume (LOR) - Bezirksregionen (bis Ende 2020)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_bezirksregionen/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_bezirksregionen.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_bezirksregionen/lor_bezirksregionen.geojson)

### Lebensweltlich orientierte Räume (LOR) - Bezirksregionen (seit 2021)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_bezirksregionen/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_bezirksregionen_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_bezirksregionen_2021/lor_bezirksregionen_2021.geojson)

### Lebensweltlich orientierte Räume (LOR) - Planungsräume (bis Ende 2020)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_bezirksregionen/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_planungsraeume.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_planungsgraeume/lor_planungsraeume.geojson)

### Lebensweltlich orientierte Räume (LOR) - Planungsräume (bis Ende 2020)

* owner: Amt für Statistik Berlin-Brandenburg
* url: https://daten.odis-berlin.de/de/dataset/lor_bezirksregionen/
* license: CC-BY-3.0-Namensnennung
* updated: 2021-09-09

**Files**

* [lor_planungsraeume_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_planungsgraeume_2021/lor_planungsraeume_2021.geojson)

## Transformation Steps

* [Geojson converter](../lib/transform/data_geojson_converter.py) converts shape files into geojson
* [Property converter](../lib/transform/data_property_converter.py) renames and removes properties of geojson features
* [Geometry converter](../lib/transform/data_geometry_converter.py) converts inconsistent geometry
* [Projection converter](../lib/transform/data_projection_converter.py) converts geojson to polar projection (epsg:4326)
* [Data combiner](../lib/transform/data_combiner.py) combines district geojson files into city
* [Bounding box converter](../lib/transform/data_bounding_box_converter.py) adds a bounding box to each feature
* [LOR area matcher](../lib/transform/data_lor_area_matcher.py) identifies overlaps in LOR areas between until-2020 and from-2021 taxonomy

## Output Ports

### Berlin Lor City

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-city
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-city.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-city/berlin-lor-city.geojson)

### Berlin Lor District Regions From 2021

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-district-regions-from-2021
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-district-regions-from-2021.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson)

### Berlin Lor District Regions Until 2020

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-district-regions-until-2020
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-district-regions-until-2020.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson)

### Berlin Lor Districts

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-districts
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-districts.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-districts/berlin-lor-districts.geojson)

### Berlin Lor Forecast Areas From 2021

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-forecast-areas-from-2021
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-forecast-areas-from-2021.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson)

### Berlin Lor Forecast Areas Until 2020

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-forecast-areas-until-2020
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-forecast-areas-until-2020.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson)

### Berlin Lor Planning Areas From 2021

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-planning-areas-from-2021
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-planning-areas-from-2021.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson)

### Berlin Lor Planning Areas Until 2020

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/02-silver/berlin-lor-planning-areas-until-2020
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-planning-areas-until-2020.geojson](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/02-silver/berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson)

### Berlin Lor Matches

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-berlin-lor-geodata/tree/main/data/03-gold/berlin-lor-matches
* license: CC-BY 4.0
* updated: 2025-06-01

**Files**

* [berlin-lor-matches.json](https://raw.githubusercontent.com/open-data-product/open-data-product-berlin-lor-geodata/main/data/03-gold/berlin-lor-matches/berlin-lor-matches.json)

## Consumers

**Who is the consumer of the Data Product?**

Consumers of this data product may include

* projects that display LORs
* other data products that combine geospatial data with statistics data

## Use Cases

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used

* to display data related to LORs in Berlin on an interactive map

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).