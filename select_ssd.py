from knowledge_base import knowledge_base
import variables
def select_ssds(build_status, budget_option):
    if build_status == "heavy" and budget_option == 1:
        ssd_1 = knowledge_base["heavy"]["high"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["heavy"]["high"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["heavy"]["high"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["heavy"]["high"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["heavy"]["high"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3, variables.quotation_4]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3, variables.quotation_4

    elif build_status == "heavy" and budget_option == 2:
        ssd_1 = knowledge_base["heavy"]["mid"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["heavy"]["mid"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["heavy"]["mid"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["heavy"]["mid"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["heavy"]["mid"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "heavy" and budget_option == 3:
        ssd_1 = knowledge_base["heavy"]["low"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["heavy"]["low"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["heavy"]["low"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["heavy"]["low"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["heavy"]["low"]["ssd"]["ssd_5"]
        ssd_6 = knowledge_base["heavy"]["low"]["ssd"]["ssd_6"]
        ssd_7 = knowledge_base["heavy"]["low"]["ssd"]["ssd_7"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
                "SSD 6": ssd_6,
                "SSD 7": ssd_7
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "moderate" and budget_option == 1:
        ssd_1 = knowledge_base["moderate"]["high"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["moderate"]["high"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["moderate"]["high"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["moderate"]["high"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["moderate"]["high"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "moderate" and budget_option == 2:
        ssd_1 = knowledge_base["moderate"]["mid"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["moderate"]["mid"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["moderate"]["mid"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["moderate"]["mid"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["moderate"]["mid"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "moderate" and budget_option == 3:
        ssd_1 = knowledge_base["moderate"]["low"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["moderate"]["low"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["moderate"]["low"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["moderate"]["low"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["moderate"]["low"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "light" and budget_option == 1:
        ssd_1 = knowledge_base["light"]["high"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["light"]["high"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["light"]["high"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["light"]["high"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["light"]["high"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "light" and budget_option == 2:
        ssd_1 = knowledge_base["light"]["mid"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["light"]["mid"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["light"]["mid"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["light"]["mid"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["light"]["mid"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3

    elif build_status == "light" and budget_option == 3:
        ssd_1 = knowledge_base["light"]["low"]["ssd"]["ssd_1"]
        ssd_2 = knowledge_base["light"]["low"]["ssd"]["ssd_2"]
        ssd_3 = knowledge_base["light"]["low"]["ssd"]["ssd_3"]
        ssd_4 = knowledge_base["light"]["low"]["ssd"]["ssd_4"]
        ssd_5 = knowledge_base["light"]["low"]["ssd"]["ssd_5"]

        for i in [variables.quotation_1, variables.quotation_2, variables.quotation_3]:
            i.update({
                "SSD OPTIONS": "",
                "SSD 1": ssd_1,
                "SSD 2": ssd_2,
                "SSD 3": ssd_3,
                "SSD 4": ssd_4,
                "SSD 5": ssd_5,
            })
        return variables.quotation_1, variables.quotation_2, variables.quotation_3




