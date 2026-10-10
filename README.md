# Qiskit Fall Fest 2026 — Project Submission Template
**IIIT Kottayam Quantum Hackathon (24-Hour Sprint)**

> ⚠️ **CRITICAL INSTRUCTIONS FOR PARTICIPANTS:**
> 1. **Do NOT rename or delete the section headings** below. The automated AI evaluation and filtering system relies on this exact Markdown structure to parse and grade your project.
> 2. Replace all placeholder text enclosed in `[brackets]` with your project's details.
> 3. **Commit History Audit:** All project commits must be timestamped strictly within the 24-hour hackathon window (between **October 10, 2026 at 7:05 PM** and **October 11, 2026 at 7:05 PM**). Commits observed outside this window will result in **immediate disqualification**.
> 4. Ensure all Jupyter Notebooks have their cells **run and outputs displayed** before pushing.
> 5. Starter resources and reference guides are located in the [`references/`](./references/) folder.
> 6. **Tech Stack Flexibility:** You are free to use any external frameworks/technologies (e.g., Streamlit, React, Pygame, FastAPI, NetworkX) for your frontend, app logic, or classical baselines. However, **Qiskit MUST power the quantum core** of your project.
> 7. **Full Event Guide & Rules:** For full schedule details, track inspirations, submission steps, and grading focus areas, refer to [`HACKATHON_GUIDE.md`](./HACKATHON_GUIDE.md).

*(You may delete the instructions box above when preparing your final repository submission)*

---

# Project Title

## Project Metadata

* **Project Title:** `[A Qiskit-Powered Quantum Game]`
* **Team Name:** `[Aarohi Shakthi]`
* **Chosen Track:** `[Track 1: Quantum Games & Interactive Puzzles OR Track 2: Open-Domain Optimization & Real-World Solvers]`
* **Video Presentation Link:** `[
Not available yet]`
  *(⚠️ Crucial: Ensure link access is set to "Anyone with the link can view" on Google Drive or "Unlisted / Public" on YouTube. Locked/inaccessible links cannot be scored!)*
* **Live Demo Timestamp in Video:** `[not available yet]` *(e.g., "Demo starts at 03:45")*

### Team Members (Max 4 members)
| Name | Email | GitHub Username |
| :--- | :--- | :--- |
| `[Jakkaraju Raghavi]` | `[raghavij2006@gmail.com]` | `[raghavi]` |
| `[Member 2 Name]` | `[Email]` | `[@username]` |
| `[Member 3 Name]` | `[Email]` | `[@username]` |
| `[Member 4 Name]` | `[Email]` | `[@username]` |

---

## 1. Project Overview & Motivation

* **Summary (3–4 sentences):**  
  `[Quantum Coin Duel is an interactive quantum game built using Python and Qiskit. Players predict Heads or Tails while exploring how quantum operations influence measurement outcomes. The game demonstrates quantum superposition using the Hadamard gate, state changes using the Pauli-X gate, and measurement to obtain a classical result. A score counter makes learning quantum concepts engaging and interactive.]`

* **Why this problem / game?**  
  `[Quantum computing can be difficult for beginners to understand through theory alone. Quantum Coin Duel provides a simple, game-based way to explore quantum circuits, probability, and measurement. It connects quantum computing concepts with player decisions and encourages experimentation with different quantum operations.]`

---

## 2. Quantum Architecture & Mechanics

* **Core Quantum Principles Used:**  
  `[Superposition using the Hadamard (H) gate.

Qubit state transformation using the Pauli-X (X) gate.

Measurement collapse from a quantum state to a classical outcome..]`

* **How the Quantum Circuit is Integrated:**  
  `[he player selects a quantum operation and predicts Heads or Tails. The application constructs a one-qubit Qiskit circuit and applies the selected operation. The resulting state probabilities determine a simulated outcome, which is compared with the player's prediction to update the score.]`

* **Circuit Details:**  
  * **Number of Qubits:** `[1 qubit.]`
  * **Key Gates Used:** `[H, X, and measurement.]`
  * **Primitives Used:** `[Qiskit Statevector simulation and classical sampling based on the state probabilities.]`
  * **Other Technologies Used:** `[Python and Streamlit.]`

