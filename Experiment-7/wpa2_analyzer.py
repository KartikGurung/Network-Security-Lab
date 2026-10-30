
from scapy.all import rdpcap, EAPOL, Dot11
import sys
import os


def identify_message(key_info, nonce):

    # Extract Key Information flags
    ack = bool(key_info & 0x0080)
    mic = bool(key_info & 0x0100)
    install = bool(key_info & 0x0040)

    # Message 1: AP sends ANonce
    if ack and not mic:
        return "Message 1"

    # Message 3: AP sends key information
    elif ack and mic:
        return "Message 3"

    # Message 4: Client sends acknowledgment
    elif not ack and mic and nonce == bytes(32):
        return "Message 4"

    # Message 2: Client sends SNonce
    elif not ack and mic and nonce != bytes(32):
        return "Message 2"

    return "Other"


def analyze_capture(filename):

    print("\nWPA2 FOUR-WAY HANDSHAKE ANALYZER")
    print("=" * 60)

    # Read the capture file
    try:
        packets = rdpcap(filename)
    except Exception as error:
        print("Error reading capture:", error)
        return

    # Store frame counts and unique messages
    frame_count = {
        "Message 1": 0,
        "Message 2": 0,
        "Message 3": 0,
        "Message 4": 0
    }

    unique_messages = {
        "Message 1": set(),
        "Message 2": set(),
        "Message 3": set(),
        "Message 4": set()
    }

    eapol_count = 0
    duplicate_count = 0

    for packet in packets:

        if not packet.haslayer(EAPOL):
            continue

        data = bytes(packet[EAPOL])

        # Check for valid EAPOL-Key packet
        if len(data) < 99 or data[1] != 3:
            continue

        eapol_count += 1

        # Extract Key Information
        key_info = int.from_bytes(data[5:7], "big")

        # Extract Replay Counter
        replay_counter = int.from_bytes(data[9:17], "big")

        # Extract Nonce
        nonce_bytes = data[17:49]
        nonce = nonce_bytes.hex()

        # Extract MIC
        mic_value = data[81:97].hex()

        # Identify handshake message
        message = identify_message(key_info, nonce_bytes)

        if message == "Other":
            continue

        # Extract wireless device addresses
        transmitter = "Unknown"
        receiver = "Unknown"

        if packet.haslayer(Dot11):
            transmitter = packet[Dot11].addr2
            receiver = packet[Dot11].addr1

        # Count captured frames
        frame_count[message] += 1

        # Create a signature to identify retransmissions
        signature = (
            transmitter,
            receiver,
            replay_counter,
            key_info,
            nonce,
            mic_value
        )

        if signature in unique_messages[message]:
            duplicate_count += 1
            status = "Retransmission / Duplicate"
        else:
            unique_messages[message].add(signature)
            status = "New Message Variant"

        # Display packet information
        print("\n" + "-" * 60)
        print("Frame:", eapol_count)
        print("Handshake:", message)
        print("Status:", status)
        print("Transmitter:", transmitter)
        print("Receiver:", receiver)
        print("Replay Counter:", replay_counter)

        # Identify nonce type
        if message in ("Message 1", "Message 3"):
            print("ANonce:", nonce)

        elif message == "Message 2":
            print("SNonce:", nonce)

        elif message == "Message 4":
            print("Nonce: Zero (Acknowledgment)")

        print("MIC:", mic_value)

    # Final analysis summary
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)

    print("Total EAPOL-Key Frames:", eapol_count)

    for message in frame_count:

        print("\n" + message)
        print("Captured Frames:", frame_count[message])
        print("Unique Variants:", len(unique_messages[message]))

    print("\nDuplicate / Retransmitted Frames:", duplicate_count)

    # Check whether all four message types were detected
    if all(len(unique_messages[m]) > 0 for m in unique_messages):

        print("\nSUCCESS: All four handshake message types detected.")

    else:

        print("\nINCOMPLETE: Some handshake message types are missing.")

    # Compare ANonce values
    anonce_values = set()

    for message in ("Message 1", "Message 3"):
        for signature in unique_messages[message]:
            anonce_values.add(signature[4])

    if len(anonce_values) == 1 and anonce_values:
        print("ANonce Verification: Matching values detected.")

    elif len(anonce_values) > 1:
        print("ANonce Verification: Different values detected.")

    else:
        print("ANonce Verification: Insufficient data.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 wpa2_analyzer.py capture.pcap")
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print("Error: Capture file not found.")
        sys.exit(1)

    analyze_capture(sys.argv[1])

#  to run this code open terminal and write this command:  python3 wpa2_analyzer.py wpa2-four-way-handshake.pcap