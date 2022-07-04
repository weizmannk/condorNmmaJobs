import os
from subprocess import check_output

model_str={'BNS':'Bu2019lm','NSBH':'Bu2019nsbh'}
prior_str = {'BNS':'Bu2019lm.prior', 'NSBH':'Bu2019nsbh.prior'}
bin_type = 'BNS'
num_inj = 2500 
seed_list = [816,323,364,564,851]
Exp = [180,300]
model = model_str[bin_type]
prior = prior_str['bin_type']



def main():

    parser = argparse.ArgumentParser(
        description="Process a bilby injection file for nmma consumption and Inference on kilonova ejecta parameters."
    )
    parser.add_argument(
        "--binary-type", 
        type=str, 
        required=False,
        help="Either BNS or NSBH"
    )
    parser.add_argument(
        "--model", 
        type=str, 
        required=True, 
        help="Name of the kilonova model to be used"
    )
    parser.add_argument(
        "--interpolation_type",
        type=str, 
        help="SVD interpolation scheme.", 
        default="sklearn_gp",
    )
    parser.add_argument(
        "--seed-list", 
        metavar="seed", 
        type=int, 
        nargs='+', 
        help=" list of Injection generation seed"
    )
    parser.add_argument(
        "--exposure",  
        type=int, 
        nargs='+', 
        help="Adds realistic ToO observations during the first one or two days. Sampling depends on exposure time specified. Valid values are 180 (<1000sq deg) or 300 (>1000sq deg). Won't work w/o --ztf-sampling" 
    )
    parser.add_argument(
        "--outdir", type=str, required=True, help="Path to the output directory"
    )
    
    parser.add_argument(
        "--injection-num",
        metavar="eventnum",
        type=int,
        help="The injection number to be taken from the injection set",
    )
    parser.add_argument(
        "--condor-dag-file",
        type=str,
        required=True,
        help="The condor dag file to be created"
    )
    parser.add_argument(
        "--condor-sub-file",
        type=str,
        required=True,
        help="The condor sub file to be created"
    )
    parser.add_argument(
        "--bash-file", type=str, required=True, help="The bash file to be created"
    )
    args = parser.parse_args()
     
    logdir = os.path.join(args.outdir, f"{args.binary_type}/logs")
    if not os.path.isdir(logdir):
        os.makedirs(logdir)  
      
    seed_list = args.seed_list
    exposure  = args.exposure
    injection_num     = args.injection_num 
    
    number_jobs = len(seed_list)*len(exposure)*len(n_inj)

 
    job_number = 0
    fid =  open(args.condor_dag_file, "w")
    fid1 = open(args.bash_file, "w")
    

    for ii in range(injection_num):
        for exp in exposure:
            for seed  in seed_list:
                outdir = os.path.join(args.outdir, f"{args.binary_type}/{ii}_{exp}_{seed}".format())
                if not os.path.isdir(outdir):
                    os.makedirs(outdir)  

                fid.write("JOB %d %s\n" % (job_number, args.condor_sub_file))
                fid.write("RETRY %d 3\n" % (job_number))
                fid.write(
                    'VARS %d jobNumber="%d" outdir="%s" GWsamples="%s" EMsamples="%s"\n'
                    % (job_number, job_number, outdir, gwsamples, emsamples)
                )
                fid.write("\n\n")
                job_number = job_number + 1




                   fid1.write(
                    "%s --model %s --svd-path /home/%s/gwemlightcurves/output/svdmodels --outdir %s --label injection_%s --prior analysis.prior --tmin 0 --tmax 20 --dt 0.5 --error-budget 1 --nlive %d --Ebv-max 0 --injection %s --injection-num %s --injection-detection-limit %s --injection-outfile %s --generation-seed 42 --filters %s --plot --remove-nondetections --optimal-augmentation --optimal-augmentation-N-points %d --optimal-augmentation-filters %s --optimal-augmentation-seed %d\n"
                    % (
                        lc_analysis,
                        args.model,
                        os.environ["USER"],
                        outdir,
                        args.model,
                        args.nlive,
                        args.injection_file,
                        str(index),
                        args.injection_detection_limit,
                        injfile,
                        args.filters,
                        args.optimal_augmentation_N_points,
                        args.optimal_augmentation_filters,
                        ii,
                    )
    
        
    
    nmma_create_injection --prior-file ./{bin_type}.prior --eos-file ./ALF2.dat --binary-type {bin_type} --n-injection {n_inj} --original-parameters --extension json
 