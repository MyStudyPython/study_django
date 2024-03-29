# 导入 django form 类
from django import forms

# 导入序列化器
from rest_framework import serializers

# 导入模型类
from .models import Course

from django.contrib.auth.models import User


class CouseForm(forms.ModelForm):
    class Meta:
        # form 对应的哪个模型类
        model = Course
        # form 表单有哪些字段
        filelds = ("name", "introduction", "teacher", "price")
        # filelds = "__all__"


# 模型类的写法 跟 django 的 form 类的写法很类似
# class CouseSerializer(serializers.ModelSerializer):
#     """
#     teacher 这里是外键
#     只能得到外键id

#     要是想要得到名字的话
#     就需要那用户的名称序列化出来

#     source  需要指定一个源
#     这个用户不是自己新建课程的时候的用户，是系统的用户，所以需要设置为 只读

#     CharField → ReadOnlyFieldField
#     """

#     teacher = serializers.ReadOnlyField(source="teacher.username")  # 外键字段只读

#     class Meta:
#         # form 对应的哪个模型类
#         model = Course  # 写法和上面的CourseForm 类似
#         # 除去哪些字段
#         # exec(
#         #     "id",
#         # )
#         # form 表单有哪些字段
#         # filelds = ("name", "introduction", "teacher", "price")

#         # 如果要和 __all__ 一致的话
#         # filelds = (
#         #     "id",
#         #     "name",
#         #     "introduction",
#         #     "teacher",
#         #     "price",
#         #     "created_at",
#         #     "update_at",
#         # )
#         filelds = "__all__"  # 所有字段

#         # 对于外键字段的序列化，可以指定便利的深度
#         depth = 2  # 表内子表关联父表，父表又关联到另外的父表


# class CouseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher = serializers.ReadOnlyField(source="teacher.username")  # 外键字段只读

#     class Meta:
#         model = Course  # 写法和上面的CourseForm 类似
#         filelds = "__all__"  # 所有字段


class UserSerializer(serializers.ModelSerializer):
    # 复杂的继承Serializer
    # class UserSerializer(serializers.Serializer):
    "用户模型类"

    class Meta:
        model = User
        """
        url 不是固定的 只是默认值，

        也可以改成 link 和其他名称，
        但是要在 setting.py中设置URL_FIELD_NAME使全局生效
        """
        filelds = (
            "id",
            "url",
            "name",
            "introduction",
            "teacher",
            "price",
            "created_at",
            "update_at",
        )
