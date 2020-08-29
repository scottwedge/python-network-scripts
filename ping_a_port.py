from argparse import ArgumentParser, SUPPRESS
import socket
import struct
import logging

def main():
    # Command Line Parser
    parser = ArgumentParser(add_help=False,description="Ping a port on a certain network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All Command Line Arguments
    requiredArgs.add_argument("-s","--server",required=True,help="the IP address of server")
    requiredArgs.add_argument("-p","--port",required=True,help="the port the server listens on")
    requiredArgs.add_argument("-l","--logfile",required=True,help="where it will keep a record of actions")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All Arugments
    args = vars(parser.parse_args())

    port = int(args["port"])
    address = str(args["server"])
    logpath = str(args["logfile"])

    logging.basicConfig(filename=logpath, filemode='w', format='%(asctime)s | %(levelname)s : %(message)s', datefmt='%d-%B-%Y %H:%M:%S')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info(f'Socket successfully created.')
        s.connect((address, port))
        logging.info(f'Socket connected to {address}, {port}.')
        msg = s.recv(1024)
        logging.info(f'Message from server: {msg.decode("utf-8")}.')
    except socket.error as err:
        logging.error(f'Socket creation failed with error {err}.')
    except:
        logging.error(f'Unknown error has occured with socket.')


if __name__ == '__main__':
    main()
