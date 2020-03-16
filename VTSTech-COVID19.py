#COVID-19 JHU.EDU CSSE Data Analytics
#v0.46 2020-03-16 10:09:05 AM
#Written by VTSTech (veritas@vts-tech.org)
#John Hopkins University CSSE Data
#
#git clone https://github.com/CSSEGISandData/COVID-19
#cd COVID-19
#wget https://github.com/Veritas83/VTSTech-COVID19.py/raw/master/VTSTech-COVID19.py

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
calc=""

country_dict = {
	"af" : "Afghanistan",
	"ax" : "Aland",
	"al" : "Albania",
	"dz" : "Algeria",
	"as" : "American Samoa"  ,
	"ad" : "Andorra",
	"ao" : "Angola" ,
	"ai" : "Anguilla"  ,
	"aq" : "Antarctica",
	"ag" : "Antigua and Barbuda",
	"ar" : "Argentina" ,
	"am" : "Armenia",
	"aw" : "Aruba"  ,
	"au" : "Australia" ,
	"at" : "Austria",
	"az" : "Azerbaijan",
	"bs" : "Bahamas",
	"bh" : "Bahrain",
	"bd" : "Bangladesh",
	"bb" : "Barbados"  ,
	"by" : "Belarus",
	"be" : "Belgium",
	"bz" : "Belize" ,
	"bj" : "Benin"  ,
	"bm" : "Bermuda",
	"bt" : "Bhutan" ,
	"bo" : "Bolivia"  ,
	"bq" : "Bonaire, Sint Eustatius and Saba"  ,
	"ba" : "Bosnia and Herzegovina",
	"bw" : "Botswana"  ,
	"bv" : "Bouvet Island",
	"br" : "Brazil" ,
	"io" : "British Indian Ocean Territory" ,
	"bn" : "Brunei Darussalam"  ,
	"bg" : "Bulgaria"  ,
	"bf" : "Burkina Faso" ,
	"bi" : "Burundi",
	"kh" : "Cambodia"  ,
	"cm" : "Cameroon"  ,
	"ca" : "Canada" ,
	"cv" : "Cabo Verde",
	"ky" : "Cayman Islands"  ,
	"cf" : "Central African Republic" ,
	"td" : "Chad",
	"cl" : "Chile"  ,
	"cn" : "China"  ,
	"cx" : "Christmas Island",
	"cc" : "Cocos (Keeling) Islands"  ,
	"co" : "Colombia"  ,
	"cs" : "Cruise Ship",
	"km" : "Comoros",
	"cg" : "Congo (Kinshasa)"  ,
	"cd" : "Congo (Democratic Republic of the)",
	"ck" : "Cook Islands" ,
	"cr" : "Costa Rica",
	"ci" : "Cote d'Ivoire",
	"hr" : "Croatia",
	"cu" : "Cuba",
	"cw" : "Curacao",
	"cy" : "Cyprus" ,
	"cz" : "Czech Republic"  ,
	"dk" : "Denmark",
	"dj" : "Djibouti"  ,
	"dm" : "Dominica"  ,
	"do" : "Dominican Republic" ,
	"ec" : "Ecuador",
	"eg" : "Egypt"  ,
	"sv" : "El Salvador"  ,
	"gq" : "Equatorial Guinea"  ,
	"er" : "Eritrea",
	"ee" : "Estonia",
	"et" : "Ethiopia"  ,
	"fk" : "Falkland Islands (Malvinas)" ,
	"fo" : "Faroe Islands",
	"fj" : "Fiji",
	"fi" : "Finland",
	"fr" : "France" ,
	"gf" : "French Guiana",
	"pf" : "French Polynesia",
	"tf" : "French Southern Territories" ,
	"ga" : "Gabon"  ,
	"gm" : "Gambia" ,
	"ge" : "Georgia",
	"de" : "Germany",
	"gh" : "Ghana"  ,
	"gi" : "Gibraltar" ,
	"gr" : "Greece" ,
	"gl" : "Greenland" ,
	"gd" : "Grenada",
	"gp" : "Guadeloupe",
	"gu" : "Guam",
	"gt" : "Guatemala" ,
	"gg" : "Guernsey"  ,
	"gn" : "Guinea" ,
	"gw" : "Guinea-Bissau",
	"gy" : "Guyana" ,
	"ht" : "Haiti"  ,
	"hm" : "Heard Island and McDonald Islands" ,
	"va" : "Holy See"  ,
	"hn" : "Honduras"  ,
	"hk" : "Hong Kong" ,
	"hu" : "Hungary",
	"is" : "Iceland",
	"in" : "India"  ,
	"id" : "Indonesia" ,
	"ir" : "Iran"  ,
	"iq" : "Iraq",
	"ie" : "Ireland",
	"im" : "Isle of Man"  ,
	"il" : "Israel" ,
	"it" : "Italy"  ,
	"jm" : "Jamaica",
	"jp" : "Japan"  ,
	"je" : "Jersey" ,
	"jo" : "Jordan" ,
	"kz" : "Kazakhstan",
	"ke" : "Kenya"  ,
	"ki" : "Kiribati"  ,
	"kp" : "North Korea" ,
	"kr" : "South Korea",
	"kw" : "Kuwait" ,
	"kg" : "Kyrgyzstan",
	"la" : "Lao People's Democratic Republic"  ,
	"lv" : "Latvia" ,
	"lb" : "Lebanon",
	"ls" : "Lesotho",
	"lr" : "Liberia",
	"ly" : "Libya"  ,
	"li" : "Liechtenstein",
	"lt" : "Lithuania" ,
	"lu" : "Luxembourg",
	"mo" : "Macao"  ,
	"mk" : "North Macedonia",
	"mg" : "Madagascar",
	"mw" : "Malawi" ,
	"my" : "Malaysia"  ,
	"mv" : "Maldives"  ,
	"ml" : "Mali",
	"mt" : "Malta"  ,
	"mh" : "Marshall Islands",
	"mq" : "Martinique",
	"mr" : "Mauritania",
	"mu" : "Mauritius" ,
	"yt" : "Mayotte",
	"mx" : "Mexico" ,
	"fm" : "Micronesia"  ,
	"md" : "Moldova" ,
	"mc" : "Monaco" ,
	"mn" : "Mongolia"  ,
	"me" : "Montenegro",
	"ms" : "Montserrat",
	"ma" : "Morocco",
	"mz" : "Mozambique",
	"mm" : "Myanmar",
	"na" : "Namibia",
	"nr" : "Nauru"  ,
	"np" : "Nepal"  ,
	"nl" : "Netherlands"  ,
	"nc" : "New Caledonia",
	"nz" : "New Zealand"  ,
	"ni" : "Nicaragua" ,
	"ne" : "Niger"  ,
	"ng" : "Nigeria",
	"nu" : "Niue",
	"nf" : "Norfolk Island"  ,
	"mp" : "Northern Mariana Islands" ,
	"no" : "Norway" ,
	"om" : "Oman",
	"pk" : "Pakistan"  ,
	"pw" : "Palau"  ,
	"ps" : "occupied Palestinian territory",
	"pa" : "Panama" ,
	"pg" : "Papua New Guinea",
	"py" : "Paraguay"  ,
	"pe" : "Peru",
	"ph" : "Philippines"  ,
	"pn" : "Pitcairn"  ,
	"pl" : "Poland" ,
	"pt" : "Portugal"  ,
	"pr" : "Puerto Rico"  ,
	"qa" : "Qatar"  ,
	"re" : "Reunion",
	"ro" : "Romania",
	"ru" : "Russian Federation" ,
	"rw" : "Rwanda" ,
	"bl" : "Saint Barthelemy",
	"sh" : "Saint Helena, Ascension and Tristan da Cunha"  ,
	"kn" : "Saint Kitts and Nevis" ,
	"lc" : "Saint Lucia"  ,
	"mf" : "Saint Martin (French part)"  ,
	"pm" : "Saint Pierre and Miquelon",
	"vc" : "Saint Vincent and the Grenadines"  ,
	"ws" : "Samoa"  ,
	"sm" : "San Marino",
	"st" : "Sao Tome and Principe" ,
	"sa" : "Saudi Arabia" ,
	"sn" : "Senegal",
	"rs" : "Serbia" ,
	"sc" : "Seychelles",
	"sl" : "Sierra Leone" ,
	"sg" : "Singapore" ,
	"sx" : "Sint Maarten (Dutch part)",
	"sk" : "Slovakia"  ,
	"si" : "Slovenia"  ,
	"sb" : "Solomon Islands" ,
	"so" : "Somalia",
	"za" : "South Africa" ,
	"gs" : "South Georgia and the South Sandwich Islands"  ,
	"ss" : "South Sudan"  ,
	"es" : "Spain"  ,
	"lk" : "Sri Lanka" ,
	"sd" : "Sudan"  ,
	"sr" : "Suriname"  ,
	"sj" : "Svalbard and Jan Mayen",
	"sz" : "Swaziland" ,
	"se" : "Sweden" ,
	"ch" : "Switzerland"  ,
	"sy" : "Syrian Arab Republic"  ,
	"tw" : "Taiwan, Province of China",
	"tj" : "Tajikistan",
	"tz" : "Tanzania, United Republic of",
	"th" : "Thailand"  ,
	"tl" : "Timor-Leste"  ,
	"tg" : "Togo",
	"tk" : "Tokelau",
	"to" : "Tonga"  ,
	"tt" : "Trinidad and Tobago",
	"tn" : "Tunisia",
	"tr" : "Turkey" ,
	"tm" : "Turkmenistan" ,
	"tc" : "Turks and Caicos Islands" ,
	"tv" : "Tuvalu" ,
	"ug" : "Uganda" ,
	"ua" : "Ukraine",
	"ae" : "United Arab Emirates"  ,
	"gb" : "United Kingdom",
	"us" : "US" ,
	"um" : "United States Minor Outlying Islands" ,
	"uy" : "Uruguay",
	"uz" : "Uzbekistan",
	"vu" : "Vanuatu",
	"ve" : "Venezuela (Bolivarian Republic of)",
	"vn" : "Viet Nam"  ,
	"vg" : "Virgin Islands (British)" ,
	"vi" : "Virgin Islands (U.S.)" ,
	"wf" : "Wallis and Futuna"  ,
	"eh" : "Western Sahara"  ,
	"ye" : "Yemen"  ,
	"zm" : "Zambia" ,
	"zw" : "Zimbabwe"
		}
