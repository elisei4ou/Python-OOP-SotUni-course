from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.media = SocialMedia("Meta", "Instagram", 1000, "some type")

    def test_correct_init(self):
        self.assertEqual("Meta", self.media._username)
        self.assertEqual("Instagram", self.media.platform)
        self.assertEqual(1000, self.media.followers)
        self.assertEqual("some type", self.media._content_type)
        self.assertEqual([], self.media._posts)

    def test_validate_platform_with_wrong_platform_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.media.platform = "wrong"

        self.assertEqual(str(ve.exception), f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_followers_when_they_are_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.media.followers = -1

        self.assertEqual(str(ve.exception), "Followers cannot be negative.")

    def test_create_post(self):
        new_post = {'content': "new post", 'likes': 0, 'comments': []}
        expected_result = f"New {self.media._content_type} post created by {self.media._username} on {self.media._platform}."

        self.assertEqual(expected_result, self.media.create_post("new post"))
        self.assertEqual(self.media._posts, [{'content': "new post", 'likes': 0, 'comments': []}])

    def test_like_post_valid_like_index(self):
        self.media._posts = [{'content': "new post", 'likes': 0, 'comments': []}]
        result = self.media.like_post(0)
        expected_likes = 1

        self.assertEqual(result, f"Post liked by {self.media._username}.")
        self.assertEqual(self.media._posts[0]['likes'], expected_likes)

    def test_like_post_valid_index_reached_maximum_likes(self):
        self.media._posts = [{'content': "new post", 'likes': 10, 'comments': []}]
        result = self.media.like_post(0)
        expected_likes = 10

        self.assertEqual(result, f"Post has reached the maximum number of likes.")
        self.assertEqual(self.media._posts[0]['likes'], expected_likes)

    def test_like_post_invalid_index(self):
        self.media._posts = [{'content': "new post", 'likes': 10, 'comments': []}]
        result = self.media.like_post(1)

        self.assertEqual(result, "Invalid post index.")

    def test_comment_on_post_valid_comment(self):
        self.media._posts = [{'content': "new post", 'likes': 10, 'comments': []}]
        result = self.media.comment_on_post(0, "This is longer than 10 chars.")
        expected_comment = [{'content': "new post", 'likes': 10, 'comments': [{'user': self.media._username, 'comment': "This is longer than 10 chars."}]}]

        self.assertEqual(result, f"Comment added by {self.media._username} on the post.")
        self.assertEqual(expected_comment, self.media._posts)

    def test_comment_on_post_shorter_than_10_chars(self):
        self.media._posts = [{'content': "new post", 'likes': 10, 'comments': []}]
        result = self.media.comment_on_post(0, "wrong")

        self.assertEqual(result, "Comment should be more than 10 characters.")

    if __name__ == "__main__":
        main()
