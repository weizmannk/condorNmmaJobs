
model_str={'BNS':'Bu2019lm','NSBH':'Bu2019nsbh'}
prior_str = {'BNS':'Bu2019lm.prior', 'NSBH':'Bu2019nsbh.prior'}
bin_type = 'BNS'
num_inj = 2500 
seed_list = [816,323,364,564,851]
Exp = [180,300]
model = model_str[bin_type]
prior = prior_str['bin_type'] 

jobs = num_inj*len(seed_list)*len(Exp)

job=1
with open('injection_observing_scenarios.dag', 'w') as f:
   
    for n_inj in range(num_inj):
        for exp in Exp:
            for seed in seed_list:
                jobname = f'injectionObservingSeenarios_N_{job}_{n_inj}_{exp}_{seed}'.format()
                f.write(f'JOB {jobname}/injection_observing_scenarios.sub\n'.format())
                f.write('RETRY {0} 0\n'.format(jobname))
                f.write('VARS {0} n_inj="{1}"\n'.format(jobname, job))
                job+=1


data = Table.read('injections.dat', format='ascii.fast_tab')
In [4]: len(data)
Out[4]: 1482

In [5]: len(data[data['mass1']<data['mass2']])
Out[5]: 723
