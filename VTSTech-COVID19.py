#COVID-19 JHU.EDU CSSE Data Analytics
#v0.53 2020-03-26 9:38:26 PM
#Written by VTSTech (veritas@vts-tech.org)
#John Hopkins University CSSE Data
#
#git clone https://github.com/Veritas83/VTSTech-COVID19.py
#cd VTSTech-COVID19.py

import os, sys, csv
from os import listdir
from os.path import isfile, join
from pathlib import Path

data_folder = Path("csse_covid_19_data/csse_covid_19_daily_reports/")
files = [f for f in listdir(data_folder) if isfile(join(data_folder, f))]
verbose=0
mode=""
report=""
cc="" #ISO 3166-1 Alpha-2
pc="" #ISO 3166-2
calc=""
build="0.53"
k_cnt=0
cc_dict = {
	"af" : "Afghanistan",
	"ax" : "Aland",
	"al" : "Albania",
	"dz" : "Algeria",
	"as" : "American Samoa",
	"ad" : "Andorra",
	"ao" : "Angola" ,
	"ai" : "Anguilla",
	"aq" : "Antarctica",
	"ag" : "Antigua and Barbuda",
	"ar" : "Argentina" ,
	"am" : "Armenia",
	"aw" : "Aruba",
	"au" : "Australia" ,
	"at" : "Austria",
	"az" : "Azerbaijan",
	"bs" : "Bahamas",
	"bh" : "Bahrain",
	"bd" : "Bangladesh",
	"bb" : "Barbados",
	"by" : "Belarus",
	"be" : "Belgium",
	"bz" : "Belize" ,
	"bj" : "Benin",
	"bm" : "Bermuda",
	"bt" : "Bhutan" ,
	"bo" : "Bolivia",
	"bq" : "Bonaire, Sint Eustatius and Saba",
	"ba" : "Bosnia and Herzegovina",
	"bw" : "Botswana",
	"bv" : "Bouvet Island",
	"br" : "Brazil" ,
	"io" : "British Indian Ocean Territory" ,
	"bn" : "Brunei Darussalam",
	"bg" : "Bulgaria",
	"bf" : "Burkina Faso" ,
	"bi" : "Burundi",
	"kh" : "Cambodia",
	"cm" : "Cameroon",
	"ca" : "Canada" ,
	"cv" : "Cabo Verde",
	"ky" : "Cayman Islands",
	"cf" : "Central African Republic" ,
	"td" : "Chad",
	"cl" : "Chile",
	"cn" : "China",
	"cx" : "Christmas Island",
	"cc" : "Cocos (Keeling) Islands",
	"co" : "Colombia",
	"cs" : "Cruise Ship",
	"km" : "Comoros",
	"cg" : "Congo (Kinshasa)",
	"cd" : "Congo (Democratic Republic of the)",
	"ck" : "Cook Islands" ,
	"cr" : "Costa Rica",
	"ci" : "Cote d'Ivoire",
	"hr" : "Croatia",
	"cu" : "Cuba",
	"cw" : "Curacao",
	"cy" : "Cyprus" ,
	"cz" : "Czech Republic",
	"dk" : "Denmark",
	"dj" : "Djibouti",
	"dm" : "Dominica",
	"do" : "Dominican Republic" ,
	"ec" : "Ecuador",
	"eg" : "Egypt",
	"sv" : "El Salvador",
	"gq" : "Equatorial Guinea",
	"er" : "Eritrea",
	"ee" : "Estonia",
	"et" : "Ethiopia",
	"fk" : "Falkland Islands (Malvinas)" ,
	"fo" : "Faroe Islands",
	"fj" : "Fiji",
	"fi" : "Finland",
	"fr" : "France" ,
	"gf" : "French Guiana",
	"pf" : "French Polynesia",
	"tf" : "French Southern Territories" ,
	"ga" : "Gabon",
	"gm" : "Gambia" ,
	"ge" : "Georgia",
	"de" : "Germany",
	"gh" : "Ghana",
	"gi" : "Gibraltar" ,
	"gr" : "Greece" ,
	"gl" : "Greenland" ,
	"gd" : "Grenada",
	"gp" : "Guadeloupe",
	"gu" : "Guam",
	"gt" : "Guatemala" ,
	"gg" : "Guernsey",
	"gn" : "Guinea" ,
	"gw" : "Guinea-Bissau",
	"gy" : "Guyana" ,
	"ht" : "Haiti",
	"hm" : "Heard Island and McDonald Islands" ,
	"va" : "Holy See",
	"hn" : "Honduras",
	"hk" : "Hong Kong" ,
	"hu" : "Hungary",
	"is" : "Iceland",
	"in" : "India",
	"id" : "Indonesia" ,
	"ir" : "Iran",
	"iq" : "Iraq",
	"ie" : "Ireland",
	"im" : "Isle of Man",
	"il" : "Israel" ,
	"it" : "Italy",
	"jm" : "Jamaica",
	"jp" : "Japan",
	"je" : "Jersey" ,
	"jo" : "Jordan" ,
	"kz" : "Kazakhstan",
	"ke" : "Kenya",
	"ki" : "Kiribati",
	"xk" : "Kosovo",
	"kp" : "North Korea" ,
	"kr" : "South Korea",
	"kw" : "Kuwait" ,
	"kg" : "Kyrgyzstan",
	"la" : "Lao People's Democratic Republic",
	"lv" : "Latvia" ,
	"lb" : "Lebanon",
	"ls" : "Lesotho",
	"lr" : "Liberia",
	"ly" : "Libya",
	"li" : "Liechtenstein",
	"lt" : "Lithuania" ,
	"lu" : "Luxembourg",
	"mo" : "Macao",
	"mk" : "North Macedonia",
	"mg" : "Madagascar",
	"mw" : "Malawi" ,
	"my" : "Malaysia",
	"mv" : "Maldives",
	"ml" : "Mali",
	"mt" : "Malta",
	"mh" : "Marshall Islands",
	"mq" : "Martinique",
	"mr" : "Mauritania",
	"mu" : "Mauritius" ,
	"yt" : "Mayotte",
	"mx" : "Mexico" ,
	"fm" : "Micronesia",
	"md" : "Moldova" ,
	"mc" : "Monaco" ,
	"mn" : "Mongolia",
	"me" : "Montenegro",
	"ms" : "Montserrat",
	"ma" : "Morocco",
	"mz" : "Mozambique",
	"mm" : "Myanmar",
	"na" : "Namibia",
	"nr" : "Nauru",
	"np" : "Nepal",
	"nl" : "Netherlands",
	"nc" : "New Caledonia",
	"nz" : "New Zealand",
	"ni" : "Nicaragua" ,
	"ne" : "Niger",
	"ng" : "Nigeria",
	"nu" : "Niue",
	"nf" : "Norfolk Island",
	"mp" : "Northern Mariana Islands" ,
	"no" : "Norway" ,
	"om" : "Oman",
	"pk" : "Pakistan",
	"pw" : "Palau",
	"ps" : "occupied Palestinian territory",
	"pa" : "Panama" ,
	"pg" : "Papua New Guinea",
	"py" : "Paraguay",
	"pe" : "Peru",
	"ph" : "Philippines",
	"pn" : "Pitcairn",
	"pl" : "Poland" ,
	"pt" : "Portugal",
	"pr" : "Puerto Rico",
	"qa" : "Qatar",
	"re" : "Reunion",
	"ro" : "Romania",
	"ru" : "Russia" ,
	"rw" : "Rwanda" ,
	"bl" : "Saint Barthelemy",
	"sh" : "Saint Helena, Ascension and Tristan da Cunha",
	"kn" : "Saint Kitts and Nevis" ,
	"lc" : "Saint Lucia",
	"mf" : "Saint Martin (French part)",
	"pm" : "Saint Pierre and Miquelon",
	"vc" : "Saint Vincent and the Grenadines",
	"ws" : "Samoa",
	"sm" : "San Marino",
	"st" : "Sao Tome and Principe" ,
	"sa" : "Saudi Arabia" ,
	"sn" : "Senegal",
	"rs" : "Serbia" ,
	"sc" : "Seychelles",
	"sl" : "Sierra Leone" ,
	"sg" : "Singapore" ,
	"sx" : "Sint Maarten (Dutch part)",
	"sk" : "Slovakia",
	"si" : "Slovenia",
	"sb" : "Solomon Islands" ,
	"so" : "Somalia",
	"za" : "South Africa" ,
	"gs" : "South Georgia and the South Sandwich Islands",
	"ss" : "South Sudan",
	"es" : "Spain",
	"lk" : "Sri Lanka" ,
	"sd" : "Sudan",
	"sr" : "Suriname",
	"sj" : "Svalbard and Jan Mayen",
	"sz" : "Swaziland" ,
	"se" : "Sweden" ,
	"ch" : "Switzerland",
	"sy" : "Syrian Arab Republic",
	"tw" : "Taiwan, Province of China",
	"tj" : "Tajikistan",
	"tz" : "Tanzania, United Republic of",
	"th" : "Thailand",
	"tl" : "Timor-Leste",
	"tg" : "Togo",
	"tk" : "Tokelau",
	"to" : "Tonga",
	"tt" : "Trinidad and Tobago",
	"tn" : "Tunisia",
	"tr" : "Turkey" ,
	"tm" : "Turkmenistan" ,
	"tc" : "Turks and Caicos Islands" ,
	"tv" : "Tuvalu" ,
	"ug" : "Uganda" ,
	"ua" : "Ukraine",
	"ae" : "United Arab Emirates",
	"gb" : "United Kingdom",
	"us" : "US" ,
	"um" : "United States Minor Outlying Islands" ,
	"uy" : "Uruguay",
	"uz" : "Uzbekistan",
	"vu" : "Vanuatu",
	"ve" : "Venezuela (Bolivarian Republic of)",
	"vn" : "Viet Nam",
	"vg" : "Virgin Islands (British)" ,
	"vi" : "Virgin Islands (U.S.)" ,
	"wf" : "Wallis and Futuna",
	"eh" : "Western Sahara",
	"ye" : "Yemen",
	"zm" : "Zambia" ,
	"zw" : "Zimbabwe"
		}
