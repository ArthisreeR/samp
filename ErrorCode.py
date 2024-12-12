class errorCode(object):
    """docstring for ErrorCode"""
    def __init__(self):
        self.ErrorCodeDict = dict()

    def obtain_errorCode(self, errCode):
        
        self.ErrorCodeDict[3001] = "Data Type of N_most_repeats is not an Integer"
        self.ErrorCodeDict[3002] = "Data Type of Percentage_limit is not an Integer or Float"
        self.ErrorCodeDict[3003] = "Data Type of Tests Is Not Correct"
        self.ErrorCodeDict[3004] = "Warning, Empty Tests Array"
        self.ErrorCodeDict[3005] = "Valve ID must be an integer value"
        self.ErrorCodeDict[3006] = "KPI Name must be a string value"
        self.ErrorCodeDict[3007] = "Data Type of MinMove is not an Integer or Float"
        self.ErrorCodeDict[3008] = "Data Type of MaxMove is not an Integer or Float"
        self.ErrorCodeDict[3009] = "MinMove must be less than MaxMove"
        self.ErrorCodeDict[3011] = "Data Type of MinPosition is not an Integer or Float"
        self.ErrorCodeDict[3012] = "Data Type of MaxPosition is not an Integer or Float"
        self.ErrorCodeDict[3013] = "Data Type of Multiplier is not an Integer or Float"
        self.ErrorCodeDict[3014] = "Data Type of Algorithm is not correct or if not in either of STD or IQR(case sensitive)"
        self.ErrorCodeDict[3015] = "There Should Be At Least Two Data Points"
        self.ErrorCodeDict[3016] = "Mismatch in KPI names"
        self.ErrorCodeDict[3017] = "Sanity Quality Bad"
        self.ErrorCodeDict[3021] = "Upper limit must be greater than lower limit"
        self.ErrorCodeDict[3022] = "Model Details are not correct"
        self.ErrorCodeDict[3023] = "Value of User Configurable Parameter is not correct"
        self.ErrorCodeDict[3024] = "Data type of Start Date is not a string"
        self.ErrorCodeDict[3025] = "Data type of End Date is not a string"
        self.ErrorCodeDict[3026] = "Data type of Start Gap Threshold  is not an integer/float"
        self.ErrorCodeDict[3027] = "Data type of Middle Gap Threshold  is not an integer/float"
        self.ErrorCodeDict[3028] = "Data type of End Gap Threshold  is not an integer/float"
        self.ErrorCodeDict[3029] = "The given float or integer for start gap is not between 0 to 100"
        self.ErrorCodeDict[3031] = "The given float or integer for middle gap is not between 0 to 100"
        self.ErrorCodeDict[3032] = "The given float or integer for end gap is not between 0 to 100"
        self.ErrorCodeDict[3033] = "The end date is before the start date"

        self.ErrorCodeDict[3034] = "Multiplier should be an array"
        self.ErrorCodeDict[3035] = "Data Type of KPI Observation Is Not Correct"
        self.ErrorCodeDict[3036] = "Atleast one KPI should be selected for recommendation"
        self.ErrorCodeDict[3037] = "Data Type of ConcernWeights Is Not Correct"
        self.ErrorCodeDict[3038] = "Atleast one concern and its weights should be mentioned"
        self.ErrorCodeDict[3039] = "The KPIs in these recommendations IDs str_ids are not matching with observation json"

        self.ErrorCodeDict[3051] = "ID2 must be a string"
        self.ErrorCodeDict[3052] = "Valve Action is not a string or unavailable"
        self.ErrorCodeDict[3053] = "Valve Type is not a string or unavailable"
        self.ErrorCodeDict[3054] = "Configuration (condition) is empty"

        self.ErrorCodeDict[3055] = "The value of KPIs is null"
        self.ErrorCodeDict[3056] = "The value of ConditionList is null"

        self.ErrorCodeDict[3057] = "None of the rule matches with the Configuration"


        return self.ErrorCodeDict[errCode]