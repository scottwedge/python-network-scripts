from argparse import ArgumentParser, SUPPRESS
import socket

def main():
    # Command Line Parser
    parser = ArgumentParser(add_help=False,description="Ping a port on a certain network")
    requiredArgs = parser.add_argument_group("required arguments")
    optionalArgs = parser.add_argument_group("optional arguments")
    # Adding All Command Line Arguments
    requiredArgs.add_argument("-a","--address",required=True,help="address to ping")
    requiredArgs.add_argument("-p","--port",required=True,help="port to ping")
    optionalArgs.add_argument("-h","--help",action="help",default=SUPPRESS,help="show this help message and exit")
    # Getting All Arugments
    args = vars(parser.parse_args())

    port = int(args["port"])
    address = args["address"]
    if not address:
        address = socket.gethostname()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port))
        msg = s.recv(1024)
        print("Message from Server: " + msg.decode("utf-8"))
    except socket.error as err:
        print(f'Socket creation failed with error {err}')
    except:
        print(f'Unknown error has occured with Socket')


if __name__ == '__main__':
    main()