pc_dict = {
	"CA-AB" : "Alberta",
	"CA-BC" : "British Columbia",
	"CA-MB" : "Manitoba",
	"CA-NB" : "New Brunswick",
	"CA-NL" : "Newfoundland and Labrador",
	"CA-NS" : "Nova Scotia",
	"CA-NT" : "Northwest Territories",
	"CA-NU" : "Nunavut",
	"CA-ON" : "Ontario",
	"CA-PE" : "Prince Edward Island",
	"CA-QC" : "Quebec",
	"CA-SK" : "Saskatchewan",
	"US-AL" : "Alabama",
	"US-AK" : "Alaska",
	"US-AZ" : "Arizona",
	"US-AR" : "Arkansas",
	"US-CA" : "California",
	"US-CO" : "Colorado",
	"US-CT" : "Connecticut",
	"US-DE" : "Delaware",
	"US-FL" : "Florida",
	"US-GA" : "Georgia",
	"US-HI" : "Hawaii",
	"US-ID" : "Idaho",
	"US-IL" : "Illinois",
	"US-IN" : "Indiana",
	"US-IA" : "Iowa",
	"US-KS" : "Kansas",
	"US-KY" : "Kentucky",
	"US-LA" : "Louisiana",
	"US-ME" : "Maine",
	"US-MD" : "Maryland",
	"US-MA" : "Massachusetts",
	"US-MI" : "Michigan",
	"US-MN" : "Minnesota",
	"US-MS" : "Mississippi",
	"US-MO" : "Missouri",
	"US-MT" : "Montana",
	"US-NE" : "Nebraska",
	"US-NV" : "Nevada",
	"US-NH" : "New Hampshire",
	"US-NJ" : "New Jersey",
	"US-NM" : "New Mexico",
	"US-NY" : "New York",
	"US-NC" : "North Carolina",
	"US-ND" : "North Dakota",
	"US-OH" : "Ohio",
	"US-OK" : "Oklahoma",
	"US-OR" : "Oregon",
	"US-PA" : "Pennsylvania",
	"US-RI" : "Rhode Island",
	"US-SC" : "South Carolina",
	"US-SD" : "South Dakota",
	"US-TN" : "Tennessee",
	"US-TX" : "Texas",
	"US-UT" : "Utah",
	"US-VT" : "Vermont",
	"US-VA" : "Virginia",
	"US-WA" : "Washington",
	"US-WV" : "West Virginia",
	"US-WI" : "Wisconsin",
	"US-WY" : "Wyoming",
	"US-DC" : "District of Columbia",
	"US-AS" : "American Samoa",
	"US-GU" : "Guam",
	"US-MP" : "Northern Mariana Islands",
	"US-PR" : "Puerto Rico",
	"US-UM" : "United States Minor Outlying Islands",
	"US-VI" : "Virgin Islands"		
}
def getcc(cc):
   	return cc_dict[cc.lower()]
    #thx hdbo
