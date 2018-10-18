import csv
import os
#import das_client
import sys
import imp
import ssl
import Utilities.General.cmssw_das_client as das_client

ssl._create_default_https_context = ssl._create_unverified_context

#das_client=imp.load_source("das_client", "/cvmfs/cms.cern.ch/slc6_amd64_gcc530/cms/das_client/v02.17.04/bin/das_client.py")

crab_cfg_path='ZPrime_MC_studies_with_syst'
ZPrime_MC_studies_tWb=sys.argv[1]

csvfile=open(ZPrime_MC_studies_tWb,'r')
reader = csv.DictReader(csvfile, delimiter=',')#, quotechar='|')
if not os.path.exists(crab_cfg_path):
    os.makedirs(crab_cfg_path)
for row in reader:
    dataset="'"+row['dataset']+"'"
    name=row['name']
    weight=row['weighting on 1fb-1']
    generator=row['generator']
    isData=row['isData']
    isBoostedMiniAOD=row['boosted_dataset']
    #makeSystematicsTrees=row['makeSystematicsTrees']
    globalTag=row['globalTag']
#    if len(dataset)>r3:
#        requestname="'"+(dataset.split('/')[1])+"'"
    if dataset!='' and name!='':
        print 'checking dataset info for',dataset
        #ckey=das_client.x509()
        #cert=das_client.x509()
        #das_client.check_auth(ckey)
        #das_data=das_client.get_data("https://cmsweb.cern.ch","dataset="+dataset+" instance=phys/prod",0,0,0,300,ckey,cert)
        das_data=das_client.get_data("file dataset="+dataset+" instance=phys/prod")
        #print das_data
        #for d in das_data['data']:
	    ##print d
            #for dd in d['dataset']:
	        ##print dd
                #print dd['mcm']['nevents']


        outfilename=crab_cfg_path+'/crab_'+name+'.py'
        if os.path.exists(outfilename):
            for i in range(2,10):
                outfilename=crab_cfg_path+'/crab_'+name+'_v'+str(i)+'.py'
                if not os.path.exists(outfilename):
                    break
        crabout=open(outfilename,'w')
        crab_template=open('crab_cfg_BoostedAnalyserWithCrabs.py','r')
        for line in crab_template:
            if 'config.Data.inputDataset' in line:
                crabout.write('config.Data.inputDataset = '+dataset+'\n')
            elif 'config.General.requestName' in line:
                crabout.write('config.General.requestName = "'+name+'"\n')
            elif 'config.JobType.outputFiles' in line:
                crabout.write('config.JobType.outputFiles = ["'+name+'_nominal_Tree.root", "'+name+'_nominal_Cutflow.txt", "'+name+'_JESup_Tree.root", "'+name+'_JESup_Cutflow.txt", "'+name+'_JESdown_Tree.root", "'+name+'_JESdown_Cutflow.txt", "'+name+'_JERup_Tree.root", "'+name+'_JERup_Cutflow.txt", "'+name+'_JERdown_Tree.root", "'+name+'_JERdown_Cutflow.txt"]\n')
            elif 'config.JobType.pyCfgParams' in line:
                crabout.write("config.JobType.pyCfgParams = ['outName="+name+"','weight="+weight+"','isData="+isData+"','isBoostedMiniAOD=False','systematicVariations=nominal,JES,JER','LeptonChannel=veto','maxEvents=9999999999','globalTag="+globalTag+"','generatorName="+generator+"']\n")
            elif 'config.Data.outputDatasetTag' in line:
                crabout.write("config.Data.outputDatasetTag = 'MC_limits_"+name+"'\n")
            else:
                crabout.write(line)
        crab_template.close()
        crabout.close()
