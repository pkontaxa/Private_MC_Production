# Private_MC_Production
Set of commands on how to produce Private MC production for T1tttt SUSY mass points

### Install instructions
```
cmsrel 
CMSSW_8_0_5_patch1
cd CMSSW_8_0_5_patch1/src
git clone https://github.com/pkontaxa/Private_MC_Production
scram b -j 16
```

### Producing MC Events in AOD Format
Use this command to generate the cfg file from fragment:
```
cmsDriver.py Configuration/GenProduction/python/SUS-RunIISpring16FSPremix-00002-fragment.py --fileout file:SUS-RunIISpring16FSPremix-00002.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISpring16FSPremix-PUSpring16_80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent AODSIM --fast --customise SimGeneral/DataMixingModule/customiseForPremixingInput.customiseForPreMixingInput,Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions 80X_mcRun2_asymptotic_v12 --beamspot Realistic50ns13TeVCollision --customise_commands "process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)" --step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO,HLT:@fake1 --datamix PreMix --era Run2_25ns --python_filename SUS-RunIISpring16FSPremix-00002_1_cfg.py --no_exec -n 5760
```

!Note! : Due to the problem with the Neutrino Gun Dataset (https://hypernews.cern.ch/HyperNews/CMS/get/computing-tools/4235/1/1/1.html) one way to by-pass this is to use directly the file "list_of_files_Neutrino_Gun_80X.txt" inside the cfg file, before submitting jobs to crab. After submitting CRAB jobs, the system will find the relevant dataset automatically.