def getpc(pc):
    #print("Debug:", pc_dict[pc.upper()])
    return pc_dict[pc.upper()]
def getfn(msg):
	script_fn = msg.split("\\")
	for x in range(0,len(script_fn),1):
		if ("VTSTech-COVID19.py" in script_fn[x]):
			return script_fn[x]
		elif (".py" in script_fn[x]):
			return script_fn[x]
def banner():	
	print("COVID-19 JHU.EDU CSSE Data Analytics\nv"+build+" Written by VTSTech (www.VTS-Tech.org)\nData Source: https://github.com/CSSEGISandData/COVID-19\n")
def usage():
	spc=" "
	print("Usage:",getfn(sys.argv[0]),"-l")
	print(spc*6,getfn(sys.argv[0]),"-d 03-17-2020")
	print(spc*6,getfn(sys.argv[0]),"-a -dav\n")
	print("-v",spc*17,"verbose mode\n-l",spc*17,"list daily reports available\n-d MM-DD-YYYY",spc*6,"use this daily report\n-a",spc*18,end='')
	print("use all available reports\n-c US",spc*14,"filter by this country (ISO 3166-1 Alpha-2)\n-p US-NY",spc*11,"filter by this province/state (ISO-3166-2)\n-t",spc*17,"calculate global total cases (use with ",end='')
	print("-c or -p to filter)\n-td",spc*16,"calculate global total deaths\n-tr",spc*16,"calculate global total recovered\n-gdr",spc*15,"calculate global ",end='')
	print("death rate\n-grr",spc*15,"calculate global recovery rate\n-dav",spc*15,"calculate daily average new cases\n-dad",spc*15,"calculate daily average new deaths\n-dnc",spc*15,"calculate daily new cases\n-dnd",spc*15,"calculate daily new deaths\n-dnr",spc*15,"calculate daily new recovered\n-dgf",spc*16,end='')
	print("calculate daily growth factor\n-drc",spc*15,"calculate daily death rate change\n-din",spc*15,"find largest daily case increases")
