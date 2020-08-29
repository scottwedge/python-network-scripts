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
    # Getting All Arugments
    args = vars(parser.parse_args())

    port = int(args["port"])
    logpath = str(args["logfile"])

    logging.basicConfig(filename=logpath, filemode='w', format='%(asctime)s | %(levelname)s : %(message)s', datefmt='%d-%B-%Y %H:%M:%S')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f'Socket successfully created.')
        s.bind((socket.gethostname(), port))
        logging.info(f'Socket binded to {port}.')
        s.listen(5)
        logging.info(f'Socket is listening.')

        while True:
            clientsocket, address = s.accept()
            logging.info(f'Connection from {address} has been established.')
            logging.info(f'Sent a message to that address.')
            clientsocket.send(bytes("Hello!","utf-8"))
            clientsocket.close()

    except socket.error as err:
        logging.error(f'Socket creation failed with error {err}.')
    except:
        logging.error(f'Unknown error has occured with Socket.')


if __name__ == '__main__':
    main()
