# 🎨 Vibe Coder

**Unified AI Coding Assistant Orchestrator**

Seamlessly integrate Qwen CLI, Gemini CLI, and Antigravity into one powerful vibe coding workflow.

## ✨ Features

- 🤖 **Multi-Tool Integration**: Use Qwen CLI, Gemini CLI, and Antigravity together or separately
- 🧠 **Smart Mode**: Automatically selects the best tool(s) based on your prompt
- 🔄 **Sequential Mode**: Chain tools for iterative refinement (CLI → Antigravity)
- ⚡ **Parallel Mode**: Run all tools simultaneously and compare results
- ⚙️ **Configurable**: Customize workspace, default models, and tool paths
- 📁 **Workspace Management**: Centralized workspace for all your vibe coding projects

## 🚀 Installation

### Step 1: Install the underlying tools

```bash
# Install Qwen CLI
pip install qwen-cli

# Install Gemini CLI
pip install gemini-cli

# Install Antigravity (follow Google's official documentation)
# https://antigravity.google.com/install
```

### Step 2: Install Vibe Coder

```bash
# Make the script executable
chmod +x vibe_coder.py

# Optional: Create a symlink for easy access
sudo ln -s $(pwd)/vibe_coder.py /usr/local/bin/vibe-coder

# Or add to your PATH
echo 'export PATH="$PATH:'$(pwd)'"' >> ~/.bashrc
source ~/.bashrc
```

### Step 3: Verify installation

```bash
vibe-coder --status
```

## 📖 Usage

### Basic Usage

```bash
# Smart mode (automatically chooses best tools)
vibe-coder "create a todo app with React"

# With specific mode
vibe-coder "analyze this codebase" --mode sequential

# Include files in context
vibe-coder "refactor this code" --files main.py utils.py
```

### Available Modes

#### 🧠 Smart Mode (Default)
Analyzes your prompt and automatically selects the appropriate tool(s):

```bash
vibe-coder "search for best React patterns" --mode smart
# → Uses Gemini CLI (detected: web search needed)

vibe-coder "build a dashboard with charts" --mode smart
# → Uses Antigravity (detected: visual UI needed)

vibe-coder "analyze and refactor this code" --mode smart
# → Uses Qwen CLI (detected: code analysis needed)
```

**Smart Mode Keywords:**
- **Qwen CLI**: refactor, analyze, understand, codebase, review
- **Gemini CLI**: search, latest, research, web, google, cloud
- **Antigravity**: visualize, ui, interface, design, build, app, website

#### 🔄 Sequential Mode
Runs CLI analysis first, then Antigravity for visual refinement:

```bash
vibe-coder "create a landing page" --mode sequential
# 1. Qwen/Gemini generates initial code
# 2. Output saved to workspace
# 3. Antigravity refines with visual feedback
```

#### ⚡ Parallel Mode
Runs all available tools and shows results side-by-side:

```bash
vibe-coder "optimize this algorithm" --mode parallel
# Shows outputs from Qwen, Gemini, and Antigravity simultaneously
```

### Configuration

```bash
# Check current status and configuration
vibe-coder --status

# Set custom workspace
vibe-coder --workspace ~/my-vibe-projects

# Update configuration
vibe-coder --config default_model=gemini
```

### Configuration File
Located at `~/.vibe_coder_config.json`:

```json
{
  "qwen_cli_path": "qwen-cli",
  "gemini_cli_path": "gemini-cli",
  "antigravity_path": "antigravity",
  "default_model": "auto",
  "workspace": "~/vibe_coding_workspace",
  "enable_logging": true
}
```

## 🎯 Use Cases & Examples

### 1. Build a Full App
```bash
# Smart mode automatically uses sequential workflow
vibe-coder "build a weather app with live data and nice UI"
# → Gemini searches for weather API
# → Antigravity builds the UI with live preview
```

### 2. Analyze Existing Code
```bash
# Include your codebase
vibe-coder "analyze and suggest improvements" --files *.py --mode smart
# → Qwen analyzes code structure
# → Suggests refactoring opportunities
```

### 3. Research & Implement
```bash
# Parallel mode to compare approaches
vibe-coder "best way to implement authentication in Next.js" --mode parallel
# → Qwen: code analysis approach
# → Gemini: latest best practices from web
# → Antigravity: visual implementation
```

### 4. Quick Prototyping
```bash
# Sequential for iterative refinement
vibe-coder "create a kanban board" --mode sequential
# → Quick CLI generation
# → Antigravity visual polish
```

## 🔧 Advanced Usage

### Custom Workflows

You can create custom scripts that chain Vibe Coder commands:

```bash
#!/bin/bash
# my-workflow.sh

# Step 1: Research
vibe-coder "latest trends in $1" --mode parallel > research.md

# Step 2: Generate
vibe-coder "implement $1 based on research.md" --mode sequential

# Step 3: Refine in Antigravity
vibe-coder "add visual polish to workspace" --mode smart
```

### Integration with Git

```bash
# Analyze before committing
vibe-coder "review changes and suggest improvements" \
  --files $(git diff --name-only) \
  --mode smart
```

## 🎨 Workflow Recommendations

### For New Projects
```
Smart Mode → Automatically handles tool selection
```

### For Existing Codebases
```
Sequential Mode → Analysis (Qwen) → Refinement (Antigravity)
```

### For Research-Heavy Tasks
```
Parallel Mode → Compare outputs from all tools
```

### For UI-Focused Work
```
Antigravity directly or Smart Mode (will detect UI keywords)
```

## 🛠️ Troubleshooting

### Tools Not Found
```bash
vibe-coder --status
# Check which tools are missing, then install them
```

### Update Tool Paths
```bash
# Edit config manually
nano ~/.vibe_coder_config.json

# Or update via command
vibe-coder --config qwen_cli_path=/custom/path/to/qwen-cli
```

### Workspace Issues
```bash
# Set a new workspace
vibe-coder --workspace ~/new-workspace

# Verify workspace exists
ls -la $(jq -r '.workspace' ~/.vibe_coder_config.json)
```

## 🤝 Contributing

Ideas for improvements:
- Add support for more AI coding tools (Cursor, Aider, etc.)
- Implement result caching
- Add interactive mode with prompts
- Create visual dashboard for comparing outputs

## 📄 License

MIT License - Feel free to modify and use as you wish!

## 🙏 Acknowledgments

Built to integrate:
- Qwen CLI - Qwen3-Coder models
- Gemini CLI - Google's Gemini models with web search
- Antigravity - Google's full vibe coding IDE

---

**Made with ❤️ for vibe coders who want the best of all worlds**
