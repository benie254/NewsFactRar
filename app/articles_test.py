import unittest
from models import articles

Articles = articles.Articles


class ArticlesTestCase(unittest.TestCase):
    """
    Test behavior of the Articles class
    """

    def setUp(self):
        """
        Runs before every test
        """

        self.new_articles = Articles('BBC-Africa', 'Janja Park', "The Py Beast", 'A Python-an-anti Magazine',
                                     'https://techcrunch.com/2022/04/30/elons-big-week/',
                                     'https://techcrunch.com/wp-content/uploads/2019/07/DSCF2578.jpg?w=600',
                                     '2022-04-30T20:00:22Z',
                                     'Hi!\r\nI’m Greg Kumparak.\r\nI’ll be heading up Week in Review for the '
                                     'foreseeable future, with your former host Lucas Matney diving into cryptoland '
                                     'with the launch of a newsletter and podcast called Cha… [+4576 chars]')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles, Articles))


if __name__ == '__main__':
    unittest.main()
