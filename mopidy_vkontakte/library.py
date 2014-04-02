from __future__ import unicode_literals

import logging

from mopidy import backend, models

logger = logging.getLogger(__name__)


class VKLibraryProvider(backend.LibraryProvider):
    def __init__(self, *args, **kwargs):
        super(VKLibraryProvider, self).__init__(*args, **kwargs)

    root_directory = models.Ref.directory(
        uri='vkontakte:directory',
        name='VKontakte'
    )

    def find_exact(self, **query):
        pass

    def search(self, **query):
        pass

    def lookup(self, uri):
        pass

    def get_all_songs_from_album(self, album_id):
        return self.get_all_songs([('album_id', album_id)])

    def get_all_albums(self):
        return self.backend.session.call_api('audio.getAlbums')

    def get_all_songs(self, album_id=[]):
        if album_id:
            return self.backend.session.call_api(
                'audio.get', album_id)
        else:
            return self.backend.session.call_api('audio.get')
