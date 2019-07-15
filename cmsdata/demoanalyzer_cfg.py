import FWCore.ParameterSet.Config as cms
from RecoMuon.TrackingTools.MuonServiceProxy_cff import *
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
process = cms.Process("Demo")

# intialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
# **********************************************************************
# set the maximum number of events to be processed                     *
#    this number (argument of int32) is to be modified by the user     *
#    according to need and wish                                        *
#    default is preset to 10000 events                                 *
# **********************************************************************
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

# set the number of events to be skipped (if any) at end of file below

# define JSON file for your data (found in GitHub)
goodJSON = 'datasets/YOUR_JSON_FILE_GOES_HERE.txt'

myLumis = LumiList.LumiList(filename = goodJSON).getCMSSWString().split(',')
import FWCore.Utilities.FileUtils as FileUtils
# ****************************************************************************
# define the input data set here by inserting the appropriate .txt file list *
# ****************************************************************************
#
# ****************************************************************
# load the data set                                              *
# useful datasets are DoubleMu (default)            *
# To run over all data subsets, replace '10000' by '10001' etc.  *
# consecutively (make sure you save the output before rerunning) *
# and add up the histograms using root tools.                    *
# ****************************************************************
#
# *** DoubleMu data set ***
filesdata = FileUtils.loadListFromFile ('datasets/YOUR_INDEX_FILE_GOES_HERE.txt')
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(*filesdata
    )
)

# apply JSON file
#   (needs to be placed *after* the process.source input file definition!)
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

# *************************************************
# number of events to be skipped (0 by default)   *
# *************************************************
process.source.skipEvents = cms.untracked.uint32(0)

process.demo = cms.EDAnalyzer('cmsdata'
)
# ***********************************************************
# output file name                                          *
# default is DoubleMu.root                                        *
# change this according to your wish                        *
# ***********************************************************
process.TFileService = cms.Service("TFileService",
       fileName = cms.string('DoubleMu.root')
                                   )


process.p = cms.Path(process.demo)
