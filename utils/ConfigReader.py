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