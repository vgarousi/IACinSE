# &#0x...; -> letra
# &ampm; -> &

# United Kingdom of Great Britain and Northern Ireland -> United Kingdom
# Engl -> United Kingdom
# Korea (the Republic of) -> South Korea
# West Ger -> West Germany
# Jpn -> Japan
# Can -> Canada
# British Indian Ocean Territory -> British Ind. Ocean Territory
# Hong Kong -> China ?

# Indiana ... United States -> United States
# New Mexico ... United States -> United States
# Georgia ... United States -> Georgia, United States
# University of Macedonia ... Greece -> Greece
# Inner Mongolia University ... China -> China
# Colombia ... United States -> United States
# East Azerbaijan, Iran -> Iran


countries = [
  "Afghanistan",
  "Albania",
  "Algeria",
  "American Samoa",
  "Andorra",
  "Angola",
  "Anguilla",
  "Antigua & Barbuda",
  "Argentina",
  "Armenia",
  "Aruba",
  "Australia",
  "Austria",
  "Azerbaijan",
  "Bahamas",
  "Bahrain",
  "Bangladesh",
  "Barbados",
  "Belarus",
  "Belgium",
  "Belize",
  "Benin",
  "Bermuda",
  "Bhutan",
  "Bolivia",
  "Bonaire",
  "Bosnia & Herzegovina",
  "Botswana",
  "Brazil",
  "Brunei",
  "Bulgaria",
  "Burkina Faso",
  "Burundi",
  "Cambodia",
  "Cameroon",
  "Canada",
  "Canary Islands",
  "Cape Verde",
  "Cayman Islands",
  "Central African Republic",
  "Chad",
  "Channel Islands",
  "Chile",
  "China",
  "Christmas Island",
  "Cocos Island",
  "Colombia",
  "Comoros",
  "Congo",
  "Cook Islands",
  "Costa Rica",
  "Cote DIvoire",
  "Croatia",
  "Cuba",
  "Curacao",
  "Cyprus",
  "Czech Republic",
  "Denmark",
  "Djibouti",
  "Dominica",
  "Dominican Republic",
  "East Timor",
  "Ecuador",
  "Egypt",
  "El Salvador",
  "Equatorial Guinea",
  "Eritrea",
  "Estonia",
  "Ethiopia",
  "Falkland Islands",
  "Faroe Islands",
  "Fiji",
  "Finland",
  "France",
  "French Guiana",
  "French Polynesia",
  "French Southern Ter",
  "Gabon",
  "Gambia",
  #"Georgia",
  "Germany",
  "Ghana",
  "Gibraltar",
  "Great Britain",
  "Greece",
  "Greenland",
  "Grenada",
  "Guadeloupe",
  "Guam",
  "Guatemala",
  "Guinea",
  "Guyana",
  "Haiti",
  "Honduras",
  "Hong Kong",
  "Hungary",
  "Iceland",
  "Indonesia",
  "India",
  "British Ind. Ocean Territory",
  "Iran",
  "Iraq",
  "Ireland",
  "Isle of Man",
  "Israel",
  "Italy",
  "Jamaica",
  "Japan",
  "Jordan",
  "Kazakhstan",
  "Kenya",
  "Kiribati",
  "North Korea",
  "South Korea",
  "Kuwait",
  "Kyrgyzstan",
  "Laos",
  "Latvia",
  "Lebanon",
  "Lesotho",
  "Liberia",
  "Libya",
  "Liechtenstein",
  "Lithuania",
  "Luxembourg",
  "Macau",
  "Macedonia",
  "Madagascar",
  "Malaysia",
  "Malawi",
  "Maldives",
  "Mali",
  "Malta",
  "Marshall Islands",
  "Martinique",
  "Mauritania",
  "Mauritius",
  "Mayotte",
  "Mexico",
  "Midway Islands",
  "Moldova",
  "Monaco",
  "Mongolia",
  "Montserrat",
  "Morocco",
  "Mozambique",
  "Myanmar",
  "Nambia",
  "Nauru",
  "Nepal",
  "Netherland Antilles",
  "Netherlands", # (Holland, Europe)",
  "Nevis",
  "New Caledonia",
  "New Zealand",
  "Nicaragua",
  "Niger",
  "Nigeria",
  "Niue",
  "Norfolk Island",
  "Norway",
  "Oman",
  "Pakistan",
  "Palau Island",
  "Palestine",
  "Panama",
  "Papua New Guinea",
  "Paraguay",
  "Peru",
  "Philippines",
  "Pitcairn Island",
  "Poland",
  "Portugal",
  "Puerto Rico",
  "Qatar",
  "Montenegro",
  "Serbia",
  "Reunion",
  "Romania",
  "Russia",
  "Rwanda",
  "St Barthelemy",
  "St Eustatius",
  "St Helena",
  "St Kitts-Nevis",
  "St Lucia",
  "St Maarten",
  "St Pierre & Miquelon",
  "St Vincent & Grenadines",
  "Saipan",
  "Samoa",
  "Samoa American",
  "San Marino",
  "Sao Tome",  # & Principe",
  "Saudi Arabia",
  "Senegal",
  "Seychelles",
  "Sierra Leone",
  "Singapore",
  "Slovakia",
  "Slovenia",
  "Solomon Islands",
  "Somalia",
  "South Africa",
  "Spain",
  "Sri Lanka",
  "Sudan",
  "Suriname",
  "Swaziland",
  "Sweden",
  "Switzerland",
  "Syria",
  "Tahiti",
  "Taiwan",
  "Tajikistan",
  "Tanzania",
  "Thailand",
  "Togo",
  "Tokelau",
  "Tonga",
  "Trinidad & Tobago",
  "Tunisia",
  "Turkey",
  "Turkmenistan",
  "Turks & Caicos Is",
  "Tuvalu",
  "Uganda",
  "United Kingdom",
  "Ukraine",
  "United Arab Emirates",
  "United States", # of America",
  "USA", # of America",
  "Uruguay",
  "Uzbekistan",
  "Vanuatu",
  "Vatican City State",
  "Venezuela",
  "Vietnam",
  "Virgin Islands", # (Brit)",
 # "Virgin Islands (USA)",
  "Wake Island",
  "Wallis & Futana Is",
  "Yemen",
  "Zaire",
  "Zambia",
  "Zimbabwe"
]  

