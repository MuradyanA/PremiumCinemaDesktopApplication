import json
import os

from Exceptions.ParamDoesntExistsExcepion import ParamDoesntExistsException


class AppSetting:
    params = {}

    def __init__(self):
        self.get_params_from_file()

    def get_params_from_file(self):
        if os.path.exists('settings.json'):
            if os.path.getsize('settings.json') > 0:
                with open("settings.json", "r") as f:
                    AppSetting.params = json.load(f)
        else:
            open("settings.json", "x")

    def get_param(self, param_name):
        try:
            return AppSetting.params[param_name]
        except KeyError as e:
            raise ParamDoesntExistsException(e.args[0])

    def set_param(self, param_name, value):
        AppSetting.params[param_name] = value
        params = json.dumps(AppSetting.params)
        with open("settings.json", "w") as f:
            # Write the JSON string to the file
            f.write(params)

            # Close the file
            f.close()