def getreports():
	reports=""
	for x in range(0,len(files),1):
		if (".csv" in files[x]):
			reports=reports+"\n"+files[x]	
	return reports
def listreports():
	print("Daily Reports Available:\n")
	print(getreports())
def parsereports(calc):
	global mode
	global cc
	reports=getreports()
	i=0
	#print("DEBUG:", mode)
	if ("allreports" in mode):
		if (calc=="t") or (calc=="td") or (calc=="tr") or (calc=="gdr") or (calc=="grr"):
			for line in reports.split(".csv"):
				line=line+".csv"
				if (len(line)>4):
					tmp = parsereport(line.replace("\n",""),calc)
					if (tmp != 0 and tmp != None or verbose==1):print(tmp)
			if (calc=="t"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
					print("\nNational Total Cases")
				elif (len(pc)>=1):
					print("\nCountry Filter:", getcc(pc[0:2]))
					print("Prov/State Filter:", getpc(pc))
					print("\nTotal Cases")
				else:
					print("\nGlobal Total Cases")
			elif (calc=="td"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
					print("\nNational Total Deaths")
				elif (len(pc)>=1):
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
					print("\nTotal Deaths")
				else:
					print("\nGlobal Total Deaths")
			elif (calc=="tr"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
					print("\nNational Total Recovered")
				elif (len(pc)>=1):
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
					print("\nTotal Recovered")
				else:
					print("\nGlobal Total Recovered")
			elif (calc=="gdr"):
				if (len(cc)>=1):
					print("\nNational Death Rate")
					print("\nCountry Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("\nDeath Rate")
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("\nGlobal Death Rate")
			elif (calc=="grr"):
				if (len(cc)>=1):
					print("\nNational Recovery Rate")
					print("\nCountry Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("\nRecovery Rate")
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("\nGlobal Recovery Rate")
			print("\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
		elif (calc=="dav")or(calc=="dad")or(calc=="din")or(calc=="dnc")or(calc=="dnr")or(calc=="dgf")or(calc=="dnd"):
			if (calc=="dav"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				for line in reports.split(".csv"):
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						new_cases=(c_cases - p_cases)
						#print(new_cases)
						davg_cases = (davg_cases+new_cases)/i
					t_days=i				
				if (len(cc)>=1):
					print("National Average Daily New Cases:",round(davg_cases,2))
					print("\nCountry Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("Average Daily New Cases:",round(davg_cases,2))
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("Global Average Daily New Cases:",round(davg_cases,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
			elif (calc=="dad"):
				p_deaths = 0
				c_deaths = 0
				n_deaths = []
				davg_deaths=0
				for line in reports.split(".csv"):
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_deaths = c_deaths
						c_deaths = parsereport(line.replace("\n",""),"td")
						new_deaths=(c_deaths - p_deaths)
						#print(new_deaths)
						davg_deaths = (davg_deaths+new_deaths)/i
					t_days=i
				if (len(cc)>=1):
					print("National Average Daily New Deaths:",round(davg_deaths,2))
					print("\nCountry Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("Average Daily New Deaths:",round(davg_deaths,2))
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("Global Average Daily New Deaths:",round(davg_deaths,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
			elif (calc=="dnc"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				print("Daily New Cases:\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_cases=(c_cases - p_cases)
						if (new_cases != 0 or verbose==1):print(c_date+" "+str(new_cases),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nCountry Filter:", getcc(cc))
					print("\nNational Daily New Cases")
				elif (len(pc)>=1):
					print("\n\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
					print("\nDaily New Cases")
				else:
					print("\n\nGlobal Daily New Cases\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
			elif (calc=="dnd"):
				p_deaths = 0
				c_deaths = 0
				n_deaths = []
				davg_deaths=0
				print("Daily New Deaths\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_deaths = c_deaths
						c_deaths = parsereport(line.replace("\n",""),"td")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_deaths=(c_deaths - p_deaths)
						print(c_date+" "+str(new_deaths),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nCountry Filter:", getcc(cc))
					print("\nNational Daily New Deaths")
				elif (len(pc)>=1):
					print("\n\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
					print("\nDaily New Deaths")
				else:
					print("\n\nGlobal Daily New Deaths\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
			elif (calc=="dnr"):
				p_recov = 0
				c_recov = 0
				n_recov = []
				davg_recov=0
				print("Daily New Recovered\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_recov = c_recov
						c_recov = parsereport(line.replace("\n",""),"tr")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_recov=(c_recov - p_recov)
						print(c_date+" "+str(new_recov),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nCountry Filter:", getcc(cc))
					print("\nNational Daily New Recovered")
				elif (len(pc)>=1):
					print("\n\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
					print("\nDaily New Recovered")
				else:
					print("\n\nGlobal Daily New Recovered\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")				
			elif (calc=="din"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				top_cases=0
				print("Largest Daily New Cases\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						new_cases=(c_cases - p_cases)
						if (new_cases > top_cases) or (new_cases > 500):
							top_cases=new_cases
							print(c_date+" "+str(top_cases),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				elif (len(cc)>=1):
					print("\nCountry Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				print("\n\nLargest Daily New Cases\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
			elif (calc=="dgf"):
				p_cases = 0
				c_cases = 0
				n_cases = []
				davg_cases=0
				c_growth=0
				t_days=0
				print("Daily Growth Factor\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")					
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_cases = c_cases
						c_cases = parsereport(line.replace("\n",""),"t")
						#c_date = parsereport(line.replace("\n",""),"date")
						if (p_cases>0):c_growth=round((c_cases / p_cases),2)
						if (c_date=="") or (c_growth==0):
							t_days=t_days-1
						else:
							print(c_date+" "+str(c_growth),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nNational Daily Growth Factor")
					print("Country Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("\n\nDaily Growth Factor")
					print("Country Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("\n\nGlobal Daily Growth Factor")
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.")
		elif (calc=="drc"):
				p_gdr = 0
				c_gdr = 0
				n_gdr = []
				davg_gdr=0
				c_dri=0
				t_days=0
				tmp=0.0
				print("Daily Death Rate Change\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")					
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						p_gdr = float(c_gdr)
						if (parsereport(line.replace("\n",""),"gdr") != None):tmp=parsereport(line.replace("\n",""),"gdr")[11:-1]
						c_gdr = float(tmp)
						#print("Debug:", c_gdr)
						#c_date = parsereport(line.replace("\n",""),"date")
						if (p_gdr>0):c_dri=(c_gdr - p_gdr)
						if (c_date=="") or (c_dri==0):
							t_days=t_days-1
						else:
							print(c_date+" "+str(round(c_dri,3))+"%",end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nNational Daily Death Rate Change")
					print("Country Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("\n\nDaily Death Rate Change")
					print("Country Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("\n\nGlobal Daily Death Rate Change")
		elif (calc=="cdr"):
				d1_date=0
				d1_cases=0
				c_date=""
				c_cases=0
				cdr=0.0
				t_days=0
				tmp=0.0
				print("Case Doubling Rate\n")
				for line in reports.split(".csv"):
					c_date=line
					c_date.replace("\n","")					
					line=line+".csv"
					if (len(line)>4):
						i=int(i)+1
						if (parsereport(line.replace("\n",""),"cdr") != None):tmp=parsereport(line.replace("\n",""),"cdr")
						if (i==1):
							d1_date=c_date
						cdr = tmp
						#print("Debug:", cdr)
						#c_date = parsereport(line.replace("\n",""),"date")
						print(c_date+" "+str(cdr),end='')
						#davg_cases = (davg_cases+new_cases)/i
					t_days=i
				if (len(cc)>=1):
					print("\n\nNational Daily Death Rate Change")
					print("Country Filter:", getcc(cc))
				elif (len(pc)>=1):
					print("\n\nDaily Death Rate Change")
					print("Country Filter:", getcc(pc[0:2].lower()))
					print("Prov/State Filter:", getpc(pc.upper()))
				else:
					print("\n\nGlobal Daily Death Rate Change")
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v"+build+" by VTSTech Complete.") #don't indent me
	else:
		print("Error! This mode requires the -a parameter!")
def parsereport(report,calc):
	global mode
	global cc
	global pc
	global d1_date
	c_country=""
	c_prov=""
	c_cases=0
	c_deaths=0
	c_recov=0
	c_updated=""
	t_cases=0
	t_deaths=0
	t_recov=0
	gdr=0.0
	grr=0.0
	cdr=0.0
	d1_cases=0
	file_to_open = Path("csse_covid_19_data/csse_covid_19_daily_reports/" + report)
	if file_to_open.exists():
		f = open(file_to_open.absolute())
		cssereader = csv.reader(f, delimiter=',', quotechar='"')
		x=0
		for row in cssereader:
			if (x!=0):
				if (len(cc)>=1):					
					if (getcc(cc) in row[1]) or ((getcc(cc) == "South Korea") and (row[1] == "Korea, South") or (getcc(cc) == "Russia") and (row[1] == "Russian Federation")):
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						if (len(row[5])>0):
							c_recov=int(row[5])
							t_recov=int(t_recov+c_recov)
				elif (len(pc)>=1):
					if (getpc(pc) in row[0]):
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						if (len(row[5])>0):
							c_recov=int(row[5])
							t_recov=int(t_recov+c_recov)
				else:
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						if (len(row[5])>0):
							c_recov=int(row[5])
							t_recov=int(t_recov+c_recov)						
			x=x+1
		if (calc==""):
			print("Please specify a metric to calculate: -t, -td, -tr, -din, -dav, -dad, -dnc, -dnd, -dnr, -drc, -gdr, -grr")
		elif (calc=="t"):
			if (mode=="onereport"):print("Total Cases:",t_cases)
			return(t_cases)
		elif (calc=="td"):
			if (mode=="onereport"):print("Total Deaths:",t_deaths)
			return(t_deaths)
		elif (calc=="tr"):
			if (mode=="onereport"):print("Total Recovered:",t_recov)
			return(t_recov)
		elif (calc=="gdr"):
			if (t_deaths!=0) and (t_cases!=0):
				gdr=round(float(t_deaths/t_cases)*100,3)
				c_date=str(report.split(".csv")[0])
				if (mode=="onereport"):print("Global Death Rate:",gdr,"%")
				#return(str(c_updated+" "+str(gdr)+"%"))
				return(c_date+" "+str(gdr)+"%")
		elif (calc=="grr"):
			if (t_recov!=0) and (t_cases!=0):
				grr=round(float(t_recov/t_cases)*100,3)
				c_date=str(report.split(".csv")[0])
				if (mode=="onereport"):print("Global Recovery Rate:",grr,"%")
				#return(str(c_updated+" "+str(gdr)+"%"))
				return(c_date+" "+str(grr)+"%")
		elif (calc=="cdr"):
			if (t_cases!=0) or (c_cases!=0):
				c_date=str(report.split(".csv")[0])
				if (d1_cases==0 and t_cases>=1):
					d1_cases=c_cases
				#print("Debug:",t_days)
				#cdr=float((t_days-d1_cases)*(2/(c_cases/d1_cases)))
				if (mode=="onereport"):print("Case Doubling Rate:",cdr)
				#return(str(c_updated+" "+str(gdr)+"%"))
				#return(str(cdr))
				return("Not implemented yet.")
#D1 = first day, C1 = num of cases on D1
#DX = today, CX = num of cases today
#(CDR) Number of days to double = ( ( DX - D1 ) * ( ln(2) / ln( CX / C1 )) )				
		elif (calc=="date"):
			return(str(row[2]))
		f.close()
	else:
		print("Error! Requsted file does not exist.")
	#print(report)
	
def main(mode,report,cc,calc):
	global totalargs
	if (mode == "listreports"):
		banner()
		listreports()
	elif(mode == "onereport"):
		banner()
		if (len(cc) >= 1):
			print("Country Filter:",getcc(cc))
		else:
			print("Country Filter: Global")
		print("Report:",report,"\n")
		parsereport(report,calc)
	elif(mode == "allreports"):
		banner()
		parsereports(calc)
	else:
		if (totalargs>=2):
			print("Requires either -l, -a or -d to be set")
###
totalargs = len(sys.argv)
for x in range(0,totalargs,1):
	if (totalargs >= 7):	
		banner()
		print("Too many arguments! Check command line.")
		usage()
		quit()
	elif (sys.argv[x] == "-v") or (totalargs==1 and "VTSTech-COVID19.py" in getfn(sys.argv[0])):
		verbose=1
		banner()
		usage()
	elif (sys.argv[x] == "-l"):
		mode="listreports"
	elif (sys.argv[x] == "-a"):
		mode="allreports"
	elif (sys.argv[x] == "-d"):
		mode="onereport"
		if (len(sys.argv[x+1]) != 10):
			print("Error: Invalid daily report specified! (-d) Expected format: MM-DD-YYYY")
			quit()
		report=str(sys.argv[x+1]+".csv")
	elif (sys.argv[x] == "-t"):
		calc="t"
	elif (sys.argv[x] == "-td"):
		calc="td"
	elif (sys.argv[x] == "-tr"):
		calc="tr"
	elif (sys.argv[x] == "-gdr"):
		calc="gdr"
	elif (sys.argv[x] == "-grr"):
		calc="grr"
	elif (sys.argv[x] == "-dav"):
		calc="dav"
	elif (sys.argv[x] == "-dad"):
		calc="dad"
	elif (sys.argv[x] == "-din"):
		calc="din"
	elif (sys.argv[x] == "-dnc"):
		calc="dnc"
	elif (sys.argv[x] == "-dnd"):
		calc="dnd"
	elif (sys.argv[x] == "-dgf"):
		calc="dgf"
	elif (sys.argv[x] == "-drc"):
		calc="drc"
#	elif (sys.argv[x] == "-cdr"):
#		calc="cdr"
	elif (sys.argv[x] == "-dnr"):
		calc="dnr"
	elif (sys.argv[x] == "-p"):
		pc=str(sys.argv[x+1]).upper()
		if (len(pc) != 5):
			print("Error: Invalid province/state code specified! (-p) Expected format: US-TX")
			quit()
	elif (sys.argv[x] == "-c"):
		cc=str(sys.argv[x+1]).lower()
		if (len(cc) != 2):
			print("Error: Invalid country code specified! (-c) Expected format: US")
			quit()
main(mode,report,cc,calc)