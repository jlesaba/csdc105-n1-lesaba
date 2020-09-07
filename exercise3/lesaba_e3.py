# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BS Computer Science
# Filename        : lesaba_e3.py
# Description     : Graded Lab Exercise 3: Command-Line Arguments and Branching Statements
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
import sys

if len(sys.argv) < 3:
    print("Usage: python3 ./lesaba_e3.py <activity or sector> <quarantine classification>")
else:
    activity_or_sector = sys.argv[1].lower()
    quarantine_classification = sys.argv[2].lower()

    people = {"ecq": "100% stay at home; Exception for workers in offices or industries permitted to operate",
                "mecq": "100% stay at home; Restricted movement, only for accessing essential goods and services; Exception for workers in offices or industries permitted to operate; Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home",
                "gcq": "Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home",
                "mgcq": "Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home"
                }

    transport = {"ecq": "No domestic flights, with limited international flights; Public transportation is not allowed; Shuttle services for employees of permitted offices or establishments, as well as point-to-point transport service, granted permission to operate by the government, with healthcare workers and other frontliners given priority",
                "mecq": "No domestic flights, with limited international flights; Controlled inbound flights; No inter-island travel; Public transportation is not allowed; Private transportation such as company shuttles and personal vehicles allowed subject to the guidelines provided by the Department of Transportation (DOTr); Biking and non-motorized transport encouraged",
                "gcq": "Public transport is allowed with strict social distancing; Inter-island travel from GCQ to GCQ allowed with safety protocols.",
                "mgcq": "Public transport is allowed with strict social distancing Inter-island travel from GCQ to GCQ allowed with safety protocols."
                }

    gatherings = {"ecq": "Mass gatherings are not allowed; Only mass gatherings that are essential for the provision of government services or authorized humanitarian activities permitted",
                "mecq": "Highly restricted (maximum of 5); Non-essential work gatherings are prohibited",
                "gcq": "Gatherings are limited to not more than ten (10) persons; Non-essential work gatherings are prohibited",
                "mgcq": "Fifty percent (50%) of the seating or venue capacity for movie screenings, concerts, sporting events, and other entertainment activities, religious services, and work conferences"
                }

    schools = {"ecq": "School premises are closed",
                "mecq": "School premises are closed",
                "gcq": "Skeletal workforce permitted in schools; Face-to-face or in-person classes are suspended",
                "mgcq": "Limited face-to-face or in-person classes may be conducted; strict compliance with minimum public health standards and consultations with local government units (LGUs) and guidelines set by the Commission on Higher Education (CHED)"
                }

    work = {"ecq": "Select industry workers permitted",
                "mecq": "Essential industries permitted to work at full capacity, with others operating at a fifty percent (50%) capacity; Work-from-home and other flexible work arrangements encouraged",
                "gcq": "Alternative work arrangements",
                "mgcq": "Full operating capacity for work in all public and private offices; Alternative work arrangements for persons who are sixty (60) years old and above, or those with other health risks"
                }

    government = {"ecq": "Skeletal workforce onsite;Work from home arrangements",
                "mecq": "Skeletal workforce onsite; Work from home arrangements",
                "gcq": "Work in all government offices under alternative work arrangements",
                "mgcq": "Work in government offices may be at full operational capacity, or under alternative work arrangements  Exercise and Sports"
                }

    if activity_or_sector == "people" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in people.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    elif activity_or_sector == "transport" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in transport.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    elif activity_or_sector == "gatherings" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in gatherings.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    elif activity_or_sector == "schools" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in schools.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    elif activity_or_sector == "work" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in work.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    elif activity_or_sector == "government" and (quarantine_classification == "ecq" or quarantine_classification == "mecq" or quarantine_classification == "gcq" or quarantine_classification == "mgcq"):
        for (type_of_quarantine, ruling) in government.items():
            if quarantine_classification == type_of_quarantine:
                print(ruling)
    else:
        print("Error: Invalid input")