from rest_framework import serializers

from education.models import Section, Material, Test


class SectionSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания Section"""

    class Meta:
        model = Section
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания Material"""

    class Meta:
        model = Material
        fields = '__all__'


class MaterialTestsSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания MaterialTests"""

    class Meta:
        model = Material
        fields = ('questions',)


class MaterialTestsAnswerSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания MaterialTests"""

    class Meta:
        model = Material
        fields = ('answer',)


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
