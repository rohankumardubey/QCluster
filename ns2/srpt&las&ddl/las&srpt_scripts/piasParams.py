import os
import sys

sim_end = 100000
link_rate = 10
mean_link_delay = 0.0000002
host_delay = 0.00002
queueSize = 240 # large queue size to get stable simulation
load_arr = [0.9, 0.8, 0.7, 0.6, 0.5]
#load_arr = [0.9, 0.5]
connections_per_pair = 1

paretoShape = 1.05

enableMultiPath = 1
perflowMP = 0

sourceAlg = 'DCTCP-Sack'
#sourceAlg='LLDCT-Sack'
initWindow = 70
ackRatio = 1
slowstartrestart = 'true'
DCTCP_g = 0.0625
min_rto = 0.002
prob_cap_ = 5

switchAlg = 'Priority'
DCTCP_K = 65
drop_prio_ = 'true'
prio_scheme_ = 2
deque_prio_ = 'true'
keep_order_ = 'true'
prio_num_arr = [8]
ECN_scheme_ = 2 #Per-port ECN marking

topology_spt = 16
topology_tors = 9
topology_spines = 4
topology_x = 1

ns_path = os.environ['HOME'] +\
    '/ns2/ns-allinone-2.34/ns-2.34/ns'
sim_script = 'spine_empirical.tcl'

interval_message = [0.000025, 0.004, 0.0000002, 0.003, 0.000004, 0.014]
workloadName = ['googleallrpc', 'facebookhadoop', 'keyvalue', 'search', 'googlerpc', 'vl2']
flow_cdf = ['Google_AllRPC.tcl', 'Facebook_HadoopDist_All.tcl', 'FacebookKeyValueMsgSizeDist.tcl', 'CDF_search.tcl', 'Google_SearchRPC.tcl', 'CDF_vl2.tcl']
meanFlowSize = [2927.354, 127796.6, 185.0, 1745.0 * 1460, 440.79, 5117*1460]

pias_thresh_0 = [[436,446,456,466,476], \
	 [38210,39976,41887,43898,45646], \
	 [183, 191, 199, 207, 215], \
	 [759*1460, 909*1460, 999*1460, 956*1460, 1059*1460], \
	 [368, 373, 378, 382, 388], \
	[750*1460, 745*1460, 907*1460, 840*1460, 805*1460] \
	]
pias_thresh_1 = [[554, 562, 570, 579, 587], \
	 [48958, 49137, 49398, 49621, 49899], \
	 [259, 262, 265, 268, 271], \
	 [1132*1460, 1329*1460, 1305*1460, 1381*1460, 1412*1460], \
	 [410, 411, 412, 414, 416], \
	[1083*1460, 1083*1460, 1301*1460, 1232*1460, 1106*1460] \
	]
pias_thresh_2 = [[633, 633, 632, 631, 630], \
	 [50905, 50897, 50888, 50878, 50869], \
	 [287, 287, 287, 287, 287], \
	 [1456*1460, 1648*1460, 1564*1460, 1718*1460, 1643*1460], \
	 [422, 422, 422, 422, 422], \
	[1416*1460, 1391*1460, 1619*1460, 1617*1460, 1401*1460] \
	]
pias_thresh_3 = [[720, 711, 702, 693, 684], \
	 [68384, 67154, 65723, 64461, 63084], \
	 [314, 311, 308, 306, 303], \
	 [1737*1460, 1960*1460, 1763*1460, 2028*1460, 1869*1460], \
	[435, 434, 433, 431, 429], \
	[13705*1460, 13689*1460, 12166*1460, 11950*1460, 10693*1460] \
	]
pias_thresh_4 = [[784, 768, 752, 736, 720], \
	 [73799, 72608, 71747, 70549, 69723], \
	 [332, 327, 322, 318, 312], \
	 [2010*1460, 2143*1460, 1956*1460, 2297*1460, 2008*1460], \
	 [442, 440, 438, 437, 426], \
	[14952*1460, 14936*1460, 12915*1460, 12238*1460, 11970*1460] \
	]
pias_thresh_5 = [[865, 835, 805, 774, 744], \
	 [76588, 75535, 74412, 73131, 72155], \
	 [352, 344, 336, 329, 321], \
	 [2199*1460, 2337*1460, 2149*1460, 2551*1460, 2115*1460], \
	 [451, 448, 445, 441, 438], \
	[21125*1460, 21149*1460, 21313*1460, 21494*1460, 21162*1460] \
	]
pias_thresh_6 = [[939, 899, 840, 799, 754], \
	 [78129, 77123, 75992, 74788, 73625], \
	 [367, 357, 347, 336, 326], \
	 [2325*1460, 2484*1460, 2309*1460, 2660*1460, 2184*1460], \
	 [457, 453, 449, 444, 440], \
	[28253*1460, 27245*1460, 26374*1460, 25720*1460, 22272*1460] \
	]