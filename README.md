# Project Dev Log

## Phase 1: Python Fundamentals & Initial Setup

* **Objective:** Learn the core basics of Python and set up the foundation for the project.
* **Progress:**  Learned fundamental Python concepts like functions, loops, modules, and conditional statements.
  * Built a terminal program that recommended specific anxiety-grounding exercises based on how stressed the user felt on a scale from 1 to 10.
* **Problems:**  My project partner had to step away early on, leaving me as a solo developer.
  * Suddenly had to take on all the backend logic and project planning myself.
* **Solutions:**  Redesigned my workflow into a step-by-step solo plan.
  * Took full ownership of both the script logic and the user interaction structure.

---

## Phase 2: AI Integration, Security & Terminal Workflows

* **Objective:** Upgrade the simple script into a real, conversational AI chatbot using Meta's Llama 3.3 model via the Groq API, keep secret keys safe, add safety warnings, and push the code to GitHub.
* **Progress:**  Integrated the Groq API to run Meta’s Llama 3.3 70B model, giving the chatbot an empathetic personality that holds context throughout a conversation.
  * Stored private API keys safely using a hidden `.env` file and updated `.gitignore` so secret keys are never leaked online.
  * Added a startup disclaimer warning users that the chatbot is for conversational support only and not a substitute for professional medical help.
  * Configured local Git version control and set up SSH authentication to upload the repository cleanly to GitHub.
* **Problems:**  **Steep Learning Curve:** Jumping from basic Python code straight into terminal navigation, API requests, environment variables, and SSH keys was a major step up in complexity.
  * **Packed Schedule:** Balanced this technical ramp-up with studying for my upcoming August SATs, which stretched this phase over three weeks.
* **Solutions:**  Switched my dev log from rigid weekly entries to milestone-based **Phases** to focus on completing key technical goals rather than arbitrary calendar dates.
  * Systematically debugged Mac terminal permissions and GitHub authentication errors by switching from basic tokens to a permanent SSH keypair.
