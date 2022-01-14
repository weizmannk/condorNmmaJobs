import numpy as np
import os

#datapath = os.getcwd()+'/'

events = np.loadtxt('/home/weizmann.kiendrebeogo/GW_EM_joint/EMdata/detectable.txt', usecols=[0]).astype(int)
with open('GWEM_total_ejecta_mass.dag', 'w') as f:
    
    for i in events:

        jobname = 'GWEMResamplingEvent{0}'.format(i)

        f.write('JOB {0} /home/weizmann.kiendrebeogo/GW_EM_joint/rundir_total_ejecta_mass/gwem_resampling.sub\n'.format(jobname))
        f.write('RETRY {0} 0\n'.format(jobname))
        f.write('VARS {0} macroeventID="{1}"\n'.format(jobname, i)) 
