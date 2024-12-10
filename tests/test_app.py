import sys
import pytest
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget


# Simple test for a PyQt6 button click with behavior
def test_button_click():
    app = QApplication(sys.argv)

    # Create a simple window with a button
    window = QWidget()
    button = QPushButton('Click Me', window)

    # Define the behavior when the button is clicked
    def on_button_click():
        button.setText('Clicked')  # Change button text when clicked

    # Connect the button click signal to the function
    button.clicked.connect(on_button_click)

    # Check that the button text is correct before clicking
    assert button.text() == 'Click Me'

    # Simulate a button click
    button.click()

    # Check if the button text changes after the click
    assert button.text() == 'Clicked'

    # Clean up
    app.quit()