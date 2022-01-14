#!/bin/bash
source  /home/weizmann.kiendrebeogo/anaconda3/envs/nmma_setup/bin/activate 

job=$1
macroeventID=$1

#OUTPUTFILE=~/workingDir/test_${job}.txt

echo $HOSTNAME
echo "params"
echo $job
echo $macroeventID



#Run 

/home/weizmann.kiendrebeogo/anaconda3/envs/nmma_setup/bin/gwem_resampling --outdir ./rundir/$(macroeventID) --EMsamples /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/EMdata/outdir/$(macroeventID)/injection_Bu2019lm_posterior_samples.dat --GWsamples /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/GWdata/outdir/inj_PhD_posterior_samples_$(macroeventID).dat --EOS /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/eos_sorted --nlive 8192 --GWprior /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/GWdata/aligned_spin.priors --EMprior /home/weizmann.kiendrebeogo/NMMA/GW_EM_joint/EM.prior --total-ejecta-mass --Neos 5000

