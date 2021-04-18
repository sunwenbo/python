import argparse
import logging
import sys

__version__ = '1.0.2'


PY3 = sys.version_info[0] == 3


class HelpFormatter(argparse.RawTextHelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            return super(HelpFormatter, self)._format_action_invocation(
                action=action)
        if PY3:
            default = self._get_default_metavar_for_optional(action)
        else:
            default = action.dest.upper()
        args_string = self._format_args(action, default)
        return '%s %s' % (', '.join(action.option_strings), args_string)


parser = argparse.ArgumentParser(
    formatter_class=HelpFormatter,
    description='LDAP utils.',
    epilog=' ')

parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s ' + __version__)
parser.add_argument('-d', '--debug', action='store_true',
                    help="enable debug logging")

subparsers = parser.add_subparsers(title='available commands')
subparser = subparsers.add_parser(
    name='server', formatter_class=HelpFormatter,
    description='A mock of LDAP server for testing authentication from '
                'other applications.',
    epilog=' ')
subparser.set_defaults(command='server')

subparser.add_argument('-H', '--host', default='localhost',
                       help='default: `localhost`')
subparser.add_argument('-P', '--port', default=3389,
                       help='default: `3389`')


def main():
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    if not hasattr(args, 'command'):
        parser.print_help()
        exit(1)

    if args.command == 'server':
        from ldap.server import Server
        Server(host=args.host, port=args.port).run()


if __name__ == '__main__':
    main()
