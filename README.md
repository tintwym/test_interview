# Programming Assignments

This repository contains solutions for two programming assignments:
1. **Word Reversal:** A C++ implementation that reverses alphanumeric words while preserving punctuation and spacing.
2. **Version Update Script:** A Python refactor of a build process script to improve maintainability and safety.

## Assignment 1: Word Reversal (C++)
- **File:** `reverse_words.cpp`
- **Logic:** Uses a two-pointer approach to identify alphanumeric segments and reverses them in-place within a string copy.
- **Build:** `g++ reverse_words.cpp -o reverse`
- **Run:** `./reverse`

## Assignment 2: Version Update (Python)
- **File:** `update_version.py`
- **Logic:** Refactored a legacy script into a modular function. Uses Regular Expressions and safe file handling to update version numbers across multiple files.
- **Run:** ```bash
  export SourcePath="/your/path"
  export BuildNum="123"
  python3 update_version.py
