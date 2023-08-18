from textual.app import App, ComposeResult
from textual.containers import Container, ScrollableContainer
from textual.widgets import Header, Footer, Button, Static


class CurrentTimeDisplay(Static):
    """A widget to display the current time."""

    def __init__(self, **kwargs):
        """Initialize the widget."""
        super().__init__(**kwargs)
        self.time = "00:00:00"

    def render(self) -> str:
        """Render the widget."""
        return f"[b]{self.time}[/b]"

class ElapsedTimeDisplay(Static):
    pass
    """A widget to display the elapsed time."""

    # def __init__(self, **kwargs):
    #     """Initialize the widget."""
    #     super().__init__(**kwargs)
    #     self.time = "00:00:00"

    # def render(self) -> str:
    #     """Render the widget."""
    #     return f"[b]{self.time}[/b]"
    
class Clock(Static):
    """A clock widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the stopwatch."""
        yield CurrentTimeDisplay()

class Stopwatch(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the stopwatch."""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield ElapsedTimeDisplay("00:00:00.00")

class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("q", "quit_program", "Quit the program"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(
            Clock(),
            Stopwatch(),
            Stopwatch(),
            Stopwatch(),
        )

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
        
    def action_quit_program(self) -> None:
        """An action to quit the program."""
        self.exit()
