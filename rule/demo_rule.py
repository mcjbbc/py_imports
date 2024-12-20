from .utils import call_me_maybe


class DemoRule:
    cloud_client: call_me_maybe("demo")

    def __init__(self):
        call_me_maybe("demo_init")

    def hi(self):
        print("demo says hi!")
