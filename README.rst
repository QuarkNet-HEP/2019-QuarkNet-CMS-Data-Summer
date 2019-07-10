QuarkNet CMS Summer 2019
========================

Introduction
------------

This Github page serves to keep all files for the QuarkNet CMS Summer team. The
goal of this project is to make CMS data received from CERN more accessible in
it's native format, ROOT.

**Table of Contents:**

* ROOT

  * `What is ROOT`_
  
  * `How to Install`_
  
  * `Basic ROOT Structure`_

ROOT
====

What is ROOT
=============

ROOT is a file format developed and used by CERN to keep large amounts of data
organized and accessible. Each ROOT file serves as it's own directory, keeping
data in objects similar to jagged arrays. It is written and typically used in
C++, but has been integrated into both Python and R.

How to Install
==============

An installation guide for ROOT can be found `here <https://root.cern/downloading-root/>`_.

ROOT can be dowloaded and used on any device, however it is more useful when
it is used in CERN's virtual machine, CERNVM.

Basic ROOT Structure
====================

ROOT is constructed like a tree. A TTree is a stored in a TFile, and is a collection
of TBranch objects. TBranch data is stored in smaller chunks, called TBaskets.

These files can be opened in order to read and write, which is most often done via
the TFile constructor.

More information on opening, writing, and creating ROOT files can be found _`here <https://root.cern.ch/root-files/>`_.



