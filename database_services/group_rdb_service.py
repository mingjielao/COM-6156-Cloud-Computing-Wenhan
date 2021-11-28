from framework.rdb_data_resource import RDBDataResource

class GroupRDBService(RDBDataResource):

    def __init__(self, connect_info):
        super().__init__(connect_info)

    def get_next_id(self):
        sql = "select max(group_id) as group_id from YYDS.group;"
        res = self._run_q(sql, fetch=True)
        res = res[0]["group_id"] + 1
        return res


