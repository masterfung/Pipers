from json import dumps
import json
from django.core.management import BaseCommand
from django.utils.html import strip_tags
from requests import get
from event.models import Event
import keys

__author__ = '@masterfung'


EVENTBRITE_OAUTH_KEY = keys.EVENTBRITE_OAUTH_KEY


class Command(BaseCommand):
    def handle(self, *args, **options):

        page = 0

        cities = [
             "san+francisco",
        ]
        while page < 50:
            for city in cities:
                print page
                page += 1
                print page
                resp = get('https://www.eventbriteapi.com/v3/events/search/?',
                           params={
                               "token": EVENTBRITE_OAUTH_KEY,
                               "venue.city": city,
                               "page": page,
                           }
                           )
                print resp
                if resp.status_code != 200:
                    print "error"
                    return

                data = dumps(resp.json(), indent=2, sort_keys=True)

                events = json.loads(data)

                events = events['events']

                x = 0
                while x <= 50:
                    x += 1

                    if not (len(events) > x):
                        break
                    print x
                    event = events[x]
                    try:
                        if event.get('venue') is not None:
                            formatted_start_time = event['start']['utc'][:-1]
                            formatted_end_time = event['end']['utc'][:-1]

                            # datetime_start = dateutil.parser.parse(event['start']['utc'])
                            # datetime_end = dateutil.parser.parse(event['end']['utc'])
                            description_info = strip_tags(event.get('description', {}))

                            eventbrite = Event.objects.update_or_create(
                                event_id=event.get('id', 0),

                                defaults={
                                          'description': description_info.get('text', 'Not Available'),
                                          'event_name': event.get('name', {}).get('text'),
                                          'event_url': event.get('url', None),

                                          'venue_name': event.get('venue', {}).get('name', 'Not Available'),
                                          'event_address': event.get('venue', {}).get('address', {}).get('address_1', 'Not Available'),
                                          'event_address2': event.get('venue', {}).get('address', {}).get('address_2', 'Not Available'),
                                          'city': event.get('venue', {}).get('address', {}).get('city', 'Not Available'),
                                          'country': event.get('venue', {}).get('address', {}).get('country', 'Not Available'),
                                          'zip': event.get('venue', {}).get('address', {}).get('postal_code', 0),
                                          'state': event.get('venue', {}).get('address', {}).get('region', 'Not Available'),
                                          'lat': event.get('venue', {}).get('latitude', 0),
                                          'lon': event.get('venue', {}).get('longitude', 0),

                                          'event_start': formatted_start_time,
                                          'event_end': formatted_end_time,
                                          },




                                # ticket_free=event.get('ticket_classes', {}).get('fee', 'Not Available'),
                                # cost=event['ticket_classes'].get('cost', {}).get('display', 'Not Available'),
                                # cost_currency=event.get('ticket_classes', {}).get('cost', {}).get('currency', 'Not Available'),
                                # event_status=event.get('status', 'Not Available')
                            )

                    except:
                        pass