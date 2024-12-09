from time import sleep

class TestWith:
    
    def __enter__(self):
        print("Initializing")

    def __exit__(self, exception_type, exception_value, traceback):
        print("Finishing")

test = TestWith()
test.__enter__()
test.__exit__(None, None, None)

print()

with TestWith() as test: print("Novamente dentro do with")

