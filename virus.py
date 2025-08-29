import os

# Example "virus signatures" (fake patterns for demo)
# In reality, AV software uses huge signature databases (hashes, byte patterns)
virus_signatures = [
    "X5O!P%@AP[4\\PZX54(P^)7CC)7}$" ,  # Example EICAR test string (safe test virus)
    "malware_pattern_123",
    "virus_exec_command"
]

def scan_file(filepath):
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
            for signature in virus_signatures:
                if signature in content:
                    return f"ALERT: Virus signature found in {filepath}"
        return f" Safe: {filepath}"
    except Exception as e:
        return f" Could not scan {filepath}: {e}"

def scan_directory(directory):
    print(f"\n Scanning directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            result = scan_file(filepath)
            print(result)

# --- Example Run ---
if __name__ == "__main__":
    folder_to_scan = input("Enter folder path to scan: ")
    scan_directory(folder_to_scan)
