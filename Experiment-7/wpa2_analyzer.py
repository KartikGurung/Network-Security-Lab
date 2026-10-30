
from scapy.all import rdpcap, EAPOL, Dot11
import sys



def identify_message(key_info, nonce):

    ack = bool(key_info & 0x0080)
    mic = bool(key_info & 0x0100)
    install = bool(key_info & 0x0040)

    # Message 1: AP sends ANonce
    if ack and not mic:
        return "Message 1 (AP -> Client)"

    # Message 3: AP sends key installation information
    elif ack and mic and install:
        return "Message 3 (AP -> Client)"

    # Message 4: Client sends acknowledgment with zero nonce
    elif not ack and mic and nonce == bytes(32):
        return "Message 4 (Client -> AP)"

    # Message 2: Client sends SNonce
    elif not ack and mic and nonce != bytes(32):
        return "Message 2 (Client -> AP)"

    return "Other EAPOL-Key Message"



def analyze_capture(filename):

    print("\n WPA2 FOUR-WAY HANDSHAKE ANALYZER")
    print("=" * 55)

    packets = rdpcap(filename)

    message_count = {
        "Message 1": 0,
        "Message 2": 0,
        "Message 3": 0,
        "Message 4": 0
    }

    eapol_count = 0

    for packet in packets:

        if not packet.haslayer(EAPOL):
            continue

        eapol_count += 1

        # Get raw EAPOL packet bytes
        data = bytes(packet[EAPOL])

        # EAPOL-Key packet has a descriptor type
        if len(data) < 99 or data[1] != 3:
            print("\nNon-Key EAPOL packet detected")
            continue

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

        if message.startswith("Message"):
            number = message.split()[1]
            message_count["Message " + number] += 1

        print("\nPacket Number:", eapol_count)
        print("Handshake:", message)

        if packet.haslayer(Dot11):
            print("Transmitter:", packet[Dot11].addr2)
            print("Receiver:", packet[Dot11].addr1)

        print("Replay Counter:", replay_counter)
        print("Nonce:", nonce)
        print("MIC:", mic_value)

    # Display final summary
    print("\n" + "=" * 55)
    print("ANALYSIS SUMMARY")
    print("=" * 55)

    print("Total EAPOL Packets:", eapol_count)

    for message, count in message_count.items():
        print(message + ":", count)

    if all(count > 0 for count in message_count.values()):
        print("\nAll four handshake message types detected.")
    else:
        print("\nSome handshake messages were not detected.")
        print("Check capture completeness and packet classification.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 wpa2_analyzer.py capture.pcapng")
        sys.exit(1)

    analyze_capture(sys.argv[1])
