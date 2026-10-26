---
layout: default
title: Geospatial Data Deposit
parent: Deposit in UBC Borealis
has_children: false 
nav_order: 4
---
# Geospatial Deposits into UBC Borealis

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>


## What is "geospatial data"?

Data sets that explicitly contain some sort of precision location elements are often titled "geospatial data" as they, as the name implies, tie a data point to a specific place. Normally, but not always, this is a place on the Earth, and geospatial data formats often involve mapping of some kind. If the words "Shapefile", "GeoJSON" or "GeoTIFF" mean anything to you, then you've probably already worked with geospatial data.

For data sets containing geospatial data, data management is slightly more complex than an [ordinary data deposit](05-1_Basic_Deposit.md), but hopefully not overwhelmingly so. The general principles are the same, but there are a few wrinkles unique to geospatial data.

In short, if you can map your data, it's (probably) geospatial data.

## Dataset Metadata

Geospatial data may require a bit of extra attention to make it more useful and findable. The first steps are identical to the [basic deposit](05_1_Basic_Deposit.md), but it continues on from there.

Once you've done the initial step of creating your dataset page, you'll need to enhance it by selecting **Edit Dataset/Metadata**. Once you've done this, you'll see that there are many more fields that you can fill in. In an ideal world, you would fill in as many as you can in as much detail as you can, but for geospatial data there is one section of particular importance, unsurprisingly titled the **Geospatial Metadata** block.

For geospatial data sets, it's crucial to identify the region your data represents, as that's one of the most important reasons for its existence. In addition to describing your data set, this block also allows people to search for your data set using a map in places that harvests your dataset's metadata, such as at <https://www.lunaris.ca/>.

The geospatial metadata block has repeating fields, and you should fill out their contents as completely as possible. The fields are repeating, so if you have files which describe different locations you can do that too. Here is an overview of the options available in the geospatial metadata block.

### Geographic coverage

This is relatively straightforward. Fill in this block to the most detailed level you can using the existing options. For example, if your data represents British Columbia, you would fill out:

* Country: Canada
* State/Province: British Columbia


### Geographic Unit

This represents the *smallest* unit available in your geospatial file(s). For example, if you have a geodatabase which contains municipalities and neighbourhoods in BC, this entry would only contain "neighbourhoods".

### Geographic Bounding Box

If you have this information, this is the most crucial field to fill out.  Entries in these fields are in are in decimal degrees, which are *not necessarily* the units of the geospatial file. For example, projected data often uses metres, which is not suitable for entry here. The values to use are the bounds for the extent of the file or data set.

Obviously, this section can only be filled out if you are using the Earth for your data. If you're mapping the geology of Mars, then these fields can't be filled out. Well, they can, but it won't necessarily make any sense, because most finding aids that use this data assume that they refer to the Earth.

### Notes

Anything of importance that doesn't fit into these fields should be put into the *Notes* field in the **Citation Metadata** block. Things that you may wish to place in that block include, but are not limited to:
    
* Projection (eg: EPSG:3157: NAD83(CSRS) / UTM zone 10N)
* Datum (eg: WGS84)
* Other information: (eg: Pixel values represent height above mean sea level).

The notes field accepts HTML; if you need to format it for readability please feel free to add some basic HTML tags, the most important of which is the paragraph tag: `<p>`. Enclose paragraphs like this `<p> Your content here </p>`. Multiple lines are completely fine.

## The README file

For geospatial data, all of the concepts outlined in [how to create a README file](03_create_readme.md) still hold true. But because geospatial files are usually more complex than other types of data you should, at a minimum:

1. **Make sure that *all* of the attributes of your vector data are clearly defined in a data dictionary. Each column in an attribute table should have a corresponding entry in your README's data dictionary, even if it appears obvious.** If your raster data has an attribute table this also applies. 

    Raster values should be clearly defined; ie. The what the pixel value represents must be clearly stated.
    
    This is _not_ an optional step.

2. Define all abbreviations. While it may seem that NDVI, NIR, and GLONASS are obvious, to researchers and others outside your field they may not be. When using abbreviations, clearly define them the first time they are used: eg. NIR (near infrared).

3. Include projection information for each geospatial data file; do not assume that other users will access your data with GIS software.

4. Geospatial data is widely used because it's easy to map, so knowing how and when it can be used is very important. Make sure to include licence information inside your README.

A good way to think about what you should include in your README file is to imagine that someone has sent you some data that you have never seen before, on a topic that you know only a little about. Think about what is required to understand it fully, to use it for analysis, what any restrictions for publication are, and how to cite it. Your documentation should answer all of those questions.

