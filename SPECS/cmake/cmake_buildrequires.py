#!/usr/bin/env python3
"""Generate BuildRequires for cmake-based projects.

Parses CMakeLists.txt to find find_package() and pkg_check_modules() calls
and outputs the corresponding BuildRequires to stdout.
"""

import re
import sys
from pathlib import Path


def find_cmake_lists():
    """Find the top-level CMakeLists.txt."""
    for p in Path().iterdir():
        if p.name == "CMakeLists.txt" and p.is_file():
            return p
    return None


def parse_cmake_requires(cmake_file):
    """Extract find_package and pkg_check_modules calls from CMakeLists.txt."""
    text = cmake_file.read_text(encoding="utf-8", errors="ignore")

    find_package = set()
    pkg_check = set()

    # find_package(Name ...)
    for m in re.finditer(r'find_package\s*\(\s*(\w+)', text):
        name = m.group(1)
        find_package.add(name)

    # pkg_check_modules(VAR ...
    for m in re.finditer(r'pkg_check_modules\s*\(\s*\w+\s+(?:REQUIRED\s+)?(?:IMPORTED_TARGET\s+)?["\']?(\S+?)["\']?', text):
        name = m.group(1)
        pkg_check.add(name)

    return find_package, pkg_check


def main():
    cmake_file = find_cmake_lists()
    if not cmake_file:
        print("ERROR: No CMakeLists.txt found", file=sys.stderr)
        sys.exit(1)

    find_package, pkg_check = parse_cmake_requires(cmake_file)

    for name in sorted(find_package):
        print(f"cmake({name})")

    for name in sorted(pkg_check):
        print(f"pkgconfig({name})")


if __name__ == "__main__":
    main()
