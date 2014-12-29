from unittest import TestCase

from container_transform.converter import Converter


class ConverterTests(TestCase):

    def test_fig_converter(self):

        filename = './container_transform/tests/fig.yml'
        conv = Converter(filename, 'fig', 'ecs')

        output = conv.convert()

        self.assertIsInstance(output, str)

    def test_ecs_converter(self):

        filename = './container_transform/tests/task.json'
        conv = Converter(filename, 'ecs', 'fig')

        fig_output = conv.convert()

        self.assertIsInstance(fig_output, str)

        self.assertEqual(0, len(conv.messages))
