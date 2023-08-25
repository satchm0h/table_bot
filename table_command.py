import logging

from webex_bot.models.command import Command
from prettytable import PrettyTable
x = PrettyTable()

log = logging.getLogger(__name__)

class TableCommand(Command):

    def __init__(self):
        super().__init__(
            command_keyword="table",
            help_message="Dump an ASCII Table",
        )

    def execute(self, prompt, attachment_actions, activity):

        ## ADD REAL CODE HERE :)

        # Using Pretty Table to export an ascii table
        x = PrettyTable()
        x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
        x.add_rows(
            [
                ["Adelaide", 1295, 1158259, 600.5],
                ["Brisbane", 5905, 1857594, 1146.4],
                ["Darwin", 112, 120900, 1714.7],
                ["Hobart", 1357, 205556, 619.5],
                ["Sydney", 2058, 4336374, 1214.8],
                ["Melbourne", 1566, 3806092, 646.9],
                ["Perth", 5386, 1554769, 869.4],
            ]
        )
        #log.info(f"Response:\n{message}")
        return f"Here is your table:\n\n```\n{x}\n```"
