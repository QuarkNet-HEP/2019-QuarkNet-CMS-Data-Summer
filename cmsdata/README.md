# DimuonSpectrum2011

This is a simple analysis example to compute the spectrum of two muon final state with CMS Open Data.

It is based on the original code in [http://opendata.web.cern.ch/record/5001] on the CERN Open Data portal (Geiser, Achim. Dutta, Irene. Hirvonsalo, Harri. Sheeran, Bridget. (2017). Example code to produce the di-muon spectrum from a CMS 2011 or 2012 primary dataset. CERN Open Data Portal. DOI: 10.7483/OPENDATA.CMS.D00J.UVB1) and modified here for direct download from github. 

The modifications with respect to the original code are the following: 
- the class name has been changed from `DemoAnalyzer` to `DimuonSpectrum2011` in order to avoid conflict for any existing `DemoAnalyzer` plugins in the working area
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
For this example, you need to create an additional directory, you can call it `WorkDir` or choose another name.
Go to this directory, and download the example code.

```

mkdir WorkDir
cd WorkDir
git clone git://github.com/cms-opendata-analyses/DimuonSpectrum2011.git

```
Go to the example directory, and compile with `scram b`. 

```
cd DimuonSpectrum2011
scram b
```

The input files are defined in the configuration file `demoanalyzer_cfg.py` and are already in the `datasets` directory. This example runs on 2011 data by default, but you also can run it on 2012 data. In this case, download to the the `datasets` directory:
- [the list of validated runs](http://opendata.web.cern.ch/record/1002) for 2012
- the file indexes for the 2012 datasets (go to a file record e.g. [/DoubleMuParked/Run2012C-22Jan2013-v1/AOD](http://opendata.web.cern.ch/record/6030) and download the file index lists).

In order not to overwrite the existing DoubleMu.root, to which you can compare your output, rename it before you run.

Run the example as configured in the configuration file. 

```
cmsRun demoanalyzer_cfg.py
```
The output of the example is a root file containing several histograms, by default DoubleMu.root with 10000 input events (small subset of data). These can be looked at using a Root Browser.

For more detailed information, read the comments in src/DimuonSpectrum2011.cc.
