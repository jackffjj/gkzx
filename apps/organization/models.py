# organization/models.py

from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField('系别地址',max_length=20)
    desc = models.CharField('描述',max_length=200)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '系别地址'
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    ORG_CHOICES = (
        ("jsjx", u"计算机系"),
        ("cjx", u"财经系"),
        ("ysx", u"艺术系"),
        ("wyx", u"外语系"),
        ("glx", u"管理系"),
        ("jdx", u"机电系"),
    )
    name = models.CharField('部门名称',max_length=50)
    desc = models.TextField('部门描述')
    category = models.CharField(max_length=20, choices=ORG_CHOICES, verbose_name=u"部门类别", default="jsjx")
    click_nums = models.IntegerField('点击数',default=0)
    tag = models.CharField('部门标签',max_length=10,default='全国知名')
    fav_nums = models.IntegerField('收藏数',default=0)
    students = models.IntegerField("学习人数",default=0)
    course_nums = models.IntegerField("课程数",default=0)
    image = models.ImageField('logo',upload_to='org/%Y/%m',max_length=100)
    address = models.CharField('部门地址',max_length=150,)
    city = models.ForeignKey(CityDict,verbose_name='所在位置',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教学部门'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        #获取部门的教师数
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name='所属教学部门',on_delete=models.CASCADE)
    name = models.CharField('教师名',max_length=50)
    work_years = models.IntegerField('工作年限',default=0)
    # work_company = models.CharField('就职公司',max_length=50)
    work_position = models.CharField('部门职位',max_length=50)
    points = models.CharField('教学特点',max_length=50)
    click_nums = models.IntegerField('点击数',default=0)
    fav_nums = models.IntegerField('收藏数',default=0)
    teacher_age = models.IntegerField('年龄',default=25)
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的教师: {1}".format(self.org, self.name)

    def get_course_nums(self):
        return self.course_set.all().count()
