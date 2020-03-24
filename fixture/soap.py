
from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_link(self):
        return Client(self.app.base_url + "/api/soap/mantisconnect.php?wsdl")

    def get_project_list(self, username, password):
        client = self.get_link()
        try:
            test_access = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for i in test_access:
                id = i.id
                name = i.name
                description = i.description
                projects.append(Project(id=id, name=name, description=description))
            return list(projects)
        except WebFault:
            return False