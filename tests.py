#!/usr/bin/python3
import unittest
import unittest.mock as mock
import model
from model import MyClass

class TestStringMethods(unittest.TestCase):

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
          mocked1.assert_called_once()
          # mocked2.assert_called_once()
          # mocked1.channel().basic().assert_called_once()
          # mocked1.channel().clever().assert_called()
          # mocked2.basic().assert_called()
          # mocked2.clever().assert_called()
          print('#############')
          self.assertEqual(mocked2.basic(1), 'channel.basic.return_value')
          # mocked.channel.assert_called_once()



if __name__ == '__main__':
    unittest.main()
