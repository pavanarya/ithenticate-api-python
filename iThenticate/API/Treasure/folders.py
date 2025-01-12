from ..Helpers import get_xml_as_string
from ..Object import Data


class Folder(object):
    def __init__(self, client):
        self.client = client

    def add(self, folder_group_id, name):
        """
        Create a new folder to folder group.

        :name: The name of the new folder to create
        """
        assert type(name) == str

        xml_string = get_xml_as_string('add_folder.xml')
        xml_string = xml_string.format(
            sid=self.client._session_id,
            name=name,
            folder_group=int(folder_group_id))

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response,
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))

    def all(self,page_no):
        xml_string = get_xml_as_string('list.xml')
        xml_string = xml_string.format(sid=self.client._session_id,
                   page=page_no,method_name='folder.list')

        xml_response = self.client.doHttpCall(data=xml_string)

        return Data(xml_response,
                    self.client.getAPIStatus(xml_response),
                    self.client.getAPIMessages(xml_response))
