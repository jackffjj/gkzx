# organization/adminx.py

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    '''系别地址'''

    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    '''系别'''

    list_display = ['name', 'desc', 'click_nums', 'fav_nums','add_time' ]
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','city__name','address','add_time']


class TeacherAdmin(object):
    '''老师'''

    list_display = [ 'name','org', 'work_years', 'add_time']
    search_fields = ['org', 'name', 'work_years']
    list_filter = ['org__name', 'name', 'work_years', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)