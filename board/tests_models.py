"""
board 앱의 models 를 테스트합니다.
"""
import logging
from faker import Faker

from django.test import TestCase

from .models import Board

logger = logging.getLogger(__name__)
fake = Faker()


class BoardModelTests(TestCase):
    """
    게시판 모델을 테스트합니다.
    """

    def setUp(self) -> None:
        # self.test_board = Board(name=fake.email(), description="테스트 게시판 입니다.")
        # print(self.test_board)

        pass

    def test_create_board(self):
        """
        임의의 값으로 게시판을 생성합니다.
        """
        for _ in range(100):
            board = Board.objects.create(name=fake.sentence(), description=fake.text())
            logger.debug(board, board.name)
        self.assertEqual(Board.objects.all().count(), 100)
