import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_auth_view(client, create_user, test_password):
   user = create_user()
   url = reverse('auth-url')
   client.login(
       username=user.username, password=test_password
   )
   response = client.get(url)
   assert response.status_code == 200

@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
      def make_auto_login(user=None):
         if user is None:
            user = create_user()
         client.login(username=user.username, password=test_password)
         return client, user

      return make_auto_login