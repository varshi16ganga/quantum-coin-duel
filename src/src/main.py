
import random
import streamlit as st
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

st.set_page_config(page_title="Quantum Coin Duel", page_icon="🪙")

st.title("🪙 Quantum Coin Duel")
st.write("Challenge the quantum world! Choose a quantum operation and predict the coin's outcome.")

if "score" not in st.session_state:
    st.session_state.score = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = 0

st.subheader("How to play")
st.write("1. Choose a quantum operation.")
st.write("2. Predict Heads or Tails.")
st.write("3. Measure the qubit to reveal the result.")

operation = st.selectbox(
    "Choose your quantum operation",
    ["Hadamard (H) — create superposition", "Pauli-X (X) — flip the qubit", "No operation — keep the initial state"]
)

prediction = st.radio("Your prediction:", ["Heads", "Tails"], horizontal=True)

if st.button("⚛️ Run Quantum Duel"):
    circuit = QuantumCircuit(1, 1)

    if operation.startswith("Hadamard"):
        circuit.h(0)
    elif operation.startswith("Pauli-X"):
        circuit.x(0)

    state = Statevector.from_instruction(circuit.remove_final_measurements(inplace=False))
    probabilities = state.probabilities()
    outcome = random.choices([0, 1], weights=probabilities, k=1)[0]

    circuit.measure(0, 0)

    result = "Heads" if outcome == 0 else "Tails"
    st.session_state.rounds += 1

    st.subheader("Quantum Circuit")
    st.code(str(circuit.draw(output="text")))

    st.write(f"Measurement result: **{result}**")

    if prediction == result:
        st.success("Correct prediction! You won this round.")
        st.session_state.score += 1
    else:
        st.info("Not this time! Try another round.")

    st.write(f"Quantum state before measurement: {state}")
    st.write(f"Score: {st.session_state.score} / {st.session_state.rounds}")

if st.button("🔄 Reset Score"):
    st.session_state.score = 0
    st.session_state.rounds = 0
    st.rerun()
