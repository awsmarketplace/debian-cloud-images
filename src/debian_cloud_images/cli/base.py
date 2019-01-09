import argparse
import logging


class BaseCommand:
    argparser_name = None
    argparser_help = None
    argparser_usage = None

    @classmethod
    def _argparse_init_base(cls):
        parser = argparse.ArgumentParser(
            usage=cls.argparser_usage,
        )
        cls._argparse_register(parser)
        return parser

    @classmethod
    def _argparse_init_sub(cls, subparsers):
        parser = subparsers.add_parser(
            name=cls.argparser_name,
            help=cls.argparser_help,
            usage=cls.argparser_usage,
        )
        cls._argparse_register(parser)
        return parser

    @classmethod
    def _argparse_register(cls, parser):
        parser.set_defaults(cls=cls)
        parser.add_argument(
            '--debug',
            action='store_true',
            help='enable debug output',
        )

    def __init__(self, *, debug=False, **kw):
        logging.basicConfig(level=debug and logging.DEBUG or logging.INFO)

    def __call__(self):
        raise NotImplementedError