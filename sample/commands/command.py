class Command:
	def __init__(self, command: str, description: str, arguments: dict = {}, options: dict = {}, flags: dict = {}):
		self.command = command
		self.description = description
		self.options = options

	def run():
		pass

	def help():
		pass