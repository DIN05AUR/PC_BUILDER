import variables
from knowledge_base import knowledge_base

def interpret_option(numbers):
    variables.build_status = None
    # check if the user needs a gpu based on the input
    gpu_required = False
    for number in numbers:
        if number in [7, 8, 9, 10, 13, 14, 15, 16]:
            gpu_required = True

    # classify the input as low, mid and high
    for number in numbers:
        if number in [0, 1, 2, 3, 4]:
            classification = "low"
            variables.result_list.append(classification)
        elif number in [5, 6, 7, 8, 9, 10, 11, 12]:
            classification = "mid"
            variables.result_list.append(classification)
        elif number in [13, 14, 15, 16]:
            classification = "high"
            variables.result_list.append(classification)

    # determine the final build status for the user
    if "high" in variables.result_list:
        variables.build_status = "heavy"
    elif "mid" in variables.result_list:
        variables.build_status = "moderate"
    else:
        variables.build_status = "light"

    # print("Does the user require a GPU: ", gpu_required)
    # print("Build Status:", variables.build_status)
    return variables.result_list, gpu_required, variables.build_status


#------------------------------------------------------------------------------------------------------------------------

def interpret_budget(budget_option):
    if budget_option == 1:
        processor_1 = knowledge_base[variables.build_status]["high"]["processors"]["processor_1"]
        processor_2 = knowledge_base[variables.build_status]["high"]["processors"]["processor_2"]
        processor_3 = knowledge_base[variables.build_status]["high"]["processors"]["processor_3"]
        # ram_1 = knowledge_base[variables.build_status]["high"]["rams"]["ram_1"]
        # ram_2 = knowledge_base[variables.build_status]["high"]["rams"]["ram_2"]
        motherboard_1 = knowledge_base[variables.build_status]["high"]["motherboards"]["motherboard_1"]
        motherboard_2 = knowledge_base[variables.build_status]["high"]["motherboards"]["motherboard_2"]

        variables.quotation_1.update({"Processor": processor_1, "Motherboard": motherboard_1}),
        variables.quotation_2.update({"Processor": processor_2, "Motherboard": motherboard_2})

    elif budget_option == 2:
        processor_1 = knowledge_base[variables.build_status]["mid"]["processors"]["processor_1"]
        processor_2 = knowledge_base[variables.build_status]["mid"]["processors"]["processor_2"]
        processor_3 = knowledge_base[variables.build_status]["mid"]["processors"]["processor_3"]

        motherboard_1 = knowledge_base[variables.build_status]["mid"]["motherboards"]["motherboard_1"]
        motherboard_2 = knowledge_base[variables.build_status]["mid"]["motherboards"]["motherboard_2"]

        variables.quotation_1.update({"Processor": processor_1, "Motherboard": motherboard_1}),
        variables.quotation_2.update({"Processor": processor_2, "Motherboard": motherboard_2})

    elif budget_option == 3:
        processor_1 = knowledge_base[variables.build_status]["low"]["processors"]["processor_1"]
        processor_2 = knowledge_base[variables.build_status]["low"]["processors"]["processor_2"]
        processor_3 = knowledge_base[variables.build_status]["low"]["processors"]["processor_3"]

        motherboard_1 = knowledge_base[variables.build_status]["low"]["motherboards"]["motherboard_1"]
        motherboard_2 = knowledge_base[variables.build_status]["low"]["motherboards"]["motherboard_2"]

        variables.quotation_1.update({"Processor": processor_1, "Motherboard": motherboard_1}),
        variables.quotation_2.update({"Processor": processor_2, "Motherboard": motherboard_2})
    # print(quotation_1)
    return variables.quotation_1, variables.quotation_2