import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AffSe9pBjD5LzUGrNBPEVbAvHGjq8bDMf8aqH0MDXGZrpkmsUoQgCcKDRHaurgWes86K4N6Omo8n6R11"
        self.client_secret = "ELrU7T5bihkpdNDlPtWy7SgbaeMfrg9daX3CaIQ_5iGguC1BvVeR-VHtYJl-EOuPgHn32nwTxmmkOInO"
        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret
        )
        self.client = PayPalHttpClient(self.environment)
