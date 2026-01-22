"""
Overlay Manager: Focus Lens Method
Strategy 2: Visual Masking for Acetylcholine Modulation
"""

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt, QPoint, QRect
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen, QRegion, QPainterPath


class FocusOverlay(QMainWindow):
    """
    Fullscreen semi-transparent overlay with a transparent 'flashlight' hole
    that follows the mouse cursor to maintain focus on specific areas.
    """

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.spotlight_radius = 150  # Radius of the transparent hole
        self.mouse_pos = QPoint(0, 0)
        self.overlay_active = False

    def init_ui(self):
        """Initialize the overlay window."""
        # Frameless, always on top, transparent background
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        # Allow mouse events to pass through to windows below (except in our paint area)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)

        # Enable mouse tracking
        self.setMouseTracking(True)

        # Set fullscreen
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.setWindowTitle("Focus Overlay")

    def toggle_overlay(self):
        """Toggle overlay visibility."""
        if self.overlay_active:
            self.hide()
            self.overlay_active = False
        else:
            self.showFullScreen()
            self.overlay_active = True
            # Center mouse position initially
            screen = QApplication.primaryScreen().geometry()
            self.mouse_pos = QPoint(screen.width() // 2, screen.height() // 2)
            self.update()

    def mouseMoveEvent(self, event):
        """Update the spotlight position as mouse moves."""
        self.mouse_pos = event.pos()
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        """Draw semi-transparent overlay with transparent hole at mouse."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Create full-screen dark overlay
        overlay_color = QColor(0, 0, 0, 200)  # Semi-transparent black
        painter.fillRect(self.rect(), overlay_color)

        # Create transparent hole at mouse position
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)

        # Draw circular transparent region (with gradient for smooth edges)
        center = self.mouse_pos

        # Main transparent circle
        painter.setBrush(QBrush(Qt.GlobalColor.transparent))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center, self.spotlight_radius, self.spotlight_radius)

        # Feathered edge (gradient effect)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        for i in range(5):
            alpha = int(40 * (i / 5))
            painter.setBrush(QBrush(QColor(0, 0, 0, alpha)))
            painter.setPen(Qt.PenStyle.NoPen)
            radius = self.spotlight_radius + (i * 10)
            painter.drawEllipse(center, radius, radius)

    def keyPressEvent(self, event):
        """Handle keyboard shortcuts."""
        if event.key() == Qt.Key.Key_Escape:
            self.toggle_overlay()
        elif event.key() == Qt.Key.Key_Plus or event.key() == Qt.Key.Key_Equal:
            # Increase spotlight size
            self.spotlight_radius = min(self.spotlight_radius + 20, 500)
            self.update()
        elif event.key() == Qt.Key.Key_Minus:
            # Decrease spotlight size
            self.spotlight_radius = max(self.spotlight_radius - 20, 50)
            self.update()

    def set_spotlight_radius(self, radius):
        """Set the spotlight radius programmatically."""
        self.spotlight_radius = max(50, min(radius, 500))
        self.update()

    def get_spotlight_radius(self):
        """Get current spotlight radius."""
        return self.spotlight_radius


class OverlayManager:
    """
    Manager class to control the focus overlay.
    Singleton pattern for single overlay instance.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.overlay = FocusOverlay()
        return cls._instance

    def toggle(self):
        """Toggle the overlay on/off."""
        self.overlay.toggle_overlay()

    def set_radius(self, radius):
        """Set spotlight radius."""
        self.overlay.set_spotlight_radius(radius)

    def get_radius(self):
        """Get spotlight radius."""
        return self.overlay.get_spotlight_radius()

    def is_active(self):
        """Check if overlay is active."""
        return self.overlay.overlay_active