def getcc(cc):
    return country_dict[cc.lower()]
    #thx hdbo		
def getfn(msg):
	script_fn = msg.split("\\")
	for x in range(0,len(script_fn),1):
		if ("VTSTech-COVID19.py" in script_fn[x]):
			return script_fn[x]
		elif (".py" in script_fn[x]):
			return script_fn[x]
def banner():	
	print("COVID-19 JHU.EDU CSSE Data Analytics\nv0.46 Written by VTSTech (www.VTS-Tech.org)\nData Source: https://github.com/CSSEGISandData/COVID-19\n")
def usage():
	spc=" "
	print("Usage:",getfn(sys.argv[0]),"-l")
	print(spc*6,getfn(sys.argv[0]),"-d 03-14-2020")
	print(spc*6,getfn(sys.argv[0]),"-a -dav\n")
	print("-v",spc*17,"verbose mode\n-l",spc*17,"list daily reports available\n-d MM-DD-YYYY",spc*6,"use this daily report\n-a",spc*18,end='')
	print("use all available reports\n-c",spc*17,"filter by this country (ISO 3166-1 Alpha-2)\n-t",spc*17,"calculate global total cases\n-td",end='')
	print(spc*17,"calculate global total deaths\n-gdr",spc*15,"calculate global death rate (use with -c for national)\n-dav",spc*15,"calculate daily average new cases\n-dad",end='')
	print(spc*16,"calculate daily average new deaths\n-dnc",spc*15,"calculate daily new cases\n-dnd",spc*15,"calculate daily new deaths\n-dgf",spc*16,end='')
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
		if (calc=="t") or (calc=="td") or (calc=="gdr"):
			for line in reports.split(".csv"):
				line=line+".csv"
				if (len(line)>4):
					tmp = parsereport(line.replace("\n",""),calc)
					if (tmp != 0 and tmp != None or verbose==1):print(tmp)
			if (calc=="t"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				print("\nTotal Cases")
			elif (calc=="td"):
				if (len(cc)>=1):
					print("\nCountry Filter:", getcc(cc))
				print("\nTotal Deaths")
			elif (calc=="gdr"):
				if (len(cc)>=1):
					print("\nNational Death Rate")
					print("\nCountry Filter:", getcc(cc))
				else:
					print("\nGlobal Death Rate")
			print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
		elif (calc=="dav")or(calc=="dad")or(calc=="din")or(calc=="dnc")or(calc=="dgf")or(calc=="dnd"):
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
				else:
					print("Global Average Daily New Cases:",round(davg_cases,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				else:
					print("Global Average Daily New Deaths:",round(davg_deaths,2))
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				else:
					print("\n\nGlobal Daily New Cases\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				else:
					print("\n\nGlobal Daily New Deaths\n")
				print("COVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				print("\n\nLargest Daily New Cases\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				else:
					print("\n\nGlobal Daily Growth Factor")
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
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
				else:
					print("\n\nGlobal Daily Death Rate Change")
				print("\nCOVID-19 JHU.EDU CSSE Data Analytics v0.46 by VTSTech Complete.")
	else:
		print("Error! This mode requires the -a parameter!")
def parsereport(report,calc):
	global mode
	global cc
	c_country=""
	c_prov=""
	c_cases=""
	c_deaths=""
	c_recov=""
	c_updated=""
	t_cases=0
	t_deaths=0
	gdr=0.0
	file_to_open = Path("csse_covid_19_data/csse_covid_19_daily_reports/" + report)
	if file_to_open.exists():
		f = open(file_to_open.absolute())
		cssereader = csv.reader(f, delimiter=',', quotechar='"')
		x=0
		for row in cssereader:
			if (x!=0):
				if (len(cc)>=1):
					if (getcc(cc) in row[1]):
						c_prov=row[0]
						c_country=row[1]
						c_updated=row[2]
						if (len(row[3])>0):
							c_cases=int(row[3])
							t_cases=int(t_cases+c_cases)
						if (len(row[4])>0):
							c_deaths=int(row[4])
							t_deaths=int(t_deaths+c_deaths)
						c_recov=row[5]
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
						c_recov=row[5]					
			x=x+1
		if (calc==""):
			print("Please select a metric to calculate: t, td, din, dav, dad, dnc, dnd, drc, gdr")
		elif (calc=="t"):
			if (mode=="onereport"):print("Total Cases:",t_cases)
			return(t_cases)
		elif (calc=="td"):
			if (mode=="onereport"):print("Total Deaths:",t_deaths)
			return(t_deaths)
		elif (calc=="gdr"):
			if (t_deaths!=0) and (t_cases!=0):
				gdr=round(float(t_deaths/t_cases)*100,3)
				c_date=str(report.split(".csv")[0])
				if (mode=="onereport"):print("Global Death Rate:",gdr,"%")
				#return(str(c_updated+" "+str(gdr)+"%"))
				return(c_date+" "+str(gdr)+"%")
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
		report=str(sys.argv[x+1]+".csv")
	elif (sys.argv[x] == "-t"):
		calc="t"
	elif (sys.argv[x] == "-td"):
		calc="td"
	elif (sys.argv[x] == "-gdr"):
		calc="gdr"
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
	elif (sys.argv[x] == "-c"):
		cc=sys.argv[x+1]
main(mode,report,cc,calc)