from pages.base_page import Basepage
from playwright.sync_api import Page, expect


class CreateCoursePage(Basepage):
    def __init__(self, page: Page):
        super().__init__( page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        self.preview_image_upload_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.preview_image_upload_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.preview_image_upload_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text').locator('textarea').first
        self.preview_image_upload_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')

        self.preview_image_remove_button = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_input = page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        self.create_course_description_input = page.get_by_test_id('create-course-form-description-input').locator('input')
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

        self.exercises_title =page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercises_button =page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        self.exercises_icon =page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_title =page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_description =page.get_by_test_id('create-course-exercises-empty-view-description-text')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('create course')

    def create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        expect(self.check_visible_create_course_button()).to_be_visible()

    def check_disable_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()



