# Maltego EXIFTool Transform

A basic Maltego local transform for Phil Harvey's mighty EXIFTool application. 

## Getting Started

Maltego can offer a way to quickly visualize meta data extracted across multiple files. The content of some of that extracted data can also be dovetailed into other transforms within the Maltego environment. For example, coordinates extracted from an image could then form the input to transforms that search geotagged social media. 

Rather than building my own GUI for EXIFTool, or using those that already exist, I decided to experiment with wrapping the application's basic functionality into a simple python-based transform script for Maltego.   

![Example of transforms in action](/doc/exif.png)

### Prerequisites

This transform is written in Python 2.7.

This transform acts as a very basic wrapper for EXIFTool, a command line application. You will need to have EXIFTool installed locally in order to use this transform. 

The EXIFTool application supports reading meta data from a vast range of different file types, not only JPG, TIFF and image file formats. [Read more here](http://owl.phy.queensu.ca/~phil/exiftool/#supported).

The transform uses the python *subprocess* module to call EXIFTool from the command line. 

You'll need the following Python module installed too if you don't already have it:

```
from bs4 import BeautifulSoup
```
and

```
import MaltegoTransform
```

This last module import is the Maltego python transform library. You can grab a copy from the [Maltego developer site](https://docs.maltego.com/helpdesk/attachments/2015007304961). 

### Installing

Download and install EXIFTool from [Phil Harvey's Webpage](http://owl.phy.queensu.ca/~phil/exiftool/). 

If you don't have *BeautifulSoup* it can easily be installed as follows:

```
pip install BeautifulSoup4
```

Configure this local transform in Maltego, [see the Configuration Guide](https://docs.maltego.com/support/solutions/articles/15000010781-local-transforms). In short, you'll need to link the transform to specific entity types and point Maltego to both your local Python installation and your local copy of this transform script. 

## Running the Transform

The EXIFTool transform can be run like any other local transform in Maltego. However, the transform will return items of meta data as a custom entity type named *maltego.MetaData*. You can install this custom entity via the .mtz (and the Maltego *Import Entities* function) in the entities directory, create your own or recode to use one of the standard Maltego entity types.

I also created a custom *maltego.LocalFile* entity which this transform would be run from. The value of this entity is simply the local filepath to a document, image or other file that I want EXIFTool to extract meta data from.

## Built With

* [Python](http://www.python.org)
* [EXIFTool by Phil Harvey](http://owl.phy.queensu.ca/~phil/exiftool/#supported)
* [BeautifulSoup's HTML Parser](https://www.crummy.com/software/BeautifulSoup/)
* [Maltego Local Python Library](https://docs.maltego.com/support/solutions/articles/15000019558-python-local-library-reference)

## Authors

* **Andrew Houlbrook** - *Initial work* - [ba2baha3o](https://github.com/ba2baha3o)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
