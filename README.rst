QuarkNet CMS Summer 2019
========================

Introduction
------------

This Github page serves to keep all files for the QuarkNet CMS Summer team. The
goal of this project is to make CMS data received from CERN more accessible in
it's native format, ROOT.

Note that each project (.csv file & ROOT file projects) have their own README, and act as standalone programs.

The recommended order to go through this page is the .csv project, then Outreach2011, then pattuples2011. This will introduce you to all concepts covered in our written program.

**Table of Contents:**

* ROOT

  * `What is ROOT?`_
  
  * `How to Install ROOT`_
  
  * `Basic ROOT Structure`_

* CERNVM

  * `What is CERNVM?`_
  
  * `How to Install and Use CERNVM`_
  
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

For `ROOT v6.18/00 <https://root.cern/content/release-61800>`_, the version used by our group, the
src can be downloaded using:

 git clone http://github.com/root-project/root.git
 
An installation guide for ROOT can be found `here <https://root.cern/downloading-root/>`_.

ROOT uses CMake as a build-generator, a process defined `here <https://root.cern/building-root>`_.

ROOT can be dowloaded and built on any device, however it is more useful when
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

`CERNVM <https://cernvm.cern.ch/>`_ is a virtual machine running Scientific Linux 7,
which is used to analyze data recieved from CMS. It is required to use CERNVM with 
these programs, as many of the methods used only work on Scientific Linux 7. 

How to Install and Use CERNVM
-----------------------------

First and foremost, `VirtualBox 5.2.2 <https://www.virtualbox.org/wiki/Download_Old_Builds_5_2/>`_ is needed to run CERNVM.

Once VirtualBox is installed, CERNVM's most recent vm image can be downloaded `here <http://cernvm.cern.ch/portal/downloads>`_. 
Open the image file with VirtualBox to start the virtual machine.

The first step to using CERNVM is to download the CMS software package. This package 
includes the commands to start using root and run programs in the CMS console.
The following commands download CMSSW and load the software to run programs:

.. code-block:: bash

    cmsrel CMSSW_5_3_32 
    cd CMSSW_5_3_32/src
    cmsenv
 
Note that every time you open a terminal in CERNVM or reload the linux kernel, you **have** to enter cmsenv in the src directory before entering commands.
