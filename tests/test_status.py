import unittest
from unittest.mock import MagicMock, patch
from tkinter import Canvas, Tk
from PIL import Image
from characters.status import StatusBar


class TestStatusBar(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=800, height=600)
        self.mock_player = MagicMock()
        self.mock_player.canvas = self.canvas
        self.mock_player.name = "naruto"
        self.mock_player.health = 100
        self.mock_player.MAX_HEALTH = 100

    def tearDown(self):
        try:
            self.canvas.destroy()
        except Exception:
            pass
        try:
            self.root.destroy()
        except Exception:
            pass

    def test_init_and_draw_self(self):
        bar = StatusBar(self.mock_player, "left", hidden=False)
        self.assertIsNotNone(bar.canvas_mugshot)
        self.assertIsNotNone(bar.canvas_health_bar)
        self.assertIsNotNone(bar.canvas_chakra_bar)

    @patch("characters.status.Image.open")
    @patch("characters.status.ImageTk.PhotoImage")
    def test_update_health(self, mock_photo, mock_open):
        mock_open.return_value = Image.new("RGB", (100, 20))
        mock_photo.return_value = MagicMock()
        bar = StatusBar(self.mock_player, "right", hidden=True)
        bar.health_bar = MagicMock()
        bar.canvas_health_bar = self.canvas.create_rectangle(0, 0, 10, 10)
        with patch.object(bar, "redraw_health") as redraw_health:
            bar.update_health()
            redraw_health.assert_called_once()

    @patch("characters.status.Image.open")
    @patch("characters.status.ImageTk.PhotoImage")
    def test_update_chakra(self, mock_photo, mock_open):
        mock_open.return_value = Image.new("RGB", (100, 20))
        mock_photo.return_value = MagicMock()
        bar = StatusBar(self.mock_player, "left", hidden=True)
        bar.canvas_chakra_bar = self.canvas.create_rectangle(0, 0, 10, 10)
        with patch.object(bar, "redraw_chakra") as redraw_chakra:
            bar.update_chakra()
            redraw_chakra.assert_called_once()

    def test_scale_health_bar_img_mirrors_left(self):
        img = Image.new("RGB", (100, 20))
        bar = StatusBar(self.mock_player, "left", hidden=True)
        with patch("characters.status.ImageOps.mirror") as mirror:
            bar.scale_health_bar_img(img)
            mirror.assert_called_once()

    def test_scale_img_limits_width(self):
        img = Image.new("RGB", (100, 20))
        bar = StatusBar(self.mock_player, "right", hidden=True)
        result = bar.scale_img(img, 0)
        self.assertEqual(result.size[0], 1)

    def test_destroy(self):
        bar = StatusBar(self.mock_player, "right", hidden=True)
        ids = [self.canvas.create_rectangle(0, 0, 10, 10) for _ in range(6)]
        (
            bar.chakra_bar,
            bar.canvas_mugshot,
            bar.canvas_health_bar,
            bar.canvas_health_outline,
            bar.canvas_chakra_bar,
            bar.canvas_chakra_outline,
        ) = ids
        with patch.object(self.canvas, "delete") as delete_mock:
            bar.destroy()
            self.assertTrue(delete_mock.called)


if __name__ == "__main__":
    unittest.main()
