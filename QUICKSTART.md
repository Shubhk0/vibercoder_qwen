# ⚡ Quick Start Guide

Get up and running with Vibe Coder in 3 minutes!

## 🚀 Installation (One Command)

```bash
./setup.sh
```

This will:
- Install Qwen CLI and Gemini CLI automatically
- Make vibe-coder globally available
- Create your workspace directory
- Run a system check

## 🎯 First Steps

### 1. Check Everything Works
```bash
vibe-coder --status
```

You should see which tools are available.

### 2. Try Your First Command
```bash
# Smart mode will pick the best tool automatically
vibe-coder "create a simple calculator app"
```

### 3. Experiment with Modes

**Smart Mode** (Default - Recommended)
```bash
vibe-coder "build a portfolio website"
```

**Sequential Mode** (Analysis → Visual Refinement)
```bash
vibe-coder "create a dashboard" --mode sequential
```

**Parallel Mode** (Compare All Tools)
```bash
vibe-coder "best way to handle forms in React" --mode parallel
```

## 🎨 Common Commands

### Build Something New
```bash
vibe-coder "create a [your idea here]"
```

### Analyze Code
```bash
vibe-coder "review this code" --files myfile.py
```

### Research & Build
```bash
vibe-coder "research [topic] and create example"
```

### Work with Multiple Files
```bash
vibe-coder "refactor these files" --files *.js *.css
```

## 🔧 Configuration

### Set Custom Workspace
```bash
vibe-coder --workspace ~/my-projects
```

### View Current Settings
```bash
vibe-coder --status
```

## 📚 Learn More

Run examples:
```bash
./examples.sh
```

Read full documentation:
```bash
cat README.md
```

Get help:
```bash
vibe-coder --help
```

## 🐛 Troubleshooting

### "Tool not found"
Install missing tools:
```bash
pip install qwen-cli gemini-cli
```

### "Permission denied"
Make scripts executable:
```bash
chmod +x vibe_coder.py setup.sh
```

### Antigravity not working
Install separately from Google's official source:
https://antigravity.google.com/install

## 💡 Pro Tips

1. **Let Smart Mode do the work** - It usually picks the right tools
2. **Use Sequential for polish** - Great for going from idea to refined product
3. **Parallel for research** - Compare different approaches side-by-side
4. **Include files for context** - Use `--files` to give more information

## 🎉 You're Ready!

Start vibe coding:
```bash
vibe-coder "what should we build today?"
```

Happy coding! 🚀
