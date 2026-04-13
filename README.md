# Quantum Key Distribution (QKD) Simulation - BB84 Protocol

## Student Information
- Name: **Abhishek Trivedi**
- Enrollment No.: **20230905040509**
- Program: **B.Tech in Computer Engineering**


## Project Title
**Simulation of Quantum Key Distribution using BB84 Protocol**

## Project Overview
This project simulates the BB84 Quantum Key Distribution protocol, demonstrating how two parties (Alice and Bob) can securely establish a shared secret key using quantum principles. The simulation is implemented in Python and models the main phases of the protocol in a classical environment.

## Objective
To demonstrate the operation of the BB84 QKD protocol and explain how raw key generation, basis sifting, error correction, and privacy amplification work together to produce a secure shared key.

## Features
- Simulates the full BB84 QKD protocol
- Generates random quantum bits and measurement bases
- Performs basis comparison and key sifting
- Simulates error correction and eavesdropping detection
- Applies privacy amplification using SHA-256 hashing
- Supports different key lengths for demonstration

## Project Structure
- `demo.py`: Main demo script that runs example QKD simulations and displays results.
- `qkd_simulation.py`: Core QKD simulation implementation containing all protocol phases.
- `requirements.txt`: Python dependency file (standard library only).
- `test_qkd.py`: Test file for validating QKD simulation behavior.

## Protocol Phases Implemented
1. **Raw Key Generation**
   - Alice generates random bits and chooses random bases.
   - Bob chooses random measurement bases.
   - The protocol simulates quantum measurement outcomes based on basis agreement.

2. **Basis Sifting**
   - Alice and Bob publicly compare their bases.
   - Bits measured in the same basis are kept as the sifted key.

3. **Error Correction**
   - The simulation models a simplified error correction process.
   - Random errors are corrected to simulate reconciliation between Alice and Bob.

4. **Privacy Amplification**
   - A hash-based method is used to shorten the sifted key.
   - This reduces any partial information an eavesdropper may have.

5. **Eavesdropping Detection**
   - The simulated error rate is checked.
   - If the error rate exceeds the threshold, the run is considered insecure.

## How to Run
1. Make sure Python 3.6 or later is installed.
2. Open a terminal in this project directory.
3. Run:

```bash
python demo.py
```

## Expected Output
The demo script prints the progress of the QKD protocol and final results, for example:

- Raw key generation phase
- Basis sifting results
- Error detection status
- Error correction results
- Final shared key output
- Key match confirmation

## Sample Output
```
Starting QKD Simulation with BB84 Protocol
==================================================
Phase 1: Raw Key Generation
Phase 2: Basis Sifting
Sifted key length: 136 bits
Eavesdropping Detection
Error rate acceptable. Proceeding.
Phase 3: Error Correction
Simulated 7 errors corrected
Phase 4: Privacy Amplification
Final key length: 64 bits
==================================================
QKD Simulation Complete
Alice's final key: 907448d08dfa1423
Bob's final key: 907448d08dfa1423
Keys match: True
```

## Requirements
- Python 3.6 or newer
- No external libraries required

## Notes
- This is a classical simulation of the BB84 protocol intended for educational use.
- The implementation demonstrates the core ideas of QKD without using actual quantum hardware.

## References
- Bennett, C. H., & Brassard, G. (1984). Quantum cryptography: Public key distribution and coin tossing.
- Ekert, A. K. (1991). Quantum cryptography based on Bell's theorem.

---

*Submitted by Abhishek Trivedi, Enrollment No. 20230905040502, B.Tech CE*
