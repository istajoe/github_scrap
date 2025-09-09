import subprocess
import os
import sys
from datetime import datetime

def run_command(command, output_file):
    # this code runs a shell command and save output to file.

    with open(output_file, "w") as f:
        process = subprocess.Popen(command, stdout=f, stderr=subprocess.PIPE, text=True)
        _, err = process.communicate()
        if process.returncode != 0:
            print(f"[!] Error running {' '.join(command)}: {err.strip()}")
        else:
            print(f"[!] Results saved to {output_file}")

def main(domain):
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    out_dir = f"results_{domain}_{timestamp}"
    os.makedirs(out_dir, exist_ok=True)

    print(f"Started subdomain enumeration for {domain}")
    print(f"Results will be saved in: {out_dir}")

    # For Sublist3r

    run_command(
        ["sublist3r", "-d", domain, "-o", f"{out_dir}/sublist3r.txt"],
        f"{out_dir}/sublist3r.txt"
    )

    # For Amass

    run_command(
        ["amass", "enum", "-passive", "-d", domain, "-o", f"{out_dir}/amass.txt"],
        f"{out_dir}/amass.txt"
    )

    # For Assetfinder

    run_command(
        ["assetfinder", "--subs-only", domain],
        f"{out_dir}/assetfinder.txt"
    )

    # For FFUF (bruteforce subdomains)

    run_command(
        ["ffuf", "-u", f"http://FUZZ.{domain}", "-w", "/usr/share/wordlists/rockyou.txt", "-o", f"{out_dir}/ffuf.json", "-of", "json"],
        f"{out_dir}/ffuf.json"
    )

    # For gobuster (directory brute force, not strictly subdomains but useful)

    run_command(
        ["gobuster", "dns", "-d", domain, "-w", "/usr/share/wordlists/rockyou.txt", "-o",  f"{out_dir}/gobuster.txt"],
        f"{out_dir}/gobuster.txt"
    )

    print("\n Enumeration complete!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <domain>")
        sys.exit(1)

    target_domain = sys.argv[1]
    main(target_domain)

