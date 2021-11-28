import middleware.context as context

from application_services.GroupResource.group_application_service import GroupResource
from database_services.group_rdb_service import GroupRDBService


class ServiceFactory:

    def __init__(self):
        self.db_connect_info = context.get_db_info()
        r_svc = GroupRDBService(self.db_connect_info)

        self.services = {}

        group_svc_config_info = {
            "db_resource": r_svc,
            "db_table_name": "group",
            "key_columns": ["group_id"]
        }
        group_svc = GroupResource(group_svc_config_info)

        self.services["group"] = group_svc

    def get_service(self, service_name):
        result = self.services.get(service_name, None)
        return result
