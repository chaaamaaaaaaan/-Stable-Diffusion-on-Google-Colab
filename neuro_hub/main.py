"""
Neuro-Learning Hub - Main Application
Entry Point & Control Dashboard
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QSlider, QGroupBox, QStatusBar, QFrame
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QColor, QPalette, QFont

from core.audio_engine import AudioEngine
from core.overlay_manager import OverlayManager


class PulseButton(QPushButton):
    """Custom button with pulse animation effect."""

    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self._color = QColor(100, 100, 100)
        self.animation = QPropertyAnimation(self, b"color")
        self.animation.setDuration(1000)
        self.animation.setLoopCount(-1)  # Infinite loop
        self.animation.setEasingCurve(QEasingCurve.Type.InOutSine)

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: rgb({color.red()}, {color.green()}, {color.blue()});
                border: 2px solid #444;
                border-radius: 8px;
                padding: 12px;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }}
            QPushButton:hover {{
                border: 2px solid #666;
            }}
        """)

    color = pyqtProperty(QColor, get_color, set_color)

    def start_pulse(self):
        """Start pulsing animation."""
        self.animation.setStartValue(QColor(50, 200, 100))
        self.animation.setEndValue(QColor(100, 255, 150))
        self.animation.start()

    def stop_pulse(self):
        """Stop pulsing animation."""
        self.animation.stop()
        self.set_color(QColor(100, 100, 100))


