# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Private_MC_Mixing'
config.General.workArea = 'DefaultCrab3Area_MC_19_01_1M_miniAOD_NEW_NEW_v2'

config.section_("JobType")
config.JobType.pluginName = 'Analysis' #'PrivateMC'
config.JobType.psetName = 'SUS-RunIISpring16MiniAODv2-00120_1_cfg.py'

config.JobType.maxMemoryMB = 4000

config.section_("Data")
#config.Data.inputDataset = '/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3/MINIAODSIM'  #'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/RAWAODSIM'

########################################### Parent Dataset #######################################
#config.Data.secondaryInputDataset= '/SingleElectron/Run2017F-v1/RAW'
##################################################################################################

#config.Data.inputDBS = 'global'

config.Data.userInputFiles = open('AOD_file_List_NEW_NEW_only_one_mass_point.txt').readlines()

#config.Data.userInputFiles = ['/store/user/pakontax/MC_Production/CRAB_PrivateMC/MC_Production_Test/181009_085352/0000/SUS-RunIISpring16FSPremix-00002_1.root']

config.Data.outputPrimaryDataset = 'T1tttt_MiniAOD_19_01_v2'

#config.Data.runRange = '305236-305250' #'300742-301283'
config.Data.splitting = 'FileBased' #'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 2 #number of events per jobs
#config.Data.totalUnits = 1000000 #number of event
config.Data.outLFNDirBase = '/store/user/pakontax/MC_Production_19_01_1M_miniAOD_NEW' 
config.Data.publication = True
config.Data.outputDatasetTag = 'MC_Production_Test_miniAOD_NEW'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_CH_CERN'

