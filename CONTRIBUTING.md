Perfect — here’s an updated CONTRIBUTING.md that references the Mission Statement from the README and emphasizes the purpose for contributors. You can paste this directly into your repository:

⸻


# Contributing to Secure Net Stack

Thank you for your interest in contributing to **Secure Net Stack**!  

Before you start, we encourage you to read the **[Mission Statement](README.md#mission)** in the README. Understanding the mission will help you align your contributions with the project's goal:  
> “To provide a modular, secure, and extensible Python framework for building encrypted network nodes and communication systems, enabling experimentation, innovation, and collaboration in secure networking.”

---

## 1. Fork and Clone the Repository

1. Fork the repository on GitHub.  
2. Clone your fork locally:

```bash
git clone git@github.com:<your-username>/secure-net-stack.git
cd secure-net-stack


⸻

2. Set Up Python Environment

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


⸻

3. Running the Project
	•	Run the demo node:

python3 examples/demo_node.py

	•	Run all unit tests:

python3 -m unittest discover -s tests

Make sure all tests pass before submitting contributions.

⸻

4. Adding Features or Fixes
	•	Modules: Core functionality is in src/
	•	Examples: Add usage examples in examples/
	•	Tests: Add corresponding unit tests in tests/
	•	Documentation: Update docs/ for architecture or workflow changes

When adding features, always consider alignment with the mission — secure, modular, and extensible networking.

⸻

5. Committing Changes

Use clear and descriptive commit messages:

git add .
git commit -m "Add feature X to SecureChannel"
git push origin <your-branch-name>


⸻

6. Submitting a Pull Request
	•	Push your branch to your fork
	•	Open a Pull Request (PR) against main
	•	Include in your PR:
	•	What your change does
	•	How it was tested
	•	Any new dependencies

⸻

7. Code Guidelines
	•	Follow PEP8 style
	•	Keep modules modular and testable
	•	Include unit tests for new features
	•	Update documentation for any architecture or workflow changes
	•	Align contributions with the mission statement

⸻

8. Thank You

Thank you for contributing to Secure Net Stack!

Your work helps advance a community-driven framework for secure networking. Every contribution—whether it’s code, tests, documentation, or ideas—makes the project more robust and useful for everyone. 🌟

---

✅ **Key Updates in This Version:**

1. References the **Mission Statement** at the top  
2. Emphasizes **alignment with mission** when adding features  
3. Retains all setup instructions, guidelines, and gratitude for contributors  

---

