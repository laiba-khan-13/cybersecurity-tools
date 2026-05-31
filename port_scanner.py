# ============================================
# PORT SCANNER - Like knocking on doors to see which are open!
# ============================================

import socket  # This is Python's "phone call" tool - lets us connect to other computers

def scan_ports(target, start_port, end_port):
    """
    This function checks if ports are open, like knocking on doors!
    target = the computer's address (like 127.0.0.1 which means "my own computer")
    start_port = first door number to check
    end_port = last door number to check
    """
    
    print(f"\n🔍 Starting scan on: {target}")
    print(f"📋 Checking ports {start_port} to {end_port}")
    print("=" * 50)
    
    # Common services that run on specific ports (like name tags on doors)
    common_services = {
        21: "FTP (File Transfer)",
        22: "SSH (Secure Login)",
        23: "Telnet (Old Remote Login)",
        25: "SMTP (Email Sending)",
        53: "DNS (Website Names)",
        80: "HTTP (Websites)",
        110: "POP3 (Email Receiving)",
        143: "IMAP (Email)",
        443: "HTTPS (Secure Websites)",
        3306: "MySQL (Database)",
        3389: "RDP (Remote Desktop)",
    }
    
    open_ports = []  # Empty list to remember which doors are open
    
    # Loop through each port number (like walking down a hallway checking each door)
    for port in range(start_port, end_port + 1):
        # Create a "sock" (like a phone receiver)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Wait half a second max for an answer
        
        # Try to connect (knock on the door)
        result = sock.connect_ex((target, port))
        
        if result == 0:  # 0 means "someone answered!" (port is open)
            service = common_services.get(port, "Unknown Service")
            print(f"🟢 Port {port} is OPEN! → {service}")
            open_ports.append(port)
        else:
            # Port is closed or blocked - don't print (too much noise!)
            pass
            
        sock.close()  # Hang up the phone
    
    # Show final results
    print("=" * 50)
    if open_ports:
        print(f"✅ Found {len(open_ports)} open ports: {open_ports}")
    else:
        print("❌ No open ports found in this range")
    
    return open_ports


# ============================================
# THIS PART RUNS WHEN YOU START THE PROGRAM
# ============================================

if __name__ == "__main__":
    print("🛡️  WELCOME TO PORT SCANNER 3000 🛡️")
    print("This tool checks which computer 'doors' are open")
    
    # Ask user what to scan
    target_ip = input("\nEnter target IP (or type '127.0.0.1' to scan your own computer): ")
    
    # Ask which ports to check
    start = int(input("Start port (try 1): "))
    end = int(input("End port (try 100 for quick test): "))
    
    # Run the scan!
    scan_ports(target_ip, start, end)
    
    print("\n🎉 Scan complete! Remember: Only scan computers you OWN or have PERMISSION to scan!")
