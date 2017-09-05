"""Entry point for tap-mailchimp."""

from singer.utils import parse_args
import tap_mailchimp.config as tapconfig
from tap_mailchimp.tap import MailChimpTap

def main():
    """Entry point for tap-mailchimp."""
    args = parse_args(tapconfig.required_keys)
    tap = MailChimpTap(args.config, args.state)
    if args.discover:
        raise NotImplementedError('Discovery not yet implemented.')
    elif args.catalog is not None:
        raise NotImplementedError('Catalog support not yet implemented.')
    elif args.properties is not None:
        raise NotImplementedError('Properties support not yet implemented.')
    else:
        tap.pour()
    return 0
