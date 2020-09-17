import unittest
from io import StringIO
import sys
import robot
from test_base import captured_io
from unittest.mock import patch


class TestClass(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\noff\n"))
    def test_name_then_off(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot_name = robot.get_robot_name()
            result = robot.get_command(robot_name)
            output = out.getvalue() + result
            self.assertEqual(output, "What do you want to name your robot? HAL: What must I do next? off")
        #print(output)
    
    @patch("sys.stdin", StringIO("HAL\nOFf\n"))
    def test_name_then_off_super(self):
        with patch("sys.stdout", new=StringIO()) as out:
            robot_name = robot.get_robot_name()
            result = robot.get_command(robot_name) 

            output = "{}{}".format(out.getvalue(),result)

            self.assertEqual(output, "What do you want to name your robot? HAL: What must I do next? off")
    
    #@patch("sys.stdin", StringIO("BENT\nforward 10\nreplay\n"))
    def test_replay_then_off(self):
        with captured_io(StringIO("BENT\nforward 10\nreplay\noff")) as (out,err):
            robot.robot_start()

        output = out.getvalue().strip()

        self.assertEqual(output ,"""What do you want to name your robot? BENT: Hello kiddo!
BENT: What must I do next?  > BENT moved forward by 10 steps.
 > BENT now at position (0,10).
BENT: What must I do next?  > BENT moved forward by 10 steps.
 > BENT now at position (0,20).
 > BENT replayed 1 commands.
 > BENT now at position (0,20).
BENT: What must I do next? BENT: Shutting down..""")

    def test_left_then_fwd30_replay(self):
        with captured_io(StringIO("HAK\nleft\noff\nforward 30\nreplay\noff\n")) as (out,err):
            robot.robot_start()
        self.maxDiff = None
        output = out.getvalue().strip()
        self.assertEqual(
            output, """What do you want to name your robot? HAK: Hello kiddo!\nHAK: What must I do next?  > HAK turned left.\n""")


if __name__ == '__main__':
    unittest.main()
