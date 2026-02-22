#!/bin/bash

# OBMC Intramurals - One-Click Startup Script (Mac/Linux)

echo "🚀 Starting OBMC Intramurals..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python3 is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

echo "✓ Python3 found: $(python3 --version)"

# Install dependencies if needed
echo ""
echo "📦 Checking dependencies..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "   Installing Flask and Flask-CORS..."
    pip3 install -q -r requirements.txt
    if [ $? -eq 0 ]; then
        echo "✓ Dependencies installed"
    else
        echo "❌ Error installing dependencies"
        exit 1
    fi
else
    echo "✓ All dependencies already installed"
fi

# Start Flask server
echo ""
echo "🔥 Starting Flask server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "✓ Server running on http://localhost:5000"
echo ""
echo "📝 Next Steps:"
echo "   1. Open index.html in your browser"
echo "   2. Use the registration and team checker"
echo "   3. Press Ctrl+C to stop the server when done"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Flask
python3 app.py
