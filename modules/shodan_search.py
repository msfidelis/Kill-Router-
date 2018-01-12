#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import shodan
from termcolor import colored

class Shodan_Search(object):

    def __init__(self):

        self._api_key = os.environ.get("SHODAN_API")
        self._api = shodan.Shodan(self._api_key)


    def validateapi(self):

        if self._api_key == "":
            print colored("[x] INVALID SHODAN API KEY:", 'red', attrs=['bold'])
            print colored("[!] Create a Account and Generate a new API KEY in https://account.shodan.io/login", 'red',
                          attrs=['bold'])
            return False
        else:
            return True


    def search(self, dork):

        results = self._api.search(dork)

        print ""
        print colored("==========================[SHODAN RESULT]==========================", 'yellow', attrs=['bold'])
        print ""
        print '[!] Results Found: %s' % results['total']
        print ""

        if results['total'] == 0:
            sys.exit()


        for result in results['matches']:
            print colored("==========================[%s]==========================",'yellow', attrs=['bold']) % result['ip_str']
            print ""
            print '[HEADER] %s' % result['data']
            print '[IP] %s' % result['ip_str']
            print '[PORT] %s' % result['port']
            print '[Country] %s' % result['location']['country_code']
            print '[Region] %s' % result['location']['region_code']
            print '[City] %s' % result['location']['city']
            print ''

        return results


