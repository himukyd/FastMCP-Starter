# FastMCP Starter

A beginner-friendly Model Context Protocol (MCP) server built with FastMCP. This project demonstrates the core building blocks of an MCP server, including tools, resources, and prompts, and serves as a foundation for building more advanced MCP applications.

## Features

- 🔧 MCP Tools
- 📄 MCP Resources
- 💬 MCP Prompts
- 🚀 Local development and testing
- ☁️ FastMCP Cloud deployment
- 🧪 Compatible with MCP Inspector

## Project Structure

```
fastmcp-starter/
├── server.py
├── pyproject.toml
├── README.md
├── .env.example
└── requirements.txt
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/<your-username>/fastmcp-starter.git
cd fastmcp-starter
```

### Install dependencies

```bash
uv sync
```

### Run the server

```bash
fastmcp dev server.py
```

### Test with MCP Inspector

```bash
fastmcp inspector
```

## Tools

- Hello Tool
- Calculator Tool
- Current Time Tool
- Random Quote Tool

## Resources

- About
- Version
- Developer Information

## Prompts

- Code Reviewer
- Email Writer
- Bug Fixer

## Deployment

This project can be deployed directly to FastMCP Cloud.

## Future Improvements

- Authentication
- Database Integration
- External APIs
- RAG Support
- GitHub Integration
- File Management
- AI-powered Tools

