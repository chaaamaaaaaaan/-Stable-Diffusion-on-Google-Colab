#!/bin/bash
# Neuro-Learning Hub Launcher

echo "🧠 Starting Neuro-Learning Hub..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/update requirements
echo "Checking dependencies..."
pip install -q -r requirements.txt

# Run the application
echo "Launching application..."
python main.py

# Deactivate on exit
deactivate
