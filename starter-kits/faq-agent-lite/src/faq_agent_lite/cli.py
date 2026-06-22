from __future__ import annotations

import argparse
from pathlib import Path

from .agent import FAQAgent


DEMO_QUESTIONS_PATH = Path(__file__).resolve().parents[2] / "data" / "demo_questions.txt"


def load_demo_questions(path: Path = DEMO_QUESTIONS_PATH) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def print_answer(question: str, agent: FAQAgent) -> None:
    result = agent.answer(question)
    print(f"Q: {result.question}")
    print(f"A: {result.answer}")
    print(f"Source: {result.source_id} | Category: {result.category} | Confidence: {result.confidence:.2f}")
    print(f"Handoff: {result.handoff_note}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run FAQ Agent Lite")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("demo", help="Run built-in demo questions")

    ask_parser = subparsers.add_parser("ask", help="Ask one question")
    ask_parser.add_argument("question", help="Question to answer")

    args = parser.parse_args()
    agent = FAQAgent()

    if args.command == "demo":
        for question in load_demo_questions():
            print_answer(question, agent)
    elif args.command == "ask":
        print_answer(args.question, agent)


if __name__ == "__main__":
    main()
