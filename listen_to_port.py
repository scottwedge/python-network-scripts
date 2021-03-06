from argparse import ArgumentParser, SUPPRESS
import socket
import struct
import logging

def main():
    # Command Line Parser
    parser = ArgumentParser(add_help=False,description="Listen to a port on the current network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All Command Line Arguments
    requiredArgs.add_argument("-p","--port",required=True,help="the port server listens on")
    requiredArgs.add_argument("-l","--logfile",required=True,help="where it will keep a record of actions")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All Arguments
    args = vars(parser.parse_args())

    # Relaying ALL Arguments into Variables
    port = int(args["port"])
    logpath = str(args["logfile"])

    # Logging Setup
    logging.basicConfig(level=logging.NOTSET,filename=logpath,filemode='w',format='%(asctime)s | %(levelname)s : %(message)s',datefmt='%d-%B-%Y %H:%M:%S')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f'Socket successfully created.')
        s.bind((socket.gethostname(), port))
        logging.info(f'Socket binded to {port}.')
        s.listen(5)
        logging.info(f'Socket is listening.')

        while True:
            try:
                clientsocket, address = s.accept()
                logging.info(f'Connection from {address} has been established.')

                head = clientsocket.recv(16)
                body = clientsocket.recv(8)

                logging.info(f'Head of Packet Received: {head}')
                logging.info(f'Body of Packet Received: {body}')

                clientsocket.close()
            except (BlockingIOError, InterruptedError, ConnectionAbortedError):
                pass

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