class NeuroHubDashboard(QMainWindow):
    """Main application dashboard for Neuro-Learning Hub."""

    def __init__(self):
        super().__init__()
        self.audio_engine = AudioEngine()
        self.overlay_manager = OverlayManager()
        self.init_ui()
        self.apply_dark_theme()

    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Neuro-Learning Hub - Limit Breakthrough System")
        self.setGeometry(100, 100, 600, 500)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("🧠 Neuro-Learning Hub")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        main_layout.addWidget(title)

        subtitle = QLabel("Cognitive Enhancement Control Center")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(QFont("Arial", 10))
        subtitle.setStyleSheet("color: #888;")
        main_layout.addWidget(subtitle)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #444;")
        main_layout.addWidget(separator)

        # Strategy 1: Neuro-Trigger Protocol (Binaural Beats)
        audio_group = self.create_audio_control_group()
        main_layout.addWidget(audio_group)

        # Strategy 2: Focus Lens Method (Screen Overlay)
        overlay_group = self.create_overlay_control_group()
        main_layout.addWidget(overlay_group)

        # Spacer
        main_layout.addStretch()

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready - All systems nominal")

        # Connect audio engine status updates
        self.audio_engine.statusChanged.connect(self.update_status)

    def create_audio_control_group(self):
        """Create control group for audio/binaural beats."""
        group = QGroupBox("Strategy 1: Neuro-Trigger Protocol")
        group.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout = QVBoxLayout()

        # Description
        desc = QLabel("40Hz Gamma Wave Binaural Beats (L: 440Hz, R: 480Hz)")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #aaa; font-size: 11px; font-weight: normal;")
        layout.addWidget(desc)

        # Toggle button with pulse animation
        self.audio_toggle_btn = PulseButton("▶ Start Binaural Beats")
        self.audio_toggle_btn.clicked.connect(self.toggle_audio)
        layout.addWidget(self.audio_toggle_btn)

        # Info label
        info = QLabel("💡 Activates Salience Network for instant concentration")
        info.setStyleSheet("color: #666; font-size: 10px; font-weight: normal; margin-top: 5px;")
        layout.addWidget(info)

        group.setLayout(layout)
        return group

    def create_overlay_control_group(self):
        """Create control group for focus overlay."""
        group = QGroupBox("Strategy 2: Focus Lens Method")
        group.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout = QVBoxLayout()

        # Description
        desc = QLabel("Visual attention masking with spotlight following cursor")
        desc.setWordWrap(True)
        desc.setStyleSheet("color: #aaa; font-size: 11px; font-weight: normal;")
        layout.addWidget(desc)

        # Toggle button
        self.overlay_toggle_btn = QPushButton("🎯 Activate Focus Overlay")
        self.overlay_toggle_btn.clicked.connect(self.toggle_overlay)
        self.overlay_toggle_btn.setStyleSheet("""
            QPushButton {
                background-color: #3a5f8f;
                border: 2px solid #444;
                border-radius: 8px;
                padding: 12px;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #4a7faf;
                border: 2px solid #666;
            }
        """)
        layout.addWidget(self.overlay_toggle_btn)

        # Spotlight radius slider
        slider_layout = QHBoxLayout()
        slider_label = QLabel("Spotlight Size:")
        slider_label.setStyleSheet("color: #aaa; font-size: 11px; font-weight: normal;")
        slider_layout.addWidget(slider_label)

        self.radius_slider = QSlider(Qt.Orientation.Horizontal)
        self.radius_slider.setMinimum(50)
        self.radius_slider.setMaximum(500)
        self.radius_slider.setValue(150)
        self.radius_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.radius_slider.setTickInterval(50)
        self.radius_slider.valueChanged.connect(self.update_spotlight_size)
        slider_layout.addWidget(self.radius_slider)

        self.radius_value_label = QLabel("150px")
        self.radius_value_label.setStyleSheet("color: #aaa; font-size: 11px; font-weight: normal;")
        slider_layout.addWidget(self.radius_value_label)

        layout.addLayout(slider_layout)

        # Info label
        info = QLabel("💡 Reduces distractions via acetylcholine modulation\n⌨ ESC to exit | +/- to resize")
        info.setStyleSheet("color: #666; font-size: 10px; font-weight: normal; margin-top: 5px;")
        layout.addWidget(info)

        group.setLayout(layout)
        return group

    def toggle_audio(self):
        """Toggle binaural beats on/off."""
        self.audio_engine.toggle()
        if self.audio_engine.is_playing:
            self.audio_toggle_btn.setText("⏸ Stop Binaural Beats")
            self.audio_toggle_btn.start_pulse()
        else:
            self.audio_toggle_btn.setText("▶ Start Binaural Beats")
            self.audio_toggle_btn.stop_pulse()

    def toggle_overlay(self):
        """Toggle focus overlay on/off."""
        self.overlay_manager.toggle()
        if self.overlay_manager.is_active():
            self.overlay_toggle_btn.setText("🔴 Deactivate Focus Overlay")
            self.overlay_toggle_btn.setStyleSheet("""
                QPushButton {
                    background-color: #8f3a3a;
                    border: 2px solid #444;
                    border-radius: 8px;
                    padding: 12px;
                    color: white;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #af4a4a;
                    border: 2px solid #666;
                }
            """)
            self.update_status("Focus overlay active - Press ESC to exit")
        else:
            self.overlay_toggle_btn.setText("🎯 Activate Focus Overlay")
            self.overlay_toggle_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3a5f8f;
                    border: 2px solid #444;
                    border-radius: 8px;
                    padding: 12px;
                    color: white;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #4a7faf;
                    border: 2px solid #666;
                }
            """)
            self.update_status("Focus overlay deactivated")

    def update_spotlight_size(self, value):
        """Update the spotlight radius."""
        self.overlay_manager.set_radius(value)
        self.radius_value_label.setText(f"{value}px")

    def update_status(self, message):
        """Update status bar with message."""
        self.status_bar.showMessage(message)

    def apply_dark_theme(self):
        """Apply dark cyberpunk-style theme."""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Base, QColor(40, 40, 40))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Button, QColor(50, 50, 50))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(80, 120, 180))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(255, 255, 255))

        self.setPalette(palette)

        # Apply global stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QGroupBox {
                border: 2px solid #444;
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 15px;
                background-color: #2a2a2a;
                color: #00ff88;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 15px;
                padding: 0 5px;
            }
            QLabel {
                color: #ddd;
            }
            QStatusBar {
                background-color: #252525;
                color: #aaa;
            }
        """)

    def closeEvent(self, event):
        """Cleanup on application close."""
        self.audio_engine.stop()
        event.accept()


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("Neuro-Learning Hub")

    dashboard = NeuroHubDashboard()
    dashboard.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
