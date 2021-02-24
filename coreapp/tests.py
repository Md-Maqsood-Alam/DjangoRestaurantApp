from django.test import TestCase

# Create your tests here.
class CoreViewsTest(TestCase):
    def test_home_view(self):
        response=self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

    def test_reservation_view(self):
        response=self.client.get('/reservation/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'reservation.html')