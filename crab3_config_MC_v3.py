# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Private_MC_Mixing'
config.General.workArea = 'DefaultCrab3Area_MC_19_01_1M_19_01'

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'SUS-RunIISpring16FSPremix-00002_1_cfg_Pantelis_v5.py'

config.JobType.maxMemoryMB = 4000

config.section_("Data")
#config.Data.inputDataset = '/DYToEE_NNPDF30_13TeV-powheg-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v3/MINIAODSIM'  #'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16DR80-FlatPU28to62HcalNZSRAWAODSIM_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/RAWAODSIM'

########################################### Parent Dataset #######################################
#config.Data.secondaryInputDataset= '/SingleElectron/Run2017F-v1/RAW'
##################################################################################################

config.Data.inputDBS = 'global'

#config.Data.userInputFiles = list(open('my_list_of_files.txt'))

#config.Data.runRange = '305236-305250' #'300742-301283'
config.Data.splitting = 'EventBased'#'EventAwareLumiBased'
config.Data.unitsPerJob = 1000 #number of events per jobs
config.Data.totalUnits = 1000000 #number of event
config.Data.outLFNDirBase = '/store/user/pakontax/MC_Production_19_01' 
config.Data.publication = False
config.Data.outputDatasetTag = 'MC_Production_Test_19_01'
#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
# json with 3.99/fb

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'

