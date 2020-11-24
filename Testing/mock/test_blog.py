import pytest
from .blog import BlogPostHistory
from unittest.mock import patch, MagicMock
from unittest import TestCase


class BlogPostHistoryTests(TestCase):

    def test_change_title(self):
        # side_effect - it allows you to perform, for example, another function or just - throw an exception.
        mock = MagicMock(side_effect=OSError)

        # the "with" syntax determines which block of code the mock will apply to.
        # The patch function takes "what to replace" as its first argument and "to what" as its second argument.
        with patch('Testing.mock.blog.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            with pytest.raises(Exception):
                post_history.change_description("desc2")
            # assert post_history.get_properties() == ("title2", "desc")


# In a block covered by "with", running change_title will replace the class field and of course it will execute the save
# method, but we replaced it with a mock that does nothing.
