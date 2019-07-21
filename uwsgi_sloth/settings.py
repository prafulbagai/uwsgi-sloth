# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

FILTER_METHODS = ('GET', 'POST', 'PUT', 'DELETE', 'PATCH')
FILTER_STATUS = ('100', '101', '102', '200', '201', '202', '203', '204', '205', '206', '207', '208', '226', '300', '301', '302', '303', '304', '305', '307', '308', '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415', '416', '417', '422', '423', '424', '426', '428', '429', '431', '500', '501', '502', '503', '504', '505', '506', '507', '508', '510', '511')

LIMIT_URL_GROUPS = 200
LIMIT_PER_URL_GROUP = 20
DEFAULT_MIN_MSECS = 200

STATIC_PATH_BOOTSTRAP = 'https://maxcdn.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css'
STATIC_PATH_JQUERY = 'https://code.jquery.com/jquery-1.7.2.min.js'

STATIC_PATH_SORTABLE_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/css/sortable-theme-bootstrap.min.css'
STATIC_PATH_SORTABLE = 'https://cdnjs.cloudflare.com/ajax/libs/sortable/0.8.0/js/sortable.min.js'

REALTIME_UPDATE_INTERVAL = 5 * 60
