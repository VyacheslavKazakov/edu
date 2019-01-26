

class MyClass:
    def _get_connection(self):
            print('get connection')

    def func2(self):
        print(4)
        self._get_connection()
        self._get_connection().channel()
        self._get_connection().basic()
        print(5)

    def consumer(self):
        test = 1
        print(0)
        channel = self._get_connection().channel()
        print(1)
        print(channel.basic(test))
        print(2)
        print(channel.clever())
        print(3)

        return
