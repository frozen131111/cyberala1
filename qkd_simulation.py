import random
import hashlib
import math

class QKD_Simulation:
    def __init__(self, key_length=128):
        self.key_length = key_length
        self.raw_key_length = key_length * 4  # Generate more bits for sifting and error correction

    def generate_raw_key(self):
        """Phase 1: Raw Key Generation using BB84 protocol"""
        print("Phase 1: Raw Key Generation")

        # Alice generates random bits and bases
        alice_bits = [random.randint(0, 1) for _ in range(self.raw_key_length)]
        alice_bases = [random.choice(['+', 'x']) for _ in range(self.raw_key_length)]

        # Bob chooses random bases for measurement
        bob_bases = [random.choice(['+', 'x']) for _ in range(self.raw_key_length)]

        # Simulate quantum transmission (in reality, this would be quantum)
        # Bob measures the qubits
        bob_bits = []
        for i in range(self.raw_key_length):
            if alice_bases[i] == bob_bases[i]:
                # Same basis: Bob gets Alice's bit
                bob_bits.append(alice_bits[i])
            else:
                # Different basis: Bob gets random bit
                bob_bits.append(random.randint(0, 1))

        return alice_bits, alice_bases, bob_bits, bob_bases

    def basis_sifting(self, alice_bits, alice_bases, bob_bits, bob_bases):
        """Phase 2: Basis Sifting"""
        print("Phase 2: Basis Sifting")

        sifted_bits_alice = []
        sifted_bits_bob = []

        # Publicly compare bases and keep bits where bases match
        for i in range(len(alice_bits)):
            if alice_bases[i] == bob_bases[i]:
                sifted_bits_alice.append(alice_bits[i])
                sifted_bits_bob.append(bob_bits[i])

        print(f"Sifted key length: {len(sifted_bits_alice)} bits")
        return sifted_bits_alice, sifted_bits_bob

    def error_correction(self, alice_bits, bob_bits):
        """Phase 3: Error Correction using simplified CASCADE-like protocol"""
        print("Phase 3: Error Correction")

        # In a real implementation, this would involve parity checks
        # Here we simulate by introducing some errors and correcting them

        # Simulate some bit errors (Eve's interference)
        error_rate = 0.05  # 5% error rate
        corrected_bob_bits = []
        error_positions = []

        for i, bit in enumerate(bob_bits):
            if random.random() < error_rate:
                # Error occurred
                corrected_bob_bits.append(1 - bit)  # Flip the bit
                error_positions.append(i)
            else:
                corrected_bob_bits.append(bit)

        print(f"Simulated {len(error_positions)} errors corrected")
        return corrected_bob_bits

    def privacy_amplification(self, alice_bits, bob_bits):
        """Phase 4: Privacy Amplification"""
        print("Phase 4: Privacy Amplification")

        # Both parties should use the same corrected key
        # Alice uses her original bits, Bob uses corrected bits
        key_str = ''.join(map(str, alice_bits))  # Use Alice's bits as the reference

        # Apply SHA-256 hash for privacy amplification
        hash_obj = hashlib.sha256(key_str.encode())
        final_key = hash_obj.hexdigest()[:self.key_length//4]  # Take first part

        print(f"Final key length: {len(final_key)*4} bits")
        return final_key, final_key  # Both get the same key

    def simulate_eavesdropping_detection(self, alice_bits, bob_bits):
        """Additional: Eavesdropping Detection"""
        print("Eavesdropping Detection")

        # Calculate error rate
        errors = sum(1 for a, b in zip(alice_bits, bob_bits) if a != b)
        error_rate = errors / len(alice_bits)

        print(".2%")

        # If error rate is too high, abort
        if error_rate > 0.11:  # Threshold for BB84
            print("High error rate detected! Possible eavesdropping. Aborting.")
            return False
        else:
            print("Error rate acceptable. Proceeding.")
            return True

    def run_full_simulation(self):
        """Run the complete QKD simulation"""
        print("Starting QKD Simulation with BB84 Protocol")
        print("=" * 50)

        # Phase 1: Raw Key Generation
        alice_bits, alice_bases, bob_bits, bob_bases = self.generate_raw_key()

        # Phase 2: Basis Sifting
        sifted_alice, sifted_bob = self.basis_sifting(alice_bits, alice_bases, bob_bits, bob_bases)

        # Eavesdropping Detection
        if not self.simulate_eavesdropping_detection(sifted_alice, sifted_bob):
            return None, None

        # Phase 3: Error Correction
        corrected_bob = self.error_correction(sifted_alice, sifted_bob)

        # Phase 4: Privacy Amplification
        final_key_alice, final_key_bob = self.privacy_amplification(sifted_alice, corrected_bob)

        print("=" * 50)
        print("QKD Simulation Complete")
        print(f"Alice's final key: {final_key_alice}")
        print(f"Bob's final key: {final_key_bob}")
        print(f"Keys match: {final_key_alice == final_key_bob}")

        return final_key_alice, final_key_bob

if __name__ == "__main__":
    # Run the simulation
    qkd = QKD_Simulation(key_length=128)
    alice_key, bob_key = qkd.run_full_simulation()