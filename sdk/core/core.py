import requests
from input.packet import single
from file.view import get_label_file_dict
from file.directory import get_directory_list
from convert.convert import convert_label


class Diffgram():


	def __init__(self):

		self.session = requests.Session()
		self.project_string_id = None

		self.debug = False

		if self.debug is True:
			self.host = "http://127.0.0.1:8080"
		else:
			self.host = "https://diffgram.com"

		self.directory_id = None
		self.name_to_file_id = None


	def auth(self, client_id, client_secret, project_string_id):
		"""
		Define authorization configuration

		Arguments
			client_id, string
			client_secret, string
			project_string_id, string

		Returns
			None

		Future
			More gracefully intial setup (ie validate upon setting)
		"""
		self.session.auth = (client_id, client_secret)
		self.project_string_id = project_string_id


	def set_default_directory(self, directory_id=None):
		"""
		-> If no id is provided fetch directory list for project
		and set first directory to default.
		-> Sets the headers of self.session

		Arguments
			directory_id, int, defaults to None

		Returns
			None

		Future
			TODO return error if invalid directory?

		"""

		if directory_id:
			# TODO check if valid?
			# data = {}
			# data["directory_id"] = directory_id
			self.directory_id = directory_id
		else:

			data = self.get_directory_list()

			self.directory_id = data["directory_list"][0]["id"]

		self.session.headers.update(
			{'directory_id': str(self.directory_id)})




setattr(Diffgram, "input_packet_single", single)
setattr(Diffgram, "get_label_file_dict", get_label_file_dict)
setattr(Diffgram, "get_directory_list", get_directory_list)
setattr(Diffgram, "convert_label", convert_label)