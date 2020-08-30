import struct

def main():
    # Packet Information
    version = 17
    message_type = 1
    message = bytes("hi", 'utf-8')

    head = struct.pack("IiI", version, message_type, len(message))
    packet = head+message
    print(packet)
    print(f'head:{packet[:12]}, message:{packet[12:]}')
    print(f'cutoff:{struct.calcsize("IiI")}')


    print(f'struct:{struct.unpack("IiI", packet[:12])}, string:{packet[12:]}')
    head, message = struct.unpack("IiI", packet[:12]), packet[12:]
    print(f'head:{head}, message:{message.decode("utf-8")}')


if __name__ == '__main__':
    main()
