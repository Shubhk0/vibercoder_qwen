#!/usr/bin/env python3
"""
Vibe Coder - Unified AI Coding Assistant Orchestrator
Integrates Qwen CLI, Gemini CLI, and Antigravity for coordinated development
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List, Dict
import shutil

class VibeCoder:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path or os.path.expanduser("~/.vibe_coder_config.json")
        self.config = self.load_config()
        
    def load_config(self) -> Dict:
        """Load configuration or create default"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        else:
            default_config = {
                "qwen_cli_path": shutil.which("qwen-cli") or "qwen-cli",
                "gemini_cli_path": shutil.which("gemini-cli") or "gemini-cli",
                "antigravity_path": shutil.which("antigravity") or "antigravity",
                "default_model": "auto",  # auto, qwen, gemini, antigravity
                "workspace": os.path.expanduser("~/vibe_coding_workspace"),
                "enable_logging": True
            }
            self.save_config(default_config)
            return default_config
    
    def save_config(self, config: Dict):
        """Save configuration to file"""
        with open(self.config_path, 'w') as f:
            json.dump(config, f, indent=2)
        print(f"✓ Configuration saved to {self.config_path}")
    
    def check_tools(self) -> Dict[str, bool]:
        """Check which tools are available"""
        tools = {
            "qwen-cli": bool(shutil.which(self.config["qwen_cli_path"])),
            "gemini-cli": bool(shutil.which(self.config["gemini_cli_path"])),
            "antigravity": bool(shutil.which(self.config["antigravity_path"]))
        }
        return tools
    
    def run_qwen(self, prompt: str, files: Optional[List[str]] = None) -> subprocess.CompletedProcess:
        """Execute Qwen CLI with given prompt"""
        cmd = [self.config["qwen_cli_path"]]
        
        if files:
            for file in files:
                cmd.extend(["--file", file])
        
        cmd.append(prompt)
        
        print(f"\n🤖 Running Qwen CLI...")
        return subprocess.run(cmd, capture_output=True, text=True)
    
    def run_gemini(self, prompt: str, files: Optional[List[str]] = None, web_search: bool = False) -> subprocess.CompletedProcess:
        """Execute Gemini CLI with given prompt"""
        cmd = [self.config["gemini_cli_path"]]
        
        if web_search:
            cmd.append("--web-search")
        
        if files:
            for file in files:
                cmd.extend(["--file", file])
        
        cmd.append(prompt)
        
        print(f"\n🔷 Running Gemini CLI...")
        return subprocess.run(cmd, capture_output=True, text=True)
    
    def run_antigravity(self, prompt: str, project_dir: Optional[str] = None) -> subprocess.CompletedProcess:
        """Execute Antigravity with given prompt"""
        cmd = [self.config["antigravity_path"]]
        
        if project_dir:
            cmd.extend(["--project", project_dir])
        
        cmd.append(prompt)
        
        print(f"\n🌟 Running Antigravity...")
        return subprocess.run(cmd, capture_output=True, text=True)
    
    def orchestrate(self, prompt: str, mode: str = "sequential", files: Optional[List[str]] = None):
        """
        Orchestrate multiple tools based on mode
        
        Modes:
        - sequential: Run Qwen/Gemini first, then Antigravity for refinement
        - parallel: Show results from all tools side by side
        - smart: Automatically choose best tool(s) based on prompt
        """
        available_tools = self.check_tools()
        
        if mode == "sequential":
            self._sequential_mode(prompt, files, available_tools)
        elif mode == "parallel":
            self._parallel_mode(prompt, files, available_tools)
        elif mode == "smart":
            self._smart_mode(prompt, files, available_tools)
        else:
            print(f"❌ Unknown mode: {mode}")
    
    def _sequential_mode(self, prompt: str, files: Optional[List[str]], available_tools: Dict[str, bool]):
        """Run tools in sequence: CLI analysis -> Antigravity refinement"""
        print("\n🔄 Sequential Mode: CLI Analysis → Antigravity Refinement")
        print("=" * 60)
        
        # Step 1: Run CLI tool for initial analysis/generation
        if available_tools.get("qwen-cli"):
            result = self.run_qwen(prompt, files)
            print("\n📝 Qwen CLI Output:")
            print(result.stdout)
            
            # Save output for Antigravity
            output_file = os.path.join(self.config["workspace"], "qwen_output.md")
            os.makedirs(self.config["workspace"], exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(result.stdout)
        
        elif available_tools.get("gemini-cli"):
            result = self.run_gemini(prompt, files, web_search=True)
            print("\n📝 Gemini CLI Output:")
            print(result.stdout)
            
            # Save output for Antigravity
            output_file = os.path.join(self.config["workspace"], "gemini_output.md")
            os.makedirs(self.config["workspace"], exist_ok=True)
            with open(output_file, 'w') as f:
                f.write(result.stdout)
        
        # Step 2: Use Antigravity for visual refinement
        if available_tools.get("antigravity"):
            refine_prompt = f"Refine and visualize this: {prompt}. Previous analysis saved in workspace."
            self.run_antigravity(refine_prompt, self.config["workspace"])
    
    def _parallel_mode(self, prompt: str, files: Optional[List[str]], available_tools: Dict[str, bool]):
        """Run all available tools in parallel and show results"""
        print("\n⚡ Parallel Mode: Running all available tools")
        print("=" * 60)
        
        results = {}
        
        if available_tools.get("qwen-cli"):
            results["qwen"] = self.run_qwen(prompt, files)
        
        if available_tools.get("gemini-cli"):
            results["gemini"] = self.run_gemini(prompt, files, web_search=True)
        
        if available_tools.get("antigravity"):
            results["antigravity"] = self.run_antigravity(prompt, self.config["workspace"])
        
        # Display all results
        for tool, result in results.items():
            print(f"\n{'=' * 60}")
            print(f"📊 {tool.upper()} Results:")
            print(f"{'=' * 60}")
            print(result.stdout)
    
    def _smart_mode(self, prompt: str, files: Optional[List[str]], available_tools: Dict[str, bool]):
        """Intelligently choose the best tool(s) based on prompt content"""
        print("\n🧠 Smart Mode: Analyzing prompt to choose optimal tools")
        print("=" * 60)
        
        prompt_lower = prompt.lower()
        
        # Heuristics for tool selection
        use_qwen = any(keyword in prompt_lower for keyword in 
                       ["refactor", "analyze", "understand", "codebase", "review"])
        
        use_gemini = any(keyword in prompt_lower for keyword in 
                        ["search", "latest", "research", "web", "google", "cloud"])
        
        use_antigravity = any(keyword in prompt_lower for keyword in 
                             ["visualize", "ui", "interface", "design", "build", "app", "website"])
        
        # Default to sequential if no clear preference
        if not (use_qwen or use_gemini or use_antigravity):
            print("📌 No specific tool preference detected. Using sequential mode.")
            self._sequential_mode(prompt, files, available_tools)
            return
        
        print(f"📌 Selected tools based on prompt analysis:")
        if use_qwen: print("  ✓ Qwen CLI (code analysis)")
        if use_gemini: print("  ✓ Gemini CLI (web search)")
        if use_antigravity: print("  ✓ Antigravity (visual development)")
        
        # Execute selected tools
        if use_qwen and available_tools.get("qwen-cli"):
            result = self.run_qwen(prompt, files)
            print(result.stdout)
        
        if use_gemini and available_tools.get("gemini-cli"):
            result = self.run_gemini(prompt, files, web_search=True)
            print(result.stdout)
        
        if use_antigravity and available_tools.get("antigravity"):
            result = self.run_antigravity(prompt, self.config["workspace"])
            print(result.stdout)
    
    def status(self):
        """Show current configuration and tool availability"""
        print("\n🎨 Vibe Coder Status")
        print("=" * 60)
        
        tools = self.check_tools()
        print("\n📦 Tool Availability:")
        for tool, available in tools.items():
            status = "✓ Available" if available else "✗ Not found"
            print(f"  {tool}: {status}")
        
        print("\n⚙️  Configuration:")
        print(f"  Workspace: {self.config['workspace']}")
        print(f"  Default Model: {self.config['default_model']}")
        print(f"  Config File: {self.config_path}")
        
        if not any(tools.values()):
            print("\n⚠️  Warning: No tools found. Please install:")
            print("  - Qwen CLI: pip install qwen-cli")
            print("  - Gemini CLI: pip install gemini-cli")
            print("  - Antigravity: Check Google's documentation")


def main():
    parser = argparse.ArgumentParser(
        description="Vibe Coder - Unified AI Coding Assistant Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  vibe-coder "create a todo app" --mode smart
  vibe-coder "analyze this codebase" --files *.py --mode sequential
  vibe-coder "search for best practices in React hooks" --mode parallel
  vibe-coder --status
  vibe-coder --config workspace=/path/to/workspace
        """
    )
    
    parser.add_argument("prompt", nargs="?", help="Your coding prompt/request")
    parser.add_argument("--mode", "-m", choices=["sequential", "parallel", "smart"], 
                       default="smart", help="Orchestration mode (default: smart)")
    parser.add_argument("--files", "-f", nargs="+", help="Files to include in context")
    parser.add_argument("--status", "-s", action="store_true", help="Show tool status")
    parser.add_argument("--config", "-c", help="Update config (format: key=value)")
    parser.add_argument("--workspace", "-w", help="Set workspace directory")
    
    args = parser.parse_args()
    
    vibe = VibeCoder()
    
    # Handle configuration
    if args.workspace:
        vibe.config["workspace"] = os.path.expanduser(args.workspace)
        vibe.save_config(vibe.config)
    
    if args.config:
        key, value = args.config.split("=", 1)
        vibe.config[key] = value
        vibe.save_config(vibe.config)
    
    # Handle status
    if args.status:
        vibe.status()
        return
    
    # Handle prompt
    if not args.prompt:
        parser.print_help()
        return
    
    vibe.orchestrate(args.prompt, mode=args.mode, files=args.files)


if __name__ == "__main__":
    main()
