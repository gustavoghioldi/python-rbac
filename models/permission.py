import yaml
import os
class Permission:  
    @staticmethod
    def get_permissions_names():
        r=list()
        with open(os.environ['PERMISSIONS_YAML']) as file:
            permissions = yaml.load(file, Loader=yaml.FullLoader)
            for service in permissions['services']:
                for res in permissions['services'][service]:
                    for action in permissions['services'][service][res]['actions']:
                        r.append('{}_{}_{}'.format(service, res, action))
        return r
    
    @staticmethod
    def can(permisions_object, service, service_path, cli_method):
        permissions = None
        with open(os.environ['PERMISSIONS_YAML']) as file:
            permissions = yaml.load(file, Loader=yaml.FullLoader)
        resource = [k for (k,v) in [i for i in permissions['services'][service].items()]  if v['path']==service_path][0]
        action = [k for (k,v) in permissions['services']['auth'][resource]['actions'].items() if v==cli_method][0]
        print ("{}_{}_{}".format(service, resource, action) in permisions_object)
        return "{}_{}_{}".format(service, resource, action)

