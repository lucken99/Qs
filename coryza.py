from collections import defaultdict
allium_cepa = {"not known","not known","not known","acrid,watery","not known","left sided","not known","warm room, evening","open air","red upperlip",}
arsenic_alb = {"on becoming cilled","not known","not known","acrid,watery","nose obstruction","right side","night", "open air, cold air","warm room","anxiety, wants warm drinks and heat.",}
arsenic_iod = {"not known","not known","not known","hot, watery","not known","not known","not known","not known","open air","Pain in maxillary sinus",}
anthemis = {"not known","not known","not known","watery","Rawnes in throat","not known","not known","warm room","not known","lachrymation, sneezing",}
arsenic_sulph Flavum = {"not known","not known","not known","profuse, watery, acrid","not known","not known","not known","cold air","not known","not known",}
arum_triphyllum = {"not known","not known","not known","acrid,watery","nose obstruction","left sided","not known","not known","not known","desire to pick lips",}
arundo = {"not known","not known","not known","dryness inside nose","Itching","not known","not known","not known","not known","salivation, boring of ear.",}
bryonia = {"overheated","not known","not known","dryness","not known","not known","not known","not known","not known","thirsty, dry mouth",}
carbo_veg = {"chilled after overheated","not known","not known","not known","not known","right to left","not known","warm room","open air","not known",}
causticum = {"not known","not known","not known","not known","Rawness","throat","not known","not known","cold drinks","hoarseness, aphonia",}
corallium_rubrum = {"not known","not known","not known","not known","nose obstructed","poaterior nares","not known","not known","not known","short, paroxysmal cough",}

d = defaultdict(int)
user_input = ["chilled afer overheated","cold air", ]
for i in user_input:
	if i != "not known" :
		if i in allium_cepa:
			d['allium_cepa'] += 1
		if i in arsenic_alb:
			d['arsenic_alb'] += 1
		if i in arsenic_iod:
			d['arsenic_iod'] += 1
		if i in anthemis:
			d['anthemis'] += 1
		if i in arsenic_sulph:
			d['arsenic_sulph'] += 1
		if i in arum_triphyllum:
			d['arum_triphyllum'] += 1
		if i in arundo:
			d['arundo'] += 1
		if i in bryonia:
			d['bryonia'] += 1
		if i in carbo_veg:
			d['carbo_veg'] += 1
		if i in causticum:
			d['causticum'] += 1
		if i in corallium_rubrum:
			d['corallium_rubrum'] += 1
