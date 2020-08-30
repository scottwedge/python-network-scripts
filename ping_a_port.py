from argparse import ArgumentParser, SUPPRESS
import socket
import struct
import logging

def main():
    # Command line parser
    parser = ArgumentParser(add_help=False,description="Ping a port on a certain network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All command line arguments
    requiredArgs.add_argument("-s","--server",required=True,help="the IP address of server")
    requiredArgs.add_argument("-p","--port",required=True,help="the port the server listens on")
    requiredArgs.add_argument("-l","--logfile",required=True,help="where it will keep a record of actions")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All arguments
    args = vars(parser.parse_args())

    # Relaying ALL arguments into variables
    port = int(args["port"])
    address = args["server"]
    logpath = str(args["logfile"])

    # Logging setup
    logging.basicConfig(level=logging.NOTSET,filename=logpath,filemode='w',format='%(asctime)s | %(levelname)s : %(message)s',datefmt='%d-%B-%Y %H:%M:%S')

    try:
        # Socket setup
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f'Socket successfully created.')
        s.connect((address, port))
        logging.info(f'Socket connected to {address}, {port}.')

        # Packet information
        version       = 17
        message_type  = 1
        message       = "HELLO"

        # Construct packet
        head = struct.pack("IiI", version, message_type, len(message))
        body = bytes(message, 'utf-8')
        packet = head+body
        logging.info(f'Packet created : {packet}.')

        # Send head of packet
        s.send(packet[:struct.calcsize("IiI")])
        logging.info(f'Head of packet has been sent to {address}, {port}.')
        # Send body of packet
        s.send(packet[struct.calcsize("IiI"):])
        logging.info(f'Body of packet has been sent to {address}, {port}.')

        # Close the socket
        s.close(s)
        logging.info(f'Socket has been closed.')

    except socket.error as err:
        logging.error(f'Socket failed with error {err}.')
    except socket.herror:
        logging.error(f'Socket failed with an address herror.')
    except socket.gaierror:
        logging.error(f'Socket failed with an address gaierror.')
    except socket.timeout:
        logging.error(f'Socket failed with a timeout error.')
    except KeyboardInterrupt:
        logging.error(f'Socket connection manually closed.')
    except:
        logging.error(f'Socket unknown error occurred.')

if __name__ == '__main__':
    main()
