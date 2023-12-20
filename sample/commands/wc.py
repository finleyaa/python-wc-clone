from command import Command

class WcCommand(Command):
	def __init__(self):
		super().__init__("wc", "Count the number of lines in a file", {
			"file"
		})
		