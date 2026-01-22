# Neuro-Learning Hub 🧠

**A cognitive enhancement desktop application based on neuroscience principles**

## Overview

Neuro-Learning Hub is a Python-based desktop application designed to maximize learning efficiency through five scientifically-backed brain mechanisms. This application provides tools to enhance focus, concentration, and memory consolidation using audio-visual techniques and adaptive learning algorithms.

## Features

### ✅ Implemented (Phase 1)

#### Strategy 1: Neuro-Trigger Protocol (Gamma Wave Activation)
- **40Hz Binaural Beats** for instant concentration
- Left channel: 440Hz, Right channel: 480Hz
- Activates the Salience Network for enhanced focus
- Real-time audio generation using SoundDevice

#### Strategy 2: Focus Lens Method (Visual Attention Control)
- **Fullscreen overlay** with spotlight effect following cursor
- Reduces visual distractions through selective masking
- Adjustable spotlight size (50-500px radius)
- Keyboard shortcuts: ESC to exit, +/- to resize
- Modulates acetylcholine for sustained attention

### 🚧 Planned (Future Phases)

#### Strategy 3: Hyper Deep Practice
- Adaptive difficulty system maintaining 70% success rate
- Flashcard and drill modes with local progress tracking
- Promotes myelination through deliberate practice

#### Strategy 4: Pre-Test & Error Hack
- Controlled failure mechanism before lessons
- Activates Locus Coeruleus for heightened alertness
- Norepinephrine spike for enhanced memory encoding

#### Strategy 5: Sleep Consolidation Mode
- Daily review of high-error items
- Red-shift theme (blue light reduction)
- Delta wave preparation for memory consolidation

## Installation

### Prerequisites
- Python 3.10 or higher
- Virtual environment (recommended)

### Setup

```bash
# Clone the repository
cd neuro_hub

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Usage

### Main Dashboard
Launch the application to access the control center:
```bash
python main.py
```

### Controls

**Binaural Beats:**
- Click "Start Binaural Beats" to activate 40Hz gamma waves
- Button pulses when active
- Click again to stop

**Focus Overlay:**
- Click "Activate Focus Overlay" to dim the screen
- A transparent spotlight follows your cursor
- Use the slider to adjust spotlight size
- Press ESC to exit overlay mode
- Use +/- keys to dynamically resize

## Technical Architecture

```
/neuro_hub
  /main.py               # Entry point, Dashboard UI
  /core
    /audio_engine.py     # Binaural beat generator (threaded)
    /overlay_manager.py  # Screen overlay with spotlight effect
    /learning_algo.py    # [Future] Adaptive difficulty logic
  /ui
    /widgets             # [Future] Custom UI components
    /windows             # [Future] Additional windows
    /styles.qss          # [Future] Custom styling
  /assets                # [Future] Icons and resources
  /requirements.txt      # Python dependencies
```

## Technology Stack

- **GUI Framework:** PyQt6
- **Audio Processing:** SoundDevice + NumPy
- **Python Version:** 3.10+
- **Future Additions:** PyQtGraph (visualization), SQLite (progress tracking)

## Scientific Background

### 40Hz Gamma Waves
Research shows that 40Hz binaural beats can enhance:
- Cognitive processing speed
- Working memory capacity
- Focused attention
- Neural synchronization

### Visual Attention Masking
The Focus Lens method leverages:
- Acetylcholine modulation for selective attention
- Reduction of peripheral distractions
- Enhanced visual processing in the spotlight area

## Development Status

- [x] Project structure
- [x] Audio engine with binaural beats
- [x] Focus overlay with spotlight effect
- [x] Dark theme UI dashboard
- [ ] Adaptive learning algorithm
- [ ] Pre-test system
- [ ] Sleep consolidation mode
- [ ] Progress tracking database
- [ ] Flashcard/drill modes

## License

MIT License - See LICENSE file for details

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Acknowledgments

Based on cognitive neuroscience research in:
- Salience Network activation
- Myelination and deliberate practice
- Norepinephrine modulation
- Memory consolidation during sleep

---

**⚠️ Disclaimer:** This application is designed for educational and productivity enhancement purposes. Consult with a healthcare professional before using if you have any neurological conditions or are sensitive to visual/audio stimuli.
