import os

def check_system():
    print("Checking system security...")
    # Simulation
    if os.path.exists("/etc/passwd"):
        print("System file detected.")
    else:
        print("Warning: System file missing!")

if __name__ == "__main__":
    check_system()
