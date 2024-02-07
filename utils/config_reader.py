import configparser


class ConfigReader:

    def get_parameters(self, parameter_name):
        config = configparser.ConfigParser()
        config.read('./config.ini')

        values = []

        items = config[parameter_name]['items'].split(',')

        for i in range(len(items)):
            values.append(items[i].replace('\"', ''))

        return values

    def get_test_case_fields_from_config(self):
        test_case_fields = ConfigReader().get_parameters("DEFAULT")
        test_case_fields.extend(ConfigReader().get_parameters("EXTENDED"))
        test_case_fields.extend(ConfigReader().get_parameters("CUSTOM"))

        return test_case_fields