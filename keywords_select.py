# -*- coding:utf-8 -*-
_author_ = "Youwei Xiao"

import json
test_passage = json.load(open("xuan.json"))

keyword_criminal_legislation= []
keyword_regulation_compliance = []
keyword_cirt = []
keyword_standards = []
keyword_certification = []
keyword_policy = []
keyword_roadmap = []
keyword_responsible_agency = []
keyword_benchmarking = []
keyword_standardisation = []
keyword_manpower = []
keyword_professional = []
keyword_agency = []
keyword_intra_state = []
keyword_intra_agency = []
keyword_public_sector = []
keyword_international_cooperation = []
keyword_national_legislation = []
keyword_un_convention_protocol = []
keyword_institutional_support = []
keyword_reporting_mechanism = []

# print len(test_passage)

for i in range(len(test_passage)):
    for element in test_passage[i]["keywords"]:
        if element.has_key("criminal legislation"):
            keyword_criminal_legislation.append(element["criminal legislation"])
            print "criminal legislation : ", keyword_criminal_legislation
        if element.has_key("regulation and compliance"):
            keyword_regulation_compliance.append(element["regulation and compliance"])
            print "regulation and compliance : ", keyword_regulation_compliance
        if element.has_key("cirt"):
            keyword_cirt.append(element["cirt"])
            print "cirt : ", keyword_cirt
        if element.has_key("standards"):
            keyword_standards.append(element["standards"])
            print "standards : ", keyword_standards
        if element.has_key("certification"):
            keyword_certification.append(element["certification"])
            print "certification : ", keyword_certification
        if element.has_key("policy"):
            keyword_policy.append(element["policy"])
            print "policy : ",keyword_policy
        if element.has_key("roadmap for governance"):
            keyword_roadmap.append(element["roadmap for governance"])
            print "roadmap for governance : ", keyword_roadmap
        if element.has_key("responsible agency"):
            keyword_responsible_agency.append(element["responsible agency"])
            print "responsible agency : ", keyword_responsible_agency
        if element.has_key("national benchmarking"):
            keyword_benchmarking.append(element["national benchmarking"])
            print "national benchmarking : ", keyword_benchmarking
        if element.has_key("standardisation development"):
            keyword_standardisation.append(element["standardisation development"])
            print "standardisation development : ", keyword_standardisation
        if element.has_key("manpower development"):
            keyword_manpower.append(element["manpower development"])
            print "manpower development : ", keyword_manpower
        if element.has_key("professional certification"):
            keyword_professional.append(element["professional certification"])
            print "professional certification : ", keyword_professional
        if element.has_key("agency certification"):
            keyword_agency.append(element["agency certification"])
            print "agency certification : ", keyword_agency
        if element.has_key("intra-state cooperation"):
            keyword_intra_state.append(element["intra-state cooperation"])
            print "intra-state cooperation : ", keyword_intra_state
        if element.has_key("intra-agency cooperation"):
            keyword_intra_agency.append(element["intra-agency cooperation"])
            print "intra-agency cooperation : ", keyword_intra_agency
        if element.has_key("public sector partnership"):
            keyword_public_sector.append(element["public sector partnership"])
            print "public sector partnership : ", keyword_public_sector
        if element.has_key("international cooperation"):
            keyword_international_cooperation.append(element["international cooperation"])
            print "international cooperation : ", keyword_international_cooperation
        if element.has_key("national legislation"):
            keyword_national_legislation.append(element["national legislation"])
            print "national legislation : ", keyword_national_legislation
        if element.has_key("un convention and protocol"):
            keyword_un_convention_protocol.append(element["un convention and protocol"])
            print "un convention and protocol : ", keyword_un_convention_protocol
        if element.has_key("institutional support"):
            keyword_institutional_support.append(element["institutional support"])
            print "institutional support", keyword_institutional_support
        if element.has_key("reporting mechanism"):
            keyword_reporting_mechanism.append(element["reporting mechanism"])
            print "reporting mechanism", keyword_reporting_mechanism
        else:
            print "nothing"

print("criminal legislation : ", keyword_criminal_legislation)
print("regulation and compliance : ", keyword_regulation_compliance)
print("cirt : ", keyword_cirt)
print("standards : ", keyword_standards)
print("certification : ", keyword_certification)
print("policy : ", keyword_policy)
print("roadmap for governance : ", keyword_roadmap)
print("responsible agency : ", keyword_responsible_agency)
print("national benchmarking : ", keyword_benchmarking)
print("standardisation development : ", keyword_standardisation)
print("manpower development : ", keyword_manpower)
print("professional certification : ", keyword_professional)
print("agency certification : ", keyword_agency)
print("intra-state cooperation : ", keyword_intra_state)
print("intra-agency cooperation : ", keyword_intra_agency)
print("public sector partnership : ", keyword_public_sector)
print("international cooperation : ", keyword_international_cooperation)
print("national legislation : ", keyword_national_legislation)
print("un convention and protocol : ", keyword_un_convention_protocol)
print("institutional support : ", keyword_institutional_support)
print("reporting mechanism : ", keyword_reporting_mechanism)

# for i in keyword_criminal_legislation:
#     print i

