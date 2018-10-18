from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = ?
config.General.workArea = 'ZPrime_studies_with_syst'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = '/afs/cern.ch/user/s/skudella/CMSSW_8_0_12/src/BoostedTTH/BoostedAnalyzer/test/mkVLQ_jettoolbox_trees_2016_cfg.py'
config.JobType.psetName = '/afs/cern.ch/user/s/skudella/CMSSW_8_0_26_patch2/src/BoostedTTH/BoostedAnalyzer/test/Zprime_ntuples_new_cfg.py'

config.JobType.maxMemoryMB = 3000
#config.Site.blacklist = ['T2_US_*']

config.JobType.outputFiles = ?
config.JobType.pyCfgParams = ?
#config.JobType.inputFiles = ['/nfs/dust/cms/user/asaibel/CMSSWProjects/CMSSW_7_6_3/src/TTH/MEIntegratorStandalone/root']


config.section_("Data")
config.Data.inputDataset = ?
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
#config.Data.totalUnits = 1
#config.Data.publishDbsUrl = 'phys03'
config.Data.outputDatasetTag = ?

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
