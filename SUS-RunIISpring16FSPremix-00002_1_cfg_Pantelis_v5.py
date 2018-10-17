import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('FastSimulation.Configuration.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('HLTrigger.Configuration.HLT_Fake1_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISpring16FSPremix-00002-fragment.py nevts:5760'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fileName = cms.untracked.string('file:SUS-RunIISpring16FSPremix-00002.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)

sourceFile = "my_list_of_files_2.txt"
readFiles = cms.untracked.vstring()
f = open(sourceFile)
fNames = f.readlines()
readFiles.extend(fNames)

process.mixData.input.fileNames = cms.untracked.vstring(readFiles)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v12', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    RandomizedParameters = cms.VPSet( (cms.PSet(
            ConfigDescription = cms.string('T1tttt_1900_100'),
            ConfigWeight = cms.double(17.2413793103),
            GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/sus_sms/SMS-GlGl/SMS-GlGl_mGl-1900_tarball.tar.xz'),
            PythiaParameters = cms.PSet(
                JetMatchingParameters = cms.vstring('JetMatching:setMad = off',
                    'JetMatching:scheme = 1',
                    'JetMatching:merge = on',
                    'JetMatching:jetAlgorithm = 2',
                    'JetMatching:etaJetMax = 5.',
                    'JetMatching:coneRadius = 1.',
                    'JetMatching:slowJetPower = 1',
                    'JetMatching:qCut = 156',
                    'JetMatching:nQmatch = 5',
                    'JetMatching:nJetMax = 2',
                    'JetMatching:doShowerKt = off',
                    '6:m0 = 172.5',
                    'Check:abortIfVeto = on'),
                parameterSets = cms.vstring('pythia8CommonSettings',
                    'pythia8CUEP8M1Settings',
                    'JetMatchingParameters'),
                pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14',
                    'Tune:ee 7',
                    'MultipartonInteractions:pT0Ref=2.4024',
                    'MultipartonInteractions:ecmPow=0.25208',
                    'MultipartonInteractions:expPow=1.6'),
                pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2',
                    'Main:timesAllowErrors = 10000',
                    'Check:epTolErr = 0.01',
                    'Beams:setProductionScalesFromLHEF = off',
                    'SLHA:keepSM = on',
                    'SLHA:minMassSM = 1000.',
                    'ParticleDecays:limitTau0 = on',
                    'ParticleDecays:tau0Max = 10',
                    'ParticleDecays:allowPhotonRadiation = on')
            ),
            SLHATableForPythia8 = cms.string('\nBLOCK MASS  # Mass Spectrum\n# PDG code           mass       particle\n   1000001     1.00000000E+05   # ~d_L\n   2000001     1.00000000E+05   # ~d_R\n   1000002     1.00000000E+05   # ~u_L\n   2000002     1.00000000E+05   # ~u_R\n   1000003     1.00000000E+05   # ~s_L\n   2000003     1.00000000E+05   # ~s_R\n   1000004     1.00000000E+05   # ~c_L\n   2000004     1.00000000E+05   # ~c_R\n   1000005     1.00000000E+05   # ~b_1\n   2000005     1.00000000E+05   # ~b_2\n   1000006     1.00000000E+05   # ~t_1\n   2000006     1.00000000E+05   # ~t_2\n   1000011     1.00000000E+05   # ~e_L\n   2000011     1.00000000E+05   # ~e_R\n   1000012     1.00000000E+05   # ~nu_eL\n   1000013     1.00000000E+05   # ~mu_L\n   2000013     1.00000000E+05   # ~mu_R\n   1000014     1.00000000E+05   # ~nu_muL\n   1000015     1.00000000E+05   # ~tau_1\n   2000015     1.00000000E+05   # ~tau_2\n   1000016     1.00000000E+05   # ~nu_tauL\n   1000021     1.900000e+03           # ~g\n   1000022     1.000000e+02           # ~chi_10\n   1000023     1.00000000E+05   # ~chi_20\n   1000025     1.00000000E+05   # ~chi_30\n   1000035     1.00000000E+05   # ~chi_40\n   1000024     1.00000000E+05   # ~chi_1+\n   1000037     1.00000000E+05   # ~chi_2+\n\n# DECAY TABLE\n#         PDG            Width\nDECAY   1000001     0.00000000E+00   # sdown_L decays\nDECAY   2000001     0.00000000E+00   # sdown_R decays\nDECAY   1000002     0.00000000E+00   # sup_L decays\nDECAY   2000002     0.00000000E+00   # sup_R decays\nDECAY   1000003     0.00000000E+00   # sstrange_L decays\nDECAY   2000003     0.00000000E+00   # sstrange_R decays\nDECAY   1000004     0.00000000E+00   # scharm_L decays\nDECAY   2000004     0.00000000E+00   # scharm_R decays\nDECAY   1000005     0.00000000E+00   # sbottom1 decays\nDECAY   2000005     0.00000000E+00   # sbottom2 decays\nDECAY   1000006     0.00000000E+00   # stop1 decays\nDECAY   2000006     0.00000000E+00   # stop2 decays\n\nDECAY   1000011     0.00000000E+00   # selectron_L decays\nDECAY   2000011     0.00000000E+00   # selectron_R decays\nDECAY   1000012     0.00000000E+00   # snu_elL decays\nDECAY   1000013     0.00000000E+00   # smuon_L decays\nDECAY   2000013     0.00000000E+00   # smuon_R decays\nDECAY   1000014     0.00000000E+00   # snu_muL decays\nDECAY   1000015     0.00000000E+00   # stau_1 decays\nDECAY   2000015     0.00000000E+00   # stau_2 decays\nDECAY   1000016     0.00000000E+00   # snu_tauL decays\nDECAY   1000021     1.00000000E+00   # gluino decays\n    0.00000000E+00    3    1000022     -1    1 # dummy allowed decay, in order to turn on off-shell decays\n    1.00000000E+00    3    1000022     -6    6\nDECAY   1000022     0.00000000E+00   # neutralino1 decays\nDECAY   1000023     0.00000000E+00   # neutralino2 decays\nDECAY   1000024     0.00000000E+00   # chargino1+ decays\nDECAY   1000025     0.00000000E+00   # neutralino3 decays\nDECAY   1000035     0.00000000E+00   # neutralino4 decays\nDECAY   1000037     0.00000000E+00   # chargino2+ decays\n')
        ) ) ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.AODSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq

# customisation of the process.

# Automatic addition of the customisation function from SimGeneral.DataMixingModule.customiseForPremixingInput
from SimGeneral.DataMixingModule.customiseForPremixingInput import customiseForPreMixingInput

#call to customisation function customiseForPreMixingInput imported from SimGeneral.DataMixingModule.customiseForPremixingInput
process = customiseForPreMixingInput(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFastSim

#call to customisation function customizeHLTforFastSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFastSim(process)

# End of customisation functions

# Customisation from command line
process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)

# Customisation from command line
process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)


