# CMSData

This is a simple analysis example to compute the spectrum of two muon final state with CMS Open Data.

It is based on the original code in [http://opendata.web.cern.ch/record/5001] on the CERN Open Data portal (Geiser, Achim. Dutta, Irene. Hirvonsalo, Harri. Sheeran, Bridget. (2017). Example code to produce the di-muon spectrum from a CMS 2011 or 2012 primary dataset. CERN Open Data Portal. DOI: 10.7483/OPENDATA.CMS.D00J.UVB1) and modified here for direct download from github. 

The modifications with respect to the original code are the following: 
- the class name has been changed from `DemoAnalyzer` to `cmsdata` in order to avoid conflict for any existing `DemoAnalyzer` plugins in the working area
- the file paths have been modified to be relative in the configuration file, i.e. they point to the `datasets` directory, which is under the directory from where there program will be run.

Run this code in [CMS Open Data VM](http://opendata.web.cern.ch/VM/CMS/2011).

If you have not installed the CMSSW area do the following:
```
cmsrel CMSSW_5_3_32
```
If you already have, start directly with:

```
cd CMSSW_5_3_32/src
cmsenv
```
For this example, you need to create an additional directory, you can call it `cern` or choose another name.
Go to this directory, and download the example code.

```

mkdir cern
cd cern
git clone git://github.com/QuarkNet-HEP/QuarkNet-CMS-Data-Summer-2019/tree/master/cmsdata.git

```
Go to the example directory, and compile with `scram b`. 

```
cd cmsdata
scram b
```

There are no imput files defined in the configuration file 'demoanalyzer_cfg.py' and no files in the 'datasets' directory, so you will need to find a DiMuon data set on cerns opendata website. An example of a good data set is one that is similar to this one: http://opendata.cern.ch/record/17. After you go to this page or find one sililar, you need to download the JSON.txt file and an index file into your datasets directory.

Run the example as configured in the configuration file. 

```
cmsRun demoanalyzer_cfg.py
```
The output of the example is a root file containing several histograms, by default DoubleMu.root with 10000 input events (small subset of data). These can be looked at using a Root Browser.

There's a more detailed description in the cmsdata.cc file.
