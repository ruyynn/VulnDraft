<div align="center">
  
  <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/VulnDraft_Logo.png" width="520" alt="VulnDraft Logo">
  
  # 🐞 VulnDraft
  
  ### Bug Report Generator for Security Researchers
  
  [![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)](https://github.com/ruyynn/VulnDraft/releases)
  [![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
  [![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
  [![Stars](https://img.shields.io/github/stars/ruyynn/VulnDraft?style=flat-square&color=yellow)](https://github.com/ruyynn/VulnDraft/stargazers)
  [![Forks](https://img.shields.io/github/forks/ruyynn/VulnDraft?style=flat-square&color=blue)](https://github.com/ruyynn/VulnDraft/network)
  
  <p align="center">
    <strong>Generate professional, platform-compliant security reports in minutes.</strong>
    <br>
    Made for bug hunters, by Ruyynn.
  </p>
  
  <p align="center">
    <a href="#-features">Features</a> •
    <a href="#-quick-start">Quick Start</a> •
    <a href="#-screenshots">Screenshots</a> •
    <a href="#-documentation">Documentation</a> •
    <a href="#-support-development">Support Development</a>
  </p>
  
  <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/demo.gif" width="800" alt="VulnDraft Demo">
  
</div>

---

## ✨ Features

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎨 Dual Interface</h3>
      <ul>
        <li>✅ <strong>CLI Interactive Mode</strong> - For terminal lovers</li>
        <li>✅ <strong>Web GUI Mode</strong> - Beautiful browser interface</li>
        <li>✅ Cross-platform (Windows, Linux, macOS, Termux)</li>
        <li>✅ REST API for automation</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>📄 Multi-Format Export</h3>
      <ul>
        <li>✅ Markdown (.md) - Ready for platform submission</li>
        <li>✅ HTML (.html) - Beautiful styled reports</li>
        <li>✅ JSON (.json) - For API integration</li>
        <li>✅ PDF (Coming soon)</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>🏆 Platform Templates</h3>
      <ul>
        <li>✅ HackerOne Style</li>
        <li>✅ Bugcrowd Style</li>
        <li>✅ Intigriti Style</li>
        <li>✅ Custom Template Support</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>📊 Advanced Features</h3>
      <ul>
        <li>✅ CVSS v3.1 Calculator</li>
        <li>✅ Multi-vulnerability Reports</li>
        <li>✅ Session Management (Save/Resume)</li>
        <li>✅ Input Validation & Sanitization</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🎯 Why VulnDraft?

> *"Finding a bug is hard enough. Writing a professional report shouldn't be."*

**VulnDraft** was born from a real problem: in bug bounty, finding the vulnerability is one challenge — but **writing a clear, structured report is another skill entirely**.

I built this tool because:
- 🔥 **Time-consuming** - Formatting reports takes valuable time
- 📋 **Inconsistent** - Every platform has different requirements
- 😤 **Frustrating** - Writing the same structure over and over again
- 🚀 **Solution** - One tool, all platforms, professional reports instantly

---

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# Git (optional)
git --version
```

Installation
```bash
# Clone the repository
git clone https://github.com/ruyynn/VulnDraft.git
cd VulnDraft
```
Install dependencies
```
pip install -r requirements.txt
```

Usage

> 🖥️ CLI Mode (Terminal)

```bash
python main.py
```
Follow the interactive prompts:

1. Enter report title and author

2. Add vulnerability details

3. Choose platform (HackerOne/Bugcrowd/Intigriti/Custom)

4. Optional: Calculate CVSS score

5. Add multiple vulnerabilities

6. Report generated automatically!

> 🌐 Web Mode (Browser)
```bash
python main.py --web
```
> Then open http://localhost:8000 in your browser.

## 🔧 API Mode (REST)
```bash
# Start server
python main.py --web

# Generate report via API
curl -X POST http://localhost:8000/api/v1/reports \
  -H "Content-Type: application/json" \
  -d '{
    "report_title": "SQL Injection Test",
    "author": "YourName",
    "platform": "hackerone",
    "vulnerabilities": [{
      "title": "SQL Injection",
      "description": "Detailed description...",
      "steps_to_reproduce": ["Step 1", "Step 2"],
      "impact": "High impact"
    }]
  }'
  ```
## 📸 Screenshots
<div align="center">
  
### 🎨 Web Interface
  
<table> <tr> <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/screenshot-web-1.png" width="400" alt="Web Interface - Form"> <br> <em>Clean, professional form interface</em> </td> <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/screenshot-web-2.png" width="400" alt="Web Interface - Report"> <br> <em> Clean, professional </em> </td> </tr> </table>
  
### 💻 CLI Interface

<table> <tr> <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/screenshot-cli-1.png" width="400" alt="CLI - Interactive"> <br> <em>Interactive CLI prompts</em> </td> <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/screenshot-cli-2.png" width="400" alt="CLI - CVSS Calculator"> <br> <em>Built-in CVSS calculator</em> </td> </tr> </table>
  
### 📄 Report Examples
  
<table> <tr> <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/Report1.png" width="400" alt="HackerOne Report"> <br> <em> Style Report</em> </td>  <td align="center"> <img src="https://raw.githubusercontent.com/ruyynn/VulnDraft/main/assets/report5.png" width="400" alt="Bugcrowd Report"> <br> <em> Style Report</em> </td> </tr> <summary> <b> </tr> </table> </details></div>


## 📁 Project Structure
```text
VulnDraft/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── config.json            # Configuration
├── core/                  # Core logic
│   ├── cvss.py           # CVSS v3.1 calculator
│   ├── prompt.py         # CLI interactive prompts
│   ├── builder.py        # Report builder
│   └── session.py        # Session management
├── api/                   # REST API
│   ├── routes.py         # FastAPI endpoints
│   └── schemas.py        # Pydantic models
├── web/                   # Web interface
│   ├── main.py           # FastAPI app
│   ├── templates/        # HTML templates
│   └── static/           # CSS/JS assets
├── templates/             # Report templates
│   ├── hackerone.md      # HackerOne style
│   ├── bugcrowd.md       # Bugcrowd style
│   ├── intigriti.md      # Intigriti style
│   └── base.html         # HTML base template
├── platforms/             # Platform validators
│   ├── hackerone.py
│   ├── bugcrowd.py
│   └── intigriti.py
├── utils/                 # Utilities
│   ├── exporter.py       # Export to MD/HTML/JSON
│   ├── validator.py      # Input validation
│   └── formatter.py      # Text formatting
└── output/                # Generated reports
```
## 🛠️ Tech Stack
| Category     | Technologies |
|--------------|--------------|
| Backend      | Python 3.8+, FastAPI, Pydantic |
| CLI          | Questionary, Click |
| Frontend     | HTML5, TailwindCSS, JavaScript |
| Templating   | Jinja2, Markdown |
| Validation   | Pydantic, Regex |
| Testing      | Pytest |

---

## 📝 Supported Platforms
| Platform    | Template | Fields                                 | Status       |
|------------|---------|---------------------------------------|-------------|
| HackerOne  | ✅      | Title, Description, Steps, Impact, CVSS | Full Support |
| Bugcrowd   | ✅      | Title, Description, Steps, Impact, PoC, CVSS | Full Support |
| Intigriti  | ✅      | Title, Summary, Technical Details, Steps, Impact | Full Support |
| Custom     | ✅      | Fully customizable                     | Full Support |

---

## 🤝 Contributing
We welcome contributions! Here’s how you can help:

## 🐛 Report Bugs
- Open an issue with detailed steps to reproduce
- Include screenshots if applicable
- Mention your OS and Python version

## 💡 Suggest Features
- Open an issue with `[FEATURE]` prefix
- Describe your use case and provide examples

## 🔧 Submit PRs
1. Fork the repository  
2. Create a feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes
```
git commit -m 'Add some AmazingFeature'
```
4. Push to branch
```
git push origin feature/AmazingFeature
```
Open a Pull Request

## 📝 Improve Documentation
Fix typos

Add examples

Translate to other languages

## 💖 Support Development

If VulnDraft helps you write better bug reports, consider supporting my work!

<div align="center"> <a href="https://saweria.co/Ruyynn" target="_blank"> <img src="https://user-images.githubusercontent.com/26188697/180601310-e82c63e4-412b-4c36-b7b5-7ba713c80380.png" width="180" alt="Support on Saweria"> </a> </div>

### Benefits of supporting:

● 🚀 Early access to new features (PDF export, more platforms)

● 🐛 Faster bug fixes

● 📚 Better documentation & examples

● ☕ Keep me caffeinated for late-night coding sessions

### 📬 Contact

Have questions, suggestions, or want to chat about bug bounty? Reach out!

<div align="center"> 

[![GitHub](https://img.shields.io/badge/GitHub-0d1117?style=for-the-badge&logo=github&logoColor=22d3ee)](https://github.com/ruyynn) 
[![Mastodon](https://img.shields.io/badge/Mastodon-0d1117?style=for-the-badge&logo=mastodon&logoColor=D14836)](https://mastodon.social/@ruyynn) 
[![Facebook](https://img.shields.io/badge/Facebook-0d1117?style=for-the-badge&logo=facebook&logoColor=22d3ee)](https://www.facebook.com/profile.php?id=61587795784907) 
[![Email](https://img.shields.io/badge/Email-0d1117?style=for-the-badge&logo=gmail&logoColor=D14836)](mailto:ruyynn@example.com) </div>

## 📄 License

Distributed under the MIT License. See LICENSE for more information.

MIT License
```text
Copyright (c) 2026 Ruyynn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions...
```

## 👥 Contributors
Thanks to these awesome people for helping make VulnDraft better!

[![Contributor](https://contrib.rocks/image?repo=ruyynn/VulnDraft)](https://github.com/ruyynn/VulnDraft/graphs/contributors)

thanks to [zeennxx](https://github.com/zeennxx) for contributions!

## ⭐ Star History

Keep track of VulnDraft’s popularity over time:

<div align="center"> 

![Star History](https://api.star-history.com/svg?repos=ruyynn/VulnDraft&type=Date) </div>


</div>
<div align="center"> <sub>Built with 💪🧠 by <a href="https://github.com/ruyynn">Ruyynn</a> | Bug bounty hunter & tool builder</sub> <br> <sub>Happy Bug Hunting! 🔥</sub> </div>

<!-- SEO Meta Tags (for GitHub repository - not visible in rendered README) Keywords: bug report generator, security report tool, bug bounty tool, hackerone report, bugcrowd template, vulnerability report, security researcher tool, pentest reporting, cvss calculator, osint tool, recon tool, bug hunter tool, security automation, python security tool, fastapi bug bounty, report automation, vulndraft -->