acaTerms = [
  ".edu",
  "Academ",
  "CEA",
  "CEFRIEL",
  "Centrum voor Wiskunde en Informatica",
  "CNAM",
  "CNR",
  "College",
  "CONICET",
  "COTEMIG",
  "CWI",
  "Democritos",
  "Dhirubhai Ambani Institute",
  "Ecole",
  "Educa",
  "ENS Cachan",
  "ENST",
  "Escuela",
  "ETS",
  "ETH Zurich",
  "Faculty",
  "FBK",
  "Fondazione Bruno Kessler",
  "Fraunhofer",
  "GMD",
  "Gran Sasso",
  "Hochschule",
  "IFAL",
  "IIT Madras",
  "IMDEA",
  "Indian Institute of Sience",
  "Indraprastha Institute of Information Technology",
  "INESC",
  "INRIA",
  "Institut",
  # "Institute of Science",
  # "Institute of Technology",
  # "Instituto",
  # "Institut EURECOM",
  # "Institut fur Informatik",
  # "Institute for Experimental Software Engineering",
  "IRISA",
  "ISISTAN",
  "ISTI",
  "Istituto",
  "ITC-irst",
  "KAIST",
  "King Abdulaziz City",
  "LAAS",
  "Laboratoire",
  "LERO",
  "M.I.T.",
  "Naval Research",
  "NEC",
  "New Mexico Institute of Mining and Technology",
  "NTNU",
  "Penn State",
  "Politec",
  "Polytech",
  "PUC-Rio",
  "Rational Software",
  "RWTH",
  "School",
  "Scuola",
  "Simula",
  "SINTEF",
  "SnT Centre for Security",
  "SRI International",
  "Stevens Institute",
  "SUNY",
  "Technion",
  "Tekniska Hogskola",
  "Turkiye Bilimsel ve Teknolojik Arastirma Kurumu",
  "Uceni Technicke",
  "UCSD",
  "UFMG",
  "UFRJ",
  "UMIST",
  "UNIRIO",
  "Univ",
  "USC",
  "USI",
  "Virginia Tech",
  "VTT",
  "Weizmann",
  "Yliopisto",
]

