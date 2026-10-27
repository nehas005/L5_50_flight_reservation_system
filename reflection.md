# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without running the program. It helps identify potential bugs, security weaknesses, maintainability concerns, and style violations early in development.

## 2. What is the purpose of Pylint, Bandit, and Flake8?

- **Pylint** checks code quality and programming practices, including unused variables, naming conventions, and other maintainability issues.
- **Bandit** checks Python source for common security risks, such as unsafe dynamic evaluation and insecure coding patterns.
- **Flake8** checks Python style and common code issues, including line length, whitespace, unused imports, and selected programming mistakes.

Using the tools together provides broader coverage than relying on only one tool.

## 3. What issues were identified and fixed?

The original program included unsafe use of `eval()`, a hardcoded API token that was printed, shell execution through `os.system()`, a mutable default list argument, a bare exception handler, MD5 hashing, and general style issues. The revised version replaced dynamic evaluation with direct arithmetic, removed the hardcoded token and shell call, used `None` for the optional list default, handled unknown flights explicitly, switched to SHA-256 and `secrets` for their respective purposes, and improved naming and formatting.

SHA-256 alone does not make a passenger identifier anonymous. Production systems must also protect personal data and avoid exposing identifiers in logs or terminal output.

## 4. How did static analysis improve the program?

The tools made problems visible in a repeatable way and provided findings that could be checked again after editing. The changes improved readability and addressed several risks that manual review might overlook. Running the tools again is important because it verifies whether the changes actually removed the reported findings.

## 5. What challenges did you face?

One challenge was understanding which warnings indicated security risks and which were style or maintainability issues. Another was ensuring that a fix did not break the program's intended behaviour. Reviewing each finding, making targeted changes, and rerunning the tools helped address these challenges.

## 6. What did you learn from this lab?

I learned that static-analysis tools have different but complementary purposes. Bandit focuses on security, Pylint on code quality, and Flake8 on style and common errors. Static analysis is most useful when it is part of a repeated workflow: analyze the original code, document findings, make fixes, rerun the tools, and retain before-and-after reports.

## Final results to fill in

Before submission, add the measured final Pylint score and the actual final Bandit and Flake8 summaries. These values must come from the reports generated for the final version of the source code.