**The importance of a README for geospatial cannot be overstated**. Describe as much as you can in as much detail as you can. It not only help others, it will help _you_ when you inevitably return to the data set six weeks, six months or six years down the line. **If your README does not contain sufficient information, your study will be returned to you by the data curators until it does**.

Of course, if you really want to have excellent documentation, you could include everything that's required for [ISO-19115 or FGDC metadata standards](https://www.fgdc.gov/metadata/iso-standards). Geospatial metadata is very complex and there are a variety of editors you can use to help you with it if you decide to have this style of metadata.

ISO-style metadata is often in the form of an XML file with the same name as a shapefile. If you have XML metadata of this type, you can either store it with the data itself or separately, according to your preference. You should make sure that the README indicates this.

## Types of Geospatial Data Files

Generally speaking, geospatial data comes in two flavours:

**Vector data:** Mathematically defined data, such as polygons, lines, points, etc. Material like and Adobe Illustrator drawing or a CAD drawing, but with geographic information included.

**Raster data:** Data in which pixel values are mapped to a particular location. This doesn't have to be colour pixels; the pixel values can present anything (like height, for example). This *can* include imagery, but is not necessarily picture-like imagery. A pixel represents an area on the Earth or other location, like a 20 m x 20 m square.

### Considerations for Geospatial Data

Like other kinds of data, geospatial data comes in a wide variety of formats. For preservation purposes, open standards are preferred. However, if you must use a proprietary format, consider using one that is well supported that doesn't require proprietary software.

In addition, because of the complexity of geospatial data or because of data storage formats, it's not always possible to store data in a single file. Where it's not possible to store everything in one file, consider compressing the files into a single file.

