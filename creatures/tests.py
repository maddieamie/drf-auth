from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import MagicalCreature

class MagicalCreatureAPITests(APITestCase):
    
    def setUp(self):
        # Create users
        self.user1 = get_user_model().objects.create_user(username='user1', password='password1')
        self.user2 = get_user_model().objects.create_user(username='user2', password='password2')

        # Create magical creatures
        self.creature1 = MagicalCreature.objects.create(
            name='Bob', 
            species='Unicorn', 
            magical_power='The tears of children', 
            description='A unicorn that strikes heart into the fear of your average man.', 
            added_by=self.user1
        )
        self.creature2 = MagicalCreature.objects.create(
            name='Sal', 
            species='Pomeranian Shifter', 
            magical_power='shifting human to pomeranian', 
            description='A lovely character from the House in the Cerulean Sea.', 
            added_by=self.user2
        )

        self.list_url = reverse('magicalcreature-list')

    def test_get_creatures_list(self):
        # Test GET request to retrieve the list of magical creatures
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        # Test the first creature's data
        self.assertEqual(response.data[0]['name'], 'Bob')
        self.assertEqual(response.data[0]['species'], 'Unicorn')
        self.assertEqual(response.data[0]['magical_power'], 'The tears of children')
        self.assertEqual(response.data[0]['description'], 'A unicorn that strikes heart into the fear of your average man.')
        self.assertEqual(response.data[0]['added_by'], self.user1.id)
        
        # Test the second creature's data
        self.assertEqual(response.data[1]['name'], 'Sal')
        self.assertEqual(response.data[1]['species'], 'Pomeranian Shifter')
        self.assertEqual(response.data[1]['magical_power'], 'shifting human to pomeranian')
        self.assertEqual(response.data[1]['description'], 'A lovely character from the House in the Cerulean Sea.')
        self.assertEqual(response.data[1]['added_by'], self.user2.id)

    def test_create_creature(self):
        # Test POST request to create a new magical creature
        self.client.login(username='user1', password='password1')
        data = {
            'name': 'Fang',
            'species': 'Dragon',
            'magical_power': 'Fire breathing',
            'description': 'A fierce dragon guarding a golden hoard.',
            'added_by': self.user1.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MagicalCreature.objects.count(), 3)
        self.assertEqual(MagicalCreature.objects.last().name, 'Fang')

    def test_update_creature(self):
        # Test PUT request to update a magical creature
        self.client.login(username='user1', password='password1')
        creature_url = reverse('magicalcreature-detail', args=[self.creature1.id])
        updated_data = {
            'name': 'Bob',
            'species': 'Unicorn',
            'magical_power': 'Healing tears',
            'description': 'A unicorn with healing powers.',
            'added_by': self.user1.id
        }
        response = self.client.put(creature_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.creature1.refresh_from_db()
        self.assertEqual(self.creature1.magical_power, 'Healing tears')

    def test_delete_creature(self):
        # Test DELETE request to remove a magical creature
        self.client.login(username='user1', password='password1')
        creature_url = reverse('magicalcreature-detail', args=[self.creature1.id])
        response = self.client.delete(creature_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MagicalCreature.objects.count(), 1)
