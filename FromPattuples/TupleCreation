## This file is part of pattuples2011.
## Copyright (C) 2014  Instituto de Fisica de Cantabria and CERN.
## Copyright (C) 2016  Helsinki Institute of Physics and CERN

## pattuples2011 is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## pattuples2011 is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with pattuples2011. If not, see <http://www.gnu.org/licenses/>.

## import skeleton process
from PhysicsTools.PatAlgos.patTemplate_cfg import *

## ------------------------------------------------------
#  NOTE: you can use a bunch of core tools of PAT to
#  taylor your PAT configuration; for a few examples
#  uncomment the lines below
## ------------------------------------------------------
from PhysicsTools.PatAlgos.tools.coreTools import *
removeMCMatching(process, ['All'])

## remove certain objects from the default sequence
removeAllPATObjectsBut(process, ['Muons','Electrons'])

# make sure to keep the created objects
process.out.outputCommands += ['keep *_offlinePrimaryVertices_*_*']
process.out.outputCommands += ['keep *_pat*_*_*',]

## let it run
process.p = cms.Path(
   process.patDefaultSequence
   )

## ------------------------------------------------------
#  In addition you usually want to change the following
#  parameters:
## ------------------------------------------------------
#
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db')
process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'

#luminosity
import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
myLumis = LumiList.LumiList(filename='Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt').getCMSSWString().split(',')
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)

#input file
import FWCore.Utilities.FileUtils as FileUtils
files2011data = FileUtils.loadListFromFile ('CMS_Run2011A_DoubleElectron_AOD_12Oct2013-v1_20000_file_index.txt') 
readFiles = cms.untracked.vstring( *files2011data )
process.source.fileNames = readFiles

#process.maxEvents.input = -1                                  ##  (e.g. -1 to run on all events)
process.maxEvents.input = 1000                               ##  (e.g. -1 to run on all events)
#output file
process.out.fileName = 'file://Electron_PAT_data_500files_1.root' ##  (e.g. 'myTuple.root')
