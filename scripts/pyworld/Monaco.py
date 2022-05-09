from Track import Track

def setupMonaco():
	#//const points = [[41,244],[47,230],[53,216],[59,201],[65,188],[73,175],[82,162],[91,150],[101,135],[109,124],[118,110],[127,99],[137,88],[151,77],[164,68],[177,57],[189,45],[200,31],[217,25],[233,28],[248,33],[268,39],[285,47],[298,54],[314,63],[329,70],[345,78],[359,87],[373,91],[388,101],[401,108],[415,114],[428,119],[442,122],[458,124],[477,123],[494,118],[508,112],[520,100],[526,85],[532,70],[541,58],[555,50],[572,47],[588,47],[604,47],[621,47],[637,47],[653,47],[668,47],[683,47],[698,53],[695,69],[688,84],[677,97],[663,107],[650,118],[638,131],[629,145],[627,162],[637,175],[654,172],[668,165],[674,150],[681,135],[693,122],[707,121],[720,129],[729,139],[734,154],[736,172],[736,190],[731,205],[722,219],[707,224],[690,230],[675,233],[659,233],[645,234],[631,236],[615,237],[600,237],[587,235],[573,234],[560,232],[547,231],[531,229],[514,227],[498,223],[484,218],[468,214],[452,209],[438,202],[424,195],[407,184],[395,172],[381,168],[368,178],[352,181],[337,178],[322,170],[317,154],[318,138],[314,122],[299,116],[284,102],[270,94],[249,89],[235,88],[213,90],[199,99],[185,111],[174,123],[180,137],[193,146],[206,155],[209,171],[202,182],[188,191],[176,202],[164,219],[150,223],[135,219],[119,213],[104,217],[99,234],[104,250],[114,264],[114,280],[101,285],[84,287],[71,285],[57,282],[41,275]]
	#//const points = [[125,127],[133,118],[141,109],[150,101],[158,92],[166,85],[174,77],[182,70],[192,63],[203,57],[212,51],[223,44],[231,36],[239,27],[248,19],[259,15],[271,15],[282,19],[292,26],[302,32],[310,39],[320,47],[331,51],[343,56],[353,61],[363,66],[375,71],[385,76],[395,82],[405,86],[416,93],[426,99],[435,106],[444,110],[454,115],[465,118],[476,120],[487,121],[498,121],[510,119],[521,114],[532,107],[542,100],[551,91],[559,82],[566,72],[575,63],[582,55],[591,48],[602,43],[613,39],[624,36],[637,35],[648,34],[659,33],[671,32],[682,32],[694,32],[705,36],[713,43],[712,55],[706,65],[695,74],[685,79],[675,83],[664,87],[653,91],[643,98],[633,106],[628,117],[631,127],[641,131],[653,132],[665,128],[675,122],[684,115],[693,109],[704,102],[715,98],[727,98],[735,105],[737,116],[737,127],[730,137],[721,145],[714,153],[703,160],[694,167],[684,174],[673,179],[663,185],[652,191],[641,195],[629,199],[619,202],[608,205],[596,207],[585,209],[573,210],[561,210],[551,210],[538,209],[527,209],[515,207],[505,205],[493,202],[482,200],[472,195],[461,190],[451,188],[440,181],[429,176],[417,177],[405,178],[395,174],[385,168],[376,160],[370,148],[364,139],[355,132],[344,125],[334,119],[322,114],[311,110],[301,105],[290,101],[279,98],[267,97],[256,96],[244,97],[232,99],[220,103],[210,108],[199,113],[189,120],[181,129],[177,141],[180,151],[187,161],[186,171],[178,181],[170,191],[162,200],[154,207],[142,211],[130,213],[120,219],[111,227],[103,233],[96,242],[89,251],[85,262],[84,275],[80,285],[70,290],[57,290],[47,285],[36,277],[29,269],[26,257],[28,246],[34,238],[45,233],[54,229],[63,222],[70,211],[77,202],[84,191],[90,182],[95,171],[100,161]]
	points = [[143,112],[150,104],[159,94],[167,86],[176,78],[185,71],[196,64],[206,56],[217,49],[228,44],[238,37],[246,28],[255,22],[266,16],[277,15],[289,18],[300,25],[309,30],[318,36],[329,43],[339,49],[350,54],[360,59],[372,64],[383,68],[395,73],[405,77],[418,81],[428,86],[439,91],[450,97],[460,103],[471,108],[481,113],[494,116],[506,117],[519,117],[531,115],[542,113],[552,108],[561,101],[571,94],[580,85],[588,77],[595,68],[602,59],[610,50],[620,43],[631,37],[643,33],[654,31],[666,29],[679,28],[692,26],[703,25],[716,25],[727,27],[738,35],[739,46],[734,58],[726,67],[715,74],[703,79],[693,83],[682,87],[671,92],[659,99],[652,108],[653,119],[663,127],[674,128],[685,124],[697,120],[708,114],[718,107],[727,100],[738,94],[750,91],[760,98],[765,108],[765,120],[759,130],[751,138],[741,146],[730,152],[720,158],[710,165],[699,171],[690,177],[678,183],[668,188],[657,192],[646,196],[634,199],[621,201],[609,203],[597,204],[584,205],[572,206],[559,206],[547,206],[536,204],[523,202],[510,200],[499,196],[488,190],[476,183],[455,171],[440,167],[429,172],[418,168],[408,162],[398,156],[395,142],[375,131],[366,124],[356,120],[347,114],[335,109],[325,103],[315,99],[302,96],[291,93],[278,92],[266,92],[254,95],[241,99],[230,104],[220,108],[208,114],[198,120],[189,127],[182,138],[185,147],[194,158],[190,167],[182,176],[175,185],[168,194],[160,201],[149,206],[138,207],[125,208],[116,215],[107,221],[100,231],[93,241],[88,252],[86,263],[84,272],[75,278],[63,280],[51,279],[42,274],[33,268],[28,257],[28,246],[32,235],[42,227],[52,221],[60,217],[69,208],[77,199],[83,188],[90,175],[97,164],[103,155],[111,145],[119,138]]
 
	width = 22
	#background = "Monaco.png"
	track = Track(points, width)
	return track