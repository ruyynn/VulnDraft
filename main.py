#!/usr/bin/env python3
"""
BUG REPORT GENERATOR PRO v1.0
Main Entry Point for CLI and Web Modes

Usage:
    python main.py                 # CLI interactive mode
    python main.py --web           # Start web server
    python main.py --web --port 8080  # Web server on custom port
"""

import sys
import argparse
import json
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

# ASCII Banner
BANNER = """
 ___ ___       __       ______               ___ __   
|   Y   .--.--|  .-----|   _  \ .----.---.-.'  _|  |_ 
|.  |   |  |  |  |     |.  |   \|   _|  _  |   _|   _|
|.  |   |_____|__|__|__|.  |    |__| |___._|__| |____|
|:  1   |              |:  1    /                     
 \:.. ./               |::.. . /                      
  `---'                `------'                       
        Bug Report Generator
    """


def main():
    """Main entry point"""
    
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="Bug Report Generator Pro - Generate professional security reports"
    )
    parser.add_argument(
        "--web", 
        action="store_true",
        help="Start web interface (FastAPI server)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8000,
        help="Port for web interface (default: 8000)"
    )
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host for web interface (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information"
    )
    
    args = parser.parse_args()
    
    # Show version
    if args.version:
        print(BANNER)
        print("Version: 1.0.0")
        print("Author: Ruyynn")
        print("License: MIT")
        return
    
    # Load config
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("❌ Error: config.json not found!")
        sys.exit(1)
    except json.JSONDecodeError:
        print("❌ Error: config.json is malformed!")
        sys.exit(1)
    
    # Web mode
    if args.web:
        print(BANNER)
        print(f"🌐 Starting web interface at http://{args.host}:{args.port}")
        print("Press Ctrl+C to stop\n")
        
        try:
            import uvicorn
            from web.main import app
            uvicorn.run(app, host=args.host, port=args.port)
        except ImportError:
            print("❌ Error: FastAPI/uvicorn not installed!")
            print("   Run: pip install fastapi uvicorn")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
            sys.exit(0)
    
    # CLI Mode
    else:
        print(BANNER)
        print("="*60)
        print("Interactive Mode - Let's create a security report")
        print("="*60)
        
        try:
            from core.prompt import ReportPrompt
            from utils.exporter import ReportExporter
            from core.builder import ReportBuilder
            
            # Create report interactively
            report = ReportPrompt.create_report()
            
            # Build report dict
            builder = ReportBuilder(config)
            report_dict = builder.build_report_dict(report)
            
            # Validate
            warnings = builder.validate_report(report)
            if warnings:
                print("\n⚠️ Validation Warnings:")
                for warning in warnings:
                    print(f"   • {warning}")
                
                proceed = input("\nContinue anyway? (y/n): ").lower()
                if proceed != 'y':
                    print("❌ Report generation cancelled.")
                    return
            
            # Export
            exporter = ReportExporter(config)
            
            print("\n📄 Generating reports...")
            exports = exporter.export_all(report_dict, report.platform)
            
            print("\n✅ Report generated successfully!")
            print(f"   📝 Markdown: {exports['markdown']}")
            print(f"   🌐 HTML: {exports['html']}")
            print(f"   📊 JSON: {exports['json']}")
            
            # Ask for preview
            preview = input("\nPreview Markdown in terminal? (y/n): ").lower()
            if preview == 'y':
                print("\n" + "="*60)
                print("PREVIEW")
                print("="*60)
                with open(exports['markdown'], 'r', encoding='utf-8') as f:
                    print(f.read())
            
            print("\n✨ Done! Happy bug hunting! 🐞")
            
        except KeyboardInterrupt:
            print("\n\n⚠️ Cancelled by user")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()