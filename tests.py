#!/usr/bin/python3
import unittest
import unittest.mock as mock
import model
from model import MyClass

class TestStringMethods(unittest.TestCase):

    @unittest.skip('Skipped test_new')
    @mock.patch('model.MyClass._get_connection.channel()')
    @mock.patch.object(MyClass, '_get_connection')
    def test_new(self, mocked1, mocked2):
        attrs = {'basic.return_value': 'channel.basic.return_value',
        'clever.return_value': 'channel.clever.return_value' }
        mocked2.configure_mock(**attrs)

        mqc = MyClass()
        print(mqc)
        print('############# There are three times call of mocked1')
        print(mqc.consumer())
        print('#############')
        print(mqc.func2())
        print('#############')
        print(mqc._get_connection().channel())
        print('############# end of three times call of mocked1')
        print('mocked1', mocked1)
        print('mocked2', mocked2)
        print('#############')
        print(mocked1.channel())
        print(mocked1.channel().basic(1))
        print(mocked1.channel().clever())
        print('#############')
        print(mocked2.basic(1))
        print(mocked2.clever())
        print('#############')
        # mocked1.assert_called_once()
        mocked1.assert_called()
        # mocked2.assert_called_once()
        # mocked1.channel().basic().assert_called_once()
        # mocked1.channel().clever().assert_called()
        # mocked2.basic().assert_called()
        # mocked2.clever().assert_called()
        print('#############')
        self.assertEqual(mocked2.basic(1), 'channel.basic.return_value')
        # mocked.channel.assert_called_once()

    @mock.patch.object(MyClass, '_get_connection')
    def test_renew(self, mocked):
        print('#############')
        print('mock configuration')
        channel = mock.MagicMock(return_value=None)
        basic = mock.MagicMock(return_value='basic')
        clever = mock.MagicMock(return_value='clever')
        channel.basic = basic
        channel.clever = clever
        mocked.channel = channel
        print('#############')
        print(mocked)
        print(channel)
        print(basic)
        print(clever)
        print('#############')
        print('#############')
        mqc = MyClass()
        print(mqc)
        print('#############')
        print(mqc.consumer())
        print('#############')
        print(mqc.func2())
        print('#############')
        print('#############')
        print(mocked.mock_calls)
        print('#############')
        print(channel.mock_calls)
        print('#############')
        print(basic.mock_calls)
        print(clever.mock_calls)
        print('#############')
        print('#############')
        self.assertEqual(basic(1), 'basic')
        self.assertEqual(clever(1), 'clever')
        mocked.assert_called()
        # mocked.channel.assert_called_once() # not called directly
        basic.assert_called_once()
        clever.assert_called_once()




if __name__ == '__main__':
    unittest.main()
