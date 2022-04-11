import configparser
import os

Config = configparser.ConfigParser()
Config
config_path = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(config_path,'config.ini')
Config.read(config_file)
Config.sections()
['COMPANY', 'PRESENTATION','PLEBIAN']


def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


comp = ConfigSectionMap("COMPANY")['company']
prod = ConfigSectionMap("COMPANY")['product_key']
pleb_name = ConfigSectionMap("PLEBIAN")["pleb"]

print(f'Company: {comp}\nKey: {prod}')
print("Presentation Folder: %s" % ConfigSectionMap('PRESENTATION')['presentation_dir'])

if pleb_name == "Nairnbot":
    print("Pleb is %s, and you need to RUN!" % pleb_name)
else:
    print("Pleb is %s, you're cool." % pleb_name)