QuarkNet CMS Summer 2019
========================

Introduction
------------

This Github page serves to keep all files for the QuarkNet CMS Summer team. The
goal of this project is to make CMS data received from CERN more accessible in
it's native format, ROOT.

**Table of Contents:**

* ROOT

  * `What is ROOT?`_
  
  * `How to Install ROOT`_
  
  * `Basic ROOT Structure`_

* CERNVM

  * `What is CERNVM?`_
  
  * `How to Install and Use CERNVM`_
  
  * `Required Downloads and Methods`_
  
ROOT
====

What is ROOT?
-------------

ROOT is a file format developed and used by CERN to keep large amounts of data
organized and accessible. Each ROOT file serves as it's own directory, keeping
data in objects similar to jagged arrays. It is written and typically used in
C++, but has been integrated into both Python and R.

How to Install ROOT
-------------------

For ROOT `v6.18/00 <https://root.cern/content/release-61800>`_, the version used by our group, the
src can be downloaded using:

 git clone http://github.com/root-project/root.git

An installation guide for ROOT can be found `here <https://root.cern/downloading-root/>`_.

ROOT can be dowloaded and used on any device, however it is more useful when
it is used in CERN's virtual machine, CERNVM.

Basic ROOT Structure
--------------------

ROOT is constructed like a tree. A TTree is a stored in a TFile, and is a collection
of TBranch objects. TBranch data is stored in smaller chunks, called TBaskets.

These files can be opened in order to read and write, which is most often done via
the TFile constructor.

More information on opening, writing, and creating ROOT files can be found `here <https://root.cern.ch/root-files/>`_.

CERNVM
======

What is CERNVM?
---------------

`CERNVM <https://cernvm.cern.ch/>`_ is a virtual machine running Scientific Linux 7, which is used to analyze data
recieved from CMS. It is required to use CERNVM with these programs, as many of the
methods used only work on Scientific Linux 7. 

How to Install and Use CERNVM
-----------------------------

First and foremost, `VirtualBox 5.2.2 <https://www.virtualbox.org/wiki/Download_Old_Builds_5_2/>`_ is needed to run CERNVM.

Once VirtualBox is installed, CERNVM