indTerms = [
  "ABB",
  "Accenture",
  "AEG",
  "Alcatel",
  "Alibaba",
  "Alstom Signalling",
  "Amazon",
  "AT&T",
  "Avaya",
  "B.V.",
  "Bank",
  "Bell ",
  "Bellcore",
  "BlackBerry",
  "Bloomberg",
  "BNP Paribas",
  "Boeing",
  "Bosch",
  "Cisco",
  "Cistel Technology",
  "Codecentric AG",
  "Co.",
  "Combitech AB",
  "Company",
  "Consulting",
  "Corp",
  "Corporation",
  "Daimler",
  "Danfoss",
  "Dell",
  "Delphi",
  "ENEL-SRI",
  "Ericsson",
  "Facebook",
  "General Electric",
  "General Motors",
  "GmbH",
  "Google",
  "Grundfos",
  "Hewlett-Packard",
  "Honeywell",
  "Hospital",
  "Huawei",
  "Husqvarna",
  "Hyundai",
  "IBM",
  "Inc",
  "Industries",
  "Industry",
  "Intel ",
  "ITA",
  "JetBrains",
  "Kestrel Institute",
  "Lexmark",
  "Limited",
  "Lockheed",
  "Ltd",
  "Lucent Technologies",
  "Medidata Solutions",
  "Microsoft",
  "Motorola",
  "NASA",
  "Nokia",
  "Nortel",
  "Oracle",
  "Oy",
  "Philips",
  "Praxis Critical Systems",
  "PricewaterhouseCoopers",
  "Prodevelop",
  "Saab",
  "Samsung",
  "SAP",
  "Scania",
  "Schlumberger",
  "Siemens",
  "Sony",
  "SpA",
  "S.p.A",
  "Sperry",
  "Statoil",
  "Sun Microsystems",
  "Symantec",
  "Tata",
#  "Telecom",
  "Telefonica",
  "Telelogic",
  "TRW",
  "TyCloud",
  "UBER",
  "Unisys",
  "Verilog",
  "Xerox",
  "Xpand IT"
]

govTerms = [
  "Air Force",
  "Army",
  "Cancer Registry of Norway",
  "Navy",
  "Police",
  "Space Agency",
  "Tax"
]

def correctSpelling (countryName):
    if countryName == "USA":
       return ("United States")
    if countryName == "British Ind. Ocean Territory":
       return ("British Indian Ocean Territory")
    if countryName == "Hong Kong":
       return ("China")
    return (countryName)

