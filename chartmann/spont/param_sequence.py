from __future__ import division
import numpy as np
import utils
utils.backup(__file__)

# see this file for parameter descriptions
from common.defaults import *

c.N_e = 200
c.N_i = int(np.floor(0.2*c.N_e))
c.N = c.N_e + c.N_i
c.N_u_e = np.floor(0.05*c.N_e)
c.N_u_i = .8*c.N_u_e

c.W_ee = utils.Bunch(use_sparse=True,
                     lamb=0.1*c.N_e,
                     avoid_self_connections=True,
                     eta_stdp = 0.001,
                     sp_prob = 0.0,
                     sp_initial=0.000,
                     no_prune = True,
                     upper_bound = 1,
                     eta_ds = 0.1
                     )

c.W_ei = utils.Bunch(use_sparse=False,
                     lamb=np.inf,
                     avoid_self_connections=False,
                     eta_istdp = 0.0,
                     h_ip=0.1)

c.W_ie = utils.Bunch(use_sparse=False,
                     lamb=np.inf,
                     avoid_self_connections=False)

c.steps_plastic = 50000
c.steps_noplastic_train = 20000
c.steps_noplastic_test = 50000
c.N_steps = c.steps_plastic + c.steps_noplastic_train \
                            + c.steps_noplastic_test
c.display = True

c.N_iterations = 20

c.noise_sig = 0

c.with_plasticity = True

c.input_gain = 0.5

c.eta_ip = 0.001
h_ip_mean = float(2*c.N_u_e)/float(c.N_e)
h_ip_range = 0.01
c.h_ip = np.random.rand(c.N_e)*h_ip_range*2 + h_ip_mean - h_ip_range
c.always_ip = True

c.T_e_max = 0.5
c.T_e_min = 0.0
c.T_i_max = 0.35
c.T_i_min = 0.0
c.ordered_thresholds = True

c.fast_inhibit = True
c.k_winner_take_all = False
c.ff_inhibition = False
c.ff_inhibition_broad = 0.0

c.experiment.module = 'chartmann.spont.experiment_sequence'
c.experiment.name = 'Experiment_sequence'

#######################################
c.stats.file_suffix = 'ds_2nd_longtest'
#######################################
c.stats.save_spikes = True
c.stats.quenching = 'test'
c.stats.quenching_window = 2
c.stats.match = False
c.stats.lstsq_mue = 1
c.stats.control_rates = False

c.source.avoid = False
c.source.control = False
c.source.test_words = ['ABCD','A_CD','E_CD']#['ABCD','DCBA']#

# Adapt delays to paper (stimulus_length*2.5)
c.wait_min_plastic = 10
c.wait_var_plastic = 0
c.wait_min_train = 10
c.wait_var_train = 0
                        
# Cluster
if c.imported_mpi:
    c.cluster.vary_param = 'source.control'#'steps_plastic'#'with_plasticity'
    c.cluster.params = [False,True]#np.linspace(0,50000,11).astype(int)#[False,True]
    c.cluster.NUMBER_OF_SIMS  = len(c.cluster.params)
    c.cluster.NUMBER_OF_CORES = MPI.COMM_WORLD.size
    c.cluster.NUMBER_LOCAL = c.cluster.NUMBER_OF_SIMS\
                             // c.cluster.NUMBER_OF_CORES
    
    
    
    
    
    
    
    
    
    
    
    
    
