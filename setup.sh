#!/bin/bash

# Vibe Coder Setup Script
# Automates installation and configuration

set -e

echo "🎨 Vibe Coder Setup"
echo "==================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python
echo "📌 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python found: $(python3 --version)${NC}"

# Install dependencies
echo ""
echo "📦 Installing AI CLI tools..."

# Qwen CLI
echo -n "Installing Qwen CLI... "
if pip install qwen-cli &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${YELLOW}⚠ Already installed or failed${NC}"
fi

# Gemini CLI
echo -n "Installing Gemini CLI... "
if pip install gemini-cli &> /dev/null; then
    echo -e "${GREEN}✓${NC}"
else
    echo -e "${YELLOW}⚠ Already installed or failed${NC}"
fi

# Note about Antigravity
echo ""
echo -e "${YELLOW}📝 Note: Antigravity must be installed separately${NC}"
echo "   Visit: https://antigravity.google.com/install"

# Make vibe_coder.py executable
echo ""
echo "🔧 Setting up Vibe Coder..."
chmod +x vibe_coder.py
echo -e "${GREEN}✓ Made vibe_coder.py executable${NC}"

# Create symlink
echo ""
read -p "Create global command 'vibe-coder'? (requires sudo) [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if sudo ln -sf "$(pwd)/vibe_coder.py" /usr/local/bin/vibe-coder; then
        echo -e "${GREEN}✓ Created global command 'vibe-coder'${NC}"
    else
        echo -e "${YELLOW}⚠ Could not create global command${NC}"
        echo "   You can manually add to PATH: export PATH=\"\$PATH:$(pwd)\""
    fi
else
    echo "Skipping global command creation"
    echo "You can run: ./vibe_coder.py or add to PATH"
fi

# Create workspace
echo ""
WORKSPACE="$HOME/vibe_coding_workspace"
if [ ! -d "$WORKSPACE" ]; then
    mkdir -p "$WORKSPACE"
    echo -e "${GREEN}✓ Created workspace: $WORKSPACE${NC}"
else
    echo -e "${YELLOW}⚠ Workspace already exists: $WORKSPACE${NC}"
fi

# Run initial status check
echo ""
echo "🔍 Checking installation..."
./vibe_coder.py --status

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Install Antigravity (if not already installed)"
echo "  2. Run: vibe-coder --status"
echo "  3. Try: vibe-coder \"create a hello world app\" --mode smart"
echo ""
echo "For help: vibe-coder --help"
echo "Documentation: cat README.md"
