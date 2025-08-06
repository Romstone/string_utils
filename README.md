A small Python utility package for string manipulation, focused on reversing the order of words in a sentence.

Includes two tiers of functionality, a full Pytest test suite, and CLI-based tier selection for testing.

---

## 🔧 Features

- ✅ **Tier 1**: Basic word-reversal with whitespace normalization
- ✅ **Tier 2**: Whitespace-preserving word-reversal + input validation
- ✅ Custom test selection via `--tier` flag

---

## 📁 Project Structure

```text
string_utils/
├── string_utils/
│   ├── __init__.py
│   └── utils.py             ← Core functions for both tiers
├── tests/
│   ├── conftest.py          ← Fixtures and CLI options
│   ├── test_basic.py        ← Tier 1 tests
│   └── test_intermediate.py ← Tier 2 tests
```

## Requirements
- Python 3.9+
- pytest 8.0+

