import pandas as pd
import json


class Error(Exception):
    """Base class for other exceptions"""
    pass


class EmptyTestArray(Error):
    """Raised when the input json has empty test array i.e. no test available"""
    pass

class TestNotArray(Error):
    """ Raised when the Data Type of Tests Key in input json is not a list"""
    pass

class MinMoveTypeError(Error):
    """ Raised If Data Type of MinMove is not Integer/float"""
    pass

class MaxMoveTypeError(Error):
    """ Raised If Data Type of MaxMove is not Integer/float"""
    pass

class MinMove_IsMore_maxMove(Error):
    """Raised when MinMove is more than the MaxMove which should not be the case"""
    pass

class ValveIDError(Error):
    """Raised when data type of valve id is not an interger"""
    pass

class KPInameError(Error):
    """Raised when data type of KPI name is not an string"""
    pass


def movementfunc(input_json,config_json):
        try:
            wrong_values = ['None','nan','inf','-inf']

            if not isinstance(input_json['Tests'], list ) :
                raise TestNotArray

            if len(input_json['Tests']) == 0:
                raise EmptyTestArray
               
            if not isinstance(input_json['MinMove'], (int,float) ) :
                raise MinMoveTypeError

            if str(input_json['MinMove']) in wrong_values:
                raise MinMoveTypeError

            if not isinstance(input_json['MaxMove'], (int,float) ) :
                raise TypeError

            if str(input_json['MaxMove']) in wrong_values:
                raise MaxMoveTypeError

            if input_json['MinMove'] >= input_json['MaxMove']:
                raise MinMove_IsMore_maxMove

            if not isinstance(input_json['Valve_id'], int ) :
                raise ValveIDError

            if not isinstance(input_json['KPI_Name'], str ) :
                raise KPInameError

        except MinMoveTypeError:
            print('Data Type of MinMove is not an Integer or Float')
            return 3007

        except MaxMoveTypeError:
            print('Data Type of MaxMove is not an Integer or Float')
            return 3008

        except EmptyTestArray :
            print('Warning : Empty Tests Array')
            return 3004

        except MinMove_IsMore_maxMove :
            print('MinMove must be less than MaxMove')
            return 3009                                                                                     

        except TestNotArray:
            print('Data Type of Tests Is Not Correct')
            return 3003                                                                     

        except ValveIDError :
            print('Valve ID must be an integer value')
            return 3005

        except KPInameError :
            print('KPI Name must be a string value')
            return 3006

        else:

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
                move_filter = ( df['Move'] >= input_json['MinMove'] ) & ( df['Move'] <= input_json['MaxMove'] )
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

