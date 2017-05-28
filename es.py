import elasticsearch
import elasticsearch_dsl
import urllib3
import elasticsearch.connection.http_urllib3
from configurations import Configurations

urllib3.disable_warnings()

class es(object):

    def __init__(self):

        self.es_connection = elasticsearch.Elasticsearch(
            hosts = Configurations.elasticsearch_enpoint,
            http_auth = Configurations.elasticsearch_auth,
            verify_certs = Configurations.elasticsearch_verify_ssl
        )

    def test_connection(self):
        return self.es_connection.info()
