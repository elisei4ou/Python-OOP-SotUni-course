from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Ivan", {"course_name": ["notes"]})

    def test_correct_init(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({"course_name": ["notes"]}, self.student.courses)

    def test_enroll_when_course_name_already_added_return_string_and_add_notes(self):
        expected_result = "Course already added. Notes have been updated."
        expected_courses = {"course_name": ["notes", "notes2", "notes3"]}

        result = self.student.enroll("course_name", ["notes2", "notes3"])

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll_when_add_course_notes_equals_letter_Y(self):
        expected_result = "Course and course notes have been added."
        expected_courses = {"course_name": ["notes"], "course_name2": ["notes2"]}

        result = self.student.enroll("course_name2", ["notes2"], "Y")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll_when_add_course_notes_equals_nothing(self):
        expected_result = "Course and course notes have been added."
        expected_courses = {"course_name": ["notes"], "course_name2": ["notes2"]}

        result = self.student.enroll("course_name2", ["notes2"], "")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll_when_only_the_course_is_added_no_notes(self):
        expected_result = "Course has been added."
        expected_courses = {"course_name": ["notes"], "course_name2": []}

        result = self.student.enroll("course_name2", ["notes2"], "NO")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_courses, self.student.courses)

    def test_add_note_when_course_name_exist_return_string(self):
        expected_result = "Notes have been updated"
        expected_notes = {"course_name": ["notes", "notes3"]}

        result = self.student.add_notes("course_name", "notes3")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, self.student.courses)

    def test_add_note_when_course_name_NOT_exist_raises_exception(self):
        expected_result = "Cannot add notes. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("not course", "notes")

        self.assertEqual(expected_result, str(ex.exception))

    def test_leave_course_when_course_exist_return_string(self):
        expected_result = "Course has been removed"
        expected_notes = {}

        result = self.student.leave_course("course_name")

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_notes, self.student.courses)

    def test_leave_course_when_course_NOT_exist_raises_exception(self):
        expected_result = "Cannot remove course. Course not found."

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("not course")

        self.assertEqual(expected_result, str(ex.exception))


if __name__ == '__main__':
    main()