To give a very common example of this problem, consider the [shapefile](https://en.wikipedia.org/wiki/Shapefile). A shapefile is not:

* a single file; it is comprised of multiple files which can vary in number depending on the data
* open source. It is a proprietary format developed by Esri Inc.

This would seem to disqualify it as a useful format for data deposits. However, because the shapefile has been around for so long and is such a common interchange format, it's widely used and has become a _de_facto_ sharing standard because of its ubiquity.

### File Formats

There are very many types of geospatial data files and it would be fruitless to discuss them all. The formats discussed below are listed because of one or more of the following:

* Common file formats
* Ease of preservation
* Open standard

While these data types may be _preferable_ for inclusion into UBC's collections, the needs of research come first. It is better to use a different, less common file format than to use another which leads to data loss. For a look at the vast variety of formats available for geospatial data, have a look at these non-exhaustive lists for [vector](https://gdal.org/drivers/vector/index.html) and [raster](https://gdal.org/drivers/raster/index.html) data formats.

### Vector Formats

#### GeoJSON

**Advantages**

* Open source standard
* Text only
* Easily preserved

**Disadvantages**

* Text format files can be very large
* GeoJSON standard requires that data be in **WGS84 only**
* Previews require that the data file be uncompressed

#### Shapefile

**Advantages**

* Very commonly used
* Previews of data may be available
* Borealis can handle compressed shapefiles in .zip format

**Disadvantages**

* Shapefiles contain multiple files and the number required may vary
* Attribute names are limited to 8 characters
* Unsuitable for large data sets
* Proprietary

#### Geopackage

* Open source standard based on the open-source SQLite database, which stores everything in a single file
* Multiple geometries and tables can be stored in a single geopackage
* It's a database, so many SQL (structured query language) functions are available as well
* Very preservation friendly

**Disadvantages**

* No preview available
* Not all that well supported in ArcGIS
* Not all features (ie, rasters) supported in all GIS software

#### Spatialite

**Advantages**

* As Geopackage
* Spatial queries are easier than Geopackages

**Disadvantages**

* Somewhat less support than Geopackage

### Raster Formats

#### GeoTIFF

GeoTIFFs are the _de facto_ standard for image distribution

**Advantages**

* Ubiquitous
* Uncompressed images can have previews displayed in Borealis
* Well suited for preservation

**Disadvantages**

* Like shapefiles, they have multiple components, up to five, and in that case they should be compressed into one file

#### NetCDF

**Advantages**

* Supported by Borealis
* Open standard, so preservation friendly
* Can support time series data

**Disadvantages**

#### Geospatial PDF

**Advantages**

* Preservation friendly

**Disadvantages**

* No write support
* Relatively uncommon

#### Esri ASCII GRID Raster

**Advantages**

* Plain text
* Relatively common
* Easily preserved
* Open standard

**Disadvantages**

* Coordinate system information is not included in the raster header
* Easily confused with Esri proprietary binary grid raster

### Combined Formats

Databases can (usually) store *both* vector and raster formats simultaneously. They have the advantages of both spatial files plus the SQL features of a database, which makes them very nice to work with.

#### Esri File Geodatabase

**Advantages**

* Very common because of the ubiquity of Esri products
* All files stored in hierarchically in a directory
* Many GIS software packages can read them

**Disadvantages**

* Proprietary
* Must be uploaded as a compressed file which preserves directory structure and hierarchy
* Not all features are available in software other than Esri's because of its proprietary nature
* Open source software may have limitations in reading stored rasters

#### Geopackage and Spatialite

**Advantages**

* As above in the [vector formats](#vector-formats) section

**Disadvantages**

* Raster support is not as full as in an Esri file geodatabase
* Not particularly well supported in Esri products

Using a database does not exempt you from making a complete data dictionary. If you are using a database, every object in it should be as completely described as if it were a standalone data package.

### Structuring Your Geospatial Data Deposit

Because a geospatial data "file" is often comprised of more than actually one file, greater care needs to be taken when packaging your data for upload.

There are a few options

1. Compressing everything into a single file.
    
    **This is least desirable option.** It is simple (ie, you've just zipped up a whole directory), but it has many disadvantages. It can't be easily preserved and it can't be previewed. Contents are difficult, if not impossible, to describe in the file metadata section. Users must download everything at once, even if they don't want to.
    
2. Compressing single files while retaining the relative hierarchy within the compressed file. For example, you have a file like this:
    ```
    .
    └── Data
        └── Specialized Data
             ├── appropriately_named_file.dbf
             ├── appropriately_named_file.prj
             ├── appropriately_named_file.qpj
             ├── appropriately_named_file.shp
             └── appropriately_named_file.shx
    ```
    
    You can compress this, retaining the directory structure (perhaps as `appropriately_named_files_shp.zip`). When downloaded and uncompressed, the intermediate directories will be automatically created.
        
    
3. Instead of the example above, you can descend to the "Specialized Data" directory and compress the files with no directory structure. Instead of keeping the hierarchy in the compressed file, you would instead add it to the **File Path** metadata. This means if users download the file and uncompress it, there would be no included directory structure, ie `appropriately_named_file.shp` and its companions would be wherever the user wanted.

    If the user decided to download all the files in the study as a zip file (by selecting multiple files and downloading), the result, when the end user unzipped the download would be:

    ```
    .
    └── Data
        └── Specialized Data
             └── appropriately_named_file_shp.zip
    ```

Of course, if you have no hierarchical structure, this doesn't really matter.

None of these approaches is better than the other. If your data set requires a particular structure **you should note that in the README file**.

---
  
Because you are normally concerned with a *data* upload, normally you would *not* include saved project from something like QGIS or ArcGIS. If you *do* need to include the saved project file, ensure that the project file uses **relative** paths to the data (ie, in relation to the saved project file) because users will not have the same drive structure. Most importantly, *you must note this in your README file*

### Uploading/Depositing Your Geospatial Data

Now that you've documented, cleaned, and compressed your data and got it ready to go, it's time to upload. You'd think this part would be straightforward!

The [Basic Deposit](05-1_Basic_Deposit.md) section of this guide mentioned zipfiles, double-zipping, and other strategies. Naturally these all go out the window when working with shapefiles. In essence, you *don't* have to double-zip shapefiles, or even _groups_ of shapefiles. For more details on how this works, please have a look at [How Dataverse Ingests Shapefiles](https://borealisdata.ca/guides/en/latest/developers/geospatial.html). Machine processing can introduce unexpected errors, though. For best results consider structuring shapefiles as noted above. If you're not getting what you want, force what you want by double-zipping your shape files. 

For other common formats:

* GeoJSON : don't zip
* GeoTIFFs: if it's a single file and you want a preview, don't zip. Otherwise, double-zip
* NetCDF: for automatic metadata extraction, don't zip. To save as a zip file, double-zip
* Zip files: If you want something other than the above to remain a zip file, double-zip 

See, straightforward!

## Getting Help with Geospatial Data Deposits

If you've gotten this far, you've already noticed that this section is much longer than the others, and it's just the "basic" guide. If you have questions, don't hesitate to [contact us for help](mailto:research.data@ubc.ca).
