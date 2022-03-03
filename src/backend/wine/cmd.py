from typing import NewType

from bottles.backend.logger import Logger  # pyright: reportMissingImports=false
from bottles.backend.wine.wineprogram import WineProgram

logging = Logger()

# Define custom types for better understanding of the code
BottleConfig = NewType('BottleConfig', dict)


class CMD(WineProgram):
    program = "WINE Command Line"
    command = "cmd"

    def run_batch(
        self, 
        batch: str, 
        terminal: bool = True, 
        args: str = "",
        environment: dict = {},
        cwd: str = None
    ):
        args = f"/c {batch} {args}"
        
        self.launch(
            args=args,
            comunicate=True,
            terminal=terminal,
            environment=environment,
            cwd=cwd,
            action_name="run_batch"
        )
