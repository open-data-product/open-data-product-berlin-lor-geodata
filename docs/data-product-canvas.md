# Data Product Canvas - Berlin LOR geodata

## Input Ports

**Input ports define the format and protocol in which data can be read (database, file, API, visualizations)**

This data product uses LOR geodata provided by [Amt für Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/) and [Geoportal Berlin](https://daten.odis-berlin.de/de/dataset/bezirksgrenzen/) available under the following URLs
 * [bezirksgrenzen/bezirksgrenzen.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/bezirksgrenzen/bezirksgrenzen.geojson) 
 * [lor_prognoseraeume/lor_prognoseraeume.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_prognoseraeume/lor_prognoseraeume.geojson) 
 * [lor_prognoseraeume_2021/lor_prognoseraeume_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_prognoseraeume_2021/lor_prognoseraeume_2021.geojson) 
 * [lor_bezirksregionen/lor_bezirksregionen.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_bezirksregionen/lor_bezirksregionen.geojson) 
 * [lor_bezirksregionen_2021/lor_bezirksregionen_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_bezirksregionen_2021/lor_bezirksregionen_2021.geojson) 
 * [lor_planungsgraeume/lor_planungsraeume.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_planungsgraeume/lor_planungsraeume.geojson) 
 * [lor_planungsgraeume_2021/lor_planungsraeume_2021.geojson](https://tsb-opendata.s3.eu-central-1.amazonaws.com/lor_planungsgraeume_2021/lor_planungsraeume_2021.geojson) 
 
## Data Product Design

**Describe everything you need to design a data product on a conceptual level.**
**Ingestion, storage, transport, wrangling, cleaning, transformations, enrichment, augmentation, analytics, SQL
statements, or used data platform services.**

This data product
* [cleans geojson features](../lib/transform/data_property_cleaner.py) by applying properties such as `id`, `name` and `area` across all files 
* [cleans geoson geometry](../lib/transform/data_geometry_cleaner.py) by removing exclaves (that prevent rendering using map services such as [Mapbox](https://www.mapbox.com/))
* [extends properties](../lib/transform/data_property_extender.py) by adding missing area property 
* [converts geojson coordinate projection](../lib/transform/data_projection_converter.py) to polar coordinates (epsg:4326)
* [calculates a bounding box](../lib/transform/data_bounding_box_converter.py) for each feature based on their coordinates

## Output Ports

**Output ports define the format and protocol in which data can be exposed (db, file, API, visualizations)**

The data of this data product is available under the following URLs
* [berlin-lor-districts/berlin-lor-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts/berlin-lor-districts.geojson)
* [berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson)
* [berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson)
* [berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson)
* [berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson)
* [berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson)
* [berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson)

Additionally, styles to display geojson files in [Mapbox](https://www.mapbox.com/) are available under the following URLs
* [berlin-lor-districts-styles/berlin-lor-districts-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-centroid-symbol-theme-dark.json)
* [berlin-lor-districts-styles/berlin-lor-districts-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-centroid-symbol-theme-light.json)
* [berlin-lor-districts-styles/berlin-lor-districts-fill-marked.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-fill-marked.json)
* [berlin-lor-districts-styles/berlin-lor-districts-fill.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-fill.json)
* [berlin-lor-districts-styles/berlin-lor-districts-line-highlighted.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-line-highlighted.json)
* [berlin-lor-districts-styles/berlin-lor-districts-line.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts-styles/berlin-lor-districts-line.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-fill-marked.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-fill-marked.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-fill.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-fill.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-from-2021-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-from-2021-centroid-symbol-theme-dark.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-from-2021-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-from-2021-centroid-symbol-theme-light.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-line-highlighted.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-line-highlighted.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-line.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-line.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-until-2020-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-until-2020-centroid-symbol-theme-dark.json)
* [berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-until-2020-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-styles/berlin-lor-forecast-areas-until-2020-centroid-symbol-theme-light.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-fill-marked.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-fill-marked.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-fill.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-fill.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-from-2021-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-from-2021-centroid-symbol-theme-dark.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-from-2021-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-from-2021-centroid-symbol-theme-light.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-line-highlighted.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-line-highlighted.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-line.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-line.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-until-2020-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-until-2020-centroid-symbol-theme-dark.json)
* [berlin-lor-district-regions-styles/berlin-lor-district-regions-until-2020-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-styles/berlin-lor-district-regions-until-2020-centroid-symbol-theme-light.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-fill-marked.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-fill-marked.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-fill.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-fill.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-from-2021-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-from-2021-centroid-symbol-theme-dark.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-from-2021-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-from-2021-centroid-symbol-theme-light.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-line-highlighted.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-line-highlighted.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-line.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-line.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-until-2020-centroid-symbol-theme-dark.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-until-2020-centroid-symbol-theme-dark.json)
* [berlin-lor-planning-areas-styles/berlin-lor-planning-areas-until-2020-centroid-symbol-theme-light.json](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-styles/berlin-lor-planning-areas-until-2020-centroid-symbol-theme-light.json)

## Metadata

### Ownership

**Domain, data product owner, organizational unit, license, version and expiration date**

* ownership: Open Lifeworlds
* domain: geodata
* license: CC-BY-4.0

### Schema

**Attributes, data types, constraints, and relationships to other elements**

The files provided within this data product are using the [geojson format](https://geojson.org/). Properties being added or altered are
* `id`: unique feature ID (string)
* `name`: feature name (string)
* `area`: feature area in sqm (float)
* `bounding_box`: feature bounding box (float array)

### Semantics

**Description, logical model**

The files provided within this data product are arranged in the following hierarchy
* districts (Bezirke)
* forecast areas (Prognoseräume)
* district regions (Bezirksregionen)
* planning areas (Planungsräume)

### Security

**Security rules applied to the data product usage e.g. public org, internal, personally identifiable information (PII)
attributes**

## Observability

### Quality metrics

**Requirements and metrics such as accuracy, completeness, integrity, or compliance to Data Governance policies**

Completeness of this data product is verified via [data_metrics.py](../lib/metrics/data_completeness.py).

### Operational metrics

**Interval of change, freshness, usage statistics, availability, number of users, data versioning, etc.**

### SLOs

**Thresholds for service level objectives to up alerting**

## Consumer

**Who is the consumer of the Data Product?**

Consumers of this data product may include
* projects that display LOR area
* other data products that combine geospatial data with statistics data

## Use Case

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used to display data related to LOR areas in Berlin on an interactive map. 

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

This data product is source-aligned since it only makes small adjustments in terms of variable naming, projection and bounding boxes.

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the current Data Product**

* **LOR**: (German: Lebensweltlich orientierte Räume) life-world oriented spaces
* **district**: (German: Bezirk)
* **forecast area**: (German: Prognoseraum)
* **district region**: (German: Bezirksregion)
* **planning area**: a spatial unit whose spatial development is planned by the public authorities

---
This data product canvas uses the template
of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).