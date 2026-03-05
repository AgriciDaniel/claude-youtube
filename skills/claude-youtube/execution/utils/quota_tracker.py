"""
YouTube Data API v3 quota tracker.

Tracks unit consumption per operation and warns before quota exhaustion.
Daily quota: 10,000 units, resets at midnight Pacific Time.

Quota costs:
    search.list    = 100 units
    videos.list    = 1 unit
    channels.list  = 1 unit
    playlistItems.list = 1 unit
    commentThreads.list = 1 unit
    videos.insert  = 100 units

Usage:
    python execution/utils/quota_tracker.py --check
    python execution/utils/quota_tracker.py --consume search.list
    python execution/utils/quota_tracker.py --consume videos.list --count 10
    python execution/utils/quota_tracker.py --reset
"""

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

TMP_DIR = Path.home() / ".claude" / ".tmp"
DAILY_QUOTA = 10000
WARN_THRESHOLD = 0.80  # Warn at 80% consumed

OPERATION_COSTS = {
    "search.list": 100,
    "videos.list": 1,
    "channels.list": 1,
    "playlistItems.list": 1,
    "commentThreads.list": 1,
    "captions.list": 1,
    "playlists.list": 1,
    "videos.insert": 100,
}

PACIFIC_OFFSET = timedelta(hours=-8)  # PST (approximate; doesn't handle DST)


def _pacific_date():
    """Return current date in Pacific Time."""
    utc_now = datetime.now(timezone.utc)
    pacific_now = utc_now + PACIFIC_OFFSET
    return pacific_now.strftime("%Y-%m-%d")


def _quota_file():
    """Return path to today's quota file."""
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    return TMP_DIR / f"youtube_quota_{_pacific_date()}.json"


def _load_quota():
    """Load today's quota state."""
    path = _quota_file()
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return {"date": _pacific_date(), "consumed": 0, "operations": {}}


def _save_quota(data):
    """Save quota state."""
    path = _quota_file()
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def get_remaining():
    """Return remaining quota units for today."""
    data = _load_quota()
    return DAILY_QUOTA - data["consumed"]


def check_quota(operation=None, count=1):
    """Check if an operation can be performed within quota.

    Returns dict with status, remaining units, and warning if applicable.
    """
    data = _load_quota()
    remaining = DAILY_QUOTA - data["consumed"]
    used_pct = data["consumed"] / DAILY_QUOTA

    result = {
        "date": data["date"],
        "consumed": data["consumed"],
        "remaining": remaining,
        "daily_quota": DAILY_QUOTA,
        "used_percent": round(used_pct * 100, 1),
    }

    if used_pct >= WARN_THRESHOLD:
        result["warning"] = (
            f"Quota {result['used_percent']}% consumed. "
            f"Only {remaining} units remaining. Use sparingly."
        )

    if operation:
        cost = OPERATION_COSTS.get(operation, 0)
        total_cost = cost * count
        result["operation"] = operation
        result["operation_cost"] = total_cost
        result["can_execute"] = total_cost <= remaining

        if not result["can_execute"]:
            result["error"] = (
                f"Operation {operation} (×{count}) costs {total_cost} units "
                f"but only {remaining} remaining. Defer to tomorrow."
            )

    return result


def consume_quota(operation, count=1):
    """Record quota consumption for an operation.

    Returns dict with updated quota state.
    """
    cost = OPERATION_COSTS.get(operation, 0)
    if cost == 0:
        return {"warning": f"Unknown operation '{operation}'. No quota consumed."}

    total_cost = cost * count
    data = _load_quota()
    remaining = DAILY_QUOTA - data["consumed"]

    if total_cost > remaining:
        return {
            "error": f"Quota exceeded. Need {total_cost} units, only {remaining} available.",
            "remaining": remaining,
            "consumed": data["consumed"],
        }

    data["consumed"] += total_cost
    op_key = operation
    data["operations"][op_key] = data["operations"].get(op_key, 0) + count
    _save_quota(data)

    new_remaining = DAILY_QUOTA - data["consumed"]
    result = {
        "operation": operation,
        "units_consumed": total_cost,
        "remaining": new_remaining,
        "used_percent": round(data["consumed"] / DAILY_QUOTA * 100, 1),
    }

    if data["consumed"] / DAILY_QUOTA >= WARN_THRESHOLD:
        result["warning"] = (
            f"Quota {result['used_percent']}% consumed. "
            f"Only {new_remaining} units remaining."
        )

    return result


def reset_quota():
    """Force reset today's quota (for testing only)."""
    data = {"date": _pacific_date(), "consumed": 0, "operations": {}}
    _save_quota(data)
    return {"status": "reset", "date": data["date"], "remaining": DAILY_QUOTA}


def main():
    parser = argparse.ArgumentParser(description="YouTube API quota tracker")
    parser.add_argument("--check", action="store_true",
                        help="Check current quota status")
    parser.add_argument("--consume", type=str,
                        help="Record quota consumption for an operation")
    parser.add_argument("--count", type=int, default=1,
                        help="Number of operations (default: 1)")
    parser.add_argument("--reset", action="store_true",
                        help="Reset quota counter (testing only)")
    parser.add_argument("--can-afford", type=str,
                        help="Check if operation is affordable")
    args = parser.parse_args()

    if args.reset:
        result = reset_quota()
    elif args.consume:
        result = consume_quota(args.consume, args.count)
    elif args.can_afford:
        result = check_quota(args.can_afford, args.count)
    elif args.check:
        result = check_quota()
    else:
        parser.print_help()
        return

    print(json.dumps(result, indent=2))
    if "error" in result:
        sys.exit(1)


if __name__ == "__main__":
    main()
