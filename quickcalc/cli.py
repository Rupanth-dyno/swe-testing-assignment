from __future__ import annotations

from quickcalc.session import QuickCalcSession


def main() -> None:
    session = QuickCalcSession()
    print("Quick-Calc CLI")
    print("Enter keys separated by spaces (e.g., '5 + 3 ='). Type 'quit' to exit.")
    print("Display:", session.state.display)

    while True:
        line = input("> ").strip()
        if line.lower() in {"quit", "exit"}:
            break
        if not line:
            continue

        for key in line.split():
            display = session.press(key)
        print("Display:", display)


if __name__ == "__main__":
    main()