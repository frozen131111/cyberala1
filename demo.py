#!/usr/bin/env python3
"""
QKD Simulation Demo
Demonstrates the complete BB84 Quantum Key Distribution protocol
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

from qkd_simulation import QKD_Simulation

def demo_basic_simulation():
    """Demonstrate a basic QKD simulation"""
    print("🔐 Quantum Key Distribution (BB84) Simulation Demo")
    print("=" * 60)

    # Create QKD simulation with 128-bit key
    qkd = QKD_Simulation(key_length=128)

    print("🎯 Simulating secure key exchange between Alice and Bob")
    print("📡 Using BB84 protocol with quantum principles")
    print()

    # Run the simulation
    alice_key, bob_key = qkd.run_full_simulation()

    print()
    print("🎉 Simulation Results:")
    print(f"   Alice's Key: {alice_key}")
    print(f"   Bob's Key:   {bob_key}")
    print(f"   Keys Match:  {'✅ Yes' if alice_key == bob_key else '❌ No'}")

    if alice_key == bob_key:
        print("\n🔒 Secure key exchange successful!")
        print("   The key can now be used for symmetric encryption.")
    else:
        print("\n❌ Key exchange failed - potential security breach!")

def demo_multiple_simulations():
    """Demonstrate multiple simulations with statistics"""
    print("\n" + "=" * 60)
    print("📊 Multiple Simulations Demo")
    print("=" * 60)

    num_sims = 5
    success_count = 0

    print(f"Running {num_sims} QKD simulations...")

    for i in range(num_sims):
        print(f"\nSimulation {i+1}:")
        qkd = QKD_Simulation(key_length=64)
        alice_key, bob_key = qkd.run_full_simulation()

        if alice_key == bob_key:
            success_count += 1
            print("   ✅ Success")
        else:
            print("   ❌ Failed")

    print(f"\n📈 Success Rate: {success_count}/{num_sims} ({success_count/num_sims*100:.1f}%)")

def demo_key_sizes():
    """Demonstrate different key sizes"""
    print("\n" + "=" * 60)
    print("🔑 Different Key Sizes Demo")
    print("=" * 60)

    key_sizes = [32, 64, 128]

    for size in key_sizes:
        print(f"\n{size}-bit Key Simulation:")
        qkd = QKD_Simulation(key_length=size)
        alice_key, bob_key = qkd.run_full_simulation()

        print(f"   Key Length: {len(alice_key)*4} bits")
        print(f"   Hex Length: {len(alice_key)} characters")
        print(f"   Success: {'✅' if alice_key == bob_key else '❌'}")

if __name__ == "__main__":
    try:
        demo_basic_simulation()
        demo_multiple_simulations()
        demo_key_sizes()

        print("\n" + "=" * 60)
        print("🎓 Educational Notes:")
        print("   • BB84 protocol provides information-theoretic security")
        print("   • Any eavesdropping increases the quantum bit error rate")
        print("   • Privacy amplification reduces Eve's knowledge to negligible levels")
        print("   • This simulation demonstrates the core concepts classically")

    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        sys.exit(1)