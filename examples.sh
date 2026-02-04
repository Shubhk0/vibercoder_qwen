#!/bin/bash

# Example Vibe Coder Workflows
# Demonstrates different ways to use the orchestrator

# Make sure vibe-coder is available
if ! command -v vibe-coder &> /dev/null; then
    echo "Please run setup.sh first or use ./vibe_coder.py"
    exit 1
fi

echo "🎨 Vibe Coder Example Workflows"
echo "================================"
echo ""

# Example 1: Build a complete web app
example_1() {
    echo "📱 Example 1: Build a Weather App"
    echo "----------------------------------"
    vibe-coder "create a weather app with live data, temperature display, and 5-day forecast. Make it look modern and responsive" --mode sequential
}

# Example 2: Analyze existing codebase
example_2() {
    echo "🔍 Example 2: Analyze Codebase"
    echo "------------------------------"
    vibe-coder "analyze this codebase and identify code smells, suggest refactorings, and highlight security issues" --files *.py *.js --mode smart
}

# Example 3: Research and implement
example_3() {
    echo "📚 Example 3: Research + Implementation"
    echo "---------------------------------------"
    vibe-coder "research the latest best practices for React state management in 2025, then create a sample implementation" --mode parallel
}

# Example 4: Quick prototyping
example_4() {
    echo "⚡ Example 4: Rapid Prototyping"
    echo "-------------------------------"
    vibe-coder "create a simple kanban board with drag and drop, local storage, and dark mode toggle" --mode smart
}

# Example 5: UI redesign
example_5() {
    echo "🎨 Example 5: UI Redesign"
    echo "-------------------------"
    vibe-coder "take this existing component and redesign it with a modern, glassmorphic aesthetic with smooth animations" --files component.jsx --mode sequential
}

# Example 6: Multi-file project
example_6() {
    echo "📦 Example 6: Full Stack Project"
    echo "--------------------------------"
    vibe-coder "create a full-stack todo app with Express backend, React frontend, MongoDB, and JWT authentication" --mode smart
}

# Menu
echo "Choose an example to run:"
echo "1) Build Weather App (Sequential)"
echo "2) Analyze Codebase (Smart)"
echo "3) Research + Implementation (Parallel)"
echo "4) Rapid Prototyping (Smart)"
echo "5) UI Redesign (Sequential)"
echo "6) Full Stack Project (Smart)"
echo "0) Exit"
echo ""
read -p "Enter choice [0-6]: " choice

case $choice in
    1) example_1 ;;
    2) example_2 ;;
    3) example_3 ;;
    4) example_4 ;;
    5) example_5 ;;
    6) example_6 ;;
    0) echo "Goodbye!"; exit 0 ;;
    *) echo "Invalid choice"; exit 1 ;;
esac
