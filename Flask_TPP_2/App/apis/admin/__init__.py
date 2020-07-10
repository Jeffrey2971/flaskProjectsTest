from flask_restful import Api

from App.apis.admin.Hello_api import TestAdminResource
from App.apis.admin.admin_user_api import AdminUsersResource
from App.models.admin.admin_user_model import AdminUser

admin_api = Api(prefix='/admin')

admin_api.add_resource(TestAdminResource, '/hello/')
admin_api.add_resource(AdminUsersResource, '/users/')
