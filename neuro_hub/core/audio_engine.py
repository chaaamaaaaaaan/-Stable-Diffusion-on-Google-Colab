"""
Audio Engine: 40Hz Gamma Wave Binaural Beat Generator
Strategy 1: Neuro-Trigger Protocol (Salience Network Activation)
"""

import numpy as np
import sounddevice as sd
from PyQt6.QtCore import QThread, pyqtSignal, QObject


class AudioEngine(QObject):
    """
    Generates continuous binaural beats for focus enhancement.
    Left: 440Hz, Right: 480Hz → 40Hz binaural beat (Gamma wave)
    """

    statusChanged = pyqtSignal(str)  # Signal for status updates

    def __init__(self, sample_rate=44100):
        super().__init__()
        self.sample_rate = sample_rate
        self.left_freq = 440  # Hz
        self.right_freq = 480  # Hz (40Hz difference for gamma)
        self.stream = None
        self.is_playing = False
        self.current_position = 0

    def _callback(self, outdata, frames, time_info, status):
        """
        Callback function for sounddevice OutputStream.
        Generates stereo sine waves in real-time.
        """
        if status:
            self.statusChanged.emit(f"Audio status: {status}")

        # Generate time array
        t = (self.current_position + np.arange(frames)) / self.sample_rate
        self.current_position += frames

        # Generate left and right channels
        left_channel = 0.3 * np.sin(2 * np.pi * self.left_freq * t)
        right_channel = 0.3 * np.sin(2 * np.pi * self.right_freq * t)

        # Combine into stereo output
        outdata[:, 0] = left_channel
        outdata[:, 1] = right_channel

    def start(self):
        """Start playing binaural beats."""
        if not self.is_playing:
            try:
                self.stream = sd.OutputStream(
                    channels=2,
                    callback=self._callback,
                    samplerate=self.sample_rate,
                    blocksize=2048
                )
                self.stream.start()
                self.is_playing = True
                self.statusChanged.emit("Binaural beats started (40Hz Gamma)")
            except Exception as e:
                self.statusChanged.emit(f"Error starting audio: {e}")

    def stop(self):
        """Stop playing binaural beats."""
        if self.is_playing and self.stream:
            try:
                self.stream.stop()
                self.stream.close()
                self.is_playing = False
                self.current_position = 0
                self.statusChanged.emit("Binaural beats stopped")
            except Exception as e:
                self.statusChanged.emit(f"Error stopping audio: {e}")

    def toggle(self):
        """Toggle audio on/off."""
        if self.is_playing:
            self.stop()
        else:
            self.start()

    def __del__(self):
        """Cleanup on deletion."""
        self.stop()


class AudioThread(QThread):
    """
    QThread wrapper for audio engine to prevent UI blocking.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.audio_engine = AudioEngine()

    def run(self):
        """Thread execution - keeps audio engine alive."""
        self.exec()  # Event loop for the thread

    def start_audio(self):
        """Start binaural beats."""
        self.audio_engine.start()

    def stop_audio(self):
        """Stop binaural beats."""
        self.audio_engine.stop()

    def toggle_audio(self):
        """Toggle audio playback."""
        self.audio_engine.toggle()
