#!/usr/bin/env python3
import os
import sys
from datetime import datetime, timedelta, timezone

import gifos

USER = "rayss868"
WIDTH = 1000
HEIGHT = 560
PADDING = 15
TIMEZONE = timezone(timedelta(hours=7))

PURPLE = "\x1b[95m"
BLUE = "\x1b[94m"
GREEN = "\x1b[92m"
WHITE = "\x1b[97m"
DIM = "\x1b[90m"
RESET = "\x1b[0m"
PROMPT = f"{PURPLE}rayss868@github{RESET} ~> "


def main():
    if not os.getenv("GITHUB_TOKEN"):
        sys.exit("GITHUB_TOKEN is required")

    now = datetime.now(TIMEZONE)
    year = now.strftime("%Y")
    stamp = now.strftime("%Y-%m-%d %H:%M:%S WIB")
    stats = gifos.utils.fetch_github_stats(user_name=USER, ignore_repos=[USER])

    terminal = gifos.Terminal(WIDTH, HEIGHT, PADDING, PADDING)
    terminal.toggle_show_cursor(False)
    terminal.gen_text(f"{PURPLE}RAYSS868 SYSTEM BIOS v2.0{RESET}", 1, count=12)
    terminal.gen_text("Initializing GitHub profile node...", 3, count=5)
    terminal.gen_text(f"{GREEN}[ OK ]{RESET} identity loaded", 5, count=5)
    terminal.gen_text(f"{GREEN}[ OK ]{RESET} repositories indexed", 6, count=5)
    terminal.gen_text(f"{GREEN}[ OK ]{RESET} live statistics connected", 7, count=5)
    terminal.gen_text(f"{GREEN}[ OK ]{RESET} terminal ready", 8, count=15)

    terminal.clear_frame()
    terminal.set_prompt(PROMPT)
    terminal.gen_prompt(1)
    terminal.toggle_show_cursor(True)
    terminal.gen_typing_text("fastfetch --profile github", 1, contin=True)
    terminal.toggle_show_cursor(False)

    lines = [
        f"{PURPLE}RAYSS868 / GITHUB NODE{RESET}",
        "------------------------",
        f"{BLUE}Role:{RESET} System Administrator | Developer",
        f"{BLUE}Location:{RESET} Indonesia",
        f"{BLUE}Focus:{RESET} Systems, Backend, Automation, Infrastructure, MCP",
        f"{BLUE}Stack:{RESET} Linux, Docker, Node.js, Python, JavaScript, Nginx",
        "",
        f"{PURPLE}LIVE GITHUB STATS{RESET}",
        "-----------------",
        f"{BLUE}Rank:{RESET} {stats.user_rank.level}",
        f"{BLUE}Stars:{RESET} {stats.total_stargazers}",
        f"{BLUE}Commits ({year}):{RESET} {stats.total_commits_last_year}",
        f"{BLUE}Pull Requests:{RESET} {stats.total_pull_requests_made}",
        f"{BLUE}Merged PRs:{RESET} {stats.total_pull_requests_merged}",
        f"{BLUE}Contributions:{RESET} {stats.total_repo_contributions}",
        "",
        f"{DIM}generated {stamp} | github.com/rayss868{RESET}",
    ]
    terminal.gen_text(lines, 3)
    terminal.gen_text("", 3 + len(lines), count=150)
    terminal.gen_gif()


if __name__ == "__main__":
    main()