def printAIG ():
    file = open("Data-Scopus.txt")
    biblioEntriesLines = file.readlines()
    i=0
    papersNotClassified = 0
    for entryLine in biblioEntriesLines:
        # -------------- PRINT COUNTRIES --------------
        #print i
        i = i+1
        entry = entryLine.split("### ", -1)
        typePaper = entry[-1].strip()
        yearPaper = entry[2].strip()
        authors = entry[6].split(";", -1)
        #print ("----------")
        #print (authors)
        #academia = 0
        #industry = 0
        if typePaper=="Article in Press" or typePaper=="Article" or typePaper=="Conference Paper":
            #print ("-----------")
            nrAcad=0
            nrIndu=0
            nrGove=0
            nrNotC=0
            paperCountries = set()
            for author in authors:
                authorCountry = {correctSpelling(country) for country in countries if country in author}
                paperCountries.update(authorCountry)
                acad = ""
                indu = ""
                gove = ""
                notC = ""
                listAcademia   = {univ.strip() for univ in acaTerms if univ in author}
                listIndustry   = {indu.strip() for indu in indTerms if indu in author}
                listGovernment = {gove.strip() for gove in govTerms if gove in author}
                if listAcademia != set():
                    acad = "A"
                    nrAcad += 1
                if listIndustry != set():
                    indu = "I"
                    nrIndu += 1
                if listGovernment != set():
                    gove = "G"
                    nrGove += 1
                if listAcademia == set() and listIndustry == set() and listGovernment == set():
                    notC = "N"
                    nrNotC += 1
                if authorCountry == set():
                   print (str(i)+"\t"+acad+"\t"+indu+"\t"+gove+"\t"+notC+"\t"+"*"+"*".join(listAcademia)+"*"+"*".join(listIndustry)+"*"+"*".join(listGovernment)+"\tNO-COUNTRY\t"+yearPaper+"\t"+author.strip())
                else:    
                   print (str(i)+"\t"+acad+"\t"+indu+"\t"+gove+"\t"+notC+"\t"+"*"+"*".join(listAcademia)+"*"+"*".join(listIndustry)+"*"+"*".join(listGovernment)+"\t"+str(authorCountry)[6:-3]+"\t"+yearPaper+"\t"+author.strip())
            #if nrNotC>0:
            #    papersNotClassified += 1
    #print papersNotClassified            
            #if paperCountries == set():
            #    print ("\t\t"+str(nrAcad)+"\t"+str(nrIndu)+"\t"+typePaper+"\tNO-COUNTRY\t"+yearPaper)
            #else:    
            #    print ("\t\t"+str(nrAcad)+"\t"+str(nrIndu)+"\t"+typePaper+"\t"+str(paperCountries)[6:-3]+"\t"+yearPaper)
#        else:
#            print ("\tIGNORED "+typePaper)

def printCountries ():
    file = open("Data-Scopus.txt")
    biblioEntriesLines = file.readlines()
    totalSetCountries = set()
    for entryLine in biblioEntriesLines:
        # -------------- PRINT COUNTRIES --------------
        entry = entryLine.split("### ", -1)
        #print (entry[6])
        authors = entry[6].split(";", -1)
        typePaper = entry[-1].strip()
        print ("----------")
        listPaperCountries = []
        authorNumber=1
        if typePaper!="Article in Press" and typePaper!="Article" and typePaper!="Conference Article":
            print ("IGNORED "+typePaper)
        else:
            for author in authors:
                #if typePaper == "Art"
                print (str(authorNumber)+": "+author.strip())
                setCountry = {country for country in countries if country in author}
                if setCountry == set():
                    listPaperCountries.append("NO-COUNTRY")
                else:
                    if len(setCountry)>1:
                        listCountry = list(setCountry) 
                        if author.rindex(listCountry[0]) > author.rindex(listCountry[1]):
                            listPaperCountries.append(correctSpelling(listCountry[0]))
                            totalSetCountries.add(correctSpelling(listCountry[0]))
                        else:
                            listPaperCountries.append(correctSpelling(listCountry[1]))
                            totalSetCountries.add(correctSpelling(listCountry[1]))
                    else:    
                        listPaperCountries.append(correctSpelling(min(setCountry)))
                        totalSetCountries.add(correctSpelling(min(setCountry)))
                authorNumber += 1
            print (listPaperCountries)
    print ("----------------------------------")
    print ("--------- ALL COUNTRIES ----------")
    print (totalSetCountries)           
 
#printCountries ()
printAIG()

