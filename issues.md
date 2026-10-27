# Static Code Analysis Issue Log

**Project:** L5_50_flight_reservation_system  
**File analyzed:** `flight_reservation_system.py`  
**Tools:** Pylint, Bandit, Flake8

This table records issues identified in the original source shared for Lab 5 and the corresponding changes in the cleaned version. Line numbers can change after edits, so descriptions are used instead of relying on post-fix line numbers.

| # | Issue | Type / tool | Original problem | Fix applied |
|---:|---|---|---|---|
| 1 | Dynamic expression evaluation | Security — Bandit | `eval(surcharge_expr)` evaluates a string as Python code and may execute unintended code. | Replaced the expression string with a numeric `surcharge_rate` argument and calculated `base_fare * surcharge_rate` directly. |
| 2 | Hardcoded API secret | Security — Bandit | A token was stored directly in the source and printed to the terminal. | Removed the hardcoded token and stopped printing it. In a real application, secrets should be supplied through a protected configuration or secret store. |
| 3 | Shell command built from a filename | Security — Bandit | `os.system("echo ... " + filename)` invokes a shell and concatenates a variable into the command. | Removed shell execution and used Python's `print()` for the status message. |
| 4 | Mutable default argument | Bug / maintainability — Pylint | `baggage_tags=[]` creates a shared list reused across calls that omit the argument. | Changed the default to `None` and initializes a new list inside the function. |
| 5 | Bare exception handler | Reliability — Flake8 / code quality | `except:` catches every exception and silently ignores failures in cancellation. | Replaced the broad handler with an explicit flight lookup and a clear `False` result for an unknown flight. |
| 6 | MD5 used for passenger identifier digest | Security — Bandit / security review | MD5 is not suitable when a cryptographic hash is required for security purposes. | Replaced MD5 with SHA-256. **Note:** SHA-256 does not anonymize a predictable passenger identifier; real passenger data needs appropriate privacy controls. |
| 7 | Predictable random PIN | Security — security review | `random.randint()` is intended for general-purpose randomness, not security-sensitive PIN generation. | Replaced it with `secrets.randbelow()` to generate a four-digit PIN using a cryptographically stronger random source. |
| 8 | Unused import and variables | Code quality — Pylint / Flake8 | `math`, `airport_fee`, and the original `base_fare` assignment were unused or not used correctly. | Removed unused code and used the fare variable in the actual fee calculation. |
| 9 | Comparison with `None` | Style — Flake8 | The original code used `flights.get(flight_no) == None`. | Used an identity check (`is None`) or a direct availability expression. |
| 10 | Long lines and missing final newline | Style — Flake8 | Several lines exceeded the configured line length and the file lacked a final newline. | Wrapped long expressions and ensured the source ends with a newline. |
| 11 | Non-standard function naming | Style — Pylint | Function names used camelCase, which does not follow the usual Python `snake_case` convention. | Renamed functions to `snake_case`. Calls to those functions were updated accordingly. |
| 12 | Flight lookup and seat validation | Correctness | The original booking check did not independently verify that the remaining seat count was positive. | Added validation for the flight's seat count before booking. |

## Verification record

Fill in these values from the final reports before submitting:

- Final Pylint score: **[enter score from `pylint_after.txt`]**
- Bandit result: **[enter final summary from `bandit_after.txt`]**
- Flake8 result: **[confirm `flake8_after.txt` is empty or list remaining findings]**

Do not claim a target was met unless the final report confirms it.
