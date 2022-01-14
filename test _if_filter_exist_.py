import numpy as np
import os
import glob

import optparse
import pandas as pd
import numpy as np

def parse_commandline(): 
    """[Create the output files to save the processed data ]
    :return: [create an output folder]
    :rtype: [optparse.Values]
    """

    parser = optparse.OptionParser()
    parser.add_option("-p", "--outdir", default= "outdirF")
    opts, args = parser.parse_args()

    return opts 

datapath =os.getcwd()

#datapath = '/home/wiezmann/GW_EM_joint/EMdata/outdir/'



lc_file = [f.name for f in os.scandir(datapath+"/outdir/") if f.is_dir() and (f.name).isdigit() ]

# =============================================================================
# Parse command line to create folders for  output data 
# =============================================================================
opts = parse_commandline()
baseOutdir = opts.outdir
if not os.path.isdir(baseOutdir):
    os.makedirs(baseOutdir)
    

with open('filter_test.txt', 'w') as f:
	for file in lc_file:
	    direct = datapath + "/outdir/"+file
	    
	    csv_file = glob.glob((direct+'/lc.csv'), recursive=True)
	    if csv_file != []:
	    
	    	data=pd.read_csv(csv_file[0])
	    	filters = np.unique(data['filter'])
	    	for filt in filters : 
	    		if filt not in ['i', 'r', 'g'] :
	    	
	    			f.write('In the fichier number {}  there are filter {} \n'.format(file, filt)) 
	    			
	    	
	    	
    	

    
    
    
    