```python
# Optional: Paste a representative snippet of your core Qiskit circuit code here
```

---

## 3. Repository Structure & How to Run

### Project Structure
```text
├── README.md               # Project documentation (this file)
├── requirements.txt        # Python dependencies
├── src/                    # Source code scripts or game application
│   └── main.py             # Main entry point (or streamlit app)
├── notebooks/              # Jupyter notebooks containing experiments
│   └── solution.ipynb      # Main runnable notebook with outputs
└── references/             # Hackathon reference guides (Track 1 & Track 2)
```

### Installation & Execution Instructions

> 💡 **Environment Recommendation:** To avoid package conflicts, we strongly suggest using a fresh Python virtual environment or Google Colab:
> ```bash
> python -m venv venv
> source venv/bin/activate    # On Windows: venv\Scripts\activate
> pip install -r requirements.txt
> ```

1. **Clone the repository:**
   ```bash
   git clone [your-repo-url]
   cd [your-repo-folder]
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the project / demo:**
   ```bash
   # If running a script or CLI game:
   python src/main.py

   # If running a Streamlit web app:
   streamlit run src/app.py

   # Or open the Jupyter Notebook:
   jupyter notebook notebooks/solution.ipynb
   # Run the Quantum Coin Duel web game
streamlit run src/main.py

# Or open the Jupyter notebook
jupyter notebook notebooks/solution.ipynb

---

## 4. Implementation Walkthrough & Live Demo

* **Walkthrough of Gameplay / Optimization Pipeline:**  
  `[The player opens the Quantum Coin Duel game.

The player selects a quantum operation: Hadamard (H), Pauli-X (X), or No operation.

The player predicts Heads or Tails.

Qiskit constructs a one-qubit quantum circuit and calculates the output-state probabilities.

The game samples an outcome and compares it with the player's prediction.

The score is updated based on whether the prediction is correct.]`

* **Key Screenshots / Terminal Output:**  
  `[Screenshots of the Quantum Coin Duel interface, quantum circuit, measurement outcome, and score will be added after the application is successfully run and tested.]`

---

## 5. Classical vs. Quantum Comparison

* **Classical Baseline / Counterpart:**  
  `[A classical coin-toss game serves as the baseline for comparison. It produces Heads or Tails using classical random sampling, with each outcome having a probability of 50% for a fair coin. This baseline helps compare classical randomness with the measurement probabilities generated by the Qiskit quantum circuit.]`

* **Comparative Analysis:**  
  `[The classical baseline generates Heads or Tails using classical random sampling, while the quantum approach uses Qiskit to calculate measurement probabilities from a quantum circuit. The Hadamard gate creates a superposition with equal probabilities for Heads and Tails, whereas the Pauli-X gate flips the initial qubit state from |0⟩ to |1⟩. These operations demonstrate different quantum behaviors and provide an interactive learning experience. The current implementation does not demonstrate a guaranteed advantage over classical coin tossing.]`

---

## 6. Performance, Results & Limitations

* **Key Results & Observations:**  
  `[The project is designed to demonstrate how quantum gates affect measurement outcomes in a one-qubit circuit. The Hadamard gate produces equal probabilities for the two outcomes, while the Pauli-X gate transforms the initial state |0⟩ into |1⟩. Gameplay results and application performance will be documented after successful testing.]`

* **Critical Reflection on Limitations:**  
  `[The current project uses a simple one-qubit simulation and does not require physical quantum hardware. Real quantum devices may produce different results because of noise, gate errors, and decoherence. Increasing the number of qubits and circuit operations can increase computational costs and make results more sensitive to errors. Future improvements could include entangled qubits, additional strategic choices, and testing on real quantum hardware.]`

---

## 7. References & Acknowledgments
- Qiskit documentation: https://docs.quantum.ibm.com/
- Streamlit documentation: https://docs.streamlit.io/
- Qiskit Fall Fest 2026 — IIIT Kottayam Hackathon reference materials provided in this repository.
- Acknowledgment: This project explores interactive quantum computing education using Python and Qiskit.

* `[Cite any open-source libraries, GitHub repositories, or research papers you referenced during the hackathon.]`
* `[Acknowledge team contributions and tools used.]`
