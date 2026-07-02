from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
from datetime import datetime
import random

# Create MCP Server
mcp = FastMCP(name="fastmcp-starter")


# -----------------------------
# Tool 1 : Welcome User
# -----------------------------
@mcp.tool(
    name="welcome_user",
    description="Greets the user with a welcome message."
)
def hello(
    user: Annotated[str, Field(description="Name of the user")]
) -> str:
    return (
        f"👋 Hello {user}!\n\n"
        "Welcome to FastMCP Starter.\n"
        "Hope you have an amazing day! 🚀"
    )


# -----------------------------
# Tool 2 : Addition
# -----------------------------
@mcp.tool(
    name="addition",
    description="Returns the addition of two numbers."
)
def add(a: float, b: float) -> float:
    return a + b


# -----------------------------
# Tool 3 : Current Date & Time
# -----------------------------
@mcp.tool(
    name="current_time",
    description="Returns the current date, time and greeting."
)
def current_time() -> str:
    now = datetime.now()

    hour = now.hour

    if 5 <= hour < 12:
        greeting = "🌅 Good Morning"
    elif 12 <= hour < 17:
        greeting = "☀️ Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "🌇 Good Evening"
    else:
        greeting = "🌙 Good Night"

    return (
        f"{greeting}\n\n"
        f"🕒 Time : {now.strftime('%I:%M:%S %p')}\n"
        f"📅 Day : {now.strftime('%A')}\n"
        f"📆 Date : {now.strftime('%d %B %Y')}"
    )


# -----------------------------
# Tool 4 : Random Quote
# -----------------------------
quotes = [
    "Believe you can and you're halfway there.",
    "Success is the sum of small efforts repeated every day.",
    "Dream big. Start small. Act now.",
    "Consistency beats motivation.",
    "Every expert was once a beginner.",
    "Your only limit is your mindset.",
    "Small progress is still progress.",
    "Don't stop until you're proud."
]


@mcp.tool(
    name="random_quote",
    description="Returns a random motivational quote."
)
def random_quote() -> str:
    return random.choice(quotes)


## Now i am adding Resources

@mcp.resource("resource://about")

def about():

    return """

FastMCP Starter is a beginner-friendly Model Context Protocol (MCP) server.

Features:

- Welcome Tool

- Addition Tool

- Current Time Tool

- Random Quote Tool

Built using FastMCP.

"""

@mcp.resource("resource://developer")

def developer():

    return """

Developer: Himanshu

Education:

Master's in Mathematics and Computing

Interests:

- Generative AI

- Machine Learning

- RAG

- LangChain

- FastMCP

"""

@mcp.resource("resource://version")

def version():

    return """

FastMCP Starter

Version: 1.0.0

"""
@mcp.prompt(
    name="welcome_prompt",
    description="Generate a friendly welcome message."
)
def welcome_prompt(name: str):
    return f"""
Write a warm and friendly welcome message for {name}.

The message should:
- Be positive
- Be professional
- Wish them a great day
"""
@mcp.prompt(
    name="motivation_prompt",
    description="Generate a motivational message."
)
def motivation_prompt():
    return """
Generate a short motivational message.

The message should:
- Be inspiring
- Be under 40 words
- Be suitable for students and professionals
"""
if __name__ == "__main__":
     mcp.run(transport="streamable-http",host="0.0.0.0",port=8000,)