import pandas as pd
import json

def movementfunc(input_json,config_json):
        output_dict = {
                "Valve_id": input_json['Valve_id'],
                "KPI_Name": input_json['KPI_Name'],
                "KPI_Units": input_json['KPI_Units'],
                "MinMove": config_json["Movement_Config"]["Min_Move"],
                "MaxMove": config_json["Movement_Config"]["Max_Move"],
                "Removed": [] ,
                "OutPointQuality": "",
                "Details": "" ,
                "OutNoPoints": "",
                "Tests":[]
                }
        df = pd.DataFrame(input_json['Tests'])
        df['Move'] = df['PR_high']- df['PR_low']
        move_filter = ( df['Move'] >=config_json["Movement_Config"]["Min_Move"] ) & ( df['Move'] <= config_json["Movement_Config"]["Max_Move"])
        df_within_limit = df [ move_filter ]
        df_outside_limit = df [ ~move_filter ]
        print(df_within_limit.shape)
        print(df_outside_limit.shape)


        output_dict["OutPointQuality"] = 'Good'
        output_dict["OutNoPoints"] = df_within_limit.shape[0]
        output_dict["Details"] = ''
        output_dict["Removed"] = df_outside_limit.to_dict('records') 
        output_dict["Tests"] = df_within_limit.to_dict('records') 
        print(output_dict)
        return output_dict 

