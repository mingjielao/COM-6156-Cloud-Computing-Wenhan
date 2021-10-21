from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService


class GroupResource(BaseRDBApplicationResource):
    db_name = "YYDS"
    table_name = "groups"
    def __init__(self):
        super().__init__()


    @classmethod
    def get_links(cls, resource_data):
        for r in resource_data:
            group_id = r.get('group_id')

            links = []
            self_link = {"rel" : "self", "href" : "/groups/" + str(group_id)}
            links.append(self_link)

            users_link = {"rel" : "group_members", "href" : "/users?group_id=" + str(group_id)}
            links.append(users_link)

            r["links"] = links

        return resource_data

    @classmethod
    def create(cls, resource_data):
        next_id = RDBService.get_largest_id(cls.db_name, cls.table_name, "group_id")
        resource_data["group_id"] = next_id
        RDBService.create(cls.db_name, cls.table_name, resource_data)

    @classmethod
    def put(cls, resource_data, group_id):
        RDBService.put(cls.db_name, cls.table_name, resource_data,group_id)

    @classmethod
    def get_by_id(cls, group_id):
        res = RDBService.get_by_attribute(cls.db_name, cls.table_name, "group_id", group_id)
        res = cls.get_links(res)
        return res

    @classmethod
    def delete_by_id(cls, group_id):
        res = RDBService.delete_by_attribute(cls.db_name, cls.table_name, "group_id", group_id)
        return res

    @classmethod
    def get_data_resource_info(cls):
        return cls.db_name, cls.table_name

