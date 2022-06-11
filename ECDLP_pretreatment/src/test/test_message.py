import unittest
from main.message import messageEncrypt, messageDecrypt
from main.compress import decompress



class test_message(unittest.TestCase):
  ##初始化工作
  def setUp(self):
    pass
  #退出清理工作
  def tearDown(self):
    pass

  #具体的测试用例，一定要以test开头
  def test_messageEncrypt(self):
    # input
    p = 0xb77902abd8db9627f5d7ceca5c17ef6c5e3b0969
    a = 0x9021748e5db7962e1b208e3949d42ad0388a18c
    b = 0x744f47974caabdd8b8192e99da51c87f91cc453e
    compress_P = ['0x4f1ecacc3b1e56066b02f6a6033f940fc5c9805',0]
    P = decompress(compress_P, a, b, p)
    k = 0xe6ea1793a37dedf12ed676aef41ed68f4da4ae8f
    m = 'share a secret. '
    index = 2
    compress_Q_a =  ['0xb50e2eb55cd84112077a5acca94b4623a8b020d7', 0]
    Q_a = decompress(compress_Q_a, a, b, p)

    # output
    compress_C1 = ['0x2592c6e5b7176ef74a7c7adc9a19906445759d5', 0]
    compress_C2 = ['0x47190e98e7d440679b896e2a672c9ad58e13d212', 1]

    # check
    self.assertEqual(messageEncrypt(m, index, Q_a, P, k, a, b, p), [compress_C1, compress_C2], 'test_messageEncrypt fail')


  def test_messageDecrypt(self):
    # messageDecrypt(C1, C2, n_a, a, b, p)
    # input
    p = 0xb77902abd8db9627f5d7ceca5c17ef6c5e3b0969
    a = 0x9021748e5db7962e1b208e3949d42ad0388a18c
    b = 0x744f47974caabdd8b8192e99da51c87f91cc453e
    C1 = decompress(['0x2592c6e5b7176ef74a7c7adc9a19906445759d5', 0], a, b, p)
    C2 = decompress(['0x47190e98e7d440679b896e2a672c9ad58e13d212', 1],a, b, p)
    n_a = 0x9022802bb688656ee1914e6dd7f74e1ecd1d6780

    # check
    self.assertEqual(messageDecrypt(C1, C2, n_a, a, b, p), ['share a secret. ', '2'], 'test_messageDecrypt fail')


if __name__ =='__main__':
  unittest.main()