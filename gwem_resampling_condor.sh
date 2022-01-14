#!/bin/bash
source  /home/weizmann.kiendrebeogo/anaconda3/envs/nmma/bin/activate 




#Run
/home/weizmann.kiendrebeogo/anaconda3/envs/nmma/bin/gwem_resampling_condor --outdir output --GWsamples /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/GWdata/outdir --EMsamples /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/EMdata/outdir --EOSpath /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/eos_sorted --Neos 5000 --GWprior /home/weizmann.kiendrebeogo/NNMA/GW_EM_joint/GWdata/aligned_spin.priors --EMprior /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/EM.prior --total-ejecta-mass --condor-dag-file condor.dag --condor-sub-file condor.sub --bash-file condor.sh
