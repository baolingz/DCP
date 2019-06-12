### Common Name

NYC Facilities Database

   
### SDE Name

FacDB

   
### Tags for Guide

Facilities Database, FacDB, Health and Human Services, Education, Child Welfare, Parks, Gardens, Historical Sites, Libraries and Cultural Programs, Public Safety, Emergency Services, Administration of Justice, Core Infrastructure and Transportation, Government Administration

   
### Tags for SDE

Facilities Database, FacDB, Health and Human Services, Education, Child Welfare, Parks, Gardens, Historical Sites, Libraries and Cultural Programs, Public Safety, Emergency Services, Administration of Justice, Core Infrastructure and Transportation, Government Administration

   
### Summary

The City Planning Facilities Database aggregates more than 35,000 records from 52 different public data sources provided by City, State, and Federal agencies.

   
### Summary - Update Date

20190610

   
### Description

While each source agency classifies its facilities according to their own naming systems, we have grouped all facilities and program sites into the following seven categories to help planners navigate the data more easily: 
* Health and Human Services * Education, Child Welfare, and Youth
* Parks, Gardens, and Historical Sites * Libraries and Cultural Programs
* Public Safety, Emergency Services, and Administration of Justice
* Core Infrastructure and Transportation
* Administration of Government 

Within each of these domains, each record is further categorized into a set of facility groups, subgroups, and types that are intended to make the data easy to navigate and more useful for specific planning purposes. Facility types and names appear as they do in source datasets, wherever possible. A full listing of the facility categories is provided in the data dictionary.

   
### Description - Data Location

NYC Facilities Explorer (Capital Planning Platform), BYTES of the BIG APPLE, MDrive

   
### Data Steward

ITD - Data Engineering

   
### Data Engineer

Amanda Doyle, Baiyue Cao, Baoling Zhou, Bennett Norman

   
### Credits

DCP, DOT, DSNY, HRA, NYPL, NYSED, NYSOPRHP, SBS, HHC, DYCD, NYCHA, NYCDOE, NYSDEC, QPL, NYCDOE, DoiTT, NYSOMH, DCAS, DCLA, NYSOPWDD, BPL, USNPS, DPR, NYSDOH, DCA, DFTA, DOHMH, MOEO, USCOURTS, NYSOASAS, NYSDOCCS, NYCOURTS, NYCDOC, ACS, AMTRAK, BBPC, HRPT, MTA, NYSDOT, PANYNJ, TGI, RIOC

   
### General Constraints Use Limitations

The facilities database is being provided by the Department of City Planning (DCP) on the GitHub website for informational purposes only. DCP does not warrant the completeness, accuracy, content, or fitness for any particular purpose or use of the dataset, nor are any such warranties to be implied or inferred with respect to the dataset as furnished on the website

   
### Legal Constraints Use Limitations

DCP and the City are not liable for any deficiencies in the completeness, accuracy, content, or fitness for any particular purpose or use of the dataset, or applications utilizing Dataset, provided by any third party. The City Planning Facilities Database (FacDB) is only as good as the source data it aggregates, and the Department of City Planning cannot verify the accuracy of all records. Please read more about specific data and analysis limitations before using this data.

   
### Update Frequency

biannually

   
### Date of Last Update

20190630

   
### Date of Underlying Data
Varies by dataset
   
### Data Sources and Compilation Process

Since the facility records are aggregated from many datasets designed for different purposes, the data will be transformed over several stages to reach its final state. The stages are described below and all the scripts used are available on the [NYC Planning GitHub page](https://github.com/NYCPlanning/db-facilities-tmp). 

**Data loading.** Since the source datasets have been maintained by various agencies and updated with different frequencies, datasets will be loaded into Amazon s3 as a centralized datahub preparing for the downstream data processing. 

**Geoprocessing.** Many source datasets only provide addresses without coordinates. Records without coordinates are geocoded with the [GeoClient API](https://developer.cityofnewyork.us/api/geoclient-api) using the Address and either the Borough or ZIP Code to get the BIN, BBL, and other standardized location details. If the record can be assigned a BIN value, the BIN's centroid is used as the point geometry. Source records with only coordinates and no addresses are processed will be geocoded by their source coordinates. There are many cases where an agency provides coordinates but the coordinates they provided fall in the roadbed, and not inside a BBL boundary, due to the geocoding technique used by the source. In these cases, the geometry was replaced with the BBL centroid if a BIN could not be assigned and used for the geometry instead. Each record in the database is flagged with a code for the geoprocessing technique that was used to complete all of its information. 

**Duplicate Record Removal.** Several of the source datasets have content that overlaps with other datasets. Duplicate records were identified by querying for all the records that fall within the same BIN or BBL and have the same Facility Subgroup or Type, same Facility Name, or same Oversight Agency. The values from the duplicate records were merged before dropping the duplicate records from the database.

   
### Version
N/A
   
### Common Uses
Fair Share Analysis
   
### Data Quality

This database and its [interactive map](http://capitalplanning.nyc.gov/facilities) build upon and replace City Planning’s decades-old work on the Selected Facilities and Program Sites Database. Improvements include more facility types, improved data quality, and a restructured database for easier use. We have also automated our data-update processes for the majority of sources. Please read more about the Caveats.

   
### Caveats

**Analysis Limitations.** As a result of the data limitations and inconsistencies listed below users should be careful in their use of this database so as to avoid developing suspect analyses. For example, a comparison of the density or accessibility of facilities across neighborhoods should recognize that some of the facilities included are organizational headquarters rather than service sites and that this database is not authoritatively comprehensive. In addition, we rely on source data from other agencies to populate the database, and some of these sources may fall out-of-date. Users can find the date of each source dataset’s latest update in the source data dictionary. 

**Missing Records.** Currently, FacDB is the most comprehensive spatial data resource available for facilities run by public and non-public entities in NYC, but it does not claim to capture every facility within the specified domains. Some facilities are deliberately excluded from the data that source agencies provide in order to protect the safety and privacy of their clients. Also, many records could not be geocoded. To learn more about how the data are processed, please review the Methodology. 

**Duplicates.** Please be aware that this beta version of the database includes cases of duplicate records for the same facility because several source datasets have content that overlaps with other datasets. 

**Administrative Addresses.** There are known to be cases when the address provided in the source data is for a headquarters office rather than the facility site location. Unfortunately, these could not be systematically verified. For more detailed information on a specific facility reach out to the respective oversight agency. 

**Public Accessibility of Sites.** DCP is unable to verify the public accessibility of all sites. For example, some playgrounds or playing fields may only be accessible to participants in certain programs.

   
### Future Plans
N/A
   
### Distribution

Public

   
### Contact

If you have any questions about or comments on these data please contact the NYC DCP Capital Planning team at [Capital@planning.nyc.gov](mailto:Capital@planning.nyc.gov).

